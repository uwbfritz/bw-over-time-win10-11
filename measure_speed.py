################################################
#  Author: B. Fritz
#  Date: 2023-09-24
#  Purpose: Measure internet up/down bandwidth 
#           on Windows over time
################################################

import os
import subprocess
import time
import csv

def measure_speed():
    try:
        output = subprocess.check_output("speedtest-cli --simple", shell=True).decode("utf-8")
        
        lines = output.strip().split("\n")
        ping = lines[0].split(":")[1].strip()
        
        download_speed = lines[1].split(":")[1].strip().replace("Mbit/s", "").strip()
        upload_speed = lines[2].split(":")[1].strip().replace("Mbit/s", "").strip()
        
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        
        log_filename = "speed_log.csv"
        file_exists = os.path.isfile(log_filename)
        
        with open(log_filename, "a", newline='') as log_file:
            csv_writer = csv.writer(log_file)
            
            if not file_exists:
                csv_writer.writerow(["Time", "Ping", "Download Speed", "Upload Speed"])
            
            csv_writer.writerow([current_time, ping, download_speed, upload_speed])
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    measure_speed()
