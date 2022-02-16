import urllib.request
import pandas as pd


url = "https://s3.amazonaws.com/tcmg476/http_access_log"
file = urllib.request.urlopen(url)
for line in file:
    decoded_line = line.decode("utf-8")
#print(decoded_line)
count = 0
for i in decoded_line:
    count += count

print("Total number of logs: ", count)


