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

try:
	# Create two nodes
	node_a = graph_db.create(
	    {"name": "Renata Dimas", "jobs" : [''] }
	)
except Exception, e:
	print e

print "Criado com sucesso"
