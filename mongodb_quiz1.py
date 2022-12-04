import os
import pprint
from pymongo import MongoClient
from datetime import datetime

#เชื่อมต่อ mongoDB
connection_string = "mongodb://localhost:27017"
client = MongoClient(connection_string)

#print เพื่อดู db ที่มีทั้งหมด 
dbs = client.list_database_names() 
print(dbs) 

#กำหนดตัวแปร db ไปหา collection ใน db นั้น เทียบ sql คือ database -> table
db = client.Quiz1

#print เพื่อดู collection ที่มีทั้งหมด 
collection = db.list_collection_names() 
print(collection)

collection = db.product

#I Insert / Create
def insert_doc(orderlist,amount,price,total):
    collection = db.product
    insert_data = {
        "_orderlist"    : orderlist,
        "_amount"   : amount,
        "_price"   : price,
        "_total"      : total,
        "_date"     : datetime.today().strftime('%Y-%m-%d')
    }
    collection.insert_one(insert_data)
    ins_id = collection.insert_one(insert_data).inserted_id
    print(ins_id)

printer = pprint.PrettyPrinter()
#R Read ค้นหาข้อมูลใน collection
def find_all_people():
    #SELECT * FROM person
    people = collection.find()
    return list(people)

#U Update การอัพเดตข้อมูลใน collection
def replace_one(ids,orderlist,amount,price,total): 
    from bson.objectid import ObjectId
    _id = ObjectId(ids)
    new_doc = {
        "_orderlist"    : orderlist,
        "_amount"   : amount,
        "_price"   : price,
        "_total"      : total,
        "_date" : datetime.today().strftime('%Y-%m-%d')
    }

    collection.replace_one({"_id":_id},new_doc)

#D ลบ
def delete_doc_by_id(person_id):
    from bson.objectid import ObjectId
    _id = ObjectId(person_id)
    collection.delete_one({"_id" : _id}) #ลบ 1 row
    return _id


