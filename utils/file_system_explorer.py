# https://github.com/rahulbordoloi/Directory-Tree/


"""
    Module file_system_explorer provides functionality to display directory tree structure.
    Uses directory_tree package to explore and visualize file system hierarchies.
"""

from typing import List, Optional, Union, Dict
from directory_tree import DisplayTree
import os


def display_directory_tree(
    dir_path: str = '',
    string_rep: bool = False,
    header: bool = False,
    max_depth: float = float('inf'),
    show_hidden: bool = False,
    ignore_list: Optional[List[str]] = None,
    only_files: bool = False,
    only_dirs: bool = False,
    sort_by: int = 0
) -> Union[str, Dict[str, List[str]], None]:
    """
    Display directory tree structure using directory_tree package.

    Args:
        dir_path: Root path to display tree from. Default is current directory.
        string_rep: Return string instead of printing. Default False.
        header: Show OS and path info header. Default False.
        max_depth: Maximum depth to traverse. Default infinite.
        show_hidden: Show hidden files/dirs. Default False.
        ignore_list: List of patterns to ignore. Default None.
        only_files: Show only files. Default False.
        only_dirs: Show only directories. Default False.
        sort_by: Sort order (0=default, 1=files first, 2=dirs first). Default 0.

    Returns:
        String representation if string_rep=True, 
        Dictionary with files and directories if string_rep=False,
        None otherwise.
    """
    tree_output = DisplayTree(
        dirPath=dir_path,
        stringRep=string_rep,
        header=header,
        maxDepth=max_depth,
        showHidden=show_hidden,
        ignoreList=ignore_list,
        onlyFiles=only_files,
        onlyDirs=only_dirs,
        sortBy=sort_by
    )

    if not string_rep:
        files: List[str] = []
        directories: List[str] = []

        for root, dirs, filenames in os.walk(dir_path or os.getcwd()):
            if max_depth != float('inf'):
                depth = root[len(dir_path):].count(os.sep)
                if depth >= max_depth:
                    continue

            if ignore_list:
                dirs[:] = [d for d in dirs if d not in ignore_list]
                filenames = [f for f in filenames if f not in ignore_list]

            if not show_hidden:
                dirs[:] = [d for d in dirs if not d.startswith('.')]
                filenames = [f for f in filenames if not f.startswith('.')]

            if not only_files:
                directories.extend([os.path.join(root, d) for d in dirs])
            if not only_dirs:
                files.extend([os.path.join(root, f) for f in filenames])

        return {
            "files": files,
            "directories": directories
        }

    return tree_output


def main() -> None:
    """Test directory tree display functionality"""
    # Basic usage - current directory
    print("\nBasic directory tree:")
    display_directory_tree()

    # With header
    print("\nDirectory tree with header:")
    display_directory_tree(header=True)

    # Only files
    print("\nOnly files:")
    display_directory_tree(only_files=True)

    # Only directories
    print("\nOnly directories:")
    display_directory_tree(only_dirs=True)

    # Limited depth
    print("\nLimited to depth 2:")
    display_directory_tree(max_depth=2)

    # Get string representation
    print("\nString representation:")
    tree_str: str = display_directory_tree(string_rep=True)
    print(tree_str)

    # With ignore list
    print("\nIgnoring .git and __pycache__:")
    display_directory_tree(ignore_list=['.git', '__pycache__'])

    # Get dictionary of files and directories
    print("\nDictionary representation:")
    tree_dict: Dict[str, List[str]] = display_directory_tree()
    print("Files:", tree_dict["files"])
    print("Directories:", tree_dict["directories"])


if __name__ == '__main__':
    main()
