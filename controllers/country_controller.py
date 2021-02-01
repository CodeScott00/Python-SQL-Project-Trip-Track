from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.country_repository as country_repository
from models.country import Country 
from controllers import controller
# from app import app

travel_blueprint = Blueprint("travel",__name__)

@travel_blueprint.route("/been")
def show_countries():
    # countries = country_repository.select_all()
    # return render_template("travel/search.html", countries = countries)
    return "hello"
