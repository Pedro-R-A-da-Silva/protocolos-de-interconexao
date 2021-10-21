import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print(f'Conectado {str(rc)}')

def on_message(client, userdata, msg):
    print(f'{msg.topic} {str(msg.payload)}')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect_async("localhost", 1883, 60)
client.loop_start()
while True:
    topic = 's1'
    print("---jo..ken..pow!!!---")
    print('PEDRA(....,):0')
    print('PAPEL(\||/,):5')
    print('TESOURA(..\/,):2')
    msg = input('MOVIMENTO: ')
    client.publish(topic, msg)

    topic = 's1'
    print("---jo..ken..pow!!!---")
    print('PEDRA(....,):0')
    print('PAPEL(\||/,):5')
    print('TESOURA(..\/,):2')
    msg = input('MOVIMENTO: ')
    client.publish(topic, msg)
