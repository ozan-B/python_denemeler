from scapy.all import*


pckt_list = []

for i in range(1000):


    srcMac = RandMAC()
    dstMac = RandMAC()

    srcIp = "123.123.1.1"
    dstIp = RandIP()



    ether = Ether(src=srcMac , dst=dstMac)
    ip = IP(src=srcIp , dst=dstIp)
    pckt= ether/ip
    pckt_list.append(pckt)

    send(pckt_list, iface="wlan0" , verbose=False )
    
    print(srcMac, ":",srcIp, ">>",dstMac, ":" ,dstIp)