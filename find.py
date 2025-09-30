import os
from pathlib import Path
from datetime import datetime
from typing import Literal, TypedDict
from terminal import config


class FileInfo(TypedDict):
    path: str
    is_dir: bool
    size: int
    created: datetime
    modified: datetime


def find_files(term: str, sort_by: Literal["name", "size", "modified"] = "name") -> list[FileInfo]:
    """
    `find_files` prompts the user to find files and directories recursively under the configured root path
    whose names contain the given search term, with optional filtering and sorting.

    Behavior:
        - Respects the 'case_sensitive' setting in the global config dictionary.
        - Filters by allowed file extensions if 'allowed_extensions' is set.
        - Returns results including metadata such as size, creation time, and modification time.
        - Results are sorted by the specified key: "name", "size", or "modified".

    Args:
        term (str): The search term to look for in file and folder names.
        sort_by (Literal["name", "size", "modified"], optional):
            The field used to sort results. Defaults to "name".

    Returns:
        list[FileInfo]: A list of dictionaries (FileInfo objects) where each item
        contains:
            - path (str): Absolute file or directory path.
            - is_dir (bool): If the item is a directory then it is true, if it is a file then it is false.
            - size (int): shows the size of the file in bytes (0 bytes for directories).
            - created (str): Displays the date and time of file creation.
            - modified (str): Displays the date and time of when the file was last modified.
    """
    root = Path(config["root_path"])
    case_sensitive = config["case_sensitive"]
    allowed_exts = config["allowed_extensions"]

    results: list[FileInfo] = []
    term_to_match = term if case_sensitive else term.lower()

    for dirpath, dirnames, filenames in os.walk(root):
        for name in filenames + dirnames:
            check_name = name if case_sensitive else name.lower()

            file_path = Path(dirpath) / name
            if file_path.is_file():
                if allowed_exts and not any(name.lower().endswith(ext) for ext in allowed_exts):
                    continue

            if term_to_match in check_name:
                stat = file_path.stat()
                results.append({
                    "path": str(file_path),
                    "is_dir": file_path.is_dir(),
                    "size": stat.st_size,
                    "created": datetime.fromtimestamp(stat.st_ctime).strftime("%Y-%m-%d %H:%M:%S"),
                    "modified": datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
                })

    return sort_results(results, sort_by)


def sort_results(results: list[FileInfo], key: str = "name") -> list[FileInfo]:
    """
    Sort a list of search results by a specified key.

    Args:
        results (list[FileInfo]): 
            A list of dictionaries representing file or directory information.
            Each dictionary is expected to contain at least the keys:
            "path", "size", and "modified".
        key (str, optional): 
            The field to sort by. Accepted values:
                - "name": Sort alphabetically by file path (default).
                - "size": Sort by file size (largest first).
                - "modified": Sort by modification time (newest first).

    Returns:
        list[FileInfo]: 
            A new list of search results sorted according to the chosen key.
    """
    if key == "size":
        return sorted(results, key=lambda x: x["size"], reverse=True)
    elif key == "modified":
        return sorted(results, key=lambda x: x["modified"], reverse=True)
    else:
        return sorted(results, key=lambda x: x["path"].lower())
    

