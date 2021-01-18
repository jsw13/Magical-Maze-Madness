""" This file is the main controller for the maze game score web application. """

from flask import Flask, request, render_template, redirect
from models.score_manager import ScoreManager
from models.score import Score

app = Flask(__name__)
score_manager = ScoreManager()

@app.route("/")
def display_scores():
    return render_template("scores.html", scores=score_manager.scores)

@app.route("/api/list", methods=["GET", "DELETE"])
def list_all_scores():
    if request.method == "GET":
        return {"scores": score_manager.scores}, 200

    elif request.method == "DELETE":
        data = request.get_json()

        if data is None:
            return "Invalid data received", 400
        
        if "name" in data:
            print("Valid data received")
        else:
            return "Invalid data received", 400

        try:
            user_name = data["name"]
        except ValueError:
            return "Invalid data received", 400
        else:
            score_manager.remove_user_score(user_name)

        return "", 204

@app.route("/api/new", methods=["PUT"])
def add_new_score():
    data = request.get_json()

    if data is None:
        return "Invalid data received", 400

    if "name" in data and "score" in data:
        print("Valid data received")
    else:
        return "Invalid data received", 400

    try:
        score = Score(data["name"], data["score"])
    except ValueError:
        return "Invalid data received", 400
    else:
        score_manager.add_score(score)

    return "", 204

@app.route("/api/delete", methods=["POST"])
def delete_scores():
    user_name = request.form.get("score_name")
    if user_name == "Delete All":
            score_manager.remove_all_scores()
    else:
        score_manager.remove_user_score(user_name)
    score_manager.to_json("scores.json")
    return redirect("/")


if __name__ == "__main__":
    score_manager.from_json("scores.json")
    app.run(debug=True, port=5000)

