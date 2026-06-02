import re

def extract_ips(log_file):
    ips = []

    pattern = r"Failed password.*from (\d+\.\d+\.\d+\.\d+)"

    with open(log_file, "r") as f:
        for line in f:
            match = re.search(pattern, line)

            if match:
                ips.append(match.group(1))

    return ips
