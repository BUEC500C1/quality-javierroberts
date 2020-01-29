import pytest
from converter import romanConverter


def test_romanConverter_1():
    assert romanConverter(1) == "I"


def test_romanConverter_4():
    assert romanConverter(4) == "IV"


def test_romanConverter_5():
    assert romanConverter(5) == "V"


def test_romanConverter_10():
    assert romanConverter(10) == "X"


def test_romanConverter_40():
    assert romanConverter(40) == "XL"


def test_romanConverter_50():
    assert romanConverter(50) == "L"


def test_romanConverter_90():
    assert romanConverter(90) == "XC"


def test_romanConverter_100():
    assert romanConverter(100) == "C"


def test_romanConverter_400():
    assert romanConverter(400) == "CD"


def test_romanConverter_500():
    assert romanConverter(500) == "D"


def test_romanConverter_900():
    assert romanConverter(900) == "CM"


def test_romanConverter_1000():
    assert romanConverter(1000) == "M"


def test_romanConverter_2020():
    assert romanConverter(2020) == "MMXX"


def test_romanConverter_letter():
    assert romanConverter("4a0") == "Error, input is not integer"


def test_romanConverter_decimal():
    assert romanConverter("2.2") == "Error, input is not integer"


def test_romanConverter_empty():
    assert romanConverter() == ""


def test_romanConverter_0():
    assert romanConverter(0) == "Error, no zero conversion"


def test_romanConverter_negative():
    assert romanConverter(-4) == "Error, negative number"
