from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def process_packet(packet):
    # Check if the packet has an IP layer
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        source_ip = ip_layer.src
        destination_ip = ip_layer.dst
        protocol = ip_layer.proto

        # Determine the protocol
        protocol_name = 'TCP' if packet.haslayer(TCP) else 'UDP' if packet.haslayer(UDP) else 'Other'

        # Print packet information
        print(f"Source IP: {source_ip}")
        print(f"Destination IP: {destination_ip}")
        print(f"Protocol: {protocol_name}")

        # Display payload if TCP or UDP layer is present
        if protocol_name == 'TCP' or protocol_name == 'UDP':
            payload = bytes(packet[protocol_name].payload)
            print(f"Payload: {payload[:30]}...")  # Display the first 30 bytes of the payload
        print('-' * 40)

def main():
    print("Starting packet sniffer...")
    sniff(prn=process_packet, filter="ip", store=0)

if __name__ == "__main__":
    main()
