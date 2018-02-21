import urllib2
import json
import datetime

cur_date=datetime.datetime.now()
my_numbers = []
maxlistas = []
hmerominia = []
megisto = 0
def compare_lists(l1,l2):
  s=0
  for i in l1:
    if i in l2:
      s+=1
  return s
my_numbers = input("Give 10 numbers between 1 and 80")
for i in range (30):
    cur_date= cur_date - datetime.timedelta(days=1)
    date_str= cur_date.strftime("%d-%m-%Y")
    url='http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json'%date_str
    req= urllib2.Request(url)
    response = urllib2.urlopen(req)
    data = response.read()
    data = json.loads(data)
    klhrwseis= data['draws']['draw']
    r=[]
    for k in klhrwseis:
        tmp=k["results"]
        r.append (compare_lists(my_numbers,tmp))
    hmerominia.append(date_str)
    if max(r) > 4 :
        maxlistas.append(max(r))
megisto = max(maxlistas)
for i in range (len(maxlistas)):
    if megisto == maxlistas[i]:
        print "H mera/meres poy petyxes tous perissoterous arithmous einai: ",hmerominia[i]
print "O megistos aithmos syndiasmwn pou petyxes einai: ", megisto
