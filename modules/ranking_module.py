def create_ranking_prompt(recommendations):

    prompt = f"""
You are a recommendation ranking assistant.

Below are personalized recommendations:

{recommendations}

Task:

Identify all recommendations and arrange them
from highest suitability to lowest suitability.

Preserve the suitability scores provided.

Use this format:

1. Recommendation Name - Score: 95%
2. Recommendation Name - Score: 90%
3. Recommendation Name - Score: 85%

Do not invent new recommendations.
Do not change the scores.
"""

    return prompt