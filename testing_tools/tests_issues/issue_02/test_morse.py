import pytest
from morse import decode


@pytest.mark.parametrize(
    ("input", "output"),
    [
        ("... --- ...", "SOS"),
        ("... - --- .-. -.-- -....- - .- .-.. .", "STORY-TALE"),
        (".--. .. --.. --.. .- -..-. ... ..- ... .... ..", "PIZZA/SUSHI"),
        ("-. . -..- - -.--. .---- ----- -.--.-", "NEXT(10)"),
    ],
)
def test_decode(input, output):
    """Testing correct messages"""
    assert decode(input) == output
