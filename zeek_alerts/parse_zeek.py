
import pandas as pd

def parse_zeek_connlog(file_path):
    try:
        df = pd.read_csv(file_path, sep='\t', comment='#', low_memory=False)
        if {'ts', 'uid', 'id.orig_h', 'id.resp_h', 'proto', 'conn_state'}.issubset(df.columns):
            parsed = df[['ts', 'uid', 'id.orig_h', 'id.resp_h', 'proto', 'conn_state']]
            print(parsed.head())
            return parsed
        else:
            print("❌ Required columns not found in Zeek log.")
            return None
    except Exception as e:
        print(f"🚫 Error parsing Zeek log: {e}")
        return None
