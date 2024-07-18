import requests
import ipaddress

# Example URLs to fetch CIDRs from
url_list = [
    "https://example.com/cidr_list.txt",
    "https://anotherexample.com/another_cidr_list.txt"
]

cidr_blocks = []

# Fetch CIDRs from each URL
for url in url_list:
    response = requests.get(url)
    if response.status_code == 200:
        lines = response.text.splitlines()
        for line in lines:
            line = line.strip()
            try:
                network = ipaddress.ip_network(line, strict=False)  # Parse CIDR
                cidr_blocks.append(network)
            except ValueError as e:
                print(f"Ignoring invalid CIDR: {line} - {e}")

# Now cidr_blocks contains a list of ipaddress.IPv4Network or ipaddress.IPv6Network objects
# Use them as needed in your application
for cidr in cidr_blocks:
    print(cidr)
