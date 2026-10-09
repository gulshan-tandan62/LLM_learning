
from llm_service import generate_response


def main(): 
    modes = {
        "1": "general",
        "2": "python",
        "3": "summarizer"
    }

    while True:
        print("\nSelect Assistant Mode:")
        print("1. General Assistant")
        print("2. Python Teacher")
        print("3. Text Summarizer")
        print("Type 'exit' to quit.")

        choice = input("Enter your choice (1/2/3): ").strip().lower()

        if choice == "exit":
            print("Thanks! Bye 😊")
            break

        if choice not in modes:
            print("Error: Invalid assistant mode.")
            continue

        mode = modes[choice]

        user_input = input("Enter your question or text: ").strip()

        if user_input.lower() == "exit":
            print("thanks! Bye😊")
            break

        if not user_input:
            print("Error: Input cannot be empty.")
            continue

        try:
            answer = generate_response(user_input, mode=mode)
            print("\nGemini:")
            print(answer)

        except ValueError as error:
            print(f"Validation Error: {error}")

        except Exception as error:
            print(f"Application Error: {error}")

    

if __name__=="__main__":
    main()