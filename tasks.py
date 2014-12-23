#!/usr/bin/python

argval = input("Enter The Task ID : ")
if argval == 1:
	varinput 	= raw_input('Enter the list of numbers to sort(concat by ",") : ');
	numlist 	= varinput.split(',');
	maxvalue 	= max(numlist);
	print "Given Number List :", numlist;
	numlist.remove(maxvalue);
	seclargevalue = max(numlist);
	print "Second Largest Value :", seclargevalue;
elif argval == 2:
	import os
	import datetime

	filename		=	'sample.json';
	resultfile		=	'resultfile.txt';
	getfilesize 	= 	os.path.getsize(filename);
	fileSize 		= 	float(getfilesize) / (1024*1024);

	try:
		if fileSize > 1:		
			print "File size (%f) is greater than 1 MB" % fileSize;
		else:
			fh					=	open(resultfile, "w+");
			FileContent			= 	"File Size : %.2f" % fileSize + "\n" + "Date : %s" % datetime.datetime.now();	
			fh.write(FileContent);		
	 		fh.close();
	 		print "File writed Successfully";
	except:
	 	print "File size (%f) is greater than 1 MB" % fileSize;

elif argval == 3:
	import json
	import urllib2

	jsonfile = urllib2.urlopen('https://api.github.com/users/mralexgray/repos');
	jsonlist = json.load(jsonfile);
	cntval = 0
	for nodename in jsonlist:
	    if nodename['fork']==False:
	    	cntval += 1
	    	print "---------------------------------"
	        print "  "+nodename['name'];
	print "Total Found :"+str(cntval);
elif argval == 4:
	import mathclass
	print "\n  1. ADD  \n  2. SUBTRACT \n  3. MULTIPLY \n  4. DIVIDE \n";
	usrinput 	= input("Enter Your Choice : ");
	firstval 	= input('Enter the first number :');
	secval 		= input('Enter the second number :');
	
	obj = mathclass.mathclass(firstval,secval);

	if usrinput==1:
		obj.actaddition();
	elif usrinput==2:
		obj.actsubstraction();
	elif usrinput==3:
		obj.actmultiplication();
	elif usrinput==4:
		obj.actdivision();

	
	



