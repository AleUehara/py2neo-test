#!/usr/bin/env python
import os
from connectiondb import Connection
from utils_enum import RelationshipType
from py2neo import neo4j, cypher

#docs -->http://packages.python.org/py2neo/neo4j.html

class Relationship():
	def __init__(self, database):
		self.database = database

	def create(self, person1, person2, relationship_type):
		try:
			rel_ab = person1.create_relationship_to(person2, relationship_type)
		except Exception, e:
			print "Erro: " + str(e)


class Actor():
	def __init__(self, database, node_number=None):
		self.database = database
		if not node_number == None:
			self.person   = self.__set_node_number(node_number)

	def __set_node_number(self, node_number):
		return self.database.get_node(node_number)
	
	def get_name(self):
		print self.person["name"]

	def get_jobs(self):
		print self.person["jobs"]

	def get_relationships(self):
		for relationship in self.person.get_relationships():
			#print relationship.type
			for node in relationship.nodes:
				if not node["name"] == self.person["name"]:
					print relationship.type + " " +node["name"]
			print '------------'

	def get_related_with(self):
		for node in self.person.get_related_nodes():
			print "-" + node["name"]

	def create(self, name, jobs):
		 self.database.create({"name": name,
		 	                  "jobs": jobs
		 	                 })

#----------------------------------------
#Init
#----------------------------------------
def create_relationship(database):
	person1 = database.get_node(4)
	person2 = database.get_node(1)
	Relationship(database).create(person1, person2, RelationshipType.DATED)

def select_person(database):
	Actor(database, 4).get_name()
	Actor(database, 4).get_jobs()
	Actor(database, 4).get_relationships()
	Actor(database, 4).get_related_with()

def create_person(database):
	Actor(database).create("Marcio Lima", ["recruiter", "model"])

def find_person(database):
	node = cypher.execute(database, "START n=node(*) WHERE n.name! = 'Marcio Lima' RETURN n")
	actor_id = node[0][0][0].id
	Actor(database, actor_id).get_name()
	Actor(database, actor_id).get_jobs()

def main():
	database = Connection().get_instance()
	#create_relationship(database)
	#select_person(database)
	#create_person(database)
	find_person(database)




	
	



if __name__ == "__main__":
    try:
    	main()
    except Exception, e:
        print e


