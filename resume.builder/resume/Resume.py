'''
Created on Sep 16, 2018

@author: nnhatkhanh
'''

class Resume:
    
    def __init__(self, first_name, last_name, email, phone, place_of_birth): 
        self.first_name = first_name
        self.last_name = last_name
        self.email = email 
        self.phone = phone
        self.place_of_birth = place_of_birth

    def get_full_name(self):
        return self.first_name + " " + self.last_name
    