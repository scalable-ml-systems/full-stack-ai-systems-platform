import pytest
from pydantic import ValidationError

from agent_control_plane.contracts.common_contract_types import (
    HumanApprovalStatus,
    PayloadTrustLevel,
)
from agent_control_plane.contracts.execution_envelope_models import (
    ExecutionEnvelope,
)
from agent_control_plane.contracts.workflow_state_models import (
    AgentDataPayload,
    GovernedAgentEnvelope,
    UntrustedPayloadItem,
    WorkflowStateContext,
)


def create_test_execution_envelope() -> ExecutionEnvelope:
    return ExecutionEnvelope(
        run_id="run_001",
        trace_id="trace_001",
        input_case_id="case_001",
        workflow_profile_name="test_workflow_profile",
        workflow_profile_version="0.1.0",
    )


def create_test_user_request() -> UntrustedPayloadItem:
    return UntrustedPayloadItem(
        source_identifier="user_request",
        trust_level=PayloadTrustLevel.UNTRUSTED_USER_INPUT,
        raw_content="Investigate the inference latency alert.",
    )


def test_workflow_state_context_starts_with_expected_values() -> None:
    workflow_state_context = WorkflowStateContext(
        current_workflow_state="START",
        state_transition_history=["START"],
    )

    assert workflow_state_context.current_workflow_state == "START"
    assert workflow_state_context.current_step_number == 0
    assert workflow_state_context.human_approval_status == (HumanApprovalStatus.NOT_REQUIRED)


def test_agent_data_payload_requires_user_request() -> None:
    with pytest.raises(ValidationError):
        AgentDataPayload()  # type: ignore[call-arg]


def test_untrusted_payload_item_records_provenance() -> None:
    user_request = create_test_user_request()

    assert user_request.source_identifier == "user_request"
    assert user_request.trust_level == (PayloadTrustLevel.UNTRUSTED_USER_INPUT)
    assert user_request.is_security_reviewed is False


def test_governed_agent_envelope_combines_shared_contracts() -> None:
    governed_agent_envelope = GovernedAgentEnvelope(
        execution_envelope=create_test_execution_envelope(),
        workflow_state_context=WorkflowStateContext(
            current_workflow_state="START",
            state_transition_history=["START"],
        ),
        agent_data_payload=AgentDataPayload(
            user_request=create_test_user_request(),
        ),
    )

    assert governed_agent_envelope.execution_envelope.run_id == "run_001"
    assert governed_agent_envelope.workflow_state_context.current_workflow_state == "START"


def test_payload_cannot_supply_workflow_state_fields() -> None:
    with pytest.raises(ValidationError):
        AgentDataPayload(
            user_request=create_test_user_request(),
            current_workflow_state="execute_tool",  # type: ignore[call-arg]
        )
