import pyshark
import requests
import pickle
import os
from heuristics import Heuristics

#cap=pyshark.FileCapture(r'C:\Users\uveer\OneDrive\Documents\Project_capstone\p.cap.txt')
capture=pyshark.LiveCapture(bpf_filter='ip and port 53')
capture.sniff(timeout=10)
arrayofpackets=[]
websites=[]
for packet in capture.sniff_continuously(packet_count=4):
    print(packet)
    arofpackets=[]
    #print(packet.ip.src)
    #print
    try:
        if packet.ip:
            arofpackets.append(packet.ip.src)
            arofpackets.append(packet.length)
        if packet.tcp:
            arofpackets.append(packet.tcp.port)
            '''arofpackets.append(packet.tcp.timestamps)'''
        print(arofpackets)
        arrayofpackets.append(arofpackets)
    except:
        print("attribute isnt available in packet")
    try:
        if packet.dns:
            web=packet.dns.qry_name
            w=web
            websites.append(w)
            print(w)
            
    except:
        print("The DNS field isnt available")



'''cap'''
l=arrayofpackets
print(l)
_=os.system('cls')
print(websites)

for website in websites:
    r=requests.head('https://'+website)
    if r.status_code==200:
        w=website
        break
#dir(packet.my_layer)

import LogisticRegression
# import SupportVectorMachine


# net=pickle.load(open("build/svm_model.pkl","rb"))
# print(net.predict([[11,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,2000000,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,40,200,1000000,1000000,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,2,0,26883,0,0,80,0,0,0,0,0,0,0,0]]))

#w = w.encode('ascii', 'ignore').decode('unicode_escape')

obj=Heuristics()
#w='http://food.hubcom.com/recipe/cgi-win/recipe.exe/1'
print(obj.phishing_word_count(w))
print(obj.url_has_exe(w))
print(obj.url_tokenize(w))
q="https://"+w
print(obj.scan_pg_src(q))
logi=pickle.load(open("build/model.pkl","rb"))
w=vectorizer.transform(w)
print(logi.predict(w))















def isddos(pkt):
  if(pkt.tcp):
        '''TCP SYN FLOOD'''
        serverport={}
        src=pkt[2]
        port=pkt[3]
        '''for i in range(len(pkt)):'''
        if src in serverport:
            serverport[src]=1+serverport.get(src,0)

  if(pkt.udp):
      '''UDP FLOOD '''
      setport=set()
      setsrc=set()
      src=pkt[2]
      port=pkt[3]
      setport.add(port)
      setsrc.add(src)
      if len(setport)==len(setsrc):
          print("Traffic is from normal source")
      else:
          print("UDP Flood")


