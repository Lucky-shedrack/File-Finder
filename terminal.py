from pathlib import Path

# Global configuration dictionary
config: dict[str, object] = {
    "root_path": str(Path.home() / "Documents"),
    "case_sensitive": True,
    "page_size": 10,
    "allowed_extensions": [],  
    "bookmarks": {}           
}


def set_root_path(path: str) -> bool:
    """
    `set_root_path` updates the root search path in the configuration.

    Args:
        path (str): A filesystem path to set as the root directory.

    Returns:
        bool: True if the path exists and is a valid directory, if otherwise returns false.
    """
    p = Path(path)
    if p.exists() and p.is_dir():
        config["root_path"] = str(p)
        return True
    return False


def toggle_case_sensitive() -> None:
    """
    `toggle_case_sensitive` changes the case sensitivity setting. It changes the global configuration value for case sensitivity from True to False, or from False to True.
    """
    config["case_sensitive"] = not config["case_sensitive"]


def set_page_size(size: int) -> bool:
    """
    `set_page_size` updates the number of results displayed per page.

    Args:
        size (int): Desired page size. Must be between 4 and 25.

    Returns:
        bool: True if the size was valid and updated, False if otherwise.
    """
    if 4 <= size <= 25:
        config["page_size"] = size
        return True
    return False


def set_allowed_extensions(exts: list[str]) -> None:
    """
    `set_allowed_extensions` updates the list of allowed file extensions.

    Args:
        exts (list[str]): A list of file extensions (e.g., [".txt", ".pdf"]).
        Whitespace is stripped and extensions are normalized to lowercase.
    """
    config["allowed_extensions"] = [e.lower().strip() for e in exts if e.strip()]


def add_bookmark(name: str, path: str) -> bool:
    """
    `add_bookmark` adds a bookmark mapping a name to a directory path.

    Args:
        name (str): The bookmark label.
        path (str): The directory path to associate with the bookmark.

    Returns:
        bool: True if the path exists and is a valid directory, False if otherwise.
    """
    p = Path(path)
    if p.exists() and p.is_dir():
        config["bookmarks"][name] = str(p)
        return True
    return False


def remove_bookmark(name: str) -> bool:
    """
    `remove_bookmark` removes a bookmark by its name.

    Args:
        name (str): The bookmark label to remove.

    Returns:
        bool: True if the bookmark existed and was removed, False if no such bookmark was found.
    """
    return config["bookmarks"].pop(name, None) is not None
