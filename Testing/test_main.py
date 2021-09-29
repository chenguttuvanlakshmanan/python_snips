import main
import pytest

#******************************Pytest notes*****************************************************************************

# the test file should start with test or end with test 
# to run the test type pytest in the terminal
# stop running functions after first fail pytest -x  pytest --maxfial=2
# to get available functions in the pytest pytest --fixtures
# to run test in a class pytest -k TestClass
# to run particular test function inside a file pytest test_mod.py::test_func

# Will run all tests which are decorated with the @pytest.mark.slow decorator => ( pytest -m slow)
# to attach debugger on failure we can use pytest --pdb


# ==>>>> Detailed Report

# to get detailed report summary of the test performed pytest -ra,-ra [ all expect pass] , -rp [ all passed test]
# -rs[skipped tests]

#******************************Pytest notes*****************************************************************************

# simple function test using pytest, we can fail the test by changing input or result
def test_add():
    assert(main.add(5,4) == 9)

# this will group tests
class TestClass:
    def test_add(self):
        x = "hello"
        assert "h" in x

    def test_addother(self):
        assert(main.add(5,3) ==  8)

#function raises a error
def f():
    raise SystemExit(1)

def test_check():
    with pytest.raises(SystemExit):
        f()



     