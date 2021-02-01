from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.destination_repository as destination_repository
from models.destination import Destination

destination_blueprint = Blueprint("destination",__name__)

@destination_blueprint.route("/visit")
def show_destinations():
    destinations = destination_repository.select_all()
    return render_template("travel/visit.html", destinations = destinations)

@destination_blueprint.route("/visit/<id>", methods = ['GET'])
def show_destination(id):
    destinations = destination_repository.select(id)
    return render_template("travel/visit.html", destinations = destinations)

@destination_blueprint.route("/visit/new")
def add_destination():
    return render_template("travel/visit_new.html")

@destination_blueprint.route("/visit", methods = ['POST'])
def create_destination():
    destination_name = request.form['destination_name']
    country = request.form['country']
    destination = Destination(destination_name, country) #somethings wrong here
    destination_repository.save(destination)
    return redirect ('/visit')


# @destination_blueprint.route("/home")
# def show_destinations_home():
#     destination = destination_repository.select_all()
#     return render_template("travel/been.html", destination = destination)