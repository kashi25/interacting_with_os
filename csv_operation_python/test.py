import csv

content = [["Kashi Bhattarai", "jhapa"], ["Ashok Bhattarai", "Kathmandu"]]
with open('testing.csv', 'w') as test_csv:
    writer = csv.writer(test_csv)
    writer.writerows(content)