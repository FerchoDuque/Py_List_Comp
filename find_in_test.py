# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 17:06:18 2022

@author: Fernando Betancourt Duque
"""

#import urllib
from urllib.request import urlopen

#import json
import json
import time
from unittest import TestCase


#GLOBAL
#set the URL from the data origin
url = "https://mach-eight.uc.r.appspot.com/"


def load_data(url): 
    #assign the response of url
    resp = urlopen(url)
    
    #store the JSON response from the data origin
    data_json = json.loads(resp.read())
    data_dict = data_json['values']  
    
    return data_dict

 
def find_in(height, data_dict):    
    #set time for function
    start_time = time.time()
    
    data_set = set()  
    
    #using list comprehension
    data_set = [i['first_name'] + ' ' + i['last_name'] + '    ' + j['first_name'] + ' ' + j['last_name'] \
              for i in data_dict \
              for j in data_dict \
              if int(i['h_in']) + int(j['h_in']) == height \
              and i['first_name'] + ' ' + i['last_name'] < j['first_name'] + ' ' + j['last_name'] \
              and i['first_name'] + ' ' + i['last_name'] != j['first_name'] + ' ' + j['last_name']]
    
    return data_set, start_time
   
    
class TestFindIn(TestCase):
    """------Test Class------"""
    
    def test_find_in(self):
        """Test the find function with some data"""
        #instance test variables
        data_test = list()
        result_test = set() 
        
        data_test = load_data(url)
        
        result_test = find_in(139, data_test) 
        
        result = list(result_test[0])
        expected = ['Brevin Knight    Nate Robinson', 'Mike Wilks    Nate Robinson']
                
        self.assertEqual(result, expected)
        
    

if __name__ == '__main__':      
    #instance variable containers
    data_dict = list ()
    result = set()  
    
    #get the data
    data_dict = load_data(url)
    
    #capture the variable to validate
    height = int(input("Press Height to validate: ")) 
    
    #executes the find function
    result, start_time = find_in(height, data_dict) 
    
    #gets time execution
    searching_time = time.time() - start_time
    
    #validate and print result
    if len(result) == 0:
        print("No matches found")
    else:
        for i in range(len(result)):
            print(result[i])  
    
    print("--- %s seconds finding values ---" % (searching_time)) 
    
    