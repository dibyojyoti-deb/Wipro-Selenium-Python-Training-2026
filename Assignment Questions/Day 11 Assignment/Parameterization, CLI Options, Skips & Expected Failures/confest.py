import pytest

# This must be in conftest.py to work
def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev")

@pytest.fixture
def env_config(request):
    return request.config.getoption("--env")