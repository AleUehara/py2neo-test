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
			rel_ab = person1.create_relationship_to(person2, relationship_type, {'links': ['teste']})
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
					print relationship.get_properties().get('links')
		print '------------'

	def get_related_with(self):
		for node in self.person.get_related_nodes():
			print "-" + node["name"]

	def create(self, name, jobs):
		 self.database.create({"name": name,
		 	                  "jobs": jobs
		 	                 })

	def find_all_contains(self, name):
		node = cypher.execute(self.database, "START n=node(*) WHERE n.name! =~ '.*"+ name +".*' RETURN n")

		actor_id = ''
		if len(node) > 0:
			actors = node[0]
		return actors

	def find_by_name(self, name):
		node = cypher.execute(self.database, "START n=node(*) WHERE n.name! = '"+name+"' RETURN n")
		actor_id = ''
		if len(node) > 0:
			actor_id = node[0][0][0].id
			print actor_id
		return actor_id

#----------------------------------------
#Init
#----------------------------------------
def create_relationship(database):
	person1 = database.get_node(20505)
	person2 = database.get_node(1)
	Relationship(database).create(person1, person2, RelationshipType.DATED)

def select_person(database, actorid):
	Actor(database, actorid).get_name()
	Actor(database, actorid).get_jobs()
	Actor(database, actorid).get_relationships()
	Actor(database, actorid).get_related_with()

def create_person(database):
	Actor(database).create("Marcio Lima", ["recruiter", "model"])

def find_person(database):
	name = 'Marcio Lima'
	actorid = Actor(database).find_by_name(name)
	Actor(database, actorid).get_name()
	Actor(database, actorid).get_jobs()

def find_all_persons_that_contains_a_letter(database):
	name = 'An'
	for actor in Actor(database).find_all_contains(name):
		actorid = actor[0].id
		Actor(database, actorid).get_name()
		Actor(database, actorid).get_relationships()

def main():
	database = Connection().get_instance()
	#create_relationship(database)
	select_person(database, 20505)
	#create_person(database)
	#find_person(database)
	#find_all_persons_that_contains_a_letter(database)




	
	



if __name__ == "__main__":
    try:
    	main()
    except Exception, e:
        print e


