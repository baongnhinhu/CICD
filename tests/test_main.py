from scr.main import add


def test_add_funtion():
    assert add(3, 2) == 5
    assert add(2, 2) == 4
    assert add(2, 1) == 3
