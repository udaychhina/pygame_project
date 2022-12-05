import flask
from components import score

app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template("index.html")


@app.route("/score")
def get_score():
    score_data = score.Score()
    score_data.load_score()
    return flask.render_template("score.html", score_data=score_data)

@app.route("/score-sorted")
def get_score_sorted():
    score_data = score.Score()
    score_data.load_score()
    score_data.scores["scores"] = dict(sorted(score_data.scores["scores"].items(), key=lambda item: item[1], reverse=True))
    return flask.render_template("scores-sorted.html", score_data=score_data)

if __name__ == "__main__":
    app.run(debug=True)
