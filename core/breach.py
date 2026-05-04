def check_breach(email):
    results = []

    try:
        with open("data/breached_emails.txt") as f:
            data = f.read().splitlines()

        if email in data:
            results.append({
                "breach": "Simulated Leak",
                "severity": "High"
            })
    except:
        pass

    return results