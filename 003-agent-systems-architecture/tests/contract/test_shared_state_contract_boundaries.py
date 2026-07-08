from agent_control_plane.contracts.common_contract_types import (
    PayloadTrustLevel,
    WorkflowStepStatus,
)
from agent_control_plane.contracts.workflow_state_models import (
    AgentDataPayload,
    UntrustedPayloadItem,
)
from agent_control_plane.contracts.workflow_step_result_models import (
    PayloadUpdateRequest,
    WorkflowStepResult,
)


def create_user_request() -> UntrustedPayloadItem:
    return UntrustedPayloadItem(
        source_identifier="user_request",
        trust_level=PayloadTrustLevel.UNTRUSTED_USER_INPUT,
        raw_content="Investigate this incident.",
    )


def test_worker_result_requests_payload_update_instead_of_state_mutation() -> None:
    workflow_step_result = WorkflowStepResult(
        step_status=WorkflowStepStatus.SUCCEEDED,
        requested_next_workflow_state="collect_diagnostic_evidence",
        payload_update_requests=[
            PayloadUpdateRequest(
                target_payload_field="worker_results",
                update_value={"finding": "pod restarted"},
                update_reason="Store diagnostic result",
            )
        ],
    )

    assert workflow_step_result.requested_next_workflow_state == ("collect_diagnostic_evidence")
    assert workflow_step_result.payload_update_requests[0].target_payload_field == "worker_results"


def test_agent_payload_separates_untrusted_content() -> None:
    user_request = create_user_request()

    agent_data_payload = AgentDataPayload(
        user_request=user_request,
        untrusted_content_items=[
            UntrustedPayloadItem(
                source_identifier="tool_output_001",
                trust_level=PayloadTrustLevel.UNTRUSTED_TOOL_OUTPUT,
                raw_content={"queue_depth": 27},
            )
        ],
    )

    assert len(agent_data_payload.untrusted_content_items) == 1
    assert agent_data_payload.untrusted_content_items[0].trust_level == (
        PayloadTrustLevel.UNTRUSTED_TOOL_OUTPUT
    )
