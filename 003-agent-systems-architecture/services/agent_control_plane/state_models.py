from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4


INITIAL_WORKFLOW_STATE = "START"


def create_utc_timestamp() -> str:
    """Create a timezone-aware UTC timestamp for workflow records."""
    return datetime.now(timezone.utc).isoformat()


def create_identifier(prefix: str) -> str:
    """Create a readable unique identifier with a domain prefix."""
    return f"{prefix}_{uuid4().hex}"


@dataclass
class ExecutionEnvelope:
    """
    Stable identity for one governed agent run.

    This object should not contain volatile agent working data.
    It exists to identify and trace the workflow execution.
    """

    run_id: str
    input_id: str
    trace_id: str
    created_at_utc: str


@dataclass
class WorkflowStateContext:
    """
    Clean workflow-control state.

    This object tracks where the agent control plane is in the workflow.
    It should not store raw untrusted document text, tool outputs, or model output.
    """

    current_workflow_state: str = INITIAL_WORKFLOW_STATE
    previous_workflow_state: str | None = None
    state_history: list[str] = field(default_factory=lambda: [INITIAL_WORKFLOW_STATE])
    retry_counts_by_reason: dict[str, int] = field(default_factory=dict)
    selected_workflow_route: str | None = None
    human_review_required: bool = False
    human_review_approved: bool = False


@dataclass
class AgentDataPayload:
    """
    Volatile working data for the agent workflow.

    This object may contain user input, generated plans, intermediate answers,
    tool outputs, or error details. Later phases will treat some of this data
    as untrusted.
    """

    user_query: str
    detected_intent: str | None = None
    selected_plan_steps: list[str] = field(default_factory=list)
    current_plan_step_name: str | None = None
    latest_worker_name: str | None = None
    latest_worker_output: dict[str, Any] = field(default_factory=dict)
    draft_final_response: str | None = None
    verified_final_response: str | None = None
    error_messages: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class TraceEventRecord:
    """
    One append-only trace event.

    The trace is historical evidence of what happened during the workflow.
    It should not be confused with the current workflow state.
    """

    run_id: str
    trace_id: str
    event_name: str
    current_workflow_state: str
    next_workflow_state: str | None
    created_at_utc: str
    event_metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class GovernedAgentRun:
    """
    Full state object passed through the Agent Control Plane.

    The centralized graph orchestrator will receive this object, pass snapshots
    to workflow nodes, apply validated deltas, and append trace events.
    """

    execution_envelope: ExecutionEnvelope
    workflow_state_context: WorkflowStateContext
    agent_data_payload: AgentDataPayload
    trace_events: list[TraceEventRecord] = field(default_factory=list)


def create_initial_governed_agent_run(user_query: str, input_id: str | None = None) -> GovernedAgentRun:
    """
    Create the initial governed agent run.

    This is the starting object before routing, planning, execution, retries,
    or verification happen.
    """

    resolved_input_id = input_id or create_identifier("input")

    execution_envelope = ExecutionEnvelope(
        run_id=create_identifier("run"),
        input_id=resolved_input_id,
        trace_id=create_identifier("trace"),
        created_at_utc=create_utc_timestamp(),
    )

    workflow_state_context = WorkflowStateContext()

    agent_data_payload = AgentDataPayload(
        user_query=user_query,
    )

    return GovernedAgentRun(
        execution_envelope=execution_envelope,
        workflow_state_context=workflow_state_context,
        agent_data_payload=agent_data_payload,
    )
