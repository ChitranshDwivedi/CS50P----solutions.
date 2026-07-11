from um import count

def test_um_basic():
    assert count("um") == 1

def test_um_case_insensitive():
    assert count("Um, hello") == 1

def test_um_not_substring():
    assert count("yummy") == 0

def test_um_multiple():
    assert count("um um um") == 3

def test_um_in_sentence():
    assert count("hello, um, world") == 1
