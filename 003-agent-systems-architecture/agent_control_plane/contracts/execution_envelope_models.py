from datetime import datetime, timezone

from pydantic import BaseModel, ConfigDict, Field

from agent_control_plane.contracts.common_contract_types import (
    WorkflowExecutionStatus,
)


def current_utc_timestamp() -> datetime:
    return datetime.now(timezone.utc)


class ExecutionEnvelope(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        frozen=True,
    )

    run_id: str = Field(min_length=1)
    trace_id: str = Field(min_length=1)
    input_case_id: str = Field(min_length=1)

    workflow_profile_name: str = Field(min_length=1)
    workflow_profile_version: str = Field(min_length=1)

    created_at: datetime = Field(default_factory=current_utc_timestamp)
    started_at: datetime | None = None
    completed_at: datetime | None = None

    execution_status: WorkflowExecutionStatus = (
        WorkflowExecutionStatus.CREATED
    )
