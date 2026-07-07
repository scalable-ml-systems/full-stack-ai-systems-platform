from agent_control_plane.contracts.common_contract_types import (
    HumanApprovalStatus,
    PayloadTrustLevel,
    WorkflowExecutionStatus,
    WorkflowStepStatus,
)


def test_workflow_execution_status_values_are_stable() -> None:
    assert WorkflowExecutionStatus.CREATED == "created"
    assert WorkflowExecutionStatus.RUNNING == "running"
    assert WorkflowExecutionStatus.COMPLETED == "completed"


def test_workflow_step_status_values_are_stable() -> None:
    assert WorkflowStepStatus.SUCCEEDED == "succeeded"
    assert WorkflowStepStatus.RETRY_REQUIRED == "retry_required"


def test_human_approval_status_values_are_stable() -> None:
    assert HumanApprovalStatus.PENDING == "pending"
    assert HumanApprovalStatus.APPROVED == "approved"


def test_payload_trust_levels_distinguish_untrusted_sources() -> None:
    assert PayloadTrustLevel.UNTRUSTED_USER_INPUT != (
        PayloadTrustLevel.UNTRUSTED_TOOL_OUTPUT
    )
