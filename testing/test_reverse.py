import pytest
from applications import reverse

def test_reverse_string():
    assert reverse.reverse("hello")

def test_reverse_caps():
    assert reverse.reverse("H Ello")

