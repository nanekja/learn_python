import myprogram2
import os
import shutil
import pytest

class TestDoubleit(object):

    numbers_file_template = './oops/6_efficiency_testing/testnums_template.txt'
    numbers_file_testor = './oops/6_efficiency_testing/testnums.txt'

    def setup_class(self):
        shutil.copy(TestDoubleit.numbers_file_template, TestDoubleit.numbers_file_testor)

    def teardown_class(self):
        os.remove(TestDoubleit.numbers_file_testor)

    def test_doublelines(self):
        myprogram2.doublelines(TestDoubleit.numbers_file_testor)
        old_vals=[int(line) for line in open(TestDoubleit.numbers_file_template)]
        new_vals=[int(line) for line in open(TestDoubleit.numbers_file_testor)]
        for old_val, new_val in zip(old_vals, new_vals):
            assert int(new_val) == int(old_val) * 2

    def test_doubleit_value(self):
        assert myprogram2.doubleit(10)==20

    def test_doubleit_type(self):
        with pytest.raises(TypeError):
            myprogram2.doubleit('hello')

