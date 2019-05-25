import facemap as fm
import facedb
import sys
import socket
import time
import client

import signal
import time


def set_timeout(num, callback):
    def wrap(func):
        def handle(signum, frame):  # 收到信号 SIGALRM 后的回调函数，第一个参数是信号的数字，第二个参数是the interrupted stack frame.
            raise RuntimeError

        def to_do(*args, **kwargs):
            try:
                signal.signal(signal.SIGALRM, handle)  # 设置信号和回调函数
                signal.alarm(num)  # 设置 num 秒的闹钟
                print('start alarm signal.')
                r = func(*args, **kwargs)
                print('close alarm signal.')
                signal.alarm(0)  # 关闭闹钟
                return r
            except RuntimeError as e:
                callback()

        return to_do

    return wrap



def after_timeout():  # 超时后的处理函数
    print('timeout')
    return 1


@set_timeout(6, after_timeout)
def socket_service():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('0.0.0.0', 6666))
        s.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    a=time
    print('Waiting connection...')
    while True:
        conn, addr = s.accept()
        data = 'takephoto'
        data = data.encode()
        conn.send(data)
        getdata = conn.recv(102400)
        getdata = getdata.decode()
        conn.close()
        if getdata == 'ok':
            # print('ok')
            return True
        else:
            return False


#api函数，对接socket接口，port：8888
def loapi(key,key1='',key2='',key3='',key4=''):
    if key=='takephoto':
        socket_service()
    elif key=='updateface':
        # 更新已确认人脸参考如下
        # fm.upadtaface('2b6db1ffae9e1ee27095978f80820838','杨天瑞','1',0)
        try:
            #fm.upadtaface('2b6db1ffae9e1ee27095978f80820838', 'dly', 1, 0)
            #fm.upadtaface('1e38e7411c92e0ab5d705e0282d5ea03', 'dly', 1, 1)
            fm.upadtaface(key1,key2,key3,key4)
        except IndexError:
            print("参数传入有误，请重新输入2")
        return 0
    elif key=='upload':
        try:
            info = fm.uploadphoto(key1) #key1为图片路径
            if info != False:       #如果照片中人脸只有一人则进行搜索，如果人脸已存在则提示是否更新，不存在则提示为人脸输入信息
                face_name=fm.websearch(info)
                facedb.uploadimg(key1)
                if face_name!=False:
                    print(face_name) #是否需要更改人脸信息，需要则执行updateface
                    return face_name
                else:
                     print('输入新的人脸信息')
                     return True   #执行uploadinfo
            else:                   #如果上传的照片没有人脸或者人脸大于2人则返回False，请重新上传
                print("上传的照片中没有人脸信息或者人脸信息大于2人")
                return False
        except IndexError:
            print("参数传入有误，请重新输入3")
    elif key=='remove':
        try:
            fm.removeall(key1)
        except IndexError:
            print("参数传入有误，请重新输入4")
    elif key=='uploadinfo': #插入人脸信息
        facedb.insertface(key2, '姓名', '添加人信息', key1)  #key1为图片，key2为upload返回的token值
    else:
        print(key)
        print("参数传入有误，请重新输入5")