#!/bin/python3


import requests 
from bs4 import BeautifulSoup 


def Cf_Counter(username = 'tourist'):
    
    # the target we want to open	 
    url='https://codeforces.com/submissions/%s/page/1'%username
    
    try :
        #open with GET method 
        resp=requests.get(url)

        #http_respone 200 means OK status 
        if resp.status_code != 200 :
            print('Do U Know why i cant connect :( ?')   

        else :
            print(">>>Successfully opened the web page")   
            soup=BeautifulSoup(resp.text,'html.parser')	
            
            #find how many pages
            page = soup.find_all("div",{"class":"pagination"})
            for index in page :
                last_page = index.find_all('span',{'class':'page-index'})
             
            try :
                last_page = last_page[-1].find('a').text

            #for single page submissions
            except :
                last_page = 1

            #total accept
            ac=0
            #total reject
            rc=0

            print('>>> ditected %s'%last_page + ' pages')
            
            for page_index in range (1,int(last_page)+1) :

                a_eachPage=0
                r_eachPage=0

                #url for every page
                url2='https://codeforces.com/submissions/%s/page/%s'%(username,page_index)
                resp=requests.get(url2) 
                soup2=BeautifulSoup(resp.text,'html.parser')	

                #count verdict = accepted
                accepted = soup2.find_all("span",{"class":"verdict-accepted"})

                for item in accepted :
                    ac+=1
                    a_eachPage+=1

                print('page %s >>> '%page_index,a_eachPage,' : Problem accepted :)')
               

                #count verdict = rejected
                rejected = soup2.find_all("span",{"class":"verdict-rejected"})

                for item in rejected :
                    rc+=1
                    r_eachPage+=1
                
                print(11 *' ',r_eachPage,' : Problem rejected :(')

                #break line after reading page 
                if page_index < int(last_page) :
                    print(" " + 45 * "-")
                    
            #print result 
            print("  " + 49 * "-")
            print(' |'+16*' '+'Codeforces status'+15*' ','|')
            print(' | total accept      : %s'%ac,'  ÷)',(21-len(str(ac)))*' ','|')
            print(' | total reject      : %s'%rc,'  :!',(21-len(str(rc)))*' ','|')
            print(' | total submissions : %s'%(ac+rc),(26-len(str(ac+rc)))*' ','|')
            print("  " + 49 * "-")
     
    #when you are offline
    except requests.ConnectionError :
        print(">>> Oops I think you R offline :| ") 

username = input('Enter Username : ')
Cf_Counter(username)

