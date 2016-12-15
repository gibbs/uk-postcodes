UK Postcodes
============

A CSV of UK postal
[out codes](http://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Outward_code).
JSON and YAML datasets are generated and available for tagged versions under
the ```data``` directory.

## Contributing

Please feel free to add contributions and corrections to
the ```postcodes.csv``` CSV. Use a text editor as office applications and
suites may add unnecessary formatting.

## Database Imports

- [MySQL Import Example](#mysql-example)
- [PostgreSQL Import Example](#postgresql-example)
- [MongoDB Import Example](#mongodb-example)

### MySQL Example

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
	uk_region VARCHAR(255) NULL,
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
	@uk_region, @country, @country_string
)
SET
	postcode=@postcode, eastings=@eastings, northings=@northings,
	latitude=@latitude, longitude=@longitude, town=@town, region=@region,
	uk_region=@uk_region, country=@country, country_string=@country_string
;
~~~

### PostgreSQL Example

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
	uk_region VARCHAR(255) NULL,
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

### MongoDB Example

~~~bash
mongoimport -d [your_database_name] -c [collection_name] --type csv --file postcodes.csv --headerline
~~~
