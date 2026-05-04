def extract_metadata(email):
    return {
        "length": len(email),
        "has_number": any(char.isdigit() for char in email)
    }