import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class PromoSale(db.Model):
    __tablename__ = 'Промоакция'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    prizes = db.relationship('Participant', backref='PromoSale', lazy=True)


class Prize(db.Model):
    __tablename__ = 'Приз'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text(), nullable=False)


class Participant(db.Model):
    __tablename__ = 'Участник'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    promosale_id = db.Column(db.Integer, db.ForeignKey('promosale.id'),
                             nullable=False)


class Result(db.Model):
    __tablename__ = 'Результат проведения розыгрыша'

    winner = db.Column(db.Integer, db.ForeignKey('participant.id'))
    prize = db.Column(db.String(150), db.ForeignKey('prize.id'))
