-- Probset 2
-- Question 1


-- Create database
CREATE DATABASE hw2;

CREATE TABLE hw2.Movies (
    [Movie title]      CHAR    PRIMARY KEY,
    [Release year]     DATE CHECK([Release year] >= 1887 AND [Release year] < 2021),
    [Plot description] CHAR,
    Genre            CHAR,
    [Average Rating]   CHAR,
    [Number of votes]  INTEGER
);


CREATE TABLE Users (
    Users CHAR REFERENCES Users (Username),
    Movies CHAR REFERENCES Movies (Movie title),
    Rating INTEGER PRIMARY KEY CHECK(Rating >= 1 AND Rating <= 10)
);

CREATE TABLE Users (
    Username   CHAR PRIMARY KEY,
    [First name] CHAR,
    [Last name]  CHAR
);
