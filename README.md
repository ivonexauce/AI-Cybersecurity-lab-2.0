# AI-Cybersecurity-Lab 2.0
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 🚀 Contact

**Ivon Exauce Umba**  
PhD Scholar in AI & Blockchain Security  
📫 [umbayanga6bio@gmail.com](mailto:umbayanga6bio@gmail.com)  
🌐 www.umbaconsulting.com

---

AI-Cybersecurity-lab 2.0 is an advanced, modular cybersecurity laboratory designed to integrate Artificial Intelligence (AI) with real-time network monitoring and smart contract auditing. The goal is to simulate, analyze, and secure enterprise environments using open-source tools like **Suricata**, **Zeek**, and AI/ML-based alert scoring systems.

This lab is ideal for:  
- Security researchers  
- SOC analysts  
- Red/Blue teams  
- AI/Cybersecurity students and developers  
- Enterprises testing scalable defensive systems

---

## 🚀 How to Run

With Docker Compose (recommended):

```bash
git clone https://github.com/ivonexauce/AI-Cybersecurity-lab-2.0.git
cd AI-Cybersecurity-lab-2.0
docker-compose up --build
```
---
🧠 AI Model Details
ML Algorithms: Logistic Regression, Random Forest, XGBoost

Trained on: Suricata/Zeek logs (labelled)

Output: Alert priority (High, Medium, Low)
---
🧪 Smart Contract Tools
Mythril – for symbolic analysis

Slither – for static code analysis

Supports: .sol (Solidity) contract scanning
---
🧰 Dependencies
Python 3.10+

Docker & Docker Compose

Suricata / Zeek (via container or system)

Node.js (optional, for smart contract demos)
---
| Feature                         | Description                                                                              |
| ------------------------------- | ---------------------------------------------------------------------------------------- |
| 🧠 **AI Alert Scoring**         | Machine learning models prioritize alerts from Suricata/Zeek to reduce analyst fatigue.  |
| 📡 **Suricata IDS Integration** | Real-time packet capture and signature-based intrusion detection.                        |
| 🔬 **Zeek IDS Integration**     | Behavioral network analysis and protocol detection.                                      |
| 🔐 **Smart Contract Auditing**  | Detect vulnerabilities in Ethereum smart contracts (with tools like Mythril or Slither). |
| 📊 **Data Visualization**       | Dashboards using Plotly, Matplotlib or Streamlit for alert insights.                     |
| 🐳 **Docker Support**           | Easily deploy the entire lab with Docker or Docker Compose.                              |

---
```
AI-Cybersecurity-lab-2.0/
├── ai_alert_scoring/        # AI/ML models for alert prioritization
├── suricata_alerts/         # Suricata rules, logs, configuration
├── zeek_alerts/             # Zeek scripts, logs, analysis tools
├── smart_contract_audit/    # Tools & scripts for auditing Ethereum contracts
├── visualization/           # Dashboards and plots
├── docker-compose.yml       # One-command deploy for full stack
├── Dockerfile               # For app containerization
├── LICENSE                  # MIT License
└── README.md                # Project documentation
```

---
📜 License
MIT License — free to use, distribute, and modify.

🙌 Contributors & Community
Author: UMBA YANGA IVON EXAUCE
