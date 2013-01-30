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
	node_a = graph_db.get_node(6)
	print node_a

	print node_a["name"]

	print node_a["jobs"]


	for relationship in node_a.get_relationships():
		print relationship
	#relationship_a = graph_db.get_node(4)

	print "Relacionado com:"
	for node in node_a.get_related_nodes():
		print "-" + node["name"]
except Exception, e:
	print e

print "select executado com sucesso"	



