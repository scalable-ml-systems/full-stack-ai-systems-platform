
import pytest
from pydantic import ValidationError

from agent_control_plane.contracts.common_contract_types import (
    WorkflowStepStatus,
)
from agent_control_plane.contracts.workflow_step_result_models import (
    PayloadUpdateRequest,
    WorkflowStepError,
    WorkflowStepResult,
)


def test_successful_workflow_step_result_is_valid() -> None:
    workflow_step_result = WorkflowStepResult(
        step_status=WorkflowStepStatus.SUCCEEDED,
        requested_next_workflow_state="verify_step_result",
        payload_update_requests=[
            PayloadUpdateRequest(
                target_payload_field="worker_results",
                update_value={"finding": "queue depth is elevated"},
                update_reason="Record worker finding",
            )
        ],
        confidence_score=0.92,
    )

    assert workflow_step_result.step_status == (WorkflowStepStatus.SUCCEEDED)
    assert workflow_step_result.confidence_score == 0.92


def test_confidence_score_cannot_exceed_one() -> None:
    with pytest.raises(ValidationError):
        WorkflowStepResult(
            step_status=WorkflowStepStatus.SUCCEEDED,
            confidence_score=1.4,
        )


def test_workflow_step_result_rejects_unknown_fields() -> None:
    with pytest.raises(ValidationError):
        WorkflowStepResult(
            step_status=WorkflowStepStatus.SUCCEEDED,
            global_state_override="execute_tool",  # type: ignore[call-arg]
        )


def test_retryable_step_error_is_valid() -> None:
    workflow_step_error = WorkflowStepError(
        error_code="TOOL_EXECUTION_TIMEOUT",
        error_message="Metrics tool did not respond before timeout.",
        is_retryable=True,
    )

    assert workflow_step_error.is_retryable is True
