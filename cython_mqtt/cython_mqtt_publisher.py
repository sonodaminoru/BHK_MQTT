# -*-encode: utf-8-*-
from time import sleep
import paho.mqtt.client as mqtt
import cython_code   #ここにsetup.pyで作成したモジュールをインポートする

HOST = '192.168.3.11' #ブローカーを動かしているアドレス
PORT = 1883
KEEP_ALIVE = 60
TOPIC = 'BHX'
MESSAGE = 'test message'

PUBLISH_NUMBER = 5
SLEEP_TIME = 5

# パブリッシュする関数ここでmindwaveから取り出した値をおくる
def publish_many_times(client, topic='BHX', message='default', number=1, time=1, print_flag=False):

    total = 0
    x = 1
    y = 2
    for i in range(number):
        #ここでmessageに入れる文字列を作成する(JSON文字列やただの値など)
        #ここで呼ぶ関数はc言語の中の関数ではなく、pythonの関数名となる。
        #cython_pyx_code.pyxを参照すること
        total = cython_code.py_add(x, y)
        
        #文字列に変換
        message = str(total)
        
        client.publish(topic, message)
        if print_flag == True:
            print (topic + ' ' + message)
            
        x += 2
        y += 2
        sleep(time)

    client.disconnect()

if __name__ == '__main__':
    client = mqtt.Client(protocol=mqtt.MQTTv311)

    print ("publish start " + str(type(client)))

    client.connect(HOST, port=PORT, keepalive=KEEP_ALIVE)

    publish_many_times(client,TOPIC, MESSAGE, PUBLISH_NUMBER, SLEEP_TIME)  
