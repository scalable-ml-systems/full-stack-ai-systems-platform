from agent_control_plane.package_metadata import PROJECT_NAME, PROJECT_VERSION


def test_project_foundation_is_configured() -> None:
    assert PROJECT_NAME == "agent-systems-architecture"
    assert PROJECT_VERSION == "0.1.0"
