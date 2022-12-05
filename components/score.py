import json
import datetime


class Score:
    def __init__(self):
        self.scores = {}
        self.load_score()
        self.highest = self.scores["highest"]


    def save_score(self):
        with open('components/score.json', 'w') as f:
            json.dump(self.scores, f)

    def load_score(self):
        with open('components/score.json', 'r') as f:
            self.scores = json.load(f)

    def update(self, points):
        self.scores["latest"] = points
        self.scores["scores"].update({datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"): points})
        if self.scores["latest"] > self.scores["highest"]:
            self.scores["highest"] = self.scores["latest"]
        self.save_score()

    def __str__(self):
        return f'{self.scores["latest"]}'

    def __add__(self, point):
        return self.update(point)