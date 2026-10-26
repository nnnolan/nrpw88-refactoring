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