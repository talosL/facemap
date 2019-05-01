import facemap as fm
import facedb
import sys
import client

#api函数，对接socket接口，port：8888
def loapi(key,key1='',key2='',key3='',key4=''):
    if key=='takephoto':
        pass
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
                if face_name!=False:
                    print(face_name)
                    return info
                else:
                     return info
            else:                   #如果上传的照片没有人脸或者人脸大于2人则返回False，请重新上传
                print("上传的照片中没有人脸信息或者人脸信息大于2人")
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