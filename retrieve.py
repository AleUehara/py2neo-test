#!/usr/bin/env python
from py2neo import neo4j, cypher

graph_db = neo4j.GraphDatabaseService()

def handle_row(row):
    node = row[0]
    # do something with `node` here
    print node

cypher.execute(graph_db, "START z=node(*) RETURN z", row_handler=handle_row)
