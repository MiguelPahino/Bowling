class ScoreCard:
    def __init__(self,score_card):
        self.pins = score_card
        self.score = 0
        self.last_frame = None
        self.frame = 1

    def calculate_points(self,pins):
        points = 0
        if self.last_frame == "x":
            points = (pins[0] + pins[1]) * 2
        elif self.last_frame == "/":
            points = pins[0] * 2 + pins[1]
        else:
            points = pins[0] + pins[1]
        return points

    def roll(self,pins):
        if self.frame == 10:

        else:

    def frame(self,roll):