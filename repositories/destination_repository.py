from db.run_sql import run_sql

from models.destination import Destination
from models.country import Country 
import repositories.country_repository as country_repository

def save(destination):
    sql = "INSERT INTO destinations (destination_name, country_id) VALUES (%s, %s) RETURNING *"
    values = [destination.destination_name, destination.country.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    destination.id = id
    return destination

def select_all():
    destinations = []

    sql = "SELECT * FROM destinations"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row['country_id'])
        destination = Destination(row['destination_name'], country, row['id'])
        destinations.append(destination)
    return destinations

def select(id):
    destination = None
    sql = "SELECT * FROM destinations WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    if result is not None:
        country = country_repository.select(result['country_id'])
        destination = Destination(result['destination_name'], country, result['id'])
    return destination

def delete_all():
    sql = "DELETE FROM destinations"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM destinations WHERE id = %s"
    values = [id]
    run_sql(sql, values)
        


