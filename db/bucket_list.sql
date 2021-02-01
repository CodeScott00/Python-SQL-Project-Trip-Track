DROP TABLE IF EXISTS destinations;
DROP TABLE IF EXISTS countries;


CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    country_name VARCHAR (255),
    country_population VARCHAR(255),
    country_visited BOOLEAN
);

CREATE TABLE destinations (
    id SERIAL PRIMARY KEY,
    destination_name VARCHAR(255),
    country_id INT REFERENCES countries(id)
);