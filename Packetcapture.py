import pyshark
import joblib
from logistic import LogisReg
#cap=pyshark.FileCapture(r'C:\Users\uveer\OneDrive\Documents\Project_capstone\p.cap.txt')
capture=pyshark.LiveCapture(bpf_filter='ip and port 53')
capture.sniff(timeout=10)
arrayofpackets=[]
websites=[]
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


svm_ddos=joblib.load("SVM_DDoS")
print(svm_ddos.predict([[11,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,2000000,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,40,200,1000000,1000000,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,2,0,26883,0]]))

ob=LogisReg()
data=ob.process()
pred=ob.testing(websites)
print(pred)
'''cap'''
print(arrayofpackets)
print(websites)
dir(packet.my_layer)

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


