#!/usr/bin/python

import MySQLdb
import datetime

print "\n  1. LIST  \n  2. INSERT \n  3. UPDATE \n  4. DELETE \n";
argtype = raw_input("Enter the Action : ");
if argtype == '2':
	argbookname = raw_input("Enter the Book Name : ");
	argauthor = raw_input("Enter the Author : ");
	argisbn = raw_input("Enter the Isbn : ");
	sql = "INSERT INTO tbl_book(bookname, author, isbn, createdon)  VALUES ('%s', '%s', '%s', '%s' )" % (argbookname, argauthor, argisbn, datetime.datetime.now())
	try:
		db = MySQLdb.connect("localhost","root","password","python" )
		cursor = db.cursor()
		cursor.execute(sql)
		db.commit()
		db.close()
	except:
	   print "Query Error"+sql;
elif argtype == '3':
	argsno = input("Enter the Sno to Update : ");
	if type(argsno) == int:
		argbookname = raw_input("Enter the Book Name : ");
		argauthor = raw_input("Enter the Author : ");
		argisbn = raw_input("Enter the Isbn : ");
		sql = "UPDATE tbl_book SET bookname='%s', author='%s', isbn='%s' WHERE sno=%d" % (argbookname, argauthor, argisbn, argsno)
		try:
			db = MySQLdb.connect("localhost","root","password","python" )
			cursor = db.cursor()
			cursor.execute(sql)
			db.commit()
			db.close()
		except:
		   print "Query Error"+sql;
		
	else:
		print  "Enter The Valid Sno";
elif argtype == '4':
	argsno = input("Enter the Sno to Delete : ");
	if type(argsno) == int:
		sql = "DELETE FROM tbl_book WHERE sno=%d" % (argsno)
		try:
			db = MySQLdb.connect("localhost","root","password","python" )
			cursor = db.cursor()
			cursor.execute(sql)
			db.commit()
			db.close()
		except:
		   print "Query Error"+sql;
	else:
		print  "Enter The Valid Sno";
elif argtype == '1':
	db = MySQLdb.connect("localhost","root","password","python" )
	cursor = db.cursor()
	cursor.execute("SELECT * from tbl_book");
	data = cursor.fetchall()
	db.close()
	for row in data:
		sno 	= row[0]
		bname 	= row[1]
		bauthor = row[2]
		bisbn 	= row[3]
		bdate 	= row[4]
		print "================================================================================================================================"
		print "sno : %d  | Book name : %s             | Author : %s           | Isbn : %s            | Date : %s" % (sno, bname, bauthor, bisbn, bdate )
	print "\n"
else:
	print "U Have Entered Wrong Option Try Again";




	

