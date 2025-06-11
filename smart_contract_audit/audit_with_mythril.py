# Mythril audit script
import subprocess

def run_mythril_analysis(sol_file_path):
    try:
        result = subprocess.run(["myth", "analyze", sol_file_path, "-o", "json"], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Mythril analysis successful.")
            return result.stdout
        else:
            print("❌ Mythril error:", result.stderr)
            return None
    except Exception as e:
        print(f"🚫 Failed to run Mythril: {e}")
        return None
