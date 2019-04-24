import threading
import os
import glob as gb
import facemap as fm
import cv2
import facedb
import time

def cam():
    capInput = cv2.VideoCapture(0)
    path = r'.\haarcascade_frontalface_alt.xml'
    save_path = (r'.\img\20.jpg')
    save = (r'.\img\10.jpg')
    faceCascade = cv2.CascadeClassifier(path)
    face_right = 0  # 识别的人脸有没有在faceset中发现，有置1
    recognize_inf = 0  # 识别的人脸在faceset中发现，置1,持续显示id信息一定时间标志位
    font = cv2.FONT_HERSHEY_SIMPLEX  # 字体设置
    i = 0
    m = []
    temp = 0
    while (1):
        time_now = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime())  # 获取系统当前时间
        ret, img = capInput.read()  # 摄像头获取该帧图像
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 图像转灰度
        faces = faceCascade.detectMultiScale(gray, 1.2, 7)  # 送入Haar特征分类器
        k = cv2.waitKey(1)  # 读键盘
        if k == ord('s'):
            cv2.imwrite(save_path, img)
            imgresize = cv2.imread(save_path)
            res = cv2.resize(imgresize, (480, 360), interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(save_path, res)
            facedb.takephoto(save_path)
            print('已保存')
        if k == ord('q'):
            break
        if len(faces) == 0:  # 视频中无脸出现
            cv2.imshow('face recognition', img)
        else:
            imgpath = (r'.\img\temp\\' + time_now + '.jpg')
            if i >= 100:
                i = 0
                for x, y, w, h in faces:
                    roiImg = img[y - 50:y + h + 200, x - 25:x + w + 100]
                    cv2.imwrite(imgpath, roiImg)  # 写入该帧图像文件
                    time.sleep(0.5)
            else:
                i = i + 1
            for x, y, w, h in faces:
                # roiImg = img[y - 50:y + h + 200, x - 25:x + w + 100]
                # cv2.imwrite(imgpath, roiImg)  # 写入该帧图像文件
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 人脸矩形框
            cv2.imshow('face recognition', img)

    capInput.release()
    cv2.destroyAllWindows()

def server():

    #print("server")
    m = []
    temp_name = None
    while (1):
        img_path1 = gb.glob(r".\img\temp\\*.jpg")
        dir_path = (r".\img\temp\\")
        file_num=len([name for name in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, name))])
        print(file_num)
        if file_num <1 :
            print("sleep")
            time.sleep(2)
            continue

        else:
            #print("出现bug")
            for path in img_path1:
                #print("1")
                img2 = cv2.imread(path)
                imgpath1 = r'.\img\1.jpg'
                #cv2.imwrite(r'.\img\1.jpg', img2)  # 写入该帧图像文件
                #print("2")
                try:
                    face_information = fm.detect_face(path)
                except FileNotFoundError:
                    continue
                print(face_information)
                try:
                    if face_information['faces']:
                        key1 = face_information['faces'][0]['face_token']  # face_token
                        if face_information['faces']:
                            faceinfo,db = fm.Ssearch(path,key1)
                            user_id = faceinfo['results'][0]['user_id']  # 获得姓名
                            temp_name=user_id
                            print("{}:{}".format("来访人姓名", user_id))
                        # m.append(user_id)
                            face_inf = faceinfo['results'][0]['face_token']  # 获得人脸token
                            if db:
                                emo = fm.face_analyze(key1)
                                facedb.emoday(user_id, imgpath1, emo)
                        os.remove(path)
                        print("已处理")
                except KeyError:
                    continue
                except FileNotFoundError:
                    continue
                    # img3=cv2.imread(r'.\img\2.jpg')
            #                     # cv2.imwrite(r'.\img\1.jpg', img3)


thread=[]
t1=threading.Thread(target=cam)
thread.append(t1)
t2=threading.Thread(target=server)
thread.append(t2)

if __name__ == "__main__":
    for t in thread:
        t.start()
    for t in thread:
        t.join()