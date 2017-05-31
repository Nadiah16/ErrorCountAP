import http.client
import json

conn = http.client.HTTPConnection("papi-staging.mistsys.net")

headers = {
    'cache-control': "no-cache",
    'postman-token': "06b66e27-284b-ec7a-aa60-f7c73150c13e"
    }

conn.request("GET", "/internal/devices", headers=headers)


res = conn.getresponse()
data = res.read()
output = json.loads(data)

errorMap = []

for i in output:
    #print( i['site_id'] , i['version'] , i['mac'])
    errorMap.append("%s : %s : %s" % (i['site_id'],i['mac'], i['version']))
    
    
#for rea in output['results']:
 #   errorMap.append("%s : %s " % (rea['site_id']))
                    

with open("/home/nadiah/Desktop/sitedata.txt", "w") as f:
            for line in errorMap: print (line)
            for line in errorMap: f.write(line + '\n')
