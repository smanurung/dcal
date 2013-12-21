from User import User
import pika, sys

if __name__ == "__main__":
	tmp = sys.argv[1]
	u = User(tmp)
	print "username",u.getName()
	
#	CONSTANT
	hostname = 'localhost'
	
	connection = pika.BlockingConnection(pika.ConnectionParameters(host = hostname))
	channel = connection.channel()
	result = channel.queue_declare(exclusive = True)
	queue_name = result.method.queue
	
	while 1:
		cmd = raw_input('> ')
		param = cmd.split(' ')
		
		if(param[0].strip() == '/NAME'):
			if(param.__len__()>1):
				u.setName(param[1])
				print "INFO: Successfully change name to",u.getName()
			else:
				print "WARNING: You must enter new name to change"
