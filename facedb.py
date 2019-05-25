import pymysql
import time
import uuid
import facemap as fm
import admin
pymysql.install_as_MySQLdb()

#拍照
def takephoto(img):
    fp = open(img, 'rb')
    f1 = fp.read()
    time_now=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())#获取系统当前时间
    conn = pymysql.connect(host=admin.dbhost, user=admin.dbuser, passwd=admin.dbpasswd, db='mysql')
    cursor = conn.cursor()
    change="use face_db"
    cursor.execute(change)
    face_info = fm.detect_face(img)
    try:
        if face_info['faces']:
            if len(face_info['faces']) == 1:
                token = face_info['faces'][0]['face_token']
                name = fm.websearch(token)
                if name ==False:
                    name=insertfacestr(token, f1)
                print("token:{},name:{}".format(token, name))
                sql = "INSERT INTO cam_photo (face_path,face_token1,face_name1,time) VALUES  (%s,%s,%s,%s)"
                cursor.execute(sql, (f1, token,name,time_now))
                conn.commit()
            elif len(face_info['faces']) == 2:
                token1 = face_info['faces'][0]['face_token']
                name1 = fm.websearch(token1)
                if name1 ==False:
                    name1=insertfacestr(token1, f1)
                token2 = face_info['faces'][1]['face_token']
                name2 = fm.websearch(token2)
                if name2 ==False:
                    name2=insertfacestr(token2, f1)
                print("token:{},name:{} and token:{},name:{}".format(token1, name1, token2, name2))
                sql = "INSERT INTO cam_photo (face_path,face_token1,face_name1,face_token2,face_name2,time) VALUES  (%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql, (f1, token1, name1, token2, name2,time_now))
                conn.commit()
            else:
                sql = "INSERT INTO cam_photo (face_path,time) VALUES  (%s,%s)"
                cursor.execute(sql, (f1, time_now))
                conn.commit()

        else:
            sql = "INSERT INTO cam_photo (face_path,time) VALUES  (%s,%s)"
            cursor.execute(sql, (f1, time_now))
            conn.commit()
    except KeyError:
        return False
    # sql = "INSERT INTO cam_photo (face_path,time) VALUES  (%s,%s)"
    # cursor.execute(sql,(f1,time_now))
    # conn.commit()
    cursor.close()
    conn.close()
    print("照片已保存")

#向数据库中插入已确认人脸信息
def insertface(face_token,face_name,user_id,img=None):
    if(img==None):
        f1=None
    else:
        fp = open(img, 'rb')
        f1 = fp.read()
    time_now=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())#获取系统当前时间
    conn = pymysql.connect(host=admin.dbhost, user=admin.dbuser, passwd=admin.dbpasswd, db='mysql')
    cursor = conn.cursor()
    change="use face_db"
    cursor.execute(change)
    sql = "INSERT INTO face_1 (face_token,face_path,face_name,user_id,uptime) VALUES  (%s,%s,%s,%s,%s)"
    try:
        cursor.execute(sql,(face_token,f1,face_name,user_id,time_now))
        conn.commit()
    except pymysql.err.IntegrityError:
        print('出错')
        cursor.close()
        conn.close()
        return
    cursor.close()
    conn.close()
    print("face已添加")

#从已确认的数据库人脸修改信息
def updateface(face_token,face_name,user_id):
    time_now=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())#获取系统当前时间
    conn = pymysql.connect(host=admin.dbhost, user=admin.dbuser, passwd=admin.dbpasswd, db='mysql')
    cursor = conn.cursor()
    change = "use face_db"
    cursor.execute(change)
    sql="UPDATE face_1 SET face_name = %s,user_id=%s,uptime=%s WHERE face_token = %s"
    cursor.execute(sql,(face_name,user_id,time_now,face_token))
    conn.commit()
    cursor.close()
    conn.close()
    print("face已修改")

