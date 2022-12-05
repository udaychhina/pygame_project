import flask
from components import score

app = flask.Flask(__name__)


@app.route("/")
def index():
    score_data = score.Score()
    score_data.load_score()

    return flask.render_template("index.html", score_data=score_data)


if __name__ == "__main__":
    app.run(debug=True)
