import pyshark
import joblib
from logistic import LogisReg
from mnb import MNB
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
        if packet.ip:
            arofpackets.append(packet.ip.src)
            arofpackets.append(packet.length)
        if packet.udp:
            arofpackets.append(packet.udp.port)
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
print(svm_)
'''for i in range(len(websites)):
    websites[i]="http://"+websites[i]'''
for i in range(len(websites)):
    web = websites[i].split('.')
    if len(web)<3:
        continue
    del web[0]
    stripWeb = ".".join(web)
    websites[i] = stripWeb
    '''websites[i]=websites[0:len(websites[i])-3]'''
for i in range(len(websites)):
    websites[i]="http://www."+websites[i]
print(websites)
ob=LogisReg()
data=ob.process()
pred=ob.testing(websites)
print(pred)
obj=MNB()
print(obj.testing(websites))
print(pred)
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


