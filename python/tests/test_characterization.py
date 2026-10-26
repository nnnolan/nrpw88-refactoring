from statement import statement

PLAYS = {
    "t": {"name": "Hamlet", "type": "tragedy"},
    "c": {"name": "As You Like It", "type": "comedy"},
}

# build a one-performance invoice and run the statement function with it
def run(play_id, audience):
    invoice = {"customer": "Test", "performances": [{"playID": play_id, "audience": audience}]}
    return statement(invoice, PLAYS)

def test_tragedy_charge_and_credits_around_30_seat_threshold():
    # there shouldnt be a surcharge or credit at 30
    # each seat above 30 adds $10 and 1 credit
    at_30 = run("t", 30)
    assert " Hamlet: $400.00 (30 seats)" in at_30
    assert "You earned 0 credits" in at_30

    at_31 = run("t", 31)
    assert " Hamlet: $410.00 (31 seats)" in at_31
    assert "You earned 1 credits" in at_31


def test_comedy_charge_around_20_seat_threshold():
    # above 20 seats, comedy adds a $100 lump sum plus $5 per seat beyond 20
    # alongside with the $3 per seat base charge
    at_20 = run("c", 20)
    assert " As You Like It: $360.00 (20 seats)" in at_20

    at_21 = run("c", 21)
    assert " As You Like It: $468.00 (21 seats)" in at_21