import pytest

# Since pytest_addoption is being finicky in your environment, 
# we will use a "request.config" check which is more stable.

@pytest.fixture
def env_config(pytestconfig):
    # This looks for the option; if not found, it defaults to 'dev'
    return pytestconfig.getoption("--env", default="dev")

# 1. Parameterize multiple inputs
@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (10, 20, 30)])
def test_addition(a, b, expected):
    assert a + b == expected

# 2. Skip marker
@pytest.mark.skip(reason="Skipping as requested")
def test_skip_me():
    assert True

# 3. Xfail marker
@pytest.mark.xfail(reason="Expected to fail")
def test_fail_me():
    assert 1 == 2

# 4. Logic using the custom option
def test_env_logic(env_config):
    print(f"\nTarget Environment: {env_config}")
    assert env_config in ["dev", "prod"]