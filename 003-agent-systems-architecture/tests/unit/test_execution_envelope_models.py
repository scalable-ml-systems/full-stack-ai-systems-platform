import pytest
from pydantic import ValidationError

from agent_control_plane.contracts.common_contract_types import (
    WorkflowExecutionStatus,
)
from agent_control_plane.contracts.execution_envelope_models import (
    ExecutionEnvelope,
)


def test_execution_envelope_accepts_valid_run_identity() -> None:
    execution_envelope = ExecutionEnvelope(
        run_id="run_001",
        trace_id="trace_001",
        input_case_id="case_001",
        workflow_profile_name="test_workflow_profile",
        workflow_profile_version="0.1.0",
    )

    assert execution_envelope.run_id == "run_001"
    assert execution_envelope.execution_status == (
        WorkflowExecutionStatus.CREATED
    )


def test_execution_envelope_rejects_empty_run_id() -> None:
    with pytest.raises(ValidationError):
        ExecutionEnvelope(
            run_id="",
            trace_id="trace_001",
            input_case_id="case_001",
            workflow_profile_name="test_workflow_profile",
            workflow_profile_version="0.1.0",
        )


def test_execution_envelope_rejects_unknown_fields() -> None:
    with pytest.raises(ValidationError):
        ExecutionEnvelope(
            run_id="run_001",
            trace_id="trace_001",
            input_case_id="case_001",
            workflow_profile_name="test_workflow_profile",
            workflow_profile_version="0.1.0",
            unexpected_field="not_allowed",
        )


def test_execution_envelope_is_immutable() -> None:
    execution_envelope = ExecutionEnvelope(
        run_id="run_001",
        trace_id="trace_001",
        input_case_id="case_001",
        workflow_profile_name="test_workflow_profile",
        workflow_profile_version="0.1.0",
    )

    with pytest.raises(ValidationError):
        execution_envelope.run_id = "run_999"
