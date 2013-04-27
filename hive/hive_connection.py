import os
import sys

sys.path.append('/warehouse/hive/lib/py')

from hive_service import ThriftHive
from hive_service.ttypes import HiveServerException
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

class Connection(object):
	def __init__(self):
		try:
			self.socket = TSocket.TSocket('192.168.1.171', 10001)
			self.transport = TTransport.TBufferedTransport(self.socket)
			self.protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
			self.client = ThriftHive.Client(self.protocol)
		except Thrift.TException, tx:
			print '%s' % (tx.message)

	def open(self):
		self.transport.open()

	def close(self):
		self.transport.close()

