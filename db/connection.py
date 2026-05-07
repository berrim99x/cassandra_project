from cassandra.cluster import Cluster
from config import CASSANDRA_HOST, KEYSPACE

def connect():
    cluster = Cluster([CASSANDRA_HOST], port=9042)
    session = cluster.connect("resto_ny")
    return session