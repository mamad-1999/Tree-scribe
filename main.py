import os
import sys
import argparse
import logging

from filters import EXCLUDED_DIRECTORIES

# Import colorama only if the -c switch is used
colorama_enabled = False
if '--color' in sys.argv or '-c' in sys.argv:
    from colorama import Fore, Style, init
    init(autoreset=True)
    colorama_enabled = True

# Set up logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Global set to track visited directories
visited_directories = set()


def get_colorama_color():
    if colorama_enabled:
        return Fore.GREEN, Fore.CYAN
    else:
        return '', ''


def print_directory_tree(root_dir, indent="", depth=None, current_depth=0):
    if depth is not None and current_depth > depth:
        return "", 0

    # Check if the current directory is a symlink
    if os.path.islink(root_dir):
        logging.debug(f"Skipping symlink: {root_dir}")
        return "", 0

    # Avoid infinite loops by checking visited directories
    if root_dir in visited_directories:
        return "", 0

    visited_directories.add(root_dir)

    try:
        items = [item for item in sorted(os.listdir(root_dir))
                 if not (os.path.isdir(os.path.join(root_dir, item)) and item in EXCLUDED_DIRECTORIES)]
    except PermissionError as e:
        logging.error(f"Permission denied: {root_dir}")
        return "", 0
    except Exception as e:
        logging.error(f"Error reading directory {root_dir}: {e}")
        return "", 0

    dir_color, file_color = get_colorama_color()
    tree_structure = ""
    file_count = 0
    for index, item in enumerate(items):
        path = os.path.join(root_dir, item)
        is_last = index == len(items) - 1
        if os.path.isdir(path):
            # Check if the directory is a symlink
            if os.path.islink(path):
                logging.debug(f"Skipping symlink directory: {path}")
                continue
            tree_structure += f"{indent}├── {dir_color}{item}/\n"
            new_indent = indent + "│   " if not is_last else indent + "    "
            subdir_structure, subdir_file_count = print_directory_tree(
                path, new_indent, depth, current_depth + 1)
            tree_structure += subdir_structure
            file_count += subdir_file_count
        else:
            tree_structure += f"{indent}├── {file_color}{item}\n"
            file_count += 1
    return tree_structure, file_count


def export_to_markdown(root_dir, tree_structure):
    md_filename = os.path.join(root_dir, "directory_structure.md")
    try:
        with open(md_filename, "w") as md_file:
            md_file.write(f"# Directory structure of {root_dir}\n\n")
            md_file.write("```\n")
            md_file.write(tree_structure)
            md_file.write("```\n")
        logging.info(f"Directory structure exported to {md_filename}")
    except Exception as e:
        logging.error(f"Error exporting to Markdown: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate and optionally export a directory tree structure.")
    parser.add_argument("directory", help="Path to the root directory")
    parser.add_argument("--export-md", action="store_true",
                        help="Export the directory structure to a Markdown file")
    parser.add_argument("--depth", type=int,
                        help="Limit the depth of directory traversal")
    parser.add_argument("--verbose", action="store_true",
                        help="Enable verbose logging")
    parser.add_argument("-c", "--color", action="store_true",
                        help="Enable colorful output")

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    root_dir = args.directory
    export_md = args.export_md
    depth = args.depth
    color = args.color

    if not os.path.isdir(root_dir):
        logging.error(
            "The provided path is not a valid directory. Please try again.")
        sys.exit(1)

    # Initialize colorama if -c or --color is used
    if color:
        global colorama_enabled
        from colorama import Fore, Style, init
        init(autoreset=True)
        colorama_enabled = True

    logging.info(f"Starting directory scan for: {root_dir}")
    tree_structure, file_count = print_directory_tree(root_dir, depth=depth)
    print(Fore.YELLOW + root_dir if color else root_dir)
    print(tree_structure)
    print(f"\n├──────── [{file_count} files]")

    if export_md:
        export_to_markdown(root_dir, tree_structure)


if __name__ == "__main__":
    main()
