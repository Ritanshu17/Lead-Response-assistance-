def build_response(intent):
    problem = intent['problem']

    questions = intent['missing_information']

    if not questions:
        questions = [
            "When did this issue start?",
            "Has any repair been attempted earlier?"
        ]

    reply = f"""
        Thank you for reaching out - I understand you're experiencing {problem},

        To better assist you, I have a few questions:
        {chr(10).join('-' + q for q in questions)}

        In the meantime , we recommend:
        * Avoid temporary fixes that may trap moisture,
        * Monitor whether the issue worsens after rainfall,
        * In safe, take a photo to help assessment.

        Once we have more information, we can provide on the next step.

"""
    return reply