import csv

hosts = [["wokstation.lcal", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]]
with open('host.csv', 'w') as host_csv:
    writer = csv.writer(host_csv)
    writer.writerows(hosts)

    