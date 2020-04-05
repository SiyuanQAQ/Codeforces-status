#!/bin/python3

import json
import urllib.request

def cf_status(handle = 'tourist'):
    try :
        print('>>> reading ...')
        #codeforces-api
        user_data = json.loads(urllib.request.urlopen('http://codeforces.com/api/user.status?handle=%s&from=1'%(handle)).read().decode('utf-8'))

        accept,wrong,total = 0,0,0

        for item in user_data['result'] :
            if item['verdict'] == 'OK':
                accept+=1
            else :
                wrong+=1

            total+=1

        #print result 
        print("  " + 49 * "\033[93m-\033[00m")
        print(' \033[93m|\033[00m'+16*' '+'Codeforces status'+15*' ','\033[93m|\033[00m')
        print(' \033[93m|\033[00m total \033[92maccept      : %s\033[00m'%accept,'  \033[92m÷)\033[00m',(21-len(str(accept)))*' ','\033[93m|\033[00m')
        print(' \033[93m|\033[00m total \033[91mreject      : %s\033[00m'%wrong,'  \033[91m:!\033[00m',(21-len(str(wrong)))*' ','\033[93m|\033[00m')
        print(' \033[93m|\033[00m total \033[96msubmissions : %s\033[00m'%total,(26-len(str(total)))*' ','\033[93m|\033[00m')
        print("  " + 49 * "\033[93m-\033[00m")

    #when you have connection problem
    except :
        print(">>> Oops I think you R offline :| ") 

handle = input('Enter handle : ')
cf_status(handle)
