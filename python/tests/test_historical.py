import pytest
from statement import statement

PLAYS = {"h": {"name": "Henry V", "type": "historical"}}


def run(audience):
    invoice = {"customer": "Test", "performances": [{"playID": "h", "audience": audience}]}
    return statement(invoice, PLAYS)


def test_spec_example_35_seats():
    out = run(35)
    assert " Henry V: $725.00 (35 seats)" in out
    assert "You earned 7 credits" in out


@pytest.mark.parametrize("audience, amount, credits", [
    (20, "$500.00", 4),   # last seat with no surcharge
    (21, "$515.00", 4),   # first surcharged seat
    (4, "$500.00", 0),    # just below the first credit
    (5, "$500.00", 1),    # first credit
])
def test_historical_boundaries(audience, amount, credits):
    out = run(audience)
    assert f"Henry V: {amount} ({audience} seats)" in out
    assert f"You earned {credits} credits" in out