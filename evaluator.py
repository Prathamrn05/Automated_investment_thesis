from datetime import datetime
import random

def evaluate_pitch_deck(text):
    categories = [
        ("Problem Statement", 10),
        ("Solution/Product", 15),
        ("Market Opportunity", 20),
        ("Business Model", 15),
        ("Competitive Landscape", 10),
        ("Team", 15),
        ("Traction/Milestones", 10),
        ("Financial Projections", 10),
        ("Clarity and Presentation", 5),
    ]

    results = []
    total_score = 0
    for name, weight in categories:
        score = random.randint(4, 9)
        feedback = f"Feedback on {name}: detailed analysis with score {score}."
        results.append({
            "category": name,
            "score": score,
            "weight": weight,
            "feedback": feedback
        })
        total_score += score * (weight / 100)

    strengths = [
        "Clear problem validation with data",
        "Large target market",
        "Experienced founding team"
    ]
    weaknesses = [
        "No financial assumptions provided",
        "Unclear customer acquisition strategy"
    ]

    recommendation = "Strong Buy" if total_score > 80 else "Hold" if total_score > 60 else "Pass"
    timestamp = datetime.utcnow().strftime("%d-%m-%Y %H:%M:%S UTC")

    return {
        "startup_name": "DemoStartup",
        "overall_score": int(total_score),
        "recommendation": recommendation,
        "timestamp": timestamp,
        "categories": results,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "recommendation_text": "Focus on refining your go-to-market and team structure to attract investors.",
        "confidence_score": random.randint(60, 95)
    }
