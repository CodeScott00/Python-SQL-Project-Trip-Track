from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.country_repository as country_repository
import repositories.destination_repository as destination_repository
# from app import app

travel_blueprint = Blueprint("travel",__name__)


@travel_blueprint.route('/home', methods = ['GET'])
def new_entry():
    countries = country_repository.select_all()
    destinations = destination_repository.select_all()

    return render_template('search.html',title = "Home", countries = countries, destinations = destinations)

@travel_blueprint.route('/inspiration', methods = ['GET'])
def inspo():
    return render_template("inspo.html")