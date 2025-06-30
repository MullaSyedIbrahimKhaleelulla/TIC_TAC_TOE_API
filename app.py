from flask import Flask, request, render_template, jsonify
from models import db, Game

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ibrahim1234@localhost:5432/tic_tac_toe_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_game', methods=['POST'])
def new_game():
    data = request.json
    new_game = Game(
        player_x=data['player_x'],
        player_o=data['player_o'],
        board_state=' ' * 9,
        winner=None
    )
    db.session.add(new_game)
    db.session.commit()
    return jsonify({"game_id": new_game.id}), 201

@app.route('/play/<int:game_id>', methods=['POST'])
def play(game_id):
    data = request.json
    game = Game.query.get(game_id)
    if game:
        game.board_state = data['board_state']
        game.winner = data['winner']
        db.session.commit()
        return jsonify({"message": "Move saved."})
    return jsonify({"error": "Game not found"}), 404

@app.route('/game/<int:game_id>', methods=['GET'])
def get_game(game_id):
    game = Game.query.get(game_id)
    if game:
        return jsonify({
            "id": game.id,
            "player_x": game.player_x,
            "player_o": game.player_o,
            "board_state": game.board_state,
            "winner": game.winner
        })
    return jsonify({"error": "Game not found"}), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
