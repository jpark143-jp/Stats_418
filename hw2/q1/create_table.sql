-- Probset 2
-- Question 1


-- Create database
CREATE DATABASE hw2;

CREATE TABLE hw2.Movies (
    Movie_title      CHAR    PRIMARY KEY,
    Release_year     DATE CHECK(Release_year >= 1887 AND Release_year < 2021),
    Plot_description CHAR,
    Genre            CHAR,
    Average_Rating   CHAR,
    Number_of_votes  INTEGER
);


CREATE TABLE Users (
    Users CHAR REFERENCES Users (Username),
    Movies CHAR REFERENCES Movies (Movie_title),
    Rating INTEGER PRIMARY KEY CHECK(Rating >= 1 AND Rating <= 10)
);

CREATE TABLE Users (
    Username   CHAR PRIMARY KEY,
    First_name CHAR,
    Last_name  CHAR
);
