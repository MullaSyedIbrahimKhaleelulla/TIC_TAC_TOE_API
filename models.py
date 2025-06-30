from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_x = db.Column(db.String(50))
    player_o = db.Column(db.String(50))
    board_state = db.Column(db.String(9))      
    winner = db.Column(db.String(1))  
