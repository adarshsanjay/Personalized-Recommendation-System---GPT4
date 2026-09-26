import os


def save_results(
    profile,
    recommendations
):

    os.makedirs(
        "outputs",
        exist_ok=True
    )

    file_path = "outputs/recommendations.txt"

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "PERSONALIZED RECOMMENDATIONS\n"
        )

        file.write(
            "=" * 50 + "\n\n"
        )

        file.write(
            f"Name: {profile['name']}\n"
        )

        file.write(
            f"Age: {profile['age']}\n"
        )

        file.write(
            f"Background: {profile['background']}\n"
        )

        file.write(
            f"Interests: {profile['interests']}\n"
        )

        file.write(
            f"Skill Level: {profile['skill_level']}\n"
        )

        file.write(
            f"Preference: {profile['preference']}\n"
        )

        file.write(
            f"Goal: {profile['goal']}\n\n"
        )

        file.write(
            recommendations
        )

    return file_path