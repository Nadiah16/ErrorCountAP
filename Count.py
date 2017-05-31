import http.client
import json
import sys


conn = http.client.HTTPConnection("marvis-staging.mistsys.net")
headers = {

    'cache-control': "no-cache",

    'postman-token': "d97b415e-04ae-c8b0-12b4-c55ce883628e"

    }

inputDate = sys.argv[1]

url = "/marvis/api/v1/internal/dateinput/aps_with_errors?"
url = url.replace("dateinput", inputDate)

FILE_NAME = '/home/nadiah/Desktop/' + inputDate + '-' + 'result.txt'
NEW_FILE_NAME = inputDate + '-' + 'output.txt'

#conn.request("GET", "/marvis/api/v1/internal/2017-05-22/aps_with_errors?&limit=5000", headers=headers)

conn.request("GET", url)

res = conn.getresponse()
data = res.read()
#binary = data.content
output = json.loads(data)

errorMap = []

for rea in output['results']:
 errorMap.append("%s : %s " % (rea['FwVersion'],rea['reason_code']))

        #errorMap.append("%s : %s " % (rea['FwVersion'],rea['reason_text']))

with open(FILE_NAME, "w") as f:

            #for line in errorMap: print (line)
            for line in errorMap: f.write(line + '\n')

with open(FILE_NAME) as infile, open(NEW_FILE_NAME, 'w') as outfile:

    for line in infile:
     if not line.strip(): continue  # skip the empty line
     outfile.write(line)  # non-empty line. Write it to output 

list = []

for y in open(NEW_FILE_NAME).readlines():
  out = []
    for x in y.split(':'):
        if x not in [':','\n']:
         out.append(x)
         #print('{}'.format(x))
    out2 = []
    for x in out[1].split(' '):
        if x not in [' ','\n']:
         out2.append(x)
         #print('{}'.format(x))
         
    list.append(out[0] + ': ' + out2[1])

my_dict = {i:list.count(i) for i in list}
#print('{}'.format(my_dict))
print (json.dumps(my_dict , indent = 1))
