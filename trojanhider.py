#Created by HRP Huradpa
import subprocess
import sys
import os
system = os.name
if os.name != "posix":
	print("This Program Only Works On Linux But Your Use"+" "+system)
	sys.exit()

print("	 ")
print("   		 ◁▷◁▷   Created By hrp_huradpa_  ◁▷◁▷")
print("	  [1] Hide Trojan")
print("	  [2] Remove Trojan ")
print("	  [3] Exit ")

user_input = input("	Select Number > ")

if user_input == "3":
	print(" program is shutting")
	sys.exit() 

elif user_input == "1":
	user_trojan= input("Trojan Name > ")
	user_photo = input("Select Photo Name > ")
	subprocess.call(["steghide","embed","-cf",user_photo,"-ef",user_trojan])

elif user_input == "2":
	user_photo = input("Select Photo Name > ")
	subprocess.call(["steghide","extract","-sf",user_photo]) 

elif user_input == "3":
	print(" program is shutting")
	sys.exit()

else:
	print("Select 1, 2 or 3 and try again ")
