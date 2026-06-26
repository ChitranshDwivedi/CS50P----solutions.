import twttr

from twttr import shorten

def test_shorten_lowercase():
    assert shorten("twitter") == "twttr"

def test_shorten_uppercase():
    assert shorten("TWITTER") == "TWTTR"

def test_shorten_numbers():
    assert shorten("cs50") == "cs50"

def test_shorten_punctuation():
    assert shorten("hello, world!") == "hll, wrld!"
