import json
from ollama import chat


def retrieve(query, policy_text):
    """Return the part of the policy that matches the query.
    If the query is about phone number/IT service desk, return only relevant lines.
    Otherwise return the whole policy as fallback."""
    query_lower = query.lower()

    # Split policy into lines and keep only relevant ones
    lines = policy_text.split("\n")
    relevant = []

    keywords = ["phone", "call", "contact", "service desk", "it support", "helpdesk"]

    for line in lines:
        line_lower = line.lower()
        for kw in keywords:
            if kw in line_lower:
                relevant.append(line)
                break

    if len(relevant) == 0:
        return policy_text  # fallback: whole policy

    return "\n".join(relevant)


def generate_answer(query, retrieved_context):
    """Call Qwen with the retrieved context and the user question.
    The system prompt must forbid hallucination."""
    system_prompt = (
        "You are a university IT support assistant. "
        "Answer the user's question using ONLY the context provided below. "
        "If the answer is not in the context, say that the information is not available. "
        "Do not invent any phone numbers, emails, or URLs. "
        "Keep the answer short and factual."
    )

    user_prompt = (
        "Context:\n" + retrieved_context + "\n\n"
        "Question: " + query
    )

    response = chat(
        model="qwen3:0.6b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )

    return response.message.content