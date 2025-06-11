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
AI-Cybersecurity-lab-2.0/ — AI-Powered Network and Smart Contract Threat Detection Lab
├── ai_alert_scoring/              # AI/ML-based alert scoring
│   ├── ai_model.py                # Trained ML model for threat prioritization
│   └── feature_extractor.py       # Extracts features from parsed alerts
│
├── suricata_alerts/               # Suricata log parsing
│   ├── parse_suricata.py          # Parses Suricata JSON logs
│   └── sample_suricata.json       # Sample Suricata alert file
│
├── zeek_alerts/                   # Zeek log analysis
│   ├── parse_zeek.py              # Parses Zeek conn.log data
│   └── sample_conn.log            # Sample Zeek connection log
│
├── smart_contract_audit/          # Smart contract security tools
│   ├── audit_with_mythril.py      # Audit script using Mythril
│   ├── audit_with_slither.py      # Audit script using Slither
│   └── vulnerable_contract.sol    # Sample vulnerable Solidity contract
│
├── visualization/                 # Visualization & dashboard
│   ├── dashboard.py               # Python dashboard using matplotlib/seaborn
│   └── alert_data.csv             # Sample data for visualizing alerts
│
├── Dockerfile                     # Builds the lab environment container
├── docker-compose.yml             # Launches all services with one command
├── requirements.txt               # Python package dependencies
├── LICENSE                        # MIT License
└── README.md                      # Project overview, setup guide, and usage

```

---
📜 License
MIT License — free to use, distribute, and modify.

🙌 Contributors & Community
Author: UMBA YANGA IVON EXAUCE
