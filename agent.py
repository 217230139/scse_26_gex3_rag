from policy_loader import load_policy_documents
from rag_tool import answer_with_rag


def main():
    # Load the policy documents (function provided, do not change)
    documents = load_policy_documents()

    # Combine all document contents into one text string
    policy_text = ""
    for doc in documents:
        policy_text += doc.page_content + "\n\n"

    print("UNIVERSITY IT SUPPORT ASSISTANT (RAG)")
    print("=" * 50)

    while True:
        query = input("\nAsk a question (or type 'quit'): ").strip()

        if query.lower() == "quit":
            print("Goodbye.")
            break

        if query == "":
            print("Please enter a question.")
            continue

        answer = answer_with_rag(query, policy_text)
        print("\nAnswer:")
        print(answer)


if __name__ == "__main__":
    main()