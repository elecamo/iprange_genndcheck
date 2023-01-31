import requests
import threading
#ExAcTo

start_ip = input("Enter start IP: ")
end_ip = input("Enter end IP: ")

start_ip_parts = start_ip.split(".")
end_ip_parts = end_ip.split(".")

def check_ip(current_ip):
    url = f"http://{current_ip}"
    try:
        response = requests.get(url, timeout=0.5)
        if response.status_code == 200:
            with open("result.txt", "a") as f:
                f.write(current_ip + "\n")
            print(f"{current_ip} - OK")
        else:
            print(f"{current_ip} - NOT OK ({response.status_code})")
    except:
        print(f"{current_ip} - ERROR")

threads = []
for i in range(int(start_ip_parts[3]), int(end_ip_parts[3])+1):
    current_ip = f"{start_ip_parts[0]}.{start_ip_parts[1]}.{start_ip_parts[2]}.{i}"
    thread = threading.Thread(target=check_ip, args=(current_ip,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Working IPs written to result.txt")
