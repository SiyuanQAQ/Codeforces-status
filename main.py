#!/bin/python3

import json
import urllib.request

def cf_status(handle = 'tourist'):
    try :
        print('>>> reading ...')
        user_data = json.loads(urllib.request.urlopen('http://codeforces.com/api/user.status?handle=%s&from=1'%(handle)).read().decode('utf-8'))

        accept,wrong,total = 0,0,0

        for item in user_data['result'] :
            if item['verdict'] == 'OK':
                accept+=1
            else :
                wrong+=1

            total+=1

        #print result 
        print("  " + 49 * "-")
        print(' |'+16*' '+'Codeforces status'+15*' ','|')
        print(' | total accept      : %s'%accept,'  ÷)',(21-len(str(accept)))*' ','|')
        print(' | total reject      : %s'%wrong,'  :!',(21-len(str(wrong)))*' ','|')
        print(' | total submissions : %s'%(total),(26-len(str(total)))*' ','|')
        print("  " + 49 * "-")

    #when you have connection problem
    except :
        print(">>> Oops I think you R offline :| ") 

handle = input('Enter handle : ')
cf_status(handle)
