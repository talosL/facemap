import socket
import web
import json

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',8880))
server.listen(5)
while True:
    conn,addr=server.accept()
    print(conn,addr)
    while True:
        data=conn.recv(102400)
        print(conn,addr)
        if not data:
            print("断开连接")
            break
        data=data.decode()
        #if(web.loapi())
        #print(eval(data))
        da=json.loads(data)
        print(da['key'])
        print(da['key1'])
        print(da['key2'])
        print(da['key3'])
        print(da['key4'])
        try:
            web.loapi(da['key'],da['key1'],da['key2'],da['key3'],da['key4'])
        except:
            print("出错啦！！！")
        conn.send(data.encode())
conn.close()