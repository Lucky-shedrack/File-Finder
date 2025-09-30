from menus import show_settings, edit_settings, search_flow


def main() -> None:
    """
    `run` runs the main interactive loop of the File Search CLI application.
    Workflow:
        - Display the main menu with options to search, view settings, edit settings, or exit.
        - Continuously prompt the user until they choose to exit.
        - Routes user choices to:
            1 → Run the search workflow (`search_flow`).
            2 → Show current application settings (`show_settings`).
            3 → Edit configuration settings (`edit_settings`).
            0 → Exit the program gracefully.

    Returns:
        None
        (The function is interactive and prints output directly to the console.)
    """
    while True:
        print("\n--- File Search CLI ---")
        print("1. Search for a File/Folder")
        print("2. View Current Settings")
        print("3. Edit Settings")
        print("0. Exit")

        choice = input("Choose option: ").strip()
        if choice == "1":
            search_flow()
        elif choice == "2":
            show_settings()
        elif choice == "3":
            edit_settings()
        elif choice == "0":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()
