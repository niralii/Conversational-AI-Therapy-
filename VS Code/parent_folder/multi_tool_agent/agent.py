from google.adk.agents import Agent

def suggest_coping_technique(feeling: str) -> dict:
    """
    Suggests a coping technique based on the user's expressed feeling.

    Args:
        feeling (str): The primary emotion the user is feeling (e.g., "anxious", "sad", "angry").

    Returns:
        dict: A dictionary containing the status and a suggested technique or an error message.
    """
    feeling = feeling.lower()
    if "anxious" in feeling or "stressed" in feeling:
        return {
            "status": "success",
            "report": (
                "When you're feeling anxious, you could try the 5-4-3-2-1 grounding technique. "
                "Notice: 5 things you can see, 4 things you can feel, 3 things you can hear, "
                "2 things you can smell, and 1 thing you can taste. This can help bring you back to the present moment."
            ),
        }
    elif "sad" in feeling or "down" in feeling:
        return {
            "status": "success",
            "report": (
                "It's okay to feel sad. Sometimes, engaging in a small, enjoyable activity can help. "
                "This could be listening to a favorite song, stretching your body, or stepping outside for a moment. "
                "Be kind to yourself."
            ),
        }
    else:
        return {
            "status": "error",
            "error_message": f"I'm here to listen, but I don't have a specific technique for '{feeling}' right now.",
        }


def provide_mindfulness_exercise() -> dict:
    """
    Provides a simple mindfulness exercise to help the user center themselves.

    Returns:
        dict: A dictionary containing the status and the exercise instructions.
    """
    report = (
        "Here is a simple breathing exercise. Find a comfortable position. "
        "Inhale slowly through your nose for a count of four, hold your breath for a count of four, "
        "and then exhale slowly through your mouth for a count of six. "
        "Repeat this a few times to help calm your mind."
    )
    return {"status": "success", "report": report}


# IMPORTANT: This is a simplified example for demonstration and not a substitute for professional mental health care.
root_agent = Agent(
    name="therapy_bot_agent",
    model="gemini-2.0-flash", # You can use any compatible model
    description=(
        "An empathetic agent that provides coping techniques and mindfulness "
        "exercises to help users with their feelings."
    ),
    instruction=(
        "You are a compassionate and supportive therapy bot. Your goal is to listen "
        "to the user and, when appropriate, use your tools to offer helpful "
        "coping mechanisms or mindfulness exercises. Always respond with "
        "empathy and care. Do not give medical advice."
    ),
    tools=[suggest_coping_technique, provide_mindfulness_exercise],
)