from scapy.all import sniff, IP, TCP, UDP, Raw

def packet_callback(packet):
    # Check if the packet has an IP layer
    if packet.haslayer(IP):
        ip_layer = packet.getlayer(IP)
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        
        # Check the protocol and extract relevant information
        protocol = ip_layer.proto
        if protocol == 6:  # TCP
            protocol_name = "TCP"
            payload = packet[Raw].load if packet.haslayer(Raw) else "No Payload"
        elif protocol == 17:  # UDP
            protocol_name = "UDP"
            payload = packet[Raw].load if packet.haslayer(Raw) else "No Payload"
        else:
            protocol_name = "Other"
            payload = "No Payload"

        # Print packet details
        print(f"Source IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")
        print(f"Protocol: {protocol_name}")
        print(f"Payload: {payload}")
        print("="*50)

def main():
    print("Starting packet sniffer...")
    sniff(prn=packet_callback, store=0, filter="ip")

if __name__ == "__main__":
    main()
