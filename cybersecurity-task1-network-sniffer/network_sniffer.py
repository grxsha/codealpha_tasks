import socket
import struct

def main():
    #Create a raw socket
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

    #Bind the socket to the local host
    host = socket.gethostbyname(socket.gethostname())
    sniffer.bind((host, 0))

    #Include IP headers
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    #Enable promiscuous mode (Windows only)
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    print("Packet Sniffer Started...\nPress Ctrl+C to stop.\n")

    try:
        while True:
            raw_data, addr = sniffer.recvfrom(65535)

            #Extract IP header (first 20 bytes)
            ip_header = raw_data[:20]
            iph = struct.unpack('!BBHHHBBH4s4s', ip_header)

            version_ihl = iph[0]
            version = version_ihl >> 4
            ihl = version_ihl & 0xF

            ttl = iph[5]
            protocol = iph[6]

            source_ip = socket.inet_ntoa(iph[8])
            destination_ip = socket.inet_ntoa(iph[9])

            print("=" * 50)
            print(f"Version        : IPv{version}")
            print(f"Source IP      : {source_ip}")
            print(f"Destination IP : {destination_ip}")
            print(f"Protocol       : {protocol}")
            print(f"TTL            : {ttl}")

            #Display first 50 bytes of payload
            payload = raw_data[ihl * 4:]
            print("Payload:")
            print(payload[:50])

    except KeyboardInterrupt:
        print("\nStopping Packet Sniffer...")

        #Disable promiscuous mode (Windows)
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
        sniffer.close()

if __name__ == "__main__":
    main()