#向数据库中插入未确认人脸信息
def insertfacestr(face_token,img):
    # fp=open(img,'rb')
    # f1=fp.read()
    time_now=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())#获取系统当前时间
    conn = pymysql.connect(host=admin.dbhost, user=admin.dbuser, passwd=admin.dbpasswd, db='mysql')
    cursor = conn.cursor()
    change="use face_db"
    cursor.execute(change)
    strname=uuid.uuid4().hex
    sql = "INSERT INTO facestr_1 (face_token,face_path,face_strname,time) VALUES  (%s,%s,%s,%s)"
    try:
        cursor.execute(sql,(face_token,img,strname,time_now))
        conn.commit()
    except pymysql.err.IntegrityError:
        print('face_token已重复')
        cursor.close()
        conn.close()
        return
    cursor.close()
    conn.close()
    fm.addface(face_token,fm.strangfacest)
    fm.face_SetUserID(face_token,strname)
    return strname

#从陌生人到已确认
def strtoface(face_token,face_name,user_id):
    time_now=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())#获取系统当前时间
    conn = pymysql.connect(host=admin.dbhost, user=admin.dbuser, passwd=admin.dbpasswd, db='mysql')
    cursor = conn.cursor()
    change="use face_db"
    cursor.execute(change)
    sql = "INSERT INTO face_1 " \
          "(face_token,face_path,face_name) " \
          "SELECT distinct s.face_token,s.face_path,s.face_strname FROM facestr_1 s " \
          "WHERE s.face_token=%s "
    try:
        print('执行1')
        cursor.execute(sql,face_token)
        print('执行2')
        conn.commit()
    except pymysql.err.IntegrityError:
        print('执行3')
        cursor.close()
        conn.close()
        return
    sql="UPDATE face_1 SET face_name = %s,user_id=%s,uptime=%s WHERE face_token = %s"
    cursor.execute(sql, (face_name,user_id,time_now,face_token))
    conn.commit()
    sql="DELETE FROM facestr_1 WHERE face_token = %s"
    cursor.execute(sql,face_token)
    conn.commit()
    cursor.close()
    conn.close()

#今日来访
def today(face_name,img):
    time_now = time.strftime("%H:%M:%S", time.localtime())  # 获取系统当前时间
    conn = pymysql.connect(host=admin.dbhost, user=admin.dbuser, passwd=admin.dbpasswd, db='mysql')
    cursor = conn.cursor()
    change = "use face_db"
    cursor.execute(change)
    sel = "SELECT * FROM today WHERE face_name = %s"
    if(cursor.execute(sel,face_name)==0):
        sql = "INSERT INTO today (face_name,face_path,time) VALUES  (%s,%s,%s)"
        cursor.execute(sql, (face_name,img,time_now))
        conn.commit()
        cursor.close()
        conn.close()
        return True  #已添加来访记录
    else:
        sql = "UPDATE today SET time = %s WHERE face_name = %s"
        cursor.execute(sql,(time_now,face_name))
        conn.commit()
        cursor.close()
        conn.close()
        return False #已存在来访数据

#来访记录
def day(face_token,face_name,img):
    time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 获取系统当前时间
    conn = pymysql.connect(host=admin.dbhost, user=admin.dbuser, passwd=admin.dbpasswd, db='mysql')
    cursor = conn.cursor()
    change = "use face_db"
    cursor.execute(change)
    if today(face_name,img):
        sql = "INSERT INTO day (face_token,time,face_path,face_name) VALUES  (%s,%s,%s,%s)"
        cursor.execute(sql, (face_token, time_now,img,face_name))
        conn.commit()
        cursor.close()
        conn.close()
        print("已添加来访记录")
        return True
    else:
        sql="UPDATE day SET time = %s,face_path=%s WHERE face_name = %s AND (to_days(time) = to_days(now()))"
        cursor.execute(sql,(time_now,img,face_name))
        conn.commit()
        cursor.close()
        conn.close()
        print("已更新来访记录")
        return False

