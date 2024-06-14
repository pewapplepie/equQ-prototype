import pika, json


# params = pika.URLParameters('{{amqps://eqxhmutj:nbQbKzk0myhx7dHqeyVmHhbv0-amoiBT@prawn.rmq.cloudamqp.com/eqxhmutj}}')

# connection = pika.BlockingConnection(params)
connection_params = pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials('user', 'password'))
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='config', body=json.dumps(body), properties=properties)