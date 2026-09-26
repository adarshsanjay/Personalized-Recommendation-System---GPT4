import streamlit as st

from modules.profile_module import (
    create_profile,
    analyze_profile
)

from modules.prompt_module import (
    create_recommendation_prompt
)

from modules.recommendation_module import (
    generate_recommendations
)

from modules.ranking_module import (
    create_ranking_prompt
)

from modules.explanation_module import (
    create_explanation_prompt
)

from modules.feedback_module import (
    create_refinement_prompt
)

from modules.intent_module import (
    detect_intent
)

from modules.save_module import (
    save_results
)


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Personalized Recommendation System",
    page_icon="🎯",
    layout="wide"
)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title(
    "🎯 Personalized Recommendation System"
)

st.write(
    "A personalized recommendation system "
    "using Qwen 3 through Ollama."
)


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "profile" not in st.session_state:
    st.session_state.profile = None

if "analysis" not in st.session_state:
    st.session_state.analysis = None

if "recommendations" not in st.session_state:
    st.session_state.recommendations = ""

if "feedback" not in st.session_state:
    st.session_state.feedback = ""

if "intent" not in st.session_state:
    st.session_state.intent = ""


# --------------------------------------------------
# SIDEBAR - USER INPUT
# --------------------------------------------------

st.sidebar.header("👤 User Profile")

name = st.sidebar.text_input(
    "Name",
    value="Arun"
)

age = st.sidebar.number_input(
    "Age",
    min_value=1,
    max_value=100,
    value=20
)

background = st.sidebar.text_input(
    "Educational / Professional Background",
    value="Computer Science"
)

interests = st.sidebar.text_input(
    "Interests",
    value="Artificial Intelligence, Python"
)

