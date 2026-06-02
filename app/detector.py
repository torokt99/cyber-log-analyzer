from collections import Counter

def detect_bruteforce(ips, threshold=5):
    counter = Counter(ips)

    alerts = []

    for ip, count in counter.items():
        if count >= threshold:
            alerts.append({
                "ip": ip,
                "attempts": count
            })

    return alerts
