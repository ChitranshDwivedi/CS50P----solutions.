from working import convert

def test_am_to_pm():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_no_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_midnight():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"

def test_invalid_raises():
    try:
        convert("13:00 AM to 5:00 PM")
        assert False
    except ValueError:
        pass

def test_invalid_minutes():
    try:
        convert("9:60 AM to 5:00 PM")
        assert False
    except ValueError:
        pass

def test_no_to():
    try:
        convert("9:00 AM 5:00 PM")
        assert False
    except ValueError:
        pass
