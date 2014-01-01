from User import User
from threading import Thread
from Event import Event
import pika, sys, time

def callback(channel,method_frame,header_frame,body):
	print body

def startListening():
	print 'Listening to calendar \''+calName+'\' ...'
	global keepListening
	channel.start_consuming()

if __name__ == "__main__":
	tmp = sys.argv[1]
	u = User(tmp)
	print "username",u.getName()
	
#	CONSTANT
	hostname = 'localhost'
	
	connection = pika.BlockingConnection(pika.ConnectionParameters(host = hostname))
	global channel
	channel = connection.channel()
#	gimana cara pastiin queue name unik
	result = channel.queue_declare(exclusive = True)
	queue_name = result.method.queue
	
	while 1:
		cmd = raw_input('> ')
		param = cmd.split(' ')
		
#		comm /EXIT
		if(param[0].strip() == '/EXIT'):
			print "INFO: Successfully closed program"

			channel.stop_consuming()
			connection.close()
			break
#		comm /NAME <username>
		elif(param[0].strip() == '/NAME'):
			if(param.__len__()>1):
				u.setName(param[1])
				print "INFO: Successfully change name to",u.getName()
			else:
				print "WARNING: You must enter new name to change"
#		comm /CAL <calendar-name>
		elif(param[0].strip() == '/CAL'):
			if(param.__len__()>1):
				calName = param[1].strip()
				
				u.addCal(calName)
				x = calName + 'X'
#				make sure the calendar exists
				channel.exchange_declare(exchange=x,type='fanout')
				channel.queue_bind(exchange=x,queue=u.getQueueName())
				channel.basic_consume(callback,queue=u.getQueueName(),no_ack=False)
				
#				run listening thread
				temp = Thread(target = startListening, args = ())
				temp.start()
				u.addListener(temp)
				print "Successfully added Calendar",calName
			else:
				print "ERROR: Format /CAL <calendar-name>"
#		comm /EVT <calendar-name> <event-name> <event-place> <event-start-hour> <event-end-hour> <event-description>
#		hour consists of 4 character e.g. 04pm, 05am
#		no space character for description
		elif(param[0].strip() == '/EVT'):
			if (param.__len__() == 7):
				calName = param[1].strip()
				EvtName = param[2]
				EvtPlace = param[3]
				EvtStart = param[4]
				EvtEnd = param[5]
				EvtDesc = param[6]

				ev = Event(EvtName,EvtPlace,EvtStart,EvtEnd,EvtDesc)

				x = calName + 'X'
				channel.exchange_declare(exchange=x,type='fanout')

				message = ev.toString()
				print "message:",message
				channel.basic_publish(exchange=x,routing_key='',body=message)
				print "INFO: Event sent to calendar",calName
			else:
				print "ERROR: Parameter Error"