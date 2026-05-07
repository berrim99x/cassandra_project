CREATE KEYSPACE resto_NY
WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1};

USE resto_NY;

CREATE TABLE Restaurant (
 id INT PRIMARY KEY,
 Name VARCHAR,
 borough VARCHAR,
 BuildingNum VARCHAR,
 Street VARCHAR,
 ZipCode INT,
 Phone text,
 CuisineType VARCHAR
);

CREATE INDEX ON Restaurant (CuisineType);

CREATE TABLE Inspection (
 idRestaurant INT,
 InspectionDate date,
 ViolationCode VARCHAR,
 ViolationDescription VARCHAR,
 CriticalFlag VARCHAR,
 Score INT,
 Grade VARCHAR,
 PRIMARY KEY (idRestaurant, InspectionDate)
);

CREATE INDEX ON Inspection (Grade);