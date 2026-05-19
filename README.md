# PortSonar 📡

PortSonar is a high-performance, lightweight command-line interface (CLI) network service and reconnaissance tool written in Python. By leveraging low-level TCP socket handshakes, it sweeps targeted hosts to identify open communication ports and map active running services—all without needing external dependencies or root execution privileges.

---

## ⚙️ How It Works (TCP Connect Scan)
PortSonar utilizes the standard standard **TCP 3-Way Handshake** model via the `connect_ex()` socket method:
* **`SYN` ➡️ `SYN-ACK`**: When a port is listening, the socket connection resolves successfully (`return code 0`), marking the state as **OPEN**.
* **`SYN` ➡️ `RST`**: If the port is closed or filtered by a firewall, the handshake fails or times out, safely closing the socket without hanging the execution string.

---

## 🛠️ Key Features
* **Zero Dependencies:** Built entirely using native Python libraries (`socket`, `sys`, `datetime`).
* **Intelligent Resolution:** Automatically resolves web domains (e.g., `example.com`) to their corresponding IPv4 addresses.
* **Service Mapping:** Queries the system database to display standard service protocols (SSH, HTTP, DNS, etc.) running on detected open sockets.
* **Optimized Performance:** Configured with a tight socket timeout window to ensure rapid scanning sequences.

---

## 🚀 Installation & Usage

### 1. Clone the Asset
```bash
git clone [https://github.com/Mcnail23/portsonar.git](https://github.com/Mcnail23/portsonar.git)
cd portsonar
