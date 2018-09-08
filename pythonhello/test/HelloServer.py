'''
Created on Feb 2, 2018

@author: gongyo
'''

from flask import Flask, jsonify, request, abort, make_response
import subprocess
import json
import os
import commands
import re

# re.compile("r^[a-zA-Z0-9.-_][]*$",0).__cmp__();
# re.match("r^[a-zA-Z0-9.-_][]*$","test",0);
app = Flask(__name__)

DB_USER_KEY = 'admin3';  # request.args.get('user_key');
DB_PASSWORD_KEY = 'admin';  # request.args.get('pass_key');
u = DB_PASSWORD_KEY[3:]
print "asdf", 23
try:
#     (status, DB_PASSWORD_KEY) = commands.getstatusoutput('dir c:');
    print DB_PASSWORD_KEY
    print "HELL:" + DB_PASSWORD_KEY
#     if status == 0:
#         # return 'ERROR', 503
#         print 'SUECCESS';
#     else: 
#         print "ERROR";
       
except Exception as e:
    print "Failed to retrive user information from vault " + str(e.message)
    # return 'ERROR', 503
    
@app.route('/urest/v1/pgpool/nodes', methods=['GET'])
def get_nodes():
    return "{}"

@app.route('/urest/v1/pgpool/get_node_name', methods=['GET'])
def checkRegPattern():
   import re
   nodename = request.args.get('nodename')        
   data = json.loads(get_nodes())        
   for i in range(0, len(data)):        
       if (data[i]["nodename"] == nodename):
           return str(data[i]["nodeid"])    
   return str(-1)        
   # check for valid node name
   if re.match(r'^[a-zA-Z0-9.-_][A-Za-z0-9.-_]*$', nodename):
       data = json.loads(get_nodes())
       for i in range(0, len(data)):
           if (data[i]["nodename"] == nodename):
               return str(data[i]["nodeid"])
       return str(-1)
   else:
       return str(-1)
    
@app.route('/urest/v1/pgpool/isalive', methods=['GET'])
def is_alive():
    HOMEPATH = os.environ['HOMEPATH']
    USERNAME = os.environ['USERNAME']
    try:
        (status, DB_PASSWORD) = commands.getstatusoutput('get_secret ' + DB_PASSWORD_KEY)
        if status != 0:
            return 'ERROR', 503
    except Exception as e:
        print "is_alive Failed with error " + str(e.message)
        return 'ERROR', 503

    return "SUCCESS:" + USERNAME,200
#     cmd = "env PGCONNECT_TIMEOUT=5 env PGPASSWORD=" + DB_PASSWORD[5:] + " psql -h " + DBHOST + " -p 5432 -d " + DB_NAME + " -U " + DB_USER + " -q -c 'select 1'"
#     try:
#         ret = subprocess.call(cmd, shell=True)
#         if ret == 0:
#             return 'OK', 200
#         else:
#             return 'ERROR', 503
#     except Exception as e:
#         print "is_alive Failed with error " + str(e.message)
#         return 'ERROR', 503

     
if __name__ == "__main__":
     #app.run(host='0.0.0.0', port=5050)
  nodename=" test.host  "
  nodename = str(nodename).rstrip().lstrip()
  nodename = nodename.split(' ',1)[0]

  print nodename
  

