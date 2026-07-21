from ai_friend import generate_response


def main():
    print("AI Friend is ready. Type 'quit' to exit.\n")
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() in {"quit", "exit"}:
            print("AI Friend: Goodbye!")
            break
        print(f"AI Friend: {generate_response(user_input)}")


if __name__ == "__main__":
    main()
