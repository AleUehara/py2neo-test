#!/usr/bin/python
# -*- coding: utf-8 -*-

class RelationshipType:
    Knows, Married, Dated, Divorced = range(4)

def enum(**enums):
    return type('Enum', (), enums)

RelationshipType = enum(KNOWS='knows', 
	                    MARRIED="married", 
	                    DIVORCED="divorced",
	                    DATED="dated"
	                    )

#print RelationshipType.DATED