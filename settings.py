from terminal import config

def paginate_display(results: list[dict[str, object]]) -> None:
    """
    `paginate_display` displays search results in a paginated, interactive format.

    Args:
        results (list[dict[str, object]]):
            A list of dictionaries where each dictionary contains metadata about a file or directory. Expected keys include:
                - "path" (str): Absolute file/directory path.
                - "is_dir" (bool): If true, the item is a directory(folder), if false, the item is a file.
                - "size" (int): Shows the size of the file in bytes (0 bytes for directories).
                - "modified" (str): Displays the date and time of when the file was last modified.

    Behavior:
        - Displays a fixed number of results per page, defined by
        config["page_size"].
        - Provides interactive navigation:
            - 'n' → next page (if more results exist).
            - 'p' → previous page (if not on first page).
            - 'q' → quit pagination and return.
        - Results are numbered globally across all pages.

    Return:
        None
    """
    page_size = config["page_size"]
    total = len(results)
    page = 0

    while True:
        start = page * page_size
        end = start + page_size
        chunk = results[start:end]

        print(f"\n--- Results Page {page + 1} ---")
        for i, r in enumerate(chunk, start=1):
            print(
                f"{start + i}. {r['path']} | Dir: {r['is_dir']} | "
                f"Size: {r['size']} | Modified: {r['modified']}"
            )

        print("\nOptions: n=next, p=previous, q=quit")
        choice = input("Choose: ").strip().lower()
        if choice == "n" and end < total:
            page += 1
        elif choice == "p" and page > 0:
            page -= 1
        elif choice == "q":
            break
        else:
            print("Invalid choice or no more pages")
