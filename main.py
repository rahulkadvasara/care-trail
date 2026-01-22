# from qdrant.client import init_collection
# from agents.ingestion_agent import ingest_text
# from agents.memory_agent import retrieve_memory
# from agents.reasoning_agent import generate_response

# from dotenv import load_dotenv
# load_dotenv()


# def main():
#     print("Initializing CareTrail...")
#     init_collection()

#     print("\n--- Ingesting Sample Data ---")
#     ingest_text(
#         "Blood report shows low hemoglobin level of 9.5 g/dL.",
#         record_type="report"
#     )

#     ingest_text(
#         "Patient reports fatigue and dizziness over the past week.",
#         record_type="symptom"
#     )

#     print("\n--- Querying System ---")
#     query = "Why do I feel tired recently?"
#     memories = retrieve_memory(query)
#     answer = generate_response(query, memories)

#     print("\nAnswer:\n")
#     print(answer)

# if __name__ == "__main__":
#     main()


from dotenv import load_dotenv
load_dotenv()

from qdrant.client import init_collection
from agents.ingestion_agent import ingest_text
from agents.memory_agent import retrieve_memory
from agents.reasoning_agent import generate_response

def main():
    print("=== CareTrail: Healthcare Memory Assistant ===\n")
    init_collection()

    while True:
        print("\nChoose an option:")
        print("1. Add medical information")
        print("2. Ask a question")
        print("3. Exit")

        choice = input("Enter choice (1/2/3): ").strip()

        if choice == "1":
            text = input("\nEnter medical note or report:\n")
            record_type = input("Type (report/symptom/note): ").strip()
            ingest_text(text, record_type)
            print("\n✅ Information stored in memory.")

        elif choice == "2":
            query = input("\nAsk your question:\n")
            memories = retrieve_memory(query)
            answer = generate_response(query, memories)
            print("\nAnswer:\n")
            print(answer)

        elif choice == "3":
            print("\nExiting CareTrail.")
            break

        else:
            print("\n❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
