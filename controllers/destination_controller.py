from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.destination_repository as destination_repository
import repositories.country_repository as country_repository
from models.destination import Destination

destination_blueprint = Blueprint("destination",__name__)

@destination_blueprint.route("/destinations")
def show_destinations():
    destinations = destination_repository.select_all()
    return render_template("destinations/index.html", destinations = destinations)

@destination_blueprint.route("/destinations/<id>", methods = ['GET'])
def show_destination(id):
    destinations = destination_repository.select(id)
    return render_template("destinations/show.html", destinations = destinations)
#TO DO - Make template for sho

@destination_blueprint.route("/destinations/new")
def add_destination():
    countries = country_repository.select_all()
    print(countries)
    return render_template("destinations/new.html", countries=countries)

@destination_blueprint.route("/destinations", methods = ['POST'])
def create_destination():
    destination_name = request.form['destination_name']
    country_id = request.form['country_id']
    country = country_repository.select(country_id)
    destination = Destination(destination_name, country) 
    destination_repository.save(destination)
    return redirect('/destinations')


#delete attempt
@destination_blueprint.route("/destinations/<id>/delete", methods = ["POST"])
def delete_destination(id):
    destination_repository.delete(id)
    return redirect ("/destinations")