import math


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

    def amount_for(performance):
        play_type = play_for(performance)['type']
        audience = performance['audience']
        # tragedy is 40000 for the first 30 seats, and then 1000 for each additional seat
        if play_type == "tragedy":
            amount = 40000
            if audience > 30:
                amount += 1000 * (audience - 30)
        # comedy is 30000 for the first 20 seats, and then 10000 plus 500 for each additional seat, plus 300 per seat
        elif play_type == "comedy":
            amount = 30000
            if audience > 20:
                amount += 10000 + 500 * (audience - 20)
            amount += 300 * audience
        else:
            raise ValueError(f'unknown type: {play_type}')
        return amount

    def volume_credits_for(performance):
        credits = max(performance['audience'] - 30, 0)
        # extra credit for every five comedy attendees
        if play_for(performance)['type'] == "comedy":
            credits += math.floor(performance['audience'] / 5)
        return credits

    def total_amount():
        return sum(amount_for(perf) for perf in invoice['performances'])

    def total_volume_credits():
        return sum(volume_credits_for(perf) for perf in invoice['performances'])

    # return the statement string
    result = f'Statement for {invoice["customer"]}\n'
    for perf in invoice['performances']:
        result += f' {play_for(perf)["name"]}: {format_as_dollars(amount_for(perf) / 100)} ({perf["audience"]} seats)\n'
    result += f'Amount owed is {format_as_dollars(total_amount() / 100)}\n'
    result += f'You earned {total_volume_credits()} credits\n'
    return result