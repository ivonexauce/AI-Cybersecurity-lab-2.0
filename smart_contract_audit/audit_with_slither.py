# Slither audit script
import subprocess

def run_slither_analysis(sol_file_path):
    try:
        result = subprocess.run(["slither", sol_file_path, "--json", "slither-output.json"], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Slither analysis complete. Results saved to slither-output.json")
            return result.stdout
        else:
            print("❌ Slither error:", result.stderr)
            return None
    except Exception as e:
        print(f"🚫 Failed to run Slither: {e}")
        return None
