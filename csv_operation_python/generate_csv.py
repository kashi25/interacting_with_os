import csv

hosts = [["wokstation.lcal", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]]
with open('host.csv', 'w') as host_csv:
    varm = csv.writer(host_csv)
    varm.writerow(hosts)
    varm.writerows(hosts)
    

    