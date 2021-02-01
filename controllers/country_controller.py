from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.country_repository as country_repository
import repositories.destination_repository as destination_repository
from models.country import Country 
# from controllers import controller
# from app import app

country_blueprint = Blueprint("countries",__name__)

@country_blueprint.route("/been")
def show_countries():
    countries = country_repository.select_all()
    return render_template("travel/been.html", countries = countries)

@country_blueprint.route("/been/<id>", methods = ['GET'])
def show_country(id):
    countries = country_repository.select(id)
    return render_template("travel/been.html", countries = countries)


@country_blueprint.route("/been/new")
def add_country():
    return render_template("travel/new.html")




@country_blueprint.route("/been", methods = ['POST'])
def create_country():
    country_name = request.form['country_name']
    country_population = request.form['country_population']
    country_visited = request.form['country_visited']
    country = Country(country_name, country_population, country_visited)
    country_repository.save(country)
    return redirect ('/been')




    
    

