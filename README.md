# Network Scanner Tool

## Overview
This Python script is a network scanning tool that discovers available devices on a local network and scans for open ports on those devices. It uses libraries like Scapy for ARP-based network discovery, socket for port scanning, and netifaces for network interface information. The script is structured as a class (`myscan`) to organize the scanning logic, making it modular and reusable for network auditing or security testing purposes.

## Key Features and Functionality
- **Network Discovery**: Automatically detects the local network IP range using the default gateway and interface information.
- **IP Scanning**: Uses ARP (Address Resolution Protocol) to find active devices on the network by sending broadcast packets and collecting responses.
- **Port Scanning**: Scans a predefined list of common ports (e.g., 22, 80, 443) on discovered IPs to identify open ports.
- **Output Formatting**: Displays available IPs and their open ports in a colored, readable format using ANSI color codes.
- **Modular Design**: The `myscan` class encapsulates methods for network and port scanning, allowing for easy extension or integration.

## Technologies and Dependencies
- **Python Libraries**:
  - `socket`: For creating network sockets and performing port scans.
  - `psutil`: For system and process utilities (though not heavily used in this script).
  - `ipaddress`: For handling IP addresses and network calculations.
  - `netifaces`: For retrieving network interface information.
  - `scapy`: For packet crafting and network scanning (requires `pip install scapy`).
- **Execution Environment**: Designed to run in a Python environment (e.g., Python 3.x). Requires administrative privileges for ARP scanning on some systems.
- **Note**: Scapy may require additional setup (e.g., running as root on Linux) for full functionality.

## Purpose and Use Cases
- **Primary Purpose**: To perform basic network reconnaissance, identifying active devices and open ports for security auditing, troubleshooting, or educational purposes.
- **Potential Applications**:
  - **Network Administration**: Quickly map devices on a local network and check for open services.
  - **Security Testing**: Identify potentially vulnerable open ports on devices.
  - **Educational**: Demonstrates networking concepts like ARP, port scanning, and socket programming, suitable for Computer Networks (CN) lab exercises.
  - **Integration**: Can be extended into larger tools for automated network monitoring or integrated with other scripts.
- **Relation to Your CN Lab Environment**: This script aligns with your Java-based networking projects (e.g., ArpClient.java, ArpServer.java) by focusing on network discovery and communication, providing a Python alternative for similar tasks.

## Strengths
- **Efficiency**: Fast scanning using ARP for IP discovery and socket connections for ports.
- **Customization**: Easy to modify the list of ports or add more scanning methods.
- **User-Friendly Output**: Colored output for better readability.

## Limitations and Potential Improvements
- **Permissions**: Requires admin/root privileges for ARP scanning on some operating systems.
- **Accuracy**: Port scanning is basic and may miss some services; consider using more advanced tools like Nmap for production use.
- **Error Handling**: Limited error handling; could be improved with try-except blocks for network failures.
- **Ethical Considerations**: Use only on networks you own or have permission to scan. Unauthorized scanning may violate laws or policies.
- **Performance**: For large networks, scanning may take time; consider asynchronous methods.
- **Dependencies**: Ensure all libraries are installed, and Scapy is configured properly.

## Installation
1. Ensure Python is installed (version 3.x recommended).
2. Install the required dependencies:
   ```
   pip install scapy psutil ipaddress netifaces
   ```
3. Note: On some systems, you may need to install Scapy with additional options: `pip install scapy[complete]`.

## Usage
1. Save the script to a file, e.g., `network_scanner.py`.
2. Run the script with administrative privileges if necessary:
   ```
   sudo python network_scanner.py  # On Linux/Mac
   python network_scanner.py       # On Windows (run as admin)
   ```
3. Expected output: A list of available IPs and their open ports, displayed in colored text.
