import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print(f'Conectado {str(rc)}')
    client.subscribe("s1")
    client.subscribe("s2")

def on_message(client, userdata, msg):
    print(f'{msg.topic}{str(msg.payload)}')
    x=0
    y=0
    if(msg.topic=="s1"):
        for i in str(msg.payload):
            if i=="0":
                print("pedra")
                x+=1       
            if i=="5":
                print("papel")
                x+=1       
            if i=="2":
                print("tesoura")
                x+=1       
    if(msg.topic=="s2"):
        for i in str(msg.payload):
            while i=="0":
                print("pedra")
                y+=1
                if(msg.topic=="s1"):
                    for i in str(msg.payload):
                        if i=="2":
                            print("tesoura")
                            y-=1
                        if i=="5":
                            print("papel")
                            y+=2
        for i in str(msg.payload):
            if i=="5":
                print("papel")
                y+=1
            fim=0
            while(fim!=1):
                if(msg.topic=="s1"):
                    for i in str(msg.payload):
                        if i=="2":
                            print("tesoura")
                            y-=1
                        if i=="0":
                            print("pedra")
                            y+=2
                fim+=1
        for i in str(msg.payload):
            while i=="2":
                print("tesoura")
                y+=1
                if(msg.topic=="s1"):
                    for i in str(msg.payload):
                        if i=="5":
                            print("papel")
                            y-=1
                        if i=="0":
                            print("pedra")
                            y+=2
    if(x<y):
     print("s2 venceu")
    if(x>y):
     print("s1 venceu")

    x=[]
    y=[]
    if(msg.topic=="s1"):
            for i in str(msg.payload):
                x.append(i)
    if(msg.topic=="s2"):
            for i in str(msg.payload):
                y.append(i)
    print(x)
    print(y)
    print(x,y)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("127.0.0.1", 1883, 60)
client.loop_forever()


