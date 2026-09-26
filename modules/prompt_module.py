def create_recommendation_prompt(
    profile,
    analysis,
    feedback=""
):

    prompt = f"""
You are a personalized recommendation assistant.

USER PROFILE
------------
Name: {profile['name']}
Age: {profile['age']}
Educational/Professional Background: {profile['background']}
Interests: {profile['interests']}
Skill Level: {profile['skill_level']}
Preferred Category: {profile['preference']}
Goal: {profile['goal']}
Number of Recommendations Required: {profile['num_items']}

PREFERENCE ANALYSIS
-------------------
Primary Interest: {analysis['primary_interest']}
Secondary Interest: {analysis['secondary_interest']}
Skill Level: {analysis['skill_level']}
Goal: {analysis['goal']}
Preference: {analysis['preference']}

USER FEEDBACK
-------------
{feedback if feedback else "No previous feedback."}

TASK
----
Generate exactly {profile['num_items']} personalized recommendations.

For every recommendation provide:

1. Recommendation name
2. Suitability score from 0 to 100
3. Reason why it is suitable
4. Brief description

The recommendations should match the user's:

- interests
- skill level
- background
- goal
- preferences

Rank the recommendations from most suitable to least suitable.

Use clear formatting.
"""

    return prompt