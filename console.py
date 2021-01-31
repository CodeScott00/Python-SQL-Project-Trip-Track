import pdb
from models.country import Country
from models.destination import Destination

import repositories.country_repository as country_repository
import repositories.destination_repository as destination_repository


country_repository.delete_all()
destination_repository.delete_all()

# country_repository.select_all()
# destination_repository.select_all()

country1 = Country('Brazil', '212 million')
country_repository.save(country1)

country2 = Country('Australia', '25 million')
country_repository.save(country2)


destination_1 = Destination('Foz do Iguacu', country1)
destination_repository.save(destination_1)

destination_2 = Destination('Sydney', country2)
destination_repository.save(destination_2)


pdb.set_trace()