#!/usr/bin/env python
import pika, sys, os

rabbitHost = os.environ.get('RABBIT_HOST', 'localhost')

connection = pika.BlockingConnection(
    pika.ConnectionParameters(rabbitHost, 
                            5672, 
                            '/', 
                            pika.PlainCredentials('user', 'password')))

def main():
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)