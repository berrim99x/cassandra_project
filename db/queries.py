# Restaurants
GET_ALL_RESTAURANTS = "SELECT * FROM Restaurant"
GET_NAMES = "SELECT name FROM Restaurant"
GET_BY_ID = "SELECT name, borough FROM Restaurant WHERE id=%s"
GET_FRENCH = "SELECT name FROM Restaurant WHERE cuisinetype='French'"

# Inspections
GET_INSPECTIONS = "SELECT inspectiondate, grade FROM Inspection WHERE idrestaurant=%s"
GET_SCORE_10 = """
SELECT grade, score FROM Inspection 
WHERE idrestaurant=%s AND score >= 10 ALLOW FILTERING
"""

GET_SCORE_30 = """
SELECT grade FROM Inspection 
WHERE score > 30 ALLOW FILTERING
"""

COUNT_SCORE_30 = """
SELECT count(*) FROM Inspection 
WHERE score > 30 ALLOW FILTERING
"""