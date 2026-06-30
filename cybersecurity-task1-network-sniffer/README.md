# Basic Network Sniffer

## Objective

Develop a basic network sniffer in Python using the `socket` library to capture and analyze network packets. The program extracts useful information such as source IP, destination IP, protocol, and payload to understand how data flows through a network.

---

## Features

- Captures live network packets
- Displays source and destination IP addresses
- Displays IP version
- Displays protocol number
- Displays TTL (Time To Live)
- Displays packet payload
- Uses Python's built-in `socket` library
- No external libraries required

---

## Technologies Used

- Python 3.x
- socket
- struct

---

## Requirements

- Python 3.x
- Administrator privileges (Windows)
- Root privileges (Linux)

---

## How to Run

### Windows

Open Command Prompt as Administrator.

```bash
python network_sniffer.py
```

### Linux

```bash
sudo python3 network_sniffer.py
```

---

## Algorithm

1. Import the required modules.
2. Create a raw socket.
3. Bind it to the local IP address.
4. Enable IP header inclusion.
5. Receive packets continuously.
6. Extract the IP header.
7. Display:
   - Source IP
   - Destination IP
   - Protocol
   - TTL
   - Payload
8. Stop the program using **Ctrl + C**.

---

## Learning Outcomes

- Understand packet sniffing.
- Learn how raw sockets work.
- Analyze IP packet headers.
- Observe network traffic in real time.

---


## Author

**Grisha P**
