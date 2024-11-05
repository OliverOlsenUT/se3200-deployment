import sqlite3

class GamesDB:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("games.db")
        # use connection instance to perform db operations
        # create a cursor instance for the connection
        self.cursor = self.connection.cursor()
        self.cursor.row_factory = sqlite3.Row
    def fetchall(self):
        self.cursor.execute("SELECT * FROM games")
        games = self.cursor.fetchall()
        L = []
        for game in games:
            L.append(row_game_to_object(game))
        return L
    def fetchone(self, game_id):
        data = [game_id]
        self.cursor.execute("SELECT * FROM games WHERE id = ?", data)
        game = row_game_to_object(self.cursor.fetchone())
        return game
    def create(self, name, review, genres, cost, esrb_rating):
        data = [name, review, genres, cost, esrb_rating]
        self.cursor.execute("INSERT INTO games(name,review,genres,cost,esrb_rating)VALUES(?, ?, ?, ?, ?)", data)
        self.connection.commit()
    def update(self, game_id, name, genres, review, cost, esrb_rating):
        data = [name, review, genres, cost, esrb_rating, game_id]
        self.cursor.execute("UPDATE games SET name = ?, review = ?, genres = ?, cost = ?, esrb_rating = ? WHERE id = ?", data)
        self.connection.commit()
    def delete(self, game_id):
        self.cursor.execute("DELETE FROM games WHERE id = ?", [game_id])
        self.connection.commit()
def row_game_to_object(game):
    if not game:
        return None
    obj = {"id": game["id"],
           "name": game["name"],
           "review": game["review"],
           "genres": game["genres"],
           "esrb_rating": game["esrb_rating"],
           "cost": game["cost"]}
    return obj

if __name__ == "__main__":
    print("To run the server, run server.py")