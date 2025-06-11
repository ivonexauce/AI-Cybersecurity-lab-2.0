# Parse Suricata EVE JSON logs
import json

def parse_suricata_alerts(file_path):
    try:
        with open(file_path, 'r') as f:
            alerts = []
            for line in f:
                data = json.loads(line)
                if "alert" in data:
                    alert_info = {
                        "timestamp": data.get("timestamp"),
                        "alert_signature": data["alert"].get("signature"),
                        "src_ip": data.get("src_ip"),
                        "dest_ip": data.get("dest_ip"),
                        "protocol": data.get("proto")
                    }
                    alerts.append(alert_info)
        return alerts
    except Exception as e:
        print(f"Error parsing file: {e}")
        return []
