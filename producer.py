import pika

# Connection parameters
connection_params = pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials('user', 'password'))
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare a queue
channel.queue_declare(queue='test_queue2')

# Publish a message
channel.basic_publish(exchange='', routing_key='test_queue', body='Hello RabbitMQ!')
print(" [x] Sent 'Hello RabbitMQ!'")

# Close the connection
connection.close()
