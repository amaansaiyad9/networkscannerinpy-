====================================================
User Input-Based Nmap Port Scanner - Cybersecurity Mini Project
====================================================

Author   : DEXTER
Language : Python
Tool Used: Nmap (via python-nmap library)
Category : Cybersecurity / Networking

------------------------
📌 Project Description:
------------------------
This is a simple yet powerful command-line tool that allows users to perform network port scanning 
on any target IP address or hostname using Nmap. The scanner accepts dynamic input from the user 
and returns the status of each port along with service information.

------------------------
🔧 Features:
------------------------
✔ User-driven IP/Hostname input
✔ Custom or default port range scanning
✔ Live display of open/closed port status
✔ Identifies running services on each port
✔ Lightweight and easy to use
✔ Written in clean Python code

------------------------
🧰 Technologies Used:
------------------------
- Python 3.x
- Nmap
- python-nmap (Python wrapper for Nmap)

------------------------
📥 Installation:
------------------------
1. Make sure Python is installed:
   >> python --version

2. Install Nmap:
   >> Linux: sudo apt install nmap
   >> macOS: brew install nmap
   >> Windows: Download from https://nmap.org/download.html and add to PATH

3. Install the required Python library:
   >> pip install python-nmap

4. Run the script:
   >> python user_nmap_scanner.py

------------------------
📘 How It Works:
------------------------
1. Script asks for an IP address or domain.
2. You can enter specific ports (e.g., 22,80,443) or press Enter for default (1-1024).
3. Nmap scans the target and prints each port’s status (open/closed) and its associated service.

------------------------
📌 Example Usage:
------------------------
$ python user_nmap_scanner.py

Enter the IP address or hostname to scan: 127.0.0.1
Enter ports to scan (e.g., 22,80,443) or press Enter for default (1-1024): 22,80

[+] Scanning 127.0.0.1 on ports: 22,80 ...

Host: 127.0.0.1 (localhost) - Status: up
    Port 22/tcp - State: open - Service: ssh
    Port 80/tcp - State: closed - Service: http

------------------------
🚀 Future Enhancements:
------------------------
- Add OS and version detection
- Export results to CSV, JSON, or HTML
- Multi-host scanning
- GUI interface using Tkinter or PyQt

------------------------
📄 License:
------------------------
This project is for educational purposes only. Use responsibly.

------------------------
🙋‍♂️ Contact:
------------------------
Feel free to connect or contribute!
Email: your_email@example.com
LinkedIn: https://www.linkedin.com/in/amaan-s-50484a248/
GitHub  : https://github.com/amaansaiyad9
