import pyshark
import joblib
from heuristics import Heuristics
from logistic import LogisReg
from mnb import MNB
import warnings
import regex as re
warnings.filterwarnings("ignore")
#cap=pyshark.FileCapture(r'C:\Users\uveer\OneDrive\Documents\Project_capstone\p.cap.txt')
capture=pyshark.LiveCapture(bpf_filter='ip and port 53')
capture.sniff(timeout=10)
arrayofpackets=[]
websites=[]
svm_=[]
for packet in capture.sniff_continuously(packet_count=5):
    print(packet)
    arofpackets=[]
    #print(packet.ip.src)
    #print
    try:
            #arofpackets.append(packet.ip.src)
            #arofpackets.append(packet.length)
        if packet.udp:
            arofpackets.append(int(packet.udp.port))
            arofpackets.append(17)
            tot_fwd=0
            tot_bwd=0
            if packet.udp.port=="53" :
                tot_bwd+=1
            else:
                tot_fwd+=1
            arofpackets.extend([tot_fwd,tot_bwd])
        if packet.ip:
            arofpackets.append(int(packet.length))
        
        '''arofpackets.append(packet.tcp.timestamps)'''
        print(arofpackets)
        arrayofpackets.append(arofpackets)
    except:
        print("attribute isnt available in packet")
    try:
        if packet.dns:
            web=packet.dns.qry_name
            websites.append(web)
            print(web)
    except:
        print("The DNS field isnt available")

arofpackets=[ int(i)  for i in arofpackets]
print(arrayofpackets)
print(websites)
svm_ddos=joblib.load("build/SVM_DDoS")
a=(svm_ddos.predict([[11,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,2000000,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,40,200,1000000,1000000,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,2,0,26883,0]]))
svm_.append(a)
svm_dos=joblib.load("build/SVM_DoS")
b=(svm_dos.predict([[11,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,2000000,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,40,200,1000000,1000000,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,2,0]]))
svm_.append(b)
svm_botnets=joblib.load("build/SVM_Botnets-")
i=(svm_botnets.predict([[11,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,2000000,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,40,200,1000000,1000000,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,2,0,26883]]))
svm_.append(i)
svm_webap=joblib.load("build/SVM_webap")
j=(svm_webap.predict([[11,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,2000000,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,40,200,1000000,1000000,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,2,0,26883]]))
svm_.append(j)
#print(svm_)
svm_ftp=joblib.load("build/SVM_ftp")
k=(svm_ftp.predict(arrayofpackets))
svm_.append(k)
print(svm_)


for i in range(len(websites)):
    web = websites[i].split('.')
    if len(web)<3:
        continue
    del web[0]
    stripWeb = ".".join(web)
    websites[i] = stripWeb

# logistic_web=websites
# for url in logistic_web:
#     web = url.split('.')
#     if len(web)<3:
#         continue
#     del web[-1]
#     stripWeb = ".".join(web)
#     logistic_web[url] = stripWeb
# print(logistic_web)

web=websites
for i in range(len(web)):
    if "https://www." or "https://" in web[i]:
        url = re.compile(r"https?://(www\.)?")
        web[i] = url.sub('', web[i]).strip().strip('/')
#print(web)

for i in range(len(web)):
    webs = web[i].split('.')
    del webs[-1]
    s = ".".join(webs)
    web[i] = s
print(web)

for i in range(len(websites)):
    websites[i]="http://www."+websites[i]
print(websites)

forHtml = []
for i in range(len(websites)):
    forHtml.append(websites[i]+".com/")

heur = Heuristics()
for url in forHtml:
    print('Current URL: ', url)
    print('Tokenized: ', heur.url_tokenize(url))
    print('Exe: ', heur.url_has_exe(url))
    print('Phishing words found: ', heur.phishing_word_count(url))
    try:
        print('HTML source code: ', url, ' ', heur.scan_pg_src(url))
    except:
        print('Error in HTML scan', url)

ob=LogisReg()
#data=ob.process()
pred=ob.testing(web)
print(pred)

obj=MNB()
print(obj.testing(websites))


'''cap'''
'''dir(packet.my_layer)'''

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