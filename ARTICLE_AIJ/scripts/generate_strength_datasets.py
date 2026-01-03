"""
Generate Multimodal Finance Dataset

Creates a dataset combining numeric financial data with text customer notes
for testing SpiralCortex's multimodal reasoning capabilities.
"""

import json
import os
import random

import pandas as pd


def generate_multimodal_finance_dataset(n_samples=1000, output_file="data/multimodal_finance.csv"):
    """Generate a multimodal finance dataset with text + numeric features."""

    # Define risk categories and their characteristics
    risk_profiles = {
        "Low": {
            "credit_score_range": (700, 850),
            "income_range": (50000, 150000),
            "debt_ratio_range": (0.1, 0.3),
            "complaint_probability": 0.1,
            "positive_sentiment": 0.8,
        },
        "Medium": {
            "credit_score_range": (600, 750),
            "income_range": (30000, 80000),
            "debt_ratio_range": (0.3, 0.5),
            "complaint_probability": 0.3,
            "positive_sentiment": 0.5,
        },
        "High": {
            "credit_score_range": (400, 650),
            "income_range": (20000, 60000),
            "debt_ratio_range": (0.5, 0.8),
            "complaint_probability": 0.6,
            "positive_sentiment": 0.2,
        },
    }

    # Complaint templates for different risk levels
    complaint_templates = {
        "Low": [
            "Everything is going smoothly with my account.",
            "I'm very satisfied with the service quality.",
            "No issues whatsoever, great experience.",
            "The loan process was straightforward and fair.",
            "I appreciate the transparent communication.",
        ],
        "Medium": [
            "The interest rates seem a bit high but understandable.",
            "Sometimes the statements are confusing but I manage.",
            "Service is okay, could be better but not terrible.",
            "Had a small issue with a transaction but it got resolved.",
            "The fees are noticeable but within expectations.",
        ],
        "High": [
            "This is outrageous! The fees are killing me!",
            "I'm drowning in debt and the rates are unfair!",
            "The bank is taking advantage of vulnerable people!",
            "How can you charge so much for such poor service?",
            "This loan is destroying my financial future!",
        ],
    }

    data = []

    for _ in range(n_samples):
        # Randomly select risk level
        risk_level = random.choice(["Low", "Medium", "High"])
        profile = risk_profiles[risk_level]

        # Generate numeric features
        credit_score = random.randint(*profile["credit_score_range"])
        annual_income = random.randint(*profile["income_range"])
        debt_ratio = random.uniform(*profile["debt_ratio_range"])
        age = random.randint(25, 75)
        employment_years = random.randint(1, 40)

        # Generate account details
        account_balance = random.uniform(1000, 50000)
        monthly_payment = random.uniform(200, 2000)
        loan_amount = random.uniform(5000, 100000)

        # Generate text complaint/note
        has_complaint = random.random() < profile["complaint_probability"]
        if has_complaint:
            complaint_text = random.choice(complaint_templates[risk_level])
        else:
            # Generate neutral or positive notes
            neutral_templates = [
                "Regular account maintenance and payments.",
                "No significant issues reported this month.",
                "Customer has been active with normal transactions.",
                "Account in good standing with regular deposits.",
                "Standard banking activities observed.",
            ]
            complaint_text = random.choice(neutral_templates)

        # Add some contextual information that might contradict or support the numbers
        contextual_hints = []
        if risk_level == "High" and random.random() < 0.3:
            contextual_hints.extend(
                [
                    "Customer mentioned recent job loss.",
                    "Family emergency requiring additional funds.",
                    "Struggling with medical bills.",
                    "Unexpected home repairs needed.",
                ]
            )
        elif risk_level == "Low" and random.random() < 0.2:
            contextual_hints.extend(
                [
                    "Recently received promotion at work.",
                    "Inherited family property.",
                    "Started successful side business.",
                    "Won local business award.",
                ]
            )

        if contextual_hints:
            complaint_text += f" Note: {random.choice(contextual_hints)}"

        # Create data row
        row = {
            "credit_score": credit_score,
            "annual_income": annual_income,
            "debt_ratio": debt_ratio,
            "age": age,
            "employment_years": employment_years,
            "account_balance": round(account_balance, 2),
            "monthly_payment": round(monthly_payment, 2),
            "loan_amount": round(loan_amount, 2),
            "complaint_text": complaint_text,
            "risk_category": risk_level,
        }

        data.append(row)

    # Create DataFrame and save
    df = pd.DataFrame(data)

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    df.to_csv(output_file, index=False)
    print(f"✅ Generated multimodal finance dataset with {n_samples} samples")
    print(f"   Saved to: {output_file}")
    print(f"   Risk distribution: {df['risk_category'].value_counts().to_dict()}")

    return df