skill_level = st.sidebar.selectbox(
    "Skill Level",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

preference = st.sidebar.text_input(
    "Preferred Category / Type",
    value="Practical learning"
)

goal = st.sidebar.text_input(
    "Goal",
    value="Learn Artificial Intelligence"
)

num_items = st.sidebar.slider(
    "Number of Recommendations",
    min_value=1,
    max_value=10,
    value=5
)


# --------------------------------------------------
# CREATE PROFILE
# --------------------------------------------------

profile = create_profile(
    name,
    age,
    background,
    interests,
    skill_level,
    preference,
    goal,
    num_items
)

analysis = analyze_profile(
    profile
)

st.session_state.profile = profile
st.session_state.analysis = analysis


# --------------------------------------------------
# USER PROFILE
# --------------------------------------------------

st.header("👤 User Profile")

col1, col2 = st.columns(2)

with col1:

    st.write(
        f"**Name:** {profile['name']}"
    )

    st.write(
        f"**Age:** {profile['age']}"
    )

    st.write(
        f"**Background:** {profile['background']}"
    )

    st.write(
        f"**Interests:** {profile['interests']}"
    )


with col2:

    st.write(
        f"**Skill Level:** {profile['skill_level']}"
    )

    st.write(
        f"**Preference:** {profile['preference']}"
    )

    st.write(
        f"**Goal:** {profile['goal']}"
    )

    st.write(
        f"**Number Required:** {profile['num_items']}"
    )


# --------------------------------------------------
# PREFERENCE ANALYSIS
# --------------------------------------------------

st.header("🔍 Preference Analysis")

col1, col2, col3 = st.columns(3)

with col1:

    st.info(
        f"**Primary Interest**\n\n"
        f"{analysis['primary_interest']}"
    )

with col2:

    st.info(
        f"**Secondary Interest**\n\n"
        f"{analysis['secondary_interest']}"
    )

with col3:

    st.info(
        f"**Goal**\n\n"
        f"{analysis['goal']}"
    )

st.write(
    f"**Skill Level:** {analysis['skill_level']}"
)

st.write(
    f"**Preferred Type:** {analysis['preference']}"
)


# --------------------------------------------------
# GENERATE RECOMMENDATIONS
# --------------------------------------------------

st.header("🎯 Recommendation Generation")

if st.button(
    "Generate Recommendations",
    type="primary"
):

    prompt = create_recommendation_prompt(
        profile,
        analysis,
        st.session_state.feedback
    )

    with st.spinner(
        "Qwen is generating personalized recommendations..."
    ):

        result = generate_recommendations(
            prompt
        )

    st.session_state.recommendations = result


# --------------------------------------------------
# DISPLAY RECOMMENDATIONS
# --------------------------------------------------

if st.session_state.recommendations:

    st.header(
        "⭐ Personalized Recommendations"
    )

    st.markdown(
        st.session_state.recommendations
    )


# --------------------------------------------------
# USER FEEDBACK
# --------------------------------------------------

st.header("💬 User Feedback")

feedback = st.text_area(
    "Tell the system what you liked or disliked.",
    placeholder=(
        "Example: I prefer Artificial Intelligence "
        "and Python. I do not want Web Development."
    )
)


if st.button(
    "🔄 Refine Recommendations"
):

    if not st.session_state.recommendations:

        st.warning(
            "Generate recommendations first."
        )

    elif not feedback.strip():

        st.warning(
            "Please enter feedback."
        )

    else:

        refinement_prompt = create_refinement_prompt(
            profile,
            st.session_state.recommendations,
            feedback
        )

        with st.spinner(
            "Qwen is refining the recommendations..."
        ):

            refined = generate_recommendations(
                refinement_prompt
            )

        st.session_state.recommendations = refined
        st.session_state.feedback = feedback

        st.success(
            "Recommendations successfully refined!"
        )

        st.markdown(
            refined
        )


# --------------------------------------------------
# INTENT DETECTION
# --------------------------------------------------

st.header("🧠 Intelligent Intent Detection")

user_request = st.text_input(
    "Enter a natural-language request",
    placeholder=(
        "Example: Show my profile"
    )
)


if st.button(
    "Detect Intent"
):

    if not user_request.strip():

        st.warning(
            "Please enter a request."
        )

    else:

        with st.spinner(
            "Qwen is detecting the intent..."
        ):

            intent = detect_intent(
                user_request
            )

        st.session_state.intent = intent

        st.success(
            f"Detected Intent: {intent}"
        )


# --------------------------------------------------
# INTENT ACTION
# --------------------------------------------------

if st.session_state.intent:

    intent = st.session_state.intent

    if intent == "SHOW_PROFILE":

        st.subheader(
            "👤 Current Profile"
        )

        st.json(
            st.session_state.profile
        )

    elif intent == "EXIT":

        st.info(
            "Session exit requested."
        )

    elif intent == "SAVE_RECOMMENDATION":

        if st.session_state.recommendations:

            file_path = save_results(
                profile,
                st.session_state.recommendations
            )

            st.success(
                f"Recommendations saved to {file_path}"
            )

        else:

            st.warning(
                "Generate recommendations first."
            )


# --------------------------------------------------
# EXPLANATION
# --------------------------------------------------

st.header("💡 Recommendation Explanation")

recommendation_to_explain = st.text_input(
    "Recommendation to explain",
    placeholder="Example: Python for AI"
)

explanation_question = st.text_input(
    "Question",
    value="Why is this recommendation suitable for me?"
)


if st.button(
    "Explain Recommendation"
):

    if not recommendation_to_explain.strip():

        st.warning(
            "Enter a recommendation first."
        )

    else:

        explanation_prompt = create_explanation_prompt(
            profile,
            recommendation_to_explain,
            explanation_question
        )

        with st.spinner(
            "Qwen is generating an explanation..."
        ):

            explanation = generate_recommendations(
                explanation_prompt
            )

        st.info(
            explanation
        )


# --------------------------------------------------
# SAVE RESULTS
# --------------------------------------------------

st.header("💾 Save Results")

if st.button(
    "Save Recommendations"
):

    if not st.session_state.recommendations:

        st.warning(
            "Generate recommendations first."
        )

    else:

        file_path = save_results(
            profile,
            st.session_state.recommendations
        )

        st.success(
            f"Recommendations saved to `{file_path}`"
        )