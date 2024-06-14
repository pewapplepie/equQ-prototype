from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import UniqueConstraint
from dataclasses import dataclass

import requests

core = Flask(__name__)

CORS(core)

# Specifying the database:
core.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://microservice:microservice@db/core'

db = SQLAlchemy(core)


# Creating the School model:
@dataclass
class School(db.Model):
    id: int
    name: str
    logo: str
    description: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    logo = db.Column(db.String(255), nullable=True)
    description = db.Column(db.Text, nullable=True)


# Creating the Degree model:
@dataclass
class Degree(db.Model):
    id: int
    name: str
    school_id: int
    level: str
    description: str
    curriculum: str
    application_deadline: str
    apply_link: str
    view_count: int

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'), nullable=False)
    level = db.Column(db.String(1), nullable=False)  # B for Bachelor, M for Master, P for PhD
    description = db.Column(db.Text, nullable=True)
    curriculum = db.Column(db.Text, nullable=True)
    application_deadline = db.Column(db.Date, nullable=True)
    apply_link = db.Column(db.String(255), nullable=True)
    view_count = db.Column(db.Integer, default=0)

    school = db.relationship('School', back_populates='degrees')


# Creating the DegreeView model:
@dataclass
class DegreeView(db.Model):
    id: int
    degree_id: int
    user_id: int
    view_date: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    degree_id = db.Column(db.Integer, db.ForeignKey('degree.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    view_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    degree = db.relationship('Degree', back_populates='degree_views')
    user = db.relationship('User', back_populates='degree_views')


# Creating the User model:
@dataclass
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255))
    profile_picture = db.Column(db.String(255))
    date_of_birth = db.Column(db.Date)
    bio = db.Column(db.Text)
    interests = db.Column(db.Text)

    UniqueConstraint('degree_id', 'user_id', name='degree_user_unique')


# Setting up relationships
School.degrees = db.relationship('Degree', order_by=Degree.id, back_populates='school')
Degree.degree_views = db.relationship('DegreeView', order_by=DegreeView.id, back_populates='degree')
Degree.students = db.relationship('UserProfile', order_by=UserProfile.id, back_populates='degree')


@core.route('/')
def index():
    return '<h1>Hello World!</h1>'


if __name__ == '__main__':
    core.run(host='0.0.0.0', port=5000, debug=True)
