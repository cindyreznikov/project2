/*CREATE SCRIPT CREATE DATABASE*/
-- PROCEDURE: public.Create_Charities_Database()

-- DROP PROCEDURE public."Create_Charities_Database"();

CREATE OR REPLACE PROCEDURE public."Create_Charities_Database"(
	)
LANGUAGE 'sql'
AS $BODY$-- Database: Charities

-- DROP DATABASE "Charities";

CREATE DATABASE "Charities"
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

COMMENT ON DATABASE "Charities"
    IS 'Database with USA Charities data for Washington Universityu St Louis Data Analysis, Data Science';$BODY$;

COMMENT ON PROCEDURE public."Create_Charities_Database"()
    IS 'Attention: Use Language SQL.';

/*CREATE PROCEDURE CREATE_OBJECTS*/

-- PROCEDURE: public.Create_Objects()

-- DROP PROCEDURE public."Create_Objects"();

CREATE OR REPLACE PROCEDURE public."Create_Objects"(
	)
LANGUAGE 'sql'
AS $BODY$DROP TABLE IF EXISTS charities CASCADE ;

CREATE TABLE charities (
	    key INTEGER NOT NULL,
		accountability_score	NUMERIC NOT NULL,
		administrative_expenses	NUMERIC,
		charity_name	VARCHAR (128) NOT NULL,
		charity_url	VARCHAR (75) NOT NULL,
		city	VARCHAR (40) NOT NULL,
		cn_advisory	VARCHAR(40),
		compensation_leader_compensation	NUMERIC,
		compensation_leader_expense_percent	NUMERIC,
		compensation_leader_title	VARCHAR(60),
		excess_or_deficit_for_year	NUMERIC,
		financial_score	NUMERIC,
		fundraising_expenses	NUMERIC,
		net_assets	NUMERIC,
		organization_type	VARCHAR(160),
		other_revenue	NUMERIC,
		overall_score	NUMERIC,
		payments_to_affiliates	NUMERIC,
		program_expenses	NUMERIC,
		state	VARCHAR (3) NOT NULL,
		total_contributions	NUMERIC
		) ;
 
 -----------------TABLE CITY_COORD
 --IF SELECT COUNT(*) FROM city_coord = 0:
	DROP TABLE IF EXISTS city_coord CASCADE ;
	CREATE TABLE city_coord (
		Key		INTEGER NOT NULL,
		city	VARCHAR (40) NOT NULL,
		state	VARCHAR (3) NOT NULL,
		lat		NUMERIC,
		lng		NUMERIC
		);
---------------------VIEW
CREATE OR REPLACE VIEW public."charities_view"
 AS
 SELECT charities.accountability_score,
    charities.administrative_expenses,
    charities.charity_name,
    charities.charity_url,
    charities.city,
    charities.state,
    charities.cn_advisory,
    charities.compensation_leader_compensation,
    charities.compensation_leader_expense_percent,
    charities.compensation_leader_title,
    charities.excess_or_deficit_for_year,
    charities.financial_score,
    charities.fundraising_expenses,
    charities.net_assets,
    charities.organization_type,
    charities.other_revenue,
    charities.overall_score,
    charities.payments_to_affiliates,
    charities.program_expenses,
    charities.total_contributions,
    city_coord.lat,
    city_coord.lng
   FROM charities
     JOIN city_coord ON charities.city::text = city_coord.city::text AND charities.state::text = city_coord.state::text;

ALTER TABLE public."charities_view"
    OWNER TO postgres;

 $BODY$;

GRANT EXECUTE ON PROCEDURE public."Create_Objects"() TO pg_read_server_files;

GRANT EXECUTE ON PROCEDURE public."Create_Objects"() TO pg_write_server_files;

GRANT EXECUTE ON PROCEDURE public."Create_Objects"() TO postgres;

GRANT EXECUTE ON PROCEDURE public."Create_Objects"() TO PUBLIC;

GRANT EXECUTE ON PROCEDURE public."Create_Objects"() TO pg_execute_server_program;

GRANT EXECUTE ON PROCEDURE public."Create_Objects"() TO pg_stat_scan_tables;

GRANT EXECUTE ON PROCEDURE public."Create_Objects"() TO pg_read_all_settings;

/*END OF CREATION OF PROCEDURE "Create_Objects"*/
--===============================================

/* BEGIN OF PROCEDURE TO CREATE PROCEDURE Load_charity_data*/
-- PROCEDURE: public.Load_charity_data()

--ATTENTION: you must change the file path to match your workspace

-- DROP PROCEDURE public."Load_charity_data"();

CREATE OR REPLACE PROCEDURE public."Load_charity_data"(
	)
LANGUAGE 'sql'
AS $BODY$COPY public.charities (key, accountability_score, administrative_expenses, 
					   charity_name, charity_url, city, cn_advisory, compensation_leader_compensation,
					   compensation_leader_expense_percent, compensation_leader_title, 
					   excess_or_deficit_for_year, financial_score, fundraising_expenses, 
					   net_assets, organization_type, other_revenue, overall_score, 
					   payments_to_affiliates, program_expenses, state, total_contributions) 
					   FROM 'C:/Users/ronal/wbc/project2/project2/data/charity_data.csv' 
					   DELIMITER ',' CSV HEADER ENCODING 'UTF8';$BODY$;

COMMENT ON PROCEDURE public."Load_charity_data"()
    IS 'Load files charities_data.csv and city_coord.csv in respective tables';
/*END OF CREATION OF PROCEDURE "Load_charity_data"*/
--===============================================	

/* BEGIN OF PROCEDURE TO CREATE PROCEDURE Load_city_coord*/
-- PROCEDURE: public.Load_city_coord()

--ATTENTION: you must change the file path to match your workspace

-- DROP PROCEDURE public."Load_city_coord"();

CREATE OR REPLACE PROCEDURE public."Load_city_coord"(
	)
LANGUAGE 'sql'
AS $BODY$COPY public.city_coord (key, city, state, lat, lng) 
						FROM 'C:/Users/ronal/wbc/project2/project2/data/CITY_COORD.CSV' 
						DELIMITER ',' CSV HEADER ENCODING 'SQL_ASCII';$BODY$;

COMMENT ON PROCEDURE public."Load_city_coord"()
    IS 'Load file city_coord.csv in respective table';


