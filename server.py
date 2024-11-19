from flask import Flask, request
from games import GamesDB
app = Flask(__name__)

@app.route("/games/<int:game_id>", methods=["OPTIONS"])
def handle_cors(game_id):
    return "", 204, {"Access-Control-Allow-Origin": "*",
                     "Access-Control-Allow-Methods": "PUT, DELETE",
                     "Access-Control-Allow-Headers": "Content-Type"}

@app.route("/games/<int:game_id>", methods=["GET"])
def retrieve_game(game_id):
    db = GamesDB()
    game = db.fetchone(game_id)
    if not game:
        return "Could not find game with ID " + str(game_id), 404, {"Access-Control-Allow-Origin" : "*"}
    return game, 200, {"Access-Control-Allow-Origin": "*"}

@app.route("/games/<int:game_id>", methods=["DELETE"])
def delete_game(game_id):
    db = GamesDB()
    game = db.fetchone(game_id)
    if not game:
        return "Could not find game with ID " + str(game_id), 404, {"Access-Control-Allow-Origin" : "*"}
    db.delete(game_id)
    return "Deleted", 200, {"Access-Control-Allow-Origin" : "*"}


@app.route("/games",methods=["GET"])
def retrieve_games():
    db = GamesDB()
    return db.fetchall(), 200, {"Access-Control-Allow-Origin" : "*"}

@app.route("/games",methods=["POST"])
def create_game():
    db = GamesDB()
    print("The request data is: ", request.form)
    request.form.get("name")
    db.create(request.form["name"],
                   request.form["review"],
                   request.form["genres"], request.form["cost"], request.form["esrb_rating"])
    return "Created", 201, {"Access-Control-Allow-Origin" : "*"}

@app.route("/games/<int:game_id>", methods=["PUT"])
def update_game(game_id):
    print("update game with id", game_id)
    db = GamesDB()
    game = db.fetchone(game_id)
    if game:
        name = request.form["name"]
        genres = request.form["genres"]
        review = request.form["review"]
        cost = request.form["cost"]
        esrb_rating = request.form["esrb_rating"]
        
        db.update(game_id, name, genres, review, cost, esrb_rating)
        return "Updated", 200, {"Access-Control-Allow-Origin" : "*"}
    else:
        return "Could not find game with ID " + str(game_id), 404, {"Access-Control-Allow-Origin" : "*"}

def run():
    app.run(port=8080, host="0.0.0.0")

if __name__ == "__main__":
    run()