#来访记录情绪添加
def emoday(face_name,photo,analyze):
    fp = open(photo, 'rb')
    img = fp.read()
    time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 获取系统当前时间
    conn = pymysql.connect(host=admin.dbhost, user=admin.dbuser, passwd=admin.dbpasswd, db='mysql')
    cursor = conn.cursor()
    change = "use face_db"
    cursor.execute(change)
    sql="UPDATE day SET time = %s ,face_path=%s,face_gander=%s, face_age=%s ,face_ethnicity= %s, face_emotions=%s" \
        " WHERE face_name = %s AND (to_days(time) = to_days(now()))"
    cursor.execute(sql, (time_now, img,analyze['gander'],analyze['age'],analyze['ethnicity'],analyze['emotions'],face_name))
    conn.commit()
    sql = "UPDATE today SET time = %s ,face_path=%s,face_gander=%s, face_age=%s ,face_ethnicity= %s, face_emotions=%s" \
          " WHERE face_name = %s"
    cursor.execute(sql, (
    time_now, img, analyze['gander'], analyze['age'], analyze['ethnicity'], analyze['emotions'], face_name))
    conn.commit()
    cursor.close()
    conn.close()
    print("已更新来访情绪")

#陌生人今日来访
def today_str(face_strname,img):
    time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 获取系统当前时间
    conn = pymysql.connect(host=admin.dbhost, user=admin.dbuser, passwd=admin.dbpasswd, db='mysql')
    cursor = conn.cursor()
    change = "use face_db"
    cursor.execute(change)
    sel = "SELECT * FROM today_str WHERE face_strname = %s"
    if (cursor.execute(sel, face_strname) == 0):
        sql = "INSERT INTO today_str (face_strname,time,face_path) VALUES  (%s,%s,%s)"
        cursor.execute(sql, (face_strname, time_now,img))
        conn.commit()
        cursor.close()
        conn.close()
        return True  # 已添加来访记录
    else:
        sql = "UPDATE today_str SET time = %s WHERE face_strname = %s"
        cursor.execute(sql, (time_now, face_strname))
        conn.commit()
        cursor.close()
        conn.close()
        return False  # 已存在来访数据

#陌生人来访记录
def daystr(face_token,face_strname,img):
    time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 获取系统当前时间
    conn = pymysql.connect(host=admin.dbhost, user=admin.dbuser, passwd=admin.dbpasswd, db='mysql')
    cursor = conn.cursor()
    change = "use face_db"
    cursor.execute(change)
    if today_str(face_strname,img):
        sql = "INSERT INTO day_str (face_strname,face_path,time,face_token) VALUES  (%s,%s,%s,%s)"
        cursor.execute(sql, (face_strname, img, time_now,face_token))
        conn.commit()
        cursor.close()
        conn.close()
        print("已添加来访记录")
        return True
    else:
        sql="UPDATE day_str SET time = %s,face_path=%s WHERE face_strname = %s AND (to_days(time) = to_days(now()))"
        cursor.execute(sql,(time_now,img,face_strname))
        conn.commit()
        cursor.close()
        conn.close()
        print("已更新来访记录")
        return False


#删除陌生人信息
def removestr(face_token):
    conn = pymysql.connect(host=admin.dbhost, user=admin.dbuser, passwd=admin.dbpasswd, db='mysql')
    cursor = conn.cursor()
    change = "use face_db"
    cursor.execute(change)
    sql="delete from facestr_1 where face_token = %s"
    cursor.execute(sql,face_token)
    conn.commit()
    cursor.close()
    conn.close()

#删除人脸信息
def removeface(face_token):
    conn = pymysql.connect(host=admin.dbhost, user=admin.dbuser, passwd=admin.dbpasswd, db='mysql')
    cursor = conn.cursor()
    change = "use face_db"
    cursor.execute(change)
    sql = "delete from face_1 where face_token = %s"
    cursor.execute(sql, face_token)
    conn.commit()
    cursor.close()
    conn.close()

def uploadimg(img):
    fp = open(img, 'rb')
    img = fp.read()
    time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 获取系统当前时间
    conn = pymysql.connect(host=admin.dbhost, user=admin.dbuser, passwd=admin.dbpasswd, db='mysql')
    cursor = conn.cursor()
    change = "use face_db"
    cursor.execute(change)
    sql="INSERT INTO photo (face_path,time) VALUES  (%s,%s)"
    cursor.execute(sql, (img,time_now))
    conn.commit()
    cursor.close()
    conn.close()

