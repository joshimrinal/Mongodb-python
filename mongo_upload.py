import sys
import re
import codecs # UniCode support
from pymongo import MongoClient # For DB Connection
from pymongo.errors import ConnectionFailure # For catching exeptions

def main():
  
  # MongoDB connection
  try:
    db_conn = MongoClient(host="localhost", port=27017) # Here we specified the default parameters explicitly
    print ("Connected to MongoDB successfully!")
  except ConnectionFailure:
    sys.stderr.write("Could not connect to MongoDB: %s" % e)

  # Grab a database
  db_target = db_conn["mrinal_sample"]

  # Open file
  f = codecs.open("flas-file.txt", 'r', encoding='utf-8') # Codecs instead regular 'open' to handle UTF-8

  # Read each line
  for line in f:
    
    try: # For exception catching
      a = line.rstrip().split(' ') # In this case, it's space-separated!
      # Should be Unicode
      word_form = a[0]
      frequency_count = a[1]
      
      
      # Create dictionary object
      record = {
        "chunky": word_form,
        "bacon": frequency_count
      }
      
      # Insert document into DB
      db_target.records.insert(record) # Collections ('records' here) are lazily created
      
    # Exception handler
    except IndexError:
      sys.stderr.write( "Something wrong with this line: " + line + '\n')
      continue
    
  # Close file
  f.close()
  
if __name__ == "__main__":
  main()