#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from py2neo import neo4j, cypher

class Connection():
	def get_instance(self):
		return neo4j.GraphDatabaseService("http://localhost:7474/db/data/")