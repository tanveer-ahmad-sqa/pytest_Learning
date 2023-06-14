import pytest


@pytest.mark.math
def test_one_plus_one():
    assert 1 + 1 == 2


@pytest.mark.math
def test_failed_assertion():
    name = 'Testing'
    field_value = 'Test'
    assert name in field_value


@pytest.mark.math
def test_handle_exception():
    # import pytest
    with pytest.raises(ZeroDivisionError) as e:
        results = 1 / 0
        print(e.value)
    assert 'division by zero' in str(e.value)


def myfunc():
    raise ValueError("Exception 123 raised")


@pytest.mark.math
def test_match():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myfunc()
