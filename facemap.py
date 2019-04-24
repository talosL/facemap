# -*- coding: utf-8 -*-
import requests
from json import JSONDecoder
import cv2
import numpy
import facedb
import pymysql
import admin
from PIL import Image, ImageDraw, ImageFont


key =admin.facekey
secret =admin.facesecret
faceset1 =admin.faceset1
strangfacest=admin.facestr1
data = {"api_key":key, "api_secret": secret}



def detect_face(filepath):#传入图片文件
    http_url ="https://api-cn.faceplusplus.com/facepp/v3/detect"
    files = {"image_file": open(filepath, "rb")}

    #starttime = datetime.datetime.now()
    response = requests.post(http_url, data=data, files=files)
    #endtime = datetime.datetime.now()
    #print((endtime - starttime).seconds)
    req_con = response.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict

def detect_face_64(filepath):#传入base64编码
    http_url ="https://api-cn.faceplusplus.com/facepp/v3/detect"
    files = {"image_file": open(filepath, "rb")}

    #starttime = datetime.datetime.now()
    response = requests.post(http_url, data=data, files=files)
    req_con = response.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
   # print(req_dict)
    return req_dict

#创建faceset
def create_faceset(faceset):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/create'
    parameter = {
            'api_key':key,
            'api_secret':secret,
            'outer_id': faceset,
            
            }
    r = requests.post(url,data = parameter)
    req_con = r.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    #print(req_dict)
    return req_dict

#对比两个人脸信息
def compare(faceid_1, faceid_2):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/compare'
    parameter = {
        'api_key': key,
        'api_secret': secret,
        'face_token1': faceid_1,
        'face_token2': faceid_2
    }
    r = requests.post(url, data=parameter)
    req_con = r.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    #print(req_dict)
    return req_dict

#将face加入faceset
def addface(facetokens,faceset):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/addface'
    parameter = {
            'api_key':key,
            'api_secret':secret,
            'faceset_token':faceset,
            'face_tokens':facetokens
            }
    r = requests.post(url,params = parameter)
    req_con = r.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict

def get_face_set():
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/getfacesets'
    parameter = {
            'api_key':key,
            'api_secret':secret,
            }
    r = requests.post(url,params = parameter)
    req_con = r.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict

#删除faceset
def delete_faceset(faceset_token,check_empty):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/delete'
    parameter = {
            'api_key':key,
            'api_secret':secret,
            'faceset_token':faceset_token,
            'check_empty':check_empty
            }
    r = requests.post(url,params = parameter)
    req_con = r.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict

#faceset数据更新
def faceset_update(faceset_token,display_name,user_data):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/update'
    parameter = {
            'api_key':key,
            'api_secret':secret,
            'faceset_token':faceset_token,
            'display_name':display_name,
            'user_data':user_data
            }
    r = requests.post(url,params = parameter)
    req_con = r.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict

#获取faceset信息
def faceset_getdetail(faceset_token):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/getdetail'
    parameter = {
            'api_key':key,
            'api_secret':secret,
            'faceset_token':faceset_token,
            }
    r = requests.post(url,params = parameter)
    req_con = r.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict

#人脸对比
def face_compare(image_file1,face_token2):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/compare'
    files = {"image_file1": open(image_file1, "rb")}
    parameter = {
            'api_key':key,
            'api_secret':secret,
            'face_token2':face_token2
            }
    r = requests.post(url,files = files,params = parameter)
    req_con = r.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict

#人脸搜索
def face_search(image_file1,faceset_token):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/search'
    files = {"image_file": open(image_file1, "rb")}
    parameter = {
            'api_key':key,
            'api_secret':secret,
            'faceset_token':faceset_token
            }
    r = requests.post(url,files = files,params = parameter)
    req_con = r.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict

#基于token的人脸搜索
def face_searchtoken(face_token,faceset_token):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/search'
    parameter = {
            'api_key':key,
            'api_secret':secret,
             'face_token': face_token,
            'faceset_token':faceset_token
            }
    r = requests.post(url,data = parameter)
    req_con = r.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict

#为face设置信息
def face_SetUserID(face_token,user_id):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/face/setuserid'
    parameter = {
            'api_key':key,
            'api_secret':secret,
            'face_token':face_token,
            'user_id':user_id
            }
    r = requests.post(url,params = parameter)
    req_dict = r.json()
    print(req_dict)
    return req_dict

