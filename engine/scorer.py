def calculate_risk(username_data, breach_data):
    score = 0

    found = sum(1 for acc in username_data if acc["status"] == "Found")
    score += found * 10

    if breach_data:
        score += 60

    return min(score, 100)