from tqdm import tqdm
import re

class ProcessText(object):
    
    #Start the class with a text object
    def __init__(self,path_to_text):
        self.text = open(path_to_text, "r+")
        
    #Create a method to read lines
    def read_lines(self):
        self.lines = self.text.readlines()

    #Create a method to split lines
    def split_lines(self):
        self.list_of_lines = []
        for line in self.lines:
            self.list_of_lines.append(line.split())
            
    #Create a method to convert words to lower and removing special charcter
    def cleaning_lines(self):
        print("{:*^118}".format("*"))
        self.new_list_of_lines = []
        for line in tqdm(self.list_of_lines):
            if "****" in line:
                self.new_list_of_lines.append(line)
            else:
                self.new_list_of_lines.append([word.lower() for word in line])
                
    def change_terms(self,terms,new_terms):
        lines = []
        for line in self.new_list_of_lines:
            for i in range(len(terms)):
                line = [word.replace(terms[i], new_terms[i]) for word in line]
            lines.append(line)
        self.new_list_of_lines = lines
                
    def to_text(self):
        line_list = []
        for lines in self.new_list_of_lines:
            line_list.append(" ".join(str(word) for word in lines))
        self.text = " ".join(line for line in line_list)
        
    def write_text(self,file_name):
        f = open(file_name + ".txt","w+")
        for line in self.text:
            f.write(line)
        f.close()
                
    def print_text(self,start,stop, text = False):
        if text:
            print(self.text)
        else:
            try:
                print(self.new_list_of_lines[start:stop])
            except:
                print(self.list_of_lines[start:stop])       
