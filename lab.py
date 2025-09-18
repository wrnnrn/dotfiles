import os 

user = os.getlogin()

os.chdir(f"/home/{user}")

print("Current working directory: ", os.getcwd())
