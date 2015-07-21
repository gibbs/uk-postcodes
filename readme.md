UK Postcodes
============

A CSV of UK postal 
[out codes](http://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Outward_code).


## Contributing

Please feel free to add contributions and corrections to the CSV. Use a text
editor as office applications and suites may add unnecessary formatting.

## MySQL Import Example

Table creation.

~~~sql
CREATE TABLE outcodes (
	id INT NOT NULL AUTO_INCREMENT,
	postcode VARCHAR(5) NOT NULL,
	eastings INT(7) NOT NULL,
	northings INT(7) NOT NULL,
	latitude DECIMAL(10, 8) NOT NULL,
	longitude DECIMAL(11, 8) NOT NULL,
	town VARCHAR(255) NULL,
	region VARCHAR(255) NULL,
	country VARCHAR(3) NULL,
	country_string VARCHAR(255) NULL,
	PRIMARY KEY(id)
);
~~~

Import CSV file to table.

~~~bash
mysql -u root -p --local-infile=1
~~~

~~~sql
LOAD DATA LOCAL INFILE '/path/to/postcodes.csv'
INTO TABLE databasename.outcodes
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n'
IGNORE 1 LINES
(
	@postcode, @eastings, @northings, @latitude, @longitude, @town, @region,
	@country, @country_string
)
SET
	postcode=@postcode, eastings=@eastings, northings=@northings,
	latitude=@latitude, longitude=@longitude, town=@town, region=@region,
	country=@country, country_string=@country_string
;
~~~

## PostgresSQL Import Example

Table creation.

~~~sql
CREATE TABLE outcodes (
	postcode VARCHAR(5) NOT NULL,
	eastings INT(7) NOT NULL,
	northings INT(7) NOT NULL,
	latitude DECIMAL(10, 8) NOT NULL,
	longitude DECIMAL(11, 8) NOT NULL,
	town VARCHAR(255) NULL,
	region VARCHAR(255) NULL,
	country VARCHAR(3) NULL,
	country_string VARCHAR(255) NULL,
);
~~~


Import CSV file to table.
Navigate to the directory where your postcodes.csv is stored.

~~~bash
psql [your_database_name]
~~~

~~~sql
\copy outcodes FROM 'postcodes.csv' WITH HEADER CSV
~~~

Add an additional 'id' column to make corrections and/or updates easier.

~~~sql
ALTER TABLE outcodes ADD id serial NOT NULL PRIMARY KEY;
~~~