def generate_emotional_reasoning_dataset(
    n_samples=500, output_file="data/emotional_reasoning.json"
):
    """Generate emotional reasoning dataset for SEC vector testing."""

    # Emotion categories with intensity levels
    emotions = {
        "joy": ["happy", "excited", "content", "peaceful", "grateful"],
        "sadness": ["sad", "disappointed", "lonely", "hopeless", "depressed"],
        "anger": ["angry", "frustrated", "irritated", "furious", "enraged"],
        "fear": ["anxious", "scared", "worried", "terrified", "panicked"],
        "surprise": ["shocked", "amazed", "astonished", "startled", "bewildered"],
        "disgust": ["repulsed", "grossed out", "sickened", "appalled", "revolted"],
        "anticipation": ["expectant", "hopeful", "optimistic", "eager", "enthusiastic"],
        "trust": ["confident", "faithful", "loyal", "reliable", "dependable"],
    }

    # Mixed emotion scenarios
    mixed_emotions = [
        ("joy", "anticipation", "Excited about tomorrow but nervous"),
        ("sadness", "anger", "Disappointed and frustrated with the situation"),
        ("fear", "anticipation", "Anxious yet hopeful about the future"),
        ("surprise", "joy", "Shocked but pleased with the outcome"),
        ("trust", "fear", "Confident despite some worries"),
        ("disgust", "anger", "Repulsed and outraged by the behavior"),
        ("sadness", "trust", "Sad but still believing things will improve"),
        ("joy", "surprise", "Happy and amazed at the same time"),
    ]

    # Text templates for different emotional contexts
    text_templates = {
        "personal": [
            "I feel {} about {}",
            "I'm experiencing {} regarding {}",
            "This situation makes me feel {}",
            "{} is how I feel when I think about {}",
        ],
        "social": [
            "When {} happens, I feel {}",
            "Interacting with {} makes me feel {}",
            "The way {} treated me left me feeling {}",
            "Being around {} gives me a sense of {}",
        ],
        "professional": [
            "At work, I feel {} about {}",
            "The project makes me feel {}",
            "Dealing with {} at the office leaves me {}",
            "My job situation has me feeling {}",
        ],
    }

    data = []

    for _ in range(n_samples):
        # Decide if this is a pure emotion or mixed emotion
        is_mixed = random.random() < 0.4  # 40% mixed emotions

        if is_mixed:
            primary_emotion, secondary_emotion, description = random.choice(mixed_emotions)
            emotion_label = f"{primary_emotion}_{secondary_emotion}"
            intensity_primary = random.uniform(0.6, 1.0)
            intensity_secondary = random.uniform(0.3, 0.7)
        else:
            primary_emotion = random.choice(list(emotions.keys()))
            emotion_label = primary_emotion
            intensity_primary = random.uniform(0.5, 1.0)
            intensity_secondary = 0.0
            secondary_emotion = None

        # Choose context and generate text
        context = random.choice(["personal", "social", "professional"])
        template = random.choice(text_templates[context])

        # Fill in template with emotion words and context
        emotion_word = random.choice(emotions[primary_emotion])
        context_words = {
            "personal": [
                "my future",
                "this decision",
                "my health",
                "family matters",
                "personal goals",
            ],
            "social": [
                "my friends",
                "new people",
                "family gatherings",
                "social events",
                "relationships",
            ],
            "professional": [
                "my career",
                "the deadline",
                "my colleagues",
                "performance reviews",
                "work challenges",
            ],
        }

        context_phrase = random.choice(context_words[context])
        text = template.format(emotion_word, context_phrase)

        # Add some nuance or contradiction
        if random.random() < 0.3:
            contradictions = [
                ", though I'm trying to stay positive",
                ", even though logically it should be fine",
                ", despite what others might think",
                ", which surprises even me",
                ", though I know it's irrational",
            ]
            text += random.choice(contradictions)

        # Create SEC vector (simplified 8-dimensional representation)
        sec_vector = {
            "arousal": (
                intensity_primary
                if primary_emotion in ["joy", "anger", "fear", "surprise"]
                else 0.3
            ),
            "valence": 0.8 if primary_emotion in ["joy", "trust", "anticipation"] else -0.5,
            "dominance": 0.7 if primary_emotion in ["anger", "trust"] else 0.3,
            "anger": 1.0 if "anger" in emotion_label else 0.0,
            "fear": 1.0 if "fear" in emotion_label else 0.0,
            "joy": 1.0 if "joy" in emotion_label else 0.0,
            "sadness": 1.0 if "sadness" in emotion_label else 0.0,
            "surprise": 1.0 if "surprise" in emotion_label else 0.0,
        }

        # Adjust for mixed emotions
        if secondary_emotion:
            sec_vector[secondary_emotion] = intensity_secondary

        row = {
            "text": text,
            "primary_emotion": primary_emotion,
            "secondary_emotion": secondary_emotion,
            "emotion_label": emotion_label,
            "context": context,
            "sec_vector": sec_vector,
            "intensity_primary": intensity_primary,
            "intensity_secondary": intensity_secondary,
            "is_mixed_emotion": is_mixed,
        }

        data.append(row)

    # Save as JSON
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✅ Generated emotional reasoning dataset with {n_samples} samples")
    print(f"   Saved to: {output_file}")

    # Print emotion distribution
    emotion_counts = {}
    for item in data:
        label = item["emotion_label"]
        emotion_counts[label] = emotion_counts.get(label, 0) + 1

    print(f"   Emotion distribution: {emotion_counts}")

    return data


if __name__ == "__main__":
    # Generate both datasets
    multimodal_df = generate_multimodal_finance_dataset()
    emotional_data = generate_emotional_reasoning_dataset()
