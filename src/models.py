from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from app import db

# TODO - Create SQLAlchemy DB and Movie model


def create_db(app):
    db = SQLAlchemy(app)
    db.create_all()


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    director = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
