def create_explanation_prompt(
    profile,
    recommendation,
    user_question
):

    prompt = f"""
You are a personalized recommendation assistant.

USER PROFILE
------------
Name: {profile['name']}
Background: {profile['background']}
Interests: {profile['interests']}
Skill Level: {profile['skill_level']}
Goal: {profile['goal']}
Preference: {profile['preference']}

RECOMMENDATION
--------------
{recommendation}

USER QUESTION
-------------
{user_question}

Explain clearly why this recommendation is suitable
for the user.

Consider the user's interests, skill level,
background, goal and preference.

Keep the explanation concise and personalized.
"""

    return prompt