def analyze_email(email):
    domain = email.split("@")[-1]

    return {
        "email": email,
        "domain": domain,
        "provider": domain.split(".")[0]
    }