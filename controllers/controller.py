from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.country_repository as country_repository
# from app import app

travel_blueprint = Blueprint("travel",__name__)


@travel_blueprint.route('/home', methods = ['GET'])
def new_entry():
    countries = country_repository.select_all()
    
    return render_template('travel/search.html',title = "Home", countries = countries)

# @travel_blueprint.route('home', methods = )