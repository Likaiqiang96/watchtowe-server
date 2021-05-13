import time
localtime = time.localtime(time.time())
# time_str=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
time_str=time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()) 
print(time_str)