#cv格式转换
def cv2ImgAddText(img, text, left, top, textColor=(0, 255, 0), textSize=20):
    if (isinstance(img, numpy.ndarray)):  #判断是否OpenCV图片类型
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img)
    fontText = ImageFont.truetype(
        "font/simsun.ttc", textSize, encoding="utf-8")
    draw.text((left, top), text, textColor, font=fontText)
    return cv2.cvtColor(numpy.asarray(img), cv2.COLOR_RGB2BGR)

#情绪分析
def face_analyze(face_inf):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/face/analyze'
    analyzes={}
    parameter = {
        'api_key': key,
        'api_secret': secret,
        'return_attributes': "emotion,gender,age,ethnicity",
        'face_tokens': face_inf
    }
    response = requests.post(url, data=parameter)
    req_dict = response.json()
    #print(req_dict)
    analyzes['gander']=req_dict['faces'][0]['attributes']['gender']['value'] #性别信息
    analyzes['age']=req_dict['faces'][0]['attributes']['age']['value'] #年龄
    analyzes['ethnicity']=req_dict['faces'][0]['attributes']['ethnicity']['value'] #人种信息
    emotions=req_dict['faces'][0]['attributes']['emotion']
    #print(emotions)
    analyzes['emotions']=max(emotions, key=emotions.get)
    if(analyzes['gander']=='Male'):
        analyzes['gander']='男'
    else:
        analyzes['gander'] = '女'
    if(analyzes['ethnicity']=='ASIAN'):
        analyzes['ethnicity']='亚洲人'
    if (analyzes['ethnicity'] == 'WHITE'):
        analyzes['ethnicity'] = '白人'
    if (analyzes['ethnicity'] == 'BLACK'):
        analyzes['ethnicity'] = '黑人'
    if(analyzes['emotions']=='neutral'):
        analyzes['emotions']='平静'
    if (analyzes['emotions'] == 'anger'):
        analyzes['emotions'] = '生气'
    if (analyzes['emotions'] == 'disgust'):
        analyzes['emotions'] = '厌恶'
    if (analyzes['emotions'] == 'fear'):
        analyzes['emotions'] = '恐惧'
    if (analyzes['emotions'] == 'happiness'):
        analyzes['emotions'] = '开心'
    if (analyzes['emotions'] == 'sadness'):
        analyzes['emotions'] = '伤心'
    if (analyzes['emotions'] == 'surprise'):
        analyzes['emotions'] = '惊讶'
    print(analyzes)
    return analyzes

#移除faceset中的face信息
def removeface(face_set,face_token='RemoveAllFaceTokens'):
    url='https://api-cn.faceplusplus.com/facepp/v3/faceset/removeface'
    parameter = {
        'api_key': key,
        'api_secret': secret,
        'faceset_token': face_set,
        'face_tokens': face_token
    }
    response = requests.post(url, data=parameter)
    req_dict = response.json()
    print(req_dict)
    return req_dict


#多重人脸识别
def Msearch(photo):
    info=detect_face(photo)
    le = len(info['faces'])
    token_list=[]
    user_id=[]
    str_id=[]
    for i in range(le):
        token_list.append(info['faces'][i]['face_token'])
        idinfo = face_searchtoken(token_list[i], faceset1) #获取信息
        confidence = idinfo['results'][0]['confidence']
        thresholds = idinfo['thresholds']['1e-5']
        if confidence > 75 and thresholds < confidence:  # 置信度阈值判断
            user_id.append(idinfo['results'][0]['user_id']) #face姓名添加
            token=token_list[i]
            id=user_id[i]
            facedb.day(token,id) #数据库信息插入
        else:
            strinfo=face_searchtoken(token_list[i],strangfacest)
            print(strinfo)
            confidence = strinfo['results'][0]['confidence']
            thresholds = strinfo['thresholds']['1e-5']
            if confidence > 75 and thresholds < confidence:  # 置信度阈值判断
                str_id.append(strinfo['results'][0]['user_id'])
                str=str_id[i]
                facedb.daystr(str)
            else:
                str_id.append(strinfo['results'][0]['user_id'])
                token=token_list[i]
                facedb.insertfacestr(token,photo)
                str = str_id[i]
                facedb.daystr(str)
    print(user_id)

