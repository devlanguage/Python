'''
Created on Feb 2, 2018

@author: gongyo
'''
import subprocess
import json
import os
import commands

DB_USER_KEY = 'admin3'; #request.args.get('user_key');
DB_PASSWORD_KEY = 'admin'; #request.args.get('pass_key');

print "asdf", 23
try:
    (status,DB_PASSWORD_KEY) = commands.getstatusoutput('echo '+DB_USER_KEY);
    print "HELL" + DB_PASSWORD_KEY
    if status == 0:
        #return 'ERROR', 503
        print 'SUECCESS';
    else: 
        print "ERROR";
       
except Exception as e:
    print "Failed to retrive user information from vault "+ str(e.message)
    #return 'ERROR', 503
     
if __name__ == '__main__':
    pass