import pika, json


params = pika.URLParameters('{{amqps://eqxhmutj:nbQbKzk0myhx7dHqeyVmHhbv0-amoiBT@prawn.rmq.cloudamqp.com/eqxhmutj}}')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='core', body=json.dumps(body), properties=properties)