#单人脸搜索不加入数据库
def websearch(facetoken):
    face_info=face_searchtoken(facetoken,faceset1)
    confidence = face_info['results'][0]['confidence']
    thresholds = face_info['thresholds']['1e-5']
    if confidence > 75 and thresholds < confidence:  # 置信度阈值判断
        user_id=face_info['results'][0]['user_id']  # face姓名添加
        return user_id
    else:
        strinfo = face_searchtoken(facetoken,strangfacest)
        confidence = face_info['results'][0]['confidence']
        thresholds = face_info['thresholds']['1e-5']
        token = strinfo['results'][0]['face_token']
        if confidence > 75 and thresholds < confidence:  # 置信度阈值判断
            str_name=strinfo['results'][0]['user_id']
            return str_name
        else:
            return False

#单人脸搜索加入数据库信息
def Ssearch(photo,face_token):
    fp=open(photo,'rb')
    img=fp.read()
    face_info=face_searchtoken(face_token,faceset1)
    confidence = face_info['results'][0]['confidence']
    thresholds = face_info['thresholds']['1e-5']
    if confidence > 75 and thresholds < confidence:  # 置信度阈值判断
        user_id=face_info['results'][0]['user_id']  # face姓名添加
        token=face_info['results'][0]['face_token']
        day=facedb.day(token,user_id,img)
        return face_info,day
    else:
        str_info = face_searchtoken(face_token,strangfacest)
        confidence = str_info['results'][0]['confidence']
        thresholds = str_info['thresholds']['1e-5']
        if confidence > 75 and thresholds < confidence:  # 置信度阈值判断
            str_name=str_info['results'][0]['user_id']
            token = str_info['results'][0]['face_token']
            #print(str_name)
            day_str=facedb.daystr(token,str_name,img)
            return str_info,day_str
        else:
            str=facedb.insertfacestr(face_token, img)
            strinfo = face_searchtoken(face_token,strangfacest)
            token = strinfo['results'][0]['face_token'] #重新获取人脸信息
            day_str=facedb.daystr(token,str,img) #将人脸信息加入数据库保存
            return strinfo,day_str

#清空faceset
# def removeall(tag):#传入一个标记，如果标记为0则清空已确认人脸信息，否则清空陌生人人脸信息，执行此函数需要验证管理员密码
#     if tag==0: #清空已确认人脸信息
#         delete_faceset(faceset1,0)
#         conn = pymysql.connect(host=admin.dbhost, user=admin.dbuser, passwd=admin.dbpasswd, db='mysql')
#         cursor = conn.cursor()
#         change = "use face_db"
#         cursor.execute(change)
#         sql="TRUNCATE TABLE face_1"
#         cursor.execute(sql)
#         conn.commit()
#         cursor.close()
#         conn.close()
#     else:
#         delete_faceset(strangfacest, 0)
#         conn = pymysql.connect(host=admin.dbhost, user=admin.dbuser, passwd=admin.dbpasswd, db='mysql')
#         cursor = conn.cursor()
#         change = "use face_db"
#         cursor.execute(change)
#         sql = "TRUNCATE TABLE facestr_1"
#         cursor.execute(sql)
#         conn.commit()
#         cursor.close()
#         conn.close()

#对人脸添加信息
def upadtaface(face_token,face_name,user_id,tag):#需要传入四个数值，第一个为当前人脸的face_token,第二个为需要更改的id，第三个为更改人的id,第四个为分类标记，0为已确认的人脸，其他为陌生人
    if tag==0:#已确认人脸信息更新
        face_SetUserID(face_token,face_name)
        facedb.updateface(face_token,face_name,user_id)
    else:     #陌生人人脸信息更新
        face_SetUserID(face_token,face_name)
        addface(face_token,faceset1)
        removeface(strangfacest, face_token)
        facedb.strtoface(face_token,face_name,user_id)

#上传照片
def uploadphoto(img):#传入一张格式为jpg、png等常用图片格式文件
    face_info=detect_face(img)
    try:
        if face_info['faces']:
            if len(face_info['faces'])!=1:
                return False
            else:
                token=face_info['faces'][0]['face_token']
                return token
    except KeyError:
        return False
