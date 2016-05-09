#!/usr/bin/python

from pymongo import MongoClient




print "Starting"


client = MongoClient()
db = client.MyData

#table = client.FirstTable

#table.insert_one({"script":"ZipCrack"})
res = db.FirstTable.find().next()

print res
