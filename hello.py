#!/usr/bin/env python
import pika, time, os

rabbitHost = os.environ.get('RABBIT_HOST', 'localhost')

print('Rabbit host: ', rabbitHost)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(rabbitHost, 
                            5672, 
                            '/', 
                            pika.PlainCredentials('user', 'password')))

channel = connection.channel()
channel.queue_declare(queue='hello')

try:
    while True:
        channel.basic_publish(exchange='',
                        routing_key='hello',
                        body='Hello from sender service!')
        print("[SenderService] Sent greeting message. Waiting for Service2 to ACK")
        time.sleep(5)
except KeyboardInterrupt:
    print('Interrupted')
    