from pathlib import Path


def test_required_project_folders_exist() -> None:
    project_root = Path(__file__).resolve().parents[1]

    required_folders = [
        "services/agent_control_plane",
        "services/workflow_patterns",
        "services/observability",
        "services/mock_external_systems",
        "evaluation_harness/golden_test_cases",
        "evaluation_harness/graders",
        "evaluation_harness/report_generation",
        "evaluation_harness/trace_replay",
        "traces",
        "reports",
        "docs",
        "diagrams",
    ]

    for folder_path in required_folders:
        assert (project_root / folder_path).exists(), f"Missing folder: {folder_path}"
