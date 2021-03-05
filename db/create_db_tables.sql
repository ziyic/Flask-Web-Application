CREATE TABLE IF NOT EXISTS table_source
        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
        source NVARCHAR(50) UNIQUE);

CREATE TABLE IF NOT EXISTS table_genre
        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
        genre_name NVARCHAR(50) UNIQUE);

CREATE TABLE IF NOT EXISTS table_producer
        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
        producer_name NVARCHAR(50) UNIQUE);

CREATE TABLE IF NOT EXISTS table_anime
        (ID INTEGER PRIMARY KEY,
        anime_name NVARCHAR(500) UNIQUE,
        anime_synopsis TEXT,
        anime_rating FLOAT(8,2),
        anime_scoredBy INTEGER,
        anime_popularity FLOAT(5,2),
        anime_members FLOAT(8,2),
        anime_episodes INTEGER,
        anime_source INTEGER,
        anime_aired DATETIME,
        anime_link TEXT,
        FOREIGN KEY (anime_source ) REFERENCES table_source(ID) );

CREATE TABLE IF NOT EXISTS r_table_anime_genre
        (anime_ID INTEGER,
        genre_ID INTEGER,
        Primary key (anime_ID, genre_ID) ,
		FOREIGN key (anime_ID) REFERENCES table_anime(ID) ,
	    FOREIGN key (genre_ID) REFERENCES table_genre(ID));

CREATE TABLE IF NOT EXISTS r_table_anime_producer
        (anime_ID INTEGER,
        producer_ID INTEGER,
        Primary key (anime_ID, producer_ID) ,
		FOREIGN key (anime_ID) REFERENCES table_anime(ID) ,
	    FOREIGN key (producer_ID) REFERENCES table_producer(ID));