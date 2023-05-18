import chess.engine
from flask import Flask, request, render_template, send_from_directory

from game import ChessGame

app = Flask(__name__)

game = ChessGame()


# Render the index page
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/assets/<path:path>")
def assets(path):
    return send_from_directory('assets', path)


@app.route("/scripts/<path:path>")
def scripts(path):
    return send_from_directory('scripts', path)


# Handle the move request
@app.route("/move", methods=["POST"])
def move():
    # Get the move string from the client-side
    move_str = request.form["move"]

    app.logger.info(str(request))
    print(request)

    # Create a new chess board
    board = chess.Board()

    # Apply the move to the board
    board.push_uci(move_str)

    # Return the new board position and analysis result
    return {"fen": board.fen(), "analysis": "you're on your own"}


@app.route("/play", methods=["POST"])
def play():
    game.play()
    fen = game.board.fen()
    return {'fen': fen}


if __name__ == "__main__":
    app.run(debug=True)
