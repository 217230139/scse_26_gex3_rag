from rag import retrieve, generate_answer


def answer_with_rag(query, policy_text):
    """Full RAG pipeline: retrieve relevant context, then ask the model."""
    context = retrieve(query, policy_text)

    # If no relevant context found, tell the model not to answer
    if context.strip() == "":
        return "I'm sorry, that information is not available in the policy document."

    answer = generate_answer(query, context)
    return answer