# -port-Scanner-
"A port scanner written in python by me 4N008 with love"
"You can share you improvements with me, i'd very much appreciate"
Explanation for the provided Python script ```portscanner?.py```:

---

# Port Scanner Script

This Python script allows you to scan open and closed ports on a target host. It uses the `socket` library to establish connections and check port availability.

## Usage

1. **Requirements:**
   - Python 3.x
   - The `socket` library is included in Python's standard library.

2. **Running the Script:**
   - Save the script to a file (e.g., `portscanner?.py`).
   - Open your terminal or command prompt.
   - Navigate to the directory where the script is located.

3. **Execute the Script:**
   ```
   python portscanner?.py
   ```

4. **Script Explanation:**

   - The script defines two functions:
     - `conScan(tgtHost, tgtPort)`: Connects to the specified target host and port. If successful, it prints that the port is open; otherwise, it indicates that the port is closed.
     - `portScan(tgtHost, tgtPorts)`: Resolves the target host's IP address, scans the specified ports, and calls `conScan` for each port.

   - The main part of the script:
     - Resolves the IP address of the target host.
     - Prints the scan result (either the target name or IP address).
     - Sets a timeout for socket connections (1 second).
     - Iterates through the specified ports and performs the port scan.

5. **Example Usage:**
   ```
   python portscanner?.py
   ```

   Output:
   ```
   [+]80/tcp Open
   [+]22/tcp Open
   ```

6. **Note:**
   - Adjust the target host (`tgtHost`) and port list (`tgtPorts`) according to your requirements.

---

Feel free to customize and use this script for your network scanning needs! 🚀 

---
**Disclaimer:** Always ensure that you have proper authorization before scanning any network or system. Unauthorized port scanning can be considered malicious activity.