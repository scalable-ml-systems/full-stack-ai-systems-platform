from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from agent_control_plane.contracts.common_contract_types import (
    WorkflowStepStatus,
)


class PayloadUpdateRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    target_payload_field: str = Field(min_length=1)
    update_value: Any
    update_reason: str = Field(min_length=1)


class WorkflowStepError(BaseModel):
    model_config = ConfigDict(extra="forbid")

    error_code: str = Field(min_length=1)
    error_message: str = Field(min_length=1)
    is_retryable: bool = False


class WorkflowStepResult(BaseModel):
    model_config = ConfigDict(extra="forbid")

    step_status: WorkflowStepStatus

    requested_next_workflow_state: str | None = None

    payload_update_requests: list[PayloadUpdateRequest] = Field(default_factory=list)

    evidence_references: list[str] = Field(default_factory=list)

    confidence_score: float | None = Field(
        default=None,
        ge=0.0,
        le=1.0,
    )

    recommended_next_action: str | None = None

    errors: list[WorkflowStepError] = Field(default_factory=list)
