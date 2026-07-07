from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from agent_control_plane.contracts.common_contract_types import (
    HumanApprovalStatus,
    PayloadTrustLevel,
)

from agent_control_plane.contracts.execution_envelope_models import (
    ExecutionEnvelope,
)

class WorkflowStateContext(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )

    current_workflow_state: str = Field(min_length=1)
    previous_workflow_state: str | None = None

    state_transition_history: list[str] = Field(default_factory=list)

    current_step_number: int = Field(default=0, ge=0)

    active_worker_name: str | None = None
    active_tool_name: str | None = None

    retry_attempts_by_step: dict[str, int] = Field(default_factory=dict)

    human_approval_status: HumanApprovalStatus = (
        HumanApprovalStatus.NOT_REQUIRED
    )

    checkpoint_reference: str | None = None

class TrustedPayloadItem(BaseModel):
    model_config = ConfigDict(extra="forbid")

    item_name: str = Field(min_length=1)
    item_value: Any


class UntrustedPayloadItem(BaseModel):
    model_config = ConfigDict(extra="forbid")

    source_identifier: str = Field(min_length=1)
    trust_level: PayloadTrustLevel
    raw_content: Any
    is_security_reviewed: bool = False
    security_review_notes: list[str] = Field(default_factory=list)


class AgentDataPayload(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )

    user_request: UntrustedPayloadItem

    classified_intent: str | None = None
    selected_route: str | None = None

    workflow_plan: dict[str, Any] | None = None

    trusted_working_data: list[TrustedPayloadItem] = Field(
        default_factory=list
    )

    untrusted_content_items: list[UntrustedPayloadItem] = Field(
        default_factory=list
    )

    worker_results: list[dict[str, Any]] = Field(default_factory=list)
    tool_execution_results: list[dict[str, Any]] = Field(
        default_factory=list
    )

    draft_output: Any | None = None
    verification_results: list[dict[str, Any]] = Field(
        default_factory=list
    )

    human_review_feedback: dict[str, Any] | None = None
    final_output: Any | None = None

    errors: list[str] = Field(default_factory=list)

    profile_specific_payload: dict[str, Any] = Field(default_factory=dict)

class GovernedAgentEnvelope(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )

    execution_envelope: ExecutionEnvelope
    workflow_state_context: WorkflowStateContext
    agent_data_payload: AgentDataPayload

    trace_event_identifiers: list[str] = Field(default_factory=list)
