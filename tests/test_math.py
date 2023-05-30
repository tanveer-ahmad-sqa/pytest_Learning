

def test_one_plus_one():
    assert 1 + 1 == 2


def test_failed_assertion():
    name = 'Testing'
    field_value = 'Test'
    assert name in field_value

