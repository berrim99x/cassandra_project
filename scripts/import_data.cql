USE resto_NY;

COPY Restaurant (id, name, borough, buildingnum, street, zipcode, phone, cuisinetype)
FROM '/restaurants.csv' WITH DELIMITER=',';

COPY Inspection (idrestaurant, inspectiondate, violationcode, violationdescription,
criticalflag, score, grade)
FROM '/restaurants_inspections.csv' WITH DELIMITER=',';