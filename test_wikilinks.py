import re
import pytest

from wikilinks import wikilinks

def test_links():
    count = 0
    for source, target in wikilinks("http://mith.umd.edu"):
        count += 1
        assert source
        assert re.match("^https://..\.wikipedia.org/wiki", source)
        assert target
        assert re.match("^http://mith\.umd\.edu", target)
    assert count > 0

def test_langs():
    count = 0
    for source, target in wikilinks("http://mith.umd.edu", langs=["en"]):
        count += 1
        assert source
        assert target
        assert re.match("^https://en\.wikipedia\.org/wiki", source)
        assert re.match("^http://mith\.umd\.edu", target)
    assert count > 0

def test_two_langs():
    count = 0
    for source, target in wikilinks("http://mith.umd.edu", langs=["en", "fr"]):
        count += 1
        assert source
        assert target
        assert re.match("^https://(en|fr)\.wikipedia\.org/wiki", source)
        assert re.match("^http://mith\.umd\.edu", target)
    assert count > 0

def test_invalid_lang():
    with pytest.raises(Exception) as e:
        links = list(wikilinks("http://mith.umd.edu", langs=["en", "zz"]))
    assert e.match('invalid language code zz')
