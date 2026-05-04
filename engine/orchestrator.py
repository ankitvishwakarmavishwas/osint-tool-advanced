from core.username import check_username
from core.email import analyze_email
from core.breach import check_breach
from core.metadata import extract_metadata
from engine.scorer import calculate_risk

import json

def run_investigation(username, email):
    username_data = check_username(username) if username else []
    email_data = analyze_email(email) if email else {}
    breach_data = check_breach(email) if email else []
    metadata = extract_metadata(email) if email else {}

    risk_score = calculate_risk(username_data, breach_data)

    report = {
        "username": username_data,
        "email": email_data,
        "breaches": breach_data,
        "metadata": metadata,
        "risk_score": risk_score
    }

    with open("output/report.json", "w") as f:
        json.dump(report, f, indent=4)

    return report