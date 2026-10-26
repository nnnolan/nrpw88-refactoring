import math

# performance calculator class to encapsulate the logic for calculating
# the amount and volume credits for a performance

class PerformanceCalculator:
    def __init__(self, play, audience):
        self.play = play
        self.audience = audience

    @property
    def amount(self):
        # tragedy is 40000 for the first 30 seats, then 1000 for each additional seat
        if self.play['type'] == "tragedy":
            amount = 40000
            if self.audience > 30:
                amount += 1000 * (self.audience - 30)
        # comedy is 30000, plus 10000 and 500 per seat beyond 20, plus 300 per seat
        elif self.play['type'] == "comedy":
            amount = 30000
            if self.audience > 20:
                amount += 10000 + 500 * (self.audience - 20)
            amount += 300 * self.audience
        else:
            raise ValueError(f'unknown type: {self.play["type"]}')
        return amount

    @property
    def volume_credits(self):
        credits = max(self.audience - 30, 0)
        # extra credit for every five comedy attendees
        if self.play['type'] == "comedy":
            credits += math.floor(self.audience / 5)
        return credits

def statement(invoice: dict, plays: dict) -> str:
    """
        invoice -> dict
        plays -> dict

        this function takes a customer invoice and a list of plays
        and returns a statement string with the total amount owed and volume credits earned
        
        on successful execution, the statement will look like this:
        Statement for BigCo
            Hamlet: $650.00 (55 seats)
            As You Like It: $580.00 (35 seats)
            Amount owed is $1,230.00
            You earned 47 credits
            
        if an error occurs, the function will raise a ValueError
        with a message indicating the type of error
        
    """

    def format_as_dollars(amount):
        return f"${amount:0,.2f}"

    def play_for(performance):
        return plays[performance['playID']]

    # using the above class
    def calculator_for(performance):
        return PerformanceCalculator(play_for(performance), performance['audience'])

    def total_amount():
        return sum(calculator_for(perf).amount for perf in invoice['performances'])

    def total_volume_credits():
        return sum(calculator_for(perf).volume_credits for perf in invoice['performances'])

    result = f'Statement for {invoice["customer"]}\n'
    for perf in invoice['performances']:
        result += f' {play_for(perf)["name"]}: {format_as_dollars(calculator_for(perf).amount / 100)} ({perf["audience"]} seats)\n'
    result += f'Amount owed is {format_as_dollars(total_amount() / 100)}\n'
    result += f'You earned {total_volume_credits()} credits\n'
    return result
    # return the statement string
    result = f'Statement for {invoice["customer"]}\n'
    for perf in invoice['performances']:
        result += f' {play_for(perf)["name"]}: {format_as_dollars(amount_for(perf) / 100)} ({perf["audience"]} seats)\n'
    result += f'Amount owed is {format_as_dollars(total_amount() / 100)}\n'
    result += f'You earned {total_volume_credits()} credits\n'
    return result