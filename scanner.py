import nmap

scanner = nmap.PortScanner()

target = input("Enter IP Address: ")

print(f"Scanning {target}...")

scanner.scan(target, arguments='-sV')

for host in scanner.all_hosts():
    print(f"\nHost: {host}")

    for proto in scanner[host].all_protocols():
        ports = scanner[host][proto].keys()

        for port in ports:
            print(f"Port {port} is OPEN")

with open("report.txt", "w") as file:
    file.write("Vulnerability Scan Report\n")
    file.write(f"Target: {target}\n")
    file.write("----------------------\n")

    for host in scanner.all_hosts():
        for proto in scanner[host].all_protocols():
            for port in scanner[host][proto].keys():
                file.write(f"Port {port} OPEN\n")