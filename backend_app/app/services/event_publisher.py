import pika
import json

def publish_event(event_name, payload):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='events', exchange_type='topic')

    channel.basic_publish(exchange='events', routing_key=event_name, body=json.dumps(payload))

    connection.close()
