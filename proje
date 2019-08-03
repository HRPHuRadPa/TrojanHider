#Created by HRP Huradpa
import optparse
import subprocess
import sys
import os

system = os.name

if system != "posix":
	print("This Program Only Works On Linux")
	sys.exit()
else:

	optparse_input = optparse.OptionParser()
	optparse_input.add_option("-pht","--photo",desk="photo",help="write for Select Photo  --> (-pht or --photo) ...")
	optparse_input.add_option("-trj","--trojan",desk="trojan",help="write for Select Trojan --> (-trj or --trojan) ...")

	inputs = optparse_input.parse_args()

	user_photo= inputs.photo
	user_trojan= inputs.trojan

	print("	 ")
	print("   		   Created By HRP HuRadPa   ")
	print("	 ")
	print("trojan is hiding")

	subprocess.call(["steghide","embed",user_photo,"-ef",user_trojan])
	subprocess.call(["steghide","extract","-sf",user_photo]) 
	print(" program is shutting")
	sys.exit()
