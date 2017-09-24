import sys
import zipfile
import shlex, subprocess
import os
print """

____    __    ____  ___      .______      .______       __    ______   .______      
\   \  /  \  /   / /   \     |   _  \     |   _  \     |  |  /  __  \  |   _  \     
 \   \/    \/   / /  ^  \    |  |_)  |    |  |_)  |    |  | |  |  |  | |  |_)  |    
  \            / /  /_\  \   |      /     |      /     |  | |  |  |  | |      /     
   \    /\    / /  _____  \  |  |\  \----.|  |\  \----.|  | |  `--'  | |  |\  \----.
    \__/  \__/ /__/     \__\ | _| `._____|| _| `._____||__|  \______/  | _| `._____|
                            
                                Author : @dibsyhex
                                version : 1.0                                                    


"""

base_path = "./"



def run_owasp_dependency(project_name,file_path):
	os.chdir(base_path+project_name)

	cmd = 'dependency-check.bat --project "'+project_name+'" --scan "'+base_path+project_name +'" --out "'+project_name+'_dependecy_check_report.html"'
	args = shlex.split(cmd)
	os.chdir("../")#One directory up
	p = subprocess.Popen(args,cwd=base_path)
	stdout, stderr = p.communicate()
	print "Stdout:"+str(stdout)
	print "Stderr:"+str(stderr)
	


#Extract the file
def extract(project_name,file_path):
	print "Extracting at " + os.getcwd()
	#Extract the contents into the directory specified by base_path+project_name
	zf = zipfile.ZipFile(file_path)
	for file in zf.namelist():
		if ".jar" in file:
			zf.extract(file,base_path+project_name)
	print "Extraction Done"


def main():
	if len(sys.argv) < 3:
		print "No arguments provided"
		print "usage : python warrior.py \"ProjectName\" \"location_of_war_file\""
	global project_name
	global file_path

	project_name = sys.argv[1]
	file_path = sys.argv[2]
	extract(project_name,file_path)

	
	
	print "Running OWASP Dependency Check! It will take some time to run OWASP Dependency Check. Grab a beer or coffee while it scans !"
	run_owasp_dependency(project_name,file_path)
	print "!! Done !!"

main()