import os
import warnings
import pytest

def test_hello():
    assert True == True

@pytest.mark.skip(reason="Skip this test unless you want to test the setup")
def test_environs():
    env_vars = ['LL7MA_DB']
    for env_var in env_vars:
        assert os.getenv(env_var) is not None
