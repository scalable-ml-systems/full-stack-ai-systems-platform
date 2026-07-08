from agent_control_plane.contracts.common_contract_types import (
    HumanApprovalStatus,
    PayloadTrustLevel,
    WorkflowExecutionStatus,
    WorkflowStepStatus,
)


def test_workflow_execution_status_values_are_stable() -> None:
    assert WorkflowExecutionStatus.CREATED.value == "created"
    assert WorkflowExecutionStatus.RUNNING.value == "running"
    assert WorkflowExecutionStatus.COMPLETED.value == "completed"


def test_workflow_step_status_values_are_stable() -> None:
    assert WorkflowStepStatus.SUCCEEDED.value == "succeeded"
    assert WorkflowStepStatus.RETRY_REQUIRED.value == "retry_required"


def test_human_approval_status_values_are_stable() -> None:
    assert HumanApprovalStatus.PENDING.value == "pending"
    assert HumanApprovalStatus.APPROVED.value == "approved"


def test_payload_trust_levels_distinguish_untrusted_sources() -> None:
    assert (
        PayloadTrustLevel.UNTRUSTED_USER_INPUT.value
        != PayloadTrustLevel.UNTRUSTED_TOOL_OUTPUT.value  # type: ignore[comparison-overlap]
    )
