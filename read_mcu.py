import serial
import time
import _thread  # 导入线程包
import cv2
import numpy as np
data_ser = serial.Serial("COM15",115200,timeout = 50)
data_ser.flushInput()
data_file =r'./save/data.csv'


img = np.zeros((320, 320, 3), np.uint8) #生成一个空灰度图像

font=cv2.FONT_HERSHEY_TRIPLEX
save_count=0


def time_stamp():
  return time.strftime("%Y%m%d_%H%M%S", time.localtime())

def decode_data(data_str):
  global save_count
  global img
  decode_res=data_str.split(',')
  res_len=len(decode_res)
  print('len=',res_len)
  if res_len==17:
    decode_res.pop()
    
    # count=0
    # for res in decode_res:
    #   print(count,res)
    #   count+=1
  
    if save_count==0:
      
      print('new test')
      save_data(data_file,'\r\n'+time_stamp()+'\n')
    save_data(data_file,str(save_count)+','+data_str+time_stamp()+'\n')
    
    
    cv2.putText(img,'done...',(0,50), font, 2,(0,255,0),1)
    cv2.putText(img,str(save_count),(20,200), font, 2,(0,255,0),1)
    cv2.imshow('main',img)
    img = np.zeros((320, 320, 3), np.uint8)
    save_count+=1
  return decode_res
  


def send_cmd():
  data_ser.write('m_float()\r\n'.encode("utf-8"))
  print('cmd send..')
# def data_check(data):
  
def save_data(filename,data_to_write):
  with open(filename,"a") as f:
    f.write(data_to_write)


data_now=0
def get_data():
  while True:
    data_count = data_ser.inWaiting()
    if data_count !=0 :
      recv = data_ser.readline(data_ser.in_waiting).decode("utf-8")
      #print(time.time()," data_recv --> ", recv)
      recv=recv.strip()
      print("rec:",recv)
      decode_data(recv)
      
    time.sleep(0.5)
 


if __name__ == '__main__':
  
  _thread.start_new_thread(get_data,()) # 开启线程，执行get_data方法
  cv2.namedWindow('main',cv2.WINDOW_NORMAL)
  cv2.imshow('main',img)
 
  while 1:
    k=cv2.waitKey(1)&0xFF
    if k!=255:
      print('key press: ',chr(k))
    if k==27:
      print('exit..')
      break
    if k==32:
      cv2.putText(img,'Run...',(0,50), font, 2,(0,255,255),1)
      cv2.imshow('main',img)
      img = np.zeros((320, 320, 3), np.uint8)
      send_cmd()
      



cv2.destroyAllWindows()