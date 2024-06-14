import pika

# Connection parameters
connection_params = pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials('user', 'password'))
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare a queue
channel.queue_declare(queue='test_queue')

# Callback function to process messages
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

# Set up subscription on the queue
channel.basic_consume(queue='test_queue', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
