import cv2
import paddlehub as hub
import os
import re
import numpy as np
from PIL import Image

class Detect(object):
    def __init__(self):
        self.ocr=hub.Module(name="chinese_ocr_db_crnn_mobile")
        self.module = hub.Module(name="lac")

    def cv_imread(self,file_path):
        cv_img=cv2.imdecode(np.fromfile(file_path,dtype=np.uint8),-1)
        return cv_img
    def getTel(self,st):
        res=[]
        s=''
        regular = re.compile(r'\d{4}-\d{7}|\d{3}-\d{8}')
        tmp=re.findall(regular, st)
        #print(tmp)
        regular=re.compile(r"1[35678]\d{9}")
        #print(st)
        tmp2=re.findall(regular,st)
        #print(tmp2)
        
        for i in tmp:
            
            s=s+i+'\n'
        for i in tmp2:

            s=s+i+'\n'
        return s

    def getBrand(self,items):

        for it in items:
            ar = []
            it = it.get('text', '')
            ar.append(it)
            inputs={"text":ar}
            results = self.module.lexical_analysis(data=inputs)
            for result in results:
                for i in result['tag']:
                    if i=='ORG':
                        #print(it)
                        b = it
                        p = re.compile(r'[\u4e00-\u9fa5]')
                        res = re.findall(p, b)
                        result = ''.join(res)
                        if result != '':
                            return result
                        else:
                            return b
                        #return it

        maxx=0
        maxh=0
        brand={}
        for it in items:
            a=it['text_box_position']
            w,h=abs(int(a[1][0])-int(a[0][0])),abs(int(a[1][1])-int(a[2][1]))
            if(maxx<w*h):
                maxx=w*h
                brand=it
        
        for it in items:
            a=it['text_box_position']
            w,h=abs(int(a[1][0])-int(a[0][0])),abs(int(a[1][1])-int(a[2][1]))
            if(w>h and  h>maxh):
                maxh=h
                brand=it
        
        b=brand.get('text','')
        p = re.compile(r'[\u4e00-\u9fa5]')
        res = re.findall(p, b)
        result = ''.join(res)
        if result!='':
            return result
        else:
            return b
            
        #print(brand.get('text',0))

    def detectDir(self,dir,config,signalInfo,progressInfo):
        test_img_path=[]
        cnt=0
        for filename in os.listdir(dir):
            filename=os.path.join(dir,filename)
            #print(filename)
            if re.match(r"^.*.jpg",filename)!=None or re.match(r"^.*.png",filename)!=None:
                cnt+=1   
                test_img_path.append(filename)
        # for i in test_img_path:
        #     print(i)
        # 读取测试文件夹test.txt中的照片路径
        cnt1=0
        if test_img_path==[]:

            return
        for im in test_img_path:
            dic=self.detectFile(im,config)
            signalInfo.sinInfo.emit(dic)
            cnt1+=1
            progressInfo.proInfo.emit(int((cnt1/cnt)*100))

    
    def detectFile(self,filename,config,signalInfo=None,progressInfo=None):
        test_img_path=[]
        test_img_path.append(filename)
        dic={}
        dic['origin_path']=filename
        np_images =[self.cv_imread(image_path) for image_path in test_img_path] 
        if np_images[0] is None:
            return

        results = self.ocr.recognize_text(
                            images=np_images,         # 图片数据，ndarray.shape 为 [H, W, C]，BGR格式；
                            use_gpu=config.useGPU,            # 是否使用 GPU；若使用GPU，请先设置CUDA_VISIBLE_DEVICES环境变量
                            output_dir='result',  # 图片的保存路径，默认设为 ocr_result；
                            visualization=True,       # 是否将识别结果保存为图片文件；
                            box_thresh=0.5,           # 检测文本框置信度的阈值；
                            text_thresh=0.5)          # 识别中文文本置信度的阈值；
        for result in results:
            dic['brand']=self.getBrand(result['data'])
            
        for result in results:
            data = result['data']
            save_path = result['save_path']
            dic['save_path']=save_path
            dic['more']=''
            #print(save_path)
            for infomation in data:
                if(infomation['text']==dic['brand']):
                    pass
                elif self.getTel(infomation['text'])!='':
                    dic['tel']=self.getTel(infomation['text'])
                else:
                    dic['more']=dic['more']+infomation['text']+'\n'
            # for infomation in data:
            #     print('text: ', infomation['text'], '\nconfidence: ', infomation['confidence'], '\ntext_box_position: ', infomation['text_box_position'])
        if signalInfo is None:
            pass
        else:
            signalInfo.sinInfo.emit(dic)
        if progressInfo is None:
            pass
        else:
            progressInfo.proInfo.emit(100)
        return dic
