# import psutil
# a= psutil.cpu_percent(0.1)
# b= psutil.cpu_percent(0.1)
# print(a)
# print(b)
# d= psutil.cpu_percent(0.5)
# print(d)
# # the output
# # 0.0
# 7.1
# 14.1

import shutil
import psutil

def check_disk_usges(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75

if not check_disk_usges("/") or not check_cpu_usage():
    print( "Error")
else:
    print("every things is ok")
    

        
        