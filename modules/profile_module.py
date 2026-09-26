def create_profile(
    name,
    age,
    background,
    interests,
    skill_level,
    preference,
    goal,
    num_items
):
    profile = {
        "name": name,
        "age": age,
        "background": background,
        "interests": interests,
        "skill_level": skill_level,
        "preference": preference,
        "goal": goal,
        "num_items": num_items
    }

    return profile


def analyze_profile(profile):

    interests = [
        item.strip()
        for item in profile["interests"].split(",")
        if item.strip()
    ]

    if len(interests) > 0:
        primary_interest = interests[0]
    else:
        primary_interest = "Not specified"

    if len(interests) > 1:
        secondary_interest = interests[1]
    else:
        secondary_interest = "Not specified"

    analysis = {
        "primary_interest": primary_interest,
        "secondary_interest": secondary_interest,
        "skill_level": profile["skill_level"],
        "goal": profile["goal"],
        "preference": profile["preference"]
    }

    return analysis