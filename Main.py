from User import User
import pika, sys

if __name__ == "__main__":
	tmp = sys.argv[1]
	u = User(tmp)
	print "username",u.name
	
#	CONSTANT
	hostname = 'localhost'
	
	connection = pika.BlockingConnection(pika.ConnectionParameters(host = hostname))
	channel = connection.channel()
	result = channel.queue_declare(exclusive = True)
	queue_name = result.method.queue
	
	while 1:
		
