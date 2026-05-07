from db import queries

def get_inspections(session, rid):
    return session.execute(queries.GET_INSPECTIONS, [rid])

def get_score_10(session, rid):
    return session.execute(queries.GET_SCORE_10, [rid])

def get_score_30(session):
    return session.execute(queries.GET_SCORE_30)

def count_score_30(session):
    return session.execute(queries.COUNT_SCORE_30)