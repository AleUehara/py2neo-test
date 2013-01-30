#!/usr/bin/env python
 
"""
Simple example showing node and relationship creation plus
execution of Cypher queries
"""
 
#from __future__ import print_function
 
# Import Neo4j modules
from py2neo import neo4j, cypher
 
# Attach to the graph db instance
graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")
print graph_db.neo4j_version
#node_count = graph_db.get_node_count()

#graph_db.delete()


node_a = graph_db.get_node(1)
print node_a["name"]
#print node_a.get_related_nodes()
#print my_node


print node_a.get_relationships()[0]
print node_a.get_related_nodes()[0]["name"]

#print node_count


''' 
# Create two nodes
node_a, node_b = graph_db.create(
    {"name": "Alice"},
    {"name": "Bob"}
)
 
# Join the nodes with a relationship
rel_ab = node_a.create_relationship_to(node_b, "KNOWS")


# Build a Cypher query
query = "START a=node({A}) MATCH a-[:KNOWS]->b RETURN a,b"
 
# Define a row handler...
def print_row(row):
    a, b = row
    print(a["name"] + " knows " + b["name"])
 
# ...and execute the query
cypher.execute(graph_db, query, {"A": node_a.id}, row_handler=print_row)

'''
