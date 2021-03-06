#! /usr/bin/python3
import karkhanaiot
import pymysql


#CODE YOU SHOULD BE DEALING WITH
request = karkhanaiot.getrequest()
try:
	connection = pymysql.connect(
			db='iot',
			user='root',
			passwd='iot@karkhana',
			host='localhost'
		)
	c = connection.cursor(pymysql.cursors.DictCursor)
	dbflag = False
except:
	print("Error Connecting to database!")
	dbflag = True

#CHECK THE METHOD
if dbflag == False:
	if request['REQUEST_METHOD'] == 'GET':
		try:
			query = "SELECT * FROM imu"
			c.execute(query)
			data = c.fetchall()
			print(data)
		except:
			print("There were one or more errors in your query!")

	elif request['REQUSET_METHOD'] == 'POST':
		try:
			query = "INERT INTO imu(steps, total) VALUES(%s, %s)" \
			%(request['steps'], request['total'])
			c.execute(query)
			connection.commit()
		except:
			print("There were one or more errors in your query!")
			connection.rollback()