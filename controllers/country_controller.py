from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.country_repository as country_repository
import repositories.destination_repository as destination_repository
from models.country import Country 
# from controllers import controller
# from app import app

country_blueprint = Blueprint("countries",__name__)

#index
@country_blueprint.route("/countries")
def show_countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", countries = countries)

#show
@country_blueprint.route("/countries/<id>", methods = ['GET'])
def show_country(id):
    countries = country_repository.select(id)
    return render_template("countries/show.html", countries = countries)
#TO do - have a link on countries list to show a single country

#new - Showing the form
@country_blueprint.route("/countries/new")
def add_country():
    return render_template("countries/new.html")

#Create - where the form posts to
@country_blueprint.route("/countries", methods = ['POST'])
def create_country():
    country_name = request.form['country_name']
    country_population = request.form['country_population']
    country_visited = False
    if 'country_visited' in request.form:
        country_visited = True
    country = Country(country_name, country_population, country_visited)
    country_repository.save(country)
    return redirect('/countries')

#delete attempt
@country_blueprint.route("/countries/<id>/delete", methods = ["POST"])
def delete_country(id):
    country_repository.delete(id)
    return redirect ("/countries")

@country_blueprint.route("/countries/<id>/edit", methods = ["GET"])
def country_edit(id):
    country = country_repository.select(id)
    return render_template('countries/edit.html', country = country)
    


#update attempt
@country_blueprint.route("/countries/<id>", methods = ["POST"])
def update_country(id):
    country_name = request.form['country_name']
    country_population = request.form['country_population']
    country_visited = False
    print(request.form)
    if 'visited' in request.form:
        country_visited = True
        print(request.form)
    country = Country(country_name, country_population, country_visited, id)
    country_repository.update(country)
    return redirect ("/countries")



    
    

