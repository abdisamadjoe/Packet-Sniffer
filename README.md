# Packet Sniffer

A simple network packet sniffer tool written in Python using the `scapy` library. This tool captures and analyzes network packets, displaying relevant information such as source and destination IP addresses, protocols, and payload data. It is intended for educational purposes only.

## Features

- Captures network packets.
- Displays source and destination IP addresses.
- Identifies TCP and UDP protocols.
- Shows payload data if available.



## Requirements

- Python 3.x
- `scapy` library

### Overview

The Packet Sniffer tool captures and analyzes network packets using the `scapy` library. It provides real-time data on network traffic, including source and destination IP addresses, protocols, and payloads.

### Architecture

1. **Packet Capture:**
   - **Description:** The tool uses `scapy` to capture packets from the network interface.
   - **Details:** Packets are intercepted and stored for analysis.

2. **Packet Analysis:**
   - **Description:** Captured packets are analyzed to extract relevant information.
   - **Details:** Information such as source and destination IP addresses, protocol type (TCP/UDP), and payload data are extracted.

3. **Output Display:**
   - **Description:** Analyzed data is formatted and displayed in the terminal.
   - **Details:** Results are shown with details about each packet, making it easy to monitor network traffic.

### Key Components

- **Packet Capture Module:**
  - **Function:** Handles the capturing of network packets.
  - **Implementation:** Uses `scapy`’s `sniff` function to gather packets from the network.

- **Packet Analysis Module:**
  - **Function:** Processes captured packets to extract and interpret data.
  - **Implementation:** Analyzes packet headers to determine source and destination IPs, protocols, and payloads.

- **Display Module:**
  - **Function:** Formats and outputs the analyzed data.
  - **Implementation:** Prints packet details to the terminal in a readable format.

### Workflow

1. **Start the Sniffer:**
   - **Action:** Run the `packet_sniffer.py` script with elevated permissions.
   - **Command:** `sudo python packet_sniffer.py`

2. **Capture Packets:**
   - **Process:** The tool begins capturing packets from the specified network interface.

3. **Analyze Packets:**
   - **Process:** The tool processes each captured packet to extract relevant information.

4. **Display Results:**
   - **Output:** Packet details are displayed in the terminal.
  
   ## Languages and Utilities Used

- **Python**

## Environments Used 

- **Windows 11**
- **Visual Studio Code**

## Project Walkthrough:

<p align="center">
Code Overview: <br/>

<img src="https://github.com/user-attachments/assets/2e512c02-e92a-4244-8046-416d2204eaed" height="80%" width="80%" alt="Keylogger Code Overview"/>
<br />
<br />
Code in Action: <br/>
Source IP: 192.168.1.1
Destination IP: 192.168.1.2
Protocol: TCP
Payload: b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n'
==================================================
