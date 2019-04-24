import facemap as fm
import facedb
import sys
import client

if __name__ == "__main__":
    key=sys.argv[1]
    if key=='takephoto':
        pass
    if key=='upadtaface':
        # 更新已确认人脸参考如下
        # fm.upadtaface('2b6db1ffae9e1ee27095978f80820838','杨天瑞','1',0)
        try:
            fm.upadtaface(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
        except IndexError:
            print("参数传入有误，请重新输入")
    if key=='upload':
        try:
            info = fm.uploadphoto(sys.argv[2])
            if info != False:       #如果照片中人脸只有一人则进行搜索，如果人脸已存在则提示是否更新，不存在则提示为人脸输入信息
                face_name=fm.websearch(info)
                if face_name!=False:
                    print(face_name)
                else:
                    facedb.insertface(info,'姓名','添加人信息',sys.argv[2]) #为人脸输入信息
            else:                   #如果上传的照片没有人脸或者人脸大于2人则返回False，请重新上传
                print("上传的照片中没有人脸信息或者人脸信息大于2人")
        except IndexError:
            print("参数传入有误，请重新输入")
    if key=='remove':
        try:
            fm.removeall(sys.argv[2])
        except IndexError:
            print("参数传入有误，请重新输入")
    else:
        print("参数传入有误，请重新输入")