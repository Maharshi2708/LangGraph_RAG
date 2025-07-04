from workflows.workflow import build_workflow

def display_menu():
    print("1. Load Document (Local)")
    print("2. Load Document (From URL)")
    print("3. Ask a Query")
    print("4. Delete Document from Vector Store")
    print("5. Refresh Document")
    print("6. Exit")

def menu():
    graph = build_workflow()
    state = {}

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            file_path = input("Enter local file path: ")
            state = graph.invoke({**state, "file_path": file_path, "action": "load_local"})
            if 'summary' in state:
                print(f"\n📝 Summary:\n{state['summary']}\n")

        elif choice == '2':
            file_url = input("Enter file URL: ")
            state = graph.invoke({**state, "file_url": file_url, "action": "load_url"})
            if 'summary' in state:
                print(f"\n📝 Summary:\n{state['summary']}\n")

        elif choice == '3':
            state = graph.invoke({**state, "action": "ask_query"})

        elif choice == '4':
            state = graph.invoke({**state, "action": "delete_document"})

        elif choice == '5':
            state = graph.invoke({**state, "action": "refresh_document"})

        elif choice == '6':
            print("Exiting CLI. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
