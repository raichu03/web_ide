from datetime import datetime
import subprocess
import os


#### PATH TO STORE THE TEMPORARY CODE FILE ####
path = "/home/raichu/Desktop/code_competation/html/app/temp/"

class Run:

    def __init__(self):
        pass
    

    ##### GENERATES THE CODE FILE #####
    def codeGenerator(self, language, code):
        now = datetime.now()
        current_date = now.strftime("%d")
        current_time = now.strftime("%H:%M:%S")
        file_name = path + current_date + "_" + current_time+ "ar" +"."+ language

        with open(file_name, "w") as file:
            file.write(code)

        return file_name



    ##### RUNS THE CODE #####
    def codeRunner(self, language, code):

        file_path = self.codeGenerator(language, code)

        ### FOR PYTHON ###
        if (language=="py"):
            try:
                output = subprocess.check_output(["python3", file_path], stderr=subprocess.STDOUT, text=True)
                os.remove(file_path)
                return output

            except subprocess.CalledProcessError as e:
                return e.output

        ### FOR C ###
        elif (language=="c"):
            try:
                subprocess.check_output(["gcc", file_path, "-o", path +"executable"])
                output = subprocess.check_output([path + "./executable"], stderr=subprocess.STDOUT, text=True)
                return output
            
            except subprocess.CalledProcessError as e:
                return e.output
            
        ### FOR CPP ###   
        elif (language=="cpp"):
            try:
                subprocess.check_output(["g++", file_path, "-o", path + "executable"])
                output = subprocess.check_output([path + "./executable"], stderr=subprocess.STDOUT, text=True)
                os.remove(file_path)
                os.remove(path + "executable")
                return output
            
            except subprocess.CalledProcessError as e:
                return e.output
            
        ### FOR JAVASCRIPT ###
        elif (language=="js"):
            try:
                output = subprocess.check_output(["node", file_path], stderr=subprocess.STDOUT, text=True)
                os.remove(file_path)
                return output
            
            except subprocess.CalledProcessError as e:
                return e.output
            
        ### FOR PHP ###
        elif (language=="php"):
            try:
                output = subprocess.check_output(["php", file_path], stderr=subprocess.STDOUT, text=True)
                os.remove(file_path)
                return output
            
            except subprocess.CalledProcessError as e:
                return e.output

