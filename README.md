# 🍽️ Cassandra Restaurant Inspection System

A NoSQL project built using Python and Apache Cassandra to manage restaurant and inspection data efficiently.

---

# 📌 Project Overview

This project demonstrates how to use Apache Cassandra as a distributed NoSQL database for storing and querying large-scale restaurant inspection data.

The system allows:

- Managing restaurant information
- Managing restaurant inspections
- Executing CQL queries
- Connecting Python applications to Cassandra
- Importing CSV datasets into Cassandra

---

# 🛠️ Technologies Used

- 🐍 Python 3.11
- 🗄️ Apache Cassandra
- 🐳 Docker
- 💻 PyCharm
- 📄 CQL (Cassandra Query Language)

---

# 📂 Project Structure

```plaintext
cassandra_project/
│
├── main.py
├── config.py
├── requirements.txt
├── README.md
│
├── db/
│   ├── __init__.py
│   ├── connection.py
│   ├── queries.py
│
├── services/
│   ├── __init__.py
│   ├── restaurant_service.py
│   ├── inspection_service.py
│
├── data/
│   ├── restaurants.csv
│   ├── restaurants_inspections.csv
│
└── scripts/
    ├── create_schema.cql
    ├── import_data.cql
```

---

# 🚀 Features

✅ Cassandra database connection  
✅ Restaurant data management  
✅ Inspection records management  
✅ CSV data import  
✅ Query execution using Python  
✅ Organized and modular project structure  

---

# 🐳 Running Cassandra with Docker

## 1️⃣ Start Cassandra Container

```bash
docker run --name cassandra-db -p 9042:9042 -d cassandra:latest
```

## 2️⃣ Wait for Cassandra to Start

```bash
docker logs cassandra-db
```

Wait until you see:

```text
Starting listening for CQL clients
```

## 3️⃣ Open cqlsh

```bash
docker exec -it cassandra-db cqlsh
```

---

# 🧱 Database Creation

## Create Keyspace

```sql
CREATE KEYSPACE resto_ny
WITH REPLICATION = {
  'class': 'SimpleStrategy',
  'replication_factor': 1
};
```

## Use Keyspace

```sql
USE resto_ny;
```

---

# 🗄️ Create Tables

```sql
CREATE TABLE Restaurant (
 id INT,
 Name VARCHAR,
 borough VARCHAR,
 BuildingNum VARCHAR,
 Street VARCHAR,
 ZipCode INT,
 Phone text,
 CuisineType VARCHAR,
 PRIMARY KEY (id)
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
```

---

# 📥 Import CSV Files

## Copy CSV files into Docker container

```bash
docker cp restaurants.csv cassandra-db:/
docker cp restaurants_inspections.csv cassandra-db:/
```

## Import Data

```sql
COPY Restaurant (
id,
name,
borough,
buildingnum,
street,
zipcode,
phone,
cuisinetype
)
FROM '/restaurants.csv'
WITH DELIMITER=',';

COPY Inspection (
idrestaurant,
inspectiondate,
violationcode,
violationdescription,
criticalflag,
score,
grade
)
FROM '/restaurants_inspections.csv'
WITH DELIMITER=',';
```

---

# 💻 Python Connection Example

```python
from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'], port=9042)
session = cluster.connect("resto_ny")

print("Connected to Cassandra ✅")
```

---

# 🔍 Example Queries

## Get Restaurant Names

```python
rows = session.execute("SELECT name FROM Restaurant LIMIT 10")

for row in rows:
    print(row.name)
```

## Get Restaurant by ID

```python
rows = session.execute("SELECT name, borough FROM Restaurant WHERE id = 41569764")

for row in rows:
    print(row.name, row.borough)
```

## Get Inspections

```python
rows = session.execute("SELECT inspectiondate, grade FROM Inspection WHERE idrestaurant = 41569764")

for row in rows:
    print(row.inspectiondate, row.grade)
```

---

# ⚠️ Cassandra Notes

Apache Cassandra does not allow arbitrary filtering like relational databases.

To query non-primary-key columns, you may need:

- Secondary Indexes
- `ALLOW FILTERING`

Example:

```sql
SELECT * FROM Restaurant
WHERE borough='BROOKLYN'
ALLOW FILTERING;
```

---

# 📊 Dataset Information

Approximate dataset size:

- 🍽️ 25,000 Restaurants
- 🔍 150,000 Inspections

---

# ▶️ Running the Project

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run the application

```bash
python main.py
```

---

# 👨‍💻 Author

## Abdelhakim Berrim

Big Data & NoSQL Database Project using Apache Cassandra.

---

# 📜 License

This project is developed for educational purposes.
