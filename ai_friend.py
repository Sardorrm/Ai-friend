import os


def generate_response(user_input: str) -> str:
    text = user_input.strip()

    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        try:
            from openai import OpenAI

            client = OpenAI(api_key=api_key)
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a warm and friendly AI companion. Reply briefly and kindly.",
                    },
                    {"role": "user", "content": user_input},
                ],
                temperature=0.7,
            )
            reply = completion.choices[0].message.content
            if reply:
                return reply.strip()
        except Exception:
            pass

    if not text:
        return "Hello! I am your AI friend. Tell me how you feel."

    lowered = text.lower()
    if any(word in lowered for word in ["hello", "hi", "hey"]):
        return "Hello! I am your AI friend. How are you today?"

    if any(word in lowered for word in ["sad", "bad", "upset", "depressed", "lonely"]):
        return "I am sorry you are feeling that way. You are not alone, and I am here with you."

    if any(word in lowered for word in ["love", "beautiful", "great", "happy", "good"]):
        return "That sounds wonderful! I am glad you are feeling positive."

    if any(word in lowered for word in ["joke", "funny"]):
        return "Why do programmers prefer dark mode? Because light attracts bugs!"

    return "I am here to chat with you. Tell me more about your day."
