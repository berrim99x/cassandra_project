from db.connection import connect
from services.restaurant_service import *
from services.inspection_service import *

session = connect()

print("✅ Connected to Cassandra")

# مثال تشغيل
print("\n📌 Restaurants:")
for r in get_names(session):
    print(r.name)

print("\n📌 Restaurant 41569764:")
for r in get_by_id(session, 41569764):
    print(r.name, "-", r.borough)

print("\n📌 Inspections:")
for r in get_inspections(session, 41569764):
    print(r.inspectiondate, r.grade)

print("\n📌 Count score > 30:")
for r in count_score_30(session):
    print(r.count)