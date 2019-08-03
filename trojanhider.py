#Created by HRP Huradpa
import subprocess
import sys
import os

if os.name != "posix":
	print("This Program Only Works On Linux")
print("	 ")
print("   		 ◁▷◁▷       hrp_huradpa_  ▷◁▷◁")
print("	  [1] Hide ")
print("	  [2] Close in ")
print("	  [3] Exit ")



user_input = input("	Select Number > ")

if user_input == "3":
	print(" program is shutting")
	sys.exit() 

user_trojan= input("Trojan Name > ")
user_photo = input("Select Photo Name > ")

elif user_input == "1":
	subprocess.call(["steghide","embed",user_photo,"-ef",user_trojan])

elif user_input == "2":
	subprocess.call(["steghide","extract","-sf",image]) 

elif user_input == "3":
	print(" program is shutting")
	sys.exit()

else:
	print("Select 1, 2 or 3 and try again ")
