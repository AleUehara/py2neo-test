#!/usr/bin/env python
 
"""
Simple example showing node and relationship creation plus
execution of Cypher queries
"""
 
#from __future__ import print_function
 
# Import Neo4j modules
from py2neo import neo4j, cypher

graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")

node_a = graph_db.get_node(4)
node_b = graph_db.get_node(1)

print node_a["name"]
print node_b["name"]

try:
	rel_ab = node_a.create_relationship_to(node_b, "knows")
except Exception, e:
	print e

print "Criado com sucesso"