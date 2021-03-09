--CREATE USER flask WITH password 'flask';
--CREATE DATABASE flaskapp ENCODING 'UTF8' OWNER flask ;
CREATE TABLE IF NOT EXISTS table_source
        (ID SERIAL PRIMARY KEY ,
        source VARCHAR(50) UNIQUE);

CREATE TABLE IF NOT EXISTS table_genre
        (ID SERIAL PRIMARY KEY ,
        genre_name VARCHAR(50) UNIQUE);

CREATE TABLE IF NOT EXISTS table_producer
        (ID SERIAL PRIMARY KEY ,
        producer_name VARCHAR(50) UNIQUE);

CREATE TABLE IF NOT EXISTS table_anime
        (ID INTEGER PRIMARY KEY,
        anime_name VARCHAR(500) UNIQUE,
        anime_synopsis TEXT,
        anime_rating NUMERIC(8,2),
        anime_scoredBy INTEGER,
        anime_popularity NUMERIC(8,2),
        anime_members NUMERIC(8,2),
        anime_episodes INTEGER,
        anime_source INTEGER,
        anime_aired DATE,
        anime_link TEXT,
        FOREIGN KEY (anime_source ) REFERENCES table_source(ID) );

CREATE TABLE IF NOT EXISTS r_table_anime_genre
        (anime_ID INTEGER,
        genre_ID INTEGER,
        Primary key (anime_ID, genre_ID),
		FOREIGN key (anime_ID) REFERENCES table_anime(ID),
	    FOREIGN key (genre_ID) REFERENCES table_genre(ID));

CREATE TABLE IF NOT EXISTS r_table_anime_producer
        (anime_ID INTEGER,
        producer_ID INTEGER,
        Primary key (anime_ID, producer_ID),
		FOREIGN key (anime_ID) REFERENCES table_anime(ID),
	    FOREIGN key (producer_ID) REFERENCES table_producer(ID));