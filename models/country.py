class Country:

    def __init__(self, country_name, country_population, country_visited, id = None):
        self.country_name = country_name
        self.country_population = country_population
        self.country_visited = country_visited
        self.id = id 

    def country_city_name(self):
        return f"{self.country_name} {self.country_population}"


