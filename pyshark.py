import pyshark
#cap=pyshark.FileCapture(r'C:\Users\uveer\OneDrive\Documents\Project_capstone\p.cap.txt')
capture=pyshark.LiveCapture()
capture.sniff(timeout=10)
arrayofpackets=[]
for packet in capture.sniff_continuously(packet_count=5):
    print(packet)
    arofpackets=[]
    #print(packet.ip.src)
    #print
    if packet.ip:
        arofpackets.append(packet.ip.src)
    arofpackets.append(packet.length)
    print(arofpackets)
    arrayofpackets.append(arofpackets)
'''cap'''

print(arrayofpackets)
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


