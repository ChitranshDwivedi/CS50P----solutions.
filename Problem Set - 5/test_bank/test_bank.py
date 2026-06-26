import bank

from bank import value

# 1. Test case-insensitivity and standard "hello" greetings ($0)
def test_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("Hello, Newman") == 0

# 2. Test greetings that start with 'h' but aren't 'hello' ($20)
def test_h_greetings():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("How's it going?") == 20

# 3. Test entirely different greetings ($100)
def test_other_greetings():
    assert value("What's up?") == 100
    assert value("Good morning") == 100
