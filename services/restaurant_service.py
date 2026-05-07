from db import queries

def get_all(session):
    return session.execute(queries.GET_ALL_RESTAURANTS)

def get_names(session):
    return session.execute(queries.GET_NAMES)

def get_by_id(session, rid):
    return session.execute(queries.GET_BY_ID, [rid])

def get_french(session):
    return session.execute(queries.GET_FRENCH)