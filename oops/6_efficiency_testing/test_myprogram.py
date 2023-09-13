############### in a file called test_myprogram.py ############ This is the testing program
# The name "test" prepended to the name of our script and our function is required for Python to be able to find it when we first run pytest
import myprogram
import pytest

# unit test 1
def test_doubleit():
    assert myprogram.doubleit(10)==20

# unit test 2
def test_doubleit_type():
    with pytest.raises(TypeError):     # It's sort of like saying I assert my program double at hello raises type error.
        myprogram.doubleit('hello')


