class Country:

    def __init__(self, country_name, country_population, id = None):
        self.country_name = country_name
        self.country_population = country_population
        self.id = id 

    def country_city_name(self):
        return f"{self.country_name} {self.country_population}"


