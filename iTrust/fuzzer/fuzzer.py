import fnmatch
import os
import re
import random
import requests
import time
import subprocess


#from git import Repo

sha1 = ""
def fuzzing():
	print "kiran krishnan"
	files = []
	for root, dirnames, filenames in os.walk('C:\\Users\\kbala\\boxes\\m2\\iTrust-v23'):
		for filename in fnmatch.filter(filenames, '*.js'):
			files.append(os.path.join(root, filename))
	for file_name in files:
		#print i,"\n"
		f = open(file_name, 'r')
		lines = f.readlines()
		#lines = [" if(openAccordion < nID)", " if(openAccordion << nID)"]
		#print lines
		#break
		# To swap <
		lt = random.randint(1,1001)
		gt = random.randint(1,1001)
		eq = random.randint(1,1001)
		neq = random.randint(1,1001)
		one = random.randint(1,1001)
		zero = random.randint(1,1001)
		chgStr = random.randint(1,1001)
		#print lt
		for line in lines:
			
			#print(line,': ----------------------------------------------------------inside for')
			if(re.match('(.*)if(.*)',line) is not None or re.match('(.*)while(.*)',line) is not None):
				#print (line,": ---------------------------------------------------inside if if")
				if(re.match('(.*)<(.*)',line) is not None):
					#print"---------------------------------------START----------------------------"
					#print line,"\n"
					if(lt > 500):
						line = re.sub('<','>',line)
					#print "---------------------------------------END------------------------------"
					#print line,"\n"
			if(re.match('(.*)if(.*)',line) is not None or re.match('(.*)while(.*)',line) is not None):
	                        #print (line,": ---------------------------------------------------inside if if")
				if(re.match('(.*)>(.*)',line) is not None):
					#print"---------------------------------------START----------------------------"
					#print line,"\n"
					if(gt < 500):
						line = re.sub('>','<',line)
					#print "---------------------------------------END------------------------------
					#print line,"\n"                        
			
			if(re.match('(.*)if(.*)',line) is not None or re.match('(.*)while(.*)',line) is not None):
				#print (line,": ---------------------------------------------------inside if if")
				if(re.match('(.*)==(.*)',line) is not None):
					#print"---------------------------------------START----------------------------"
					#print line,"\n
					if(eq < 500):
						line = re.sub('==','!=',line)
					#print "---------------------------------------END------------------------------"
					#print line,"\n"
	
			if(re.match('(.*)if(.*)',line) is not None or re.match('(.*)while(.*)',line) is not None):
				#print (line,": ---------------------------------------------------inside if if")
				if(re.match('(.*)!=(.*)',line) is not None):
					#print"---------------------------------------START----------------------------"
					#print line,"\n"
					if(neq > 500):
						line = re.sub('!=','==',line)
					#print "---------------------------------------END------------------------------"
					#print line,"\n"
	
			if(re.match('(.*)0(.*)',line) is not None):
				#print"---------------------------------------START----------------------------"
				#print line,"\n"
				if(zero < 500):
					line = re.sub('0','1',line)
				#print "---------------------------------------END------------------------------"
				#print line,"\n"
	
			if(re.match('(.*)1(.*)',line) is not None):
				#print"---------------------------------------START----------------------------"
				#print line,"\n"
				if(one > 500):
					line = re.sub('1','0',line)
				#print "---------------------------------------END------------------------------"
				#print line,"\n"                      
	                        
			if(re.match('.*\"(.*)\".*',line) is not None):
				#print"---------------------------------------START----------------------------"
				#print line,"\n"
				if(chgStr > 500):
					match = re.search(".*(\".*\").*",line)
					line = line.replace(match.group(1),"\"shit\"")
				#print "---------------------------------------END------------------------------"
				#print line,"\n"                      
	
		fout = open(file_name,'w')
		for l in lines:
			fout.write(l)
		#print(file_name)
		
def gitcommit(i):
	#os.system('git add . && git commit -m "fuzzed %d"' %i)
	os.system('git add . && git commit -m "fuzzed %d"' %i)
	sha1 = os.popen('git rev-parse HEAD').read()
	print sha1

def revertcommit(i,sha):
	while True:
		response = requests.get('http://159.203.180.176:8080/job/itrust%20test/5/api/json',
								auth=('admin', 'ece6144f110d430586988c71da1f3ae1'))
		try: 
			data = response.json()
			if data['building'] != False:
				time.sleep(5)
				continue
			os.system('git checkout %s' %sha)
			break
		except ValueError:
			print data

def main():
	for i in range(1):
		os.system('git branch fuzzer && git checkout fuzzer')
		fuzzing()
		gitcommit(i)
		revertcommit(i,sha1)


if __name__ == "__main__":
	main()

