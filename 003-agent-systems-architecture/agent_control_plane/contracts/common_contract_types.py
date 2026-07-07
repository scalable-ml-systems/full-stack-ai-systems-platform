from enum import StrEnum


class WorkflowExecutionStatus(StrEnum):
    CREATED = "created"
    RUNNING = "running"
    WAITING_FOR_HUMAN_APPROVAL = "waiting_for_human_approval"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class WorkflowStepStatus(StrEnum):
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    BLOCKED = "blocked"
    WAITING = "waiting"
    RETRY_REQUIRED = "retry_required"


class HumanApprovalStatus(StrEnum):
    NOT_REQUIRED = "not_required"
    REQUIRED = "required"
    APPROVED = "approved"
    REJECTED = "rejected"
    PENDING = "pending"


class PayloadTrustLevel(StrEnum):
    TRUSTED_SYSTEM_DATA = "trusted_system_data"
    UNTRUSTED_USER_INPUT = "untrusted_user_input"
    UNTRUSTED_RETRIEVED_CONTENT = "untrusted_retrieved_content"
    UNTRUSTED_TOOL_OUTPUT = "untrusted_tool_output"
    UNTRUSTED_MODEL_OUTPUT = "untrusted_model_output"
