'''
Created on Sep 16, 2018

@author: nnhatkhanh
'''
from src.Resume import Resume
from src.ExperiencedResume import ExperiencedResume

if __name__ == '__main__':
    resume = Resume('Khanh', "Nguyen", "khanh@gmail.com", "00000", "HCM") 
    print("Experienced Resume: " + resume.get_full_name())
     
    expResume = ExperiencedResume('Khanh', "Nguyen", "khanh@gmail.com", "00000", "HCM", "900")
    expResume.get_full_name()