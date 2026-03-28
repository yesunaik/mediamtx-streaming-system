# stream_controller.py

import subprocess
import time

CONFIG_FILE = "mediamtx_config.yml"

def start_mediamtx():
    try:
        print("🚀 Starting MediaMTX server...")
        process = subprocess.Popen(
            ["./mediamtx", CONFIG_FILE],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print("✅ MediaMTX started successfully")
        return process
    except Exception as e:
        print(f"❌ Error starting MediaMTX: {e}")
        return None

def monitor_stream():
    print("📡 Monitoring streams...")
    try:
        while True:
            print("🔄 Streams running... (camera1, camera2)")
            time.sleep(5)
    except KeyboardInterrupt:
        print("\n🛑 Stopping monitoring...")

if __name__ == "__main__":
    process = start_mediamtx()
    if process:
        monitor_stream()
