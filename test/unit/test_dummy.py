from python_template.dummy import dummy_add 
import pytest

def test_add_2_3_expect_5():
	assert dummy_add(2, 3) == 5