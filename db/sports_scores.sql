DROP TABLE IF EXISTS games;
DROP table IF EXISTS players; 
DROP table IF EXISTS teams; 
DROP table IF EXISTS attributes; 


CREATE TABLE attributes (
    strength INT,
    speed INT,
    intelligence INT,
    fitness INT,
    adaptability INT
);


CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    wins INT,
    draws INT,
    defeats INT
) INHERITS (attributes);

CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    squad_number INT,
    position VARCHAR(255) NOT NULL,
    team_id INT REFERENCES teams(id)
) INHERITS (attributes);

CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    home_id INT REFERENCES teams(id),
    away_id INT REFERENCES teams(id),
    home_goals INT,
    away_goals INT,
    result INT
);


-- INSERT INTO teams (name, strength, speed, intelligence, fitness, adaptability) VALUES ('St Mirren', 5, 10, 8, 9, 7);
-- INSERT INTO teams (name, strength, speed, intelligence, fitness, adaptability) VALUES ('Morton', 5, 10, 2, 4, 6);
-- INSERT INTO players (name, strength, speed, intelligence, fitness, adaptability, team_id, squad_number) VALUES ('Peter', 5, 10, 10, 10, 10, 1, 3);
-- INSERT INTO games (home_id, away_id, home_goals, away_goals) VALUES (1, 2, 2, 1, 1)