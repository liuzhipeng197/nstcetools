import os
import sys
import hive_connection

sql='select pi_id from pd limit 10'

class HiveConnection(object):
	def __init__(self):
		self.connect()

	def connect(self):
		self.conn=hive_connection.Connection()
		self.conn.open()
	
	def __del__(self):
		self.conn.close()
	
	def hive_exec(self,sql):
		self.conn.client.execute(sql)
		print self.conn.client.fetchAll()

if __name__=='__main__':
	hc=HiveConnection()
	hc.hive_exec(sql)
