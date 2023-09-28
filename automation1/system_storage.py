import shutil
du = shutil.disk_usage("/")
print(du)
mk = du.free/du.total*100
print(mk)