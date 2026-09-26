def create_refinement_prompt(
    profile,
    previous_recommendations,
    feedback
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

PREVIOUS RECOMMENDATIONS
------------------------
{previous_recommendations}

USER FEEDBACK
-------------
{feedback}

TASK
----
Generate a refined recommendation list.

Carefully follow the user's feedback.

If the user dislikes a category, avoid it.

If the user requests a particular category,
increase recommendations from that category.

Generate exactly {profile['num_items']}
recommendations.

For each recommendation provide:

1. Name
2. Suitability score from 0 to 100
3. Reason
4. Brief description

Rank them from most suitable to least suitable.
"""

    return prompt