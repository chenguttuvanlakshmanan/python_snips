import main
import pytest

# the test file should start with test or end with test 
# to run the test type pytest in the terminal
# stop running functions after first fail pytest -x  pytest --maxfial=2
# to get available functions in the pytest pytest --fixtures
# to run test in a class pytest -k TestClass
# to run particular test function inside a file pytest test_mod.py::test_func


#*****************testing report
# to get detailed report summary of the test performed pytest -ra,-ra [ all expect pass] , -rp [ all passed test]
# -rs[skipped tests]

# simple function test using pytest
def test_add():
    assert(main.add(5,4) == 10)

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



     