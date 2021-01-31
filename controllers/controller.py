from flask import Flask, render_template, request, redirect
from flask import Blueprint
# from app import app

travel_blueprint = Blueprint("travel",__name__)


@travel_blueprint.route('/home', methods = ['GET'])
def new_entry():
    return render_template('travel/search.html')

# @travel_blueprint.route('home', methods = )