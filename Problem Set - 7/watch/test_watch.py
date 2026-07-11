from watch import parse


def test_valid_youtube_urls():
    # Test standard secure embed link
    assert parse('<iframe src="https://youtube.com"></iframe>') == "https://youtu.be"
    # Test non-www secure embed link
    assert parse('<iframe src="https://youtube.com"></iframe>') == "https://youtu.be"
    # Test non-secure HTTP embed link
    assert parse('<iframe src="http://youtube.com"></iframe>') == "https://youtu.be"


def test_html_attribute_variations():
    # Test attributes in a different order
    assert parse(
        '<iframe width="560" height="315" src="https://youtube.com" frameborder="0"></iframe>') == "https://youtu.be"
    # Test single quotes instead of double quotes
    assert parse("<iframe src='https://youtube.com'></iframe>") == "https://youtu.be"


def test_invalid_or_non_youtube_urls():
    # Test a completely different website inside an iframe
    assert parse('<iframe src="https://harvard.edu"></iframe>') is None
    # Test a different video platform (Vimeo)
    assert parse('<iframe src="https://vimeo.com"></iframe>') is None


def test_malformed_html_and_text():
    # Test plain text without HTML tags
    assert parse("Just a plain text string with no links") is None
    # Test a YouTube link that is not an embed link
    assert parse('<a href="https://youtube.com">Click Here</a>') is None
