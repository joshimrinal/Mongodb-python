from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
client = MongoClient()
try:
   # The ismaster command is cheap and does not require auth.
   client.admin.command('ismaster')
   print("Server available") # prints out if the db connection is made
except ConnectionFailure:
   print("Server not available")

	
	