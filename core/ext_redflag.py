RED_FLAGS = {
    "Urgency": [
        "urgent", "immediately", "act now", "last chance", "hurry"
    ],
    "Money / Payment": [
        "send money", "transfer", "payment", "crypto", "bitcoin", "usdt"
    ],
    "Emotional Manipulation": [
        "trust me", "please help", "i swear", "dear", "love you"
    ],
    "Authority Impersonation": [
        "police", "bank", "official", "cyber cell", "government"
    ]
}

def analyze_text(text):
    text = text.lower()
    findings = {}
    score = 0

    for category, keywords in RED_FLAGS.items():
        matches = [k for k in keywords if k in text]
        if matches:
            findings[category] = matches
            score += len(matches) * 15

    if score >= 60:
        risk = "HIGH"
    elif score >= 30:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return {
        "Risk Score": score,
        "Risk Level": risk,
        "Red Flags Found": findings if findings else "None"
    }
