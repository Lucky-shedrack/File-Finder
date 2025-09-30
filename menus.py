from terminal import (
    config,
    set_root_path,
    toggle_case_sensitive,
    set_page_size,
    set_allowed_extensions,
    add_bookmark,
    remove_bookmark,
)
from find import find_files
from settings import paginate_display


def show_settings() -> None:
    """
    `show_settings` displays the current configuration settings
    """
    print("\n--- Current Settings ---")
    for k, v in config.items():
        print(f"{k}: {v}")
    print("-----------------------\n")


def edit_settings() -> None:
    """
    `edit_settings` displays an interactive menu for editing application settings.

    Behavior:
        - Continuously displays a settings menu until the user chooses to return 
        to the main menu.
        - Allows modification of various settings stored in the global config.
        Menu options:
            1. Set root path:
                Prompts for a new root directory and updates it if valid.
            2. Toggle case sensitivity:
                Switches between case-sensitive and case-insensitive search modes.
            3. Set page size:
                Prompts for a number (3 - 20) and updates the number of results 
                displayed per page.
            4. Set allowed file extensions:
                Prompts for a comma-separated list of file extensions and updates 
                the configuration.
            5. Manage bookmarks:
                Opens the bookmark management menu for adding, removing, or 
                listing bookmarks.
            0. Back:
                Exits the settings menu and returns to the caller.

    Returns:
        None. All changes are applied directly to the configuration and 
        feedback is printed to the console.
    """
    while True:
        print("\n--- Edit Settings ---")
        print("1. Set root path")
        print("2. Toggle case sensitivity")
        print("3. Set page size")
        print("4. Set allowed file extensions")
        print("5. Manage bookmarks")
        print("0. Back to main menu")

        choice = input("Choose option: ").strip()
        if choice == "1":
            path = input("Enter new root path: ").strip()
            if set_root_path(path):
                print("✅ Root path updated")
            else:
                print("❌ Invalid path")

        elif choice == "2":
            toggle_case_sensitive()
            print(f"Case sensitivity set to {config['case_sensitive']}")

        elif choice == "3":
            try:
                size = int(input("Enter display size (3-20): "))
                if set_page_size(size):
                    print("✅ Page size updated")
                else:
                    print("❌ Invalid size")
            except ValueError:
                print("❌ Please enter a number")

        elif choice == "4":
            exts = input("Enter extensions separated by commas (e.g., .txt,.pdf): ")
            set_allowed_extensions([e.strip() for e in exts.split(",") if e.strip()])
            print("✅ Extensions updated")

        elif choice == "5":
            manage_bookmarks()

        elif choice == "0":
            break

        else:
            print("❌ Invalid choice")


def manage_bookmarks() -> None:
    """
    `manage_bookmarks` provides an interactive menu for managing bookmarks within the application.

    Behavior:
        - Continuously displays a menu until the user chooses to go back.
        - Bookmarks are stored in config["bookmarks"], a dictionary mapping
        bookmark names to filesystem paths.
    Menu options:
            1. List bookmarks:
                Displays all saved bookmarks with their names and paths.
            2. Add bookmark:
                Prompts the user for a bookmark name and path. 
                Calls add_bookmark() to validate and store it.
            3. Remove bookmark:
                Prompts the user for a bookmark name and calls remove_bookmark()
                to delete it from config.
            0. Back:
                Exits the bookmark management menu and returns to the caller.

    Returns:
        None. Prints menu options and results directly to the console.
    """
    while True:
        print("\n--- Bookmark Management ---")
        print("1. List bookmarks")
        print("2. Add bookmark")
        print("3. Remove bookmark")
        print("0. Back")

        choice = input("Choose option: ").strip()
        if choice == "1":
            if config["bookmarks"]:
                for name, path in config["bookmarks"].items():
                    print(f"{name}: {path}")
            else:
                print("No bookmarks yet.")

        elif choice == "2":
            name = input("Enter bookmark name: ").strip()
            path = input("Enter bookmark path: ").strip()
            if add_bookmark(name, path):
                print("✅ Bookmark added")
            else:
                print("❌ Invalid path")

        elif choice == "3":
            name = input("Enter bookmark name to remove: ").strip()
            if remove_bookmark(name):
                print("✅ Bookmark removed")
            else:
                print("❌ No such bookmark")

        elif choice == "0":
            break
        else:
            print("❌ Invalid choice")


def search_flow() -> None:
    """
    `search_flow` handles the interactive search process for files and directories (folders).
    Workflow:
        1. Prompt the user to enter a search term.
        2. Validate that the term is not empty; if empty, exit early with an error message.
        3. Perform a search using `find_files()` with the given term.
        4. If results are found, display them with pagination using `paginate_display()`.
        5. If no results are found, notify the user.

    Returns:
        None. All interactions and results are printed to the console.
    """
    term = input("Enter search term: ").strip()
    if not term:
        print("❌ Search term cannot be empty")
        return

    results = find_files(term)
    if results:
        paginate_display(results)
    else:
        print("❌ No results found")
