from .recommendation_module import generate_recommendations


VALID_INTENTS = {
    "GENERATE_RECOMMENDATION",
    "REFINE_RECOMMENDATION",
    "SHOW_PROFILE",
    "EXPLAIN_RECOMMENDATION",
    "SAVE_RECOMMENDATION",
    "EXIT"
}


def detect_intent(user_input):

    prompt = f"""
You are an intent classification system.

Classify the user's request into exactly ONE
of the following intents:

GENERATE_RECOMMENDATION
REFINE_RECOMMENDATION
SHOW_PROFILE
EXPLAIN_RECOMMENDATION
SAVE_RECOMMENDATION
EXIT

Examples:

"Recommend some AI courses"
= GENERATE_RECOMMENDATION

"Give me more beginner-friendly options"
= REFINE_RECOMMENDATION

"Show my profile"
= SHOW_PROFILE

"Why did you recommend this?"
= EXPLAIN_RECOMMENDATION

"Save these recommendations"
= SAVE_RECOMMENDATION

"Exit"
= EXIT

User request:
{user_input}

Return ONLY the intent name.
"""

    result = generate_recommendations(prompt)

    intent = result.strip().upper()

    if intent not in VALID_INTENTS:
        intent = "GENERATE_RECOMMENDATION"

    return intent