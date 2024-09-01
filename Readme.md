# Directory Tree Script

This script generates a visual representation of the directory structure of a specified root directory. It supports exporting the structure to a Markdown file and offers various options to customize the output.

## Features

- **Visual Directory Tree**: Display the directory structure in a tree-like format.
- **Export to Markdown**: Save the directory structure to a Markdown file for documentation purposes.
- **Depth Limiting**: Limit the depth of directory traversal to avoid overwhelming outputs for deep directory structures.
- **Colorful Output**: Colorize the terminal output to differentiate directories from files.

## Installation

1.  Ensure you have Python installed (version 3.6 or later recommended).
2.  Install the required Python packages:

        ```bash
        pip install colorama
        ```

    (just need in -c switch for colorful, you don't need install package for run the script)

## Command-Line Switches

| Switch/Option      | Description                                                     | Example Usage                              |
| ------------------ | --------------------------------------------------------------- | ------------------------------------------ |
| `<directory-path>` | Path to the root directory whose structure you want to display. | `python main.py /home/project`             |
| `--export-md`      | Export the directory structure to a Markdown file.              | `python main.py /home/project --export-md` |
| `--depth <number>` | Limit the depth of directory traversal.                         | `python main.py /home/project --depth 2`   |
| `--verbose`        | Enable verbose logging for detailed output.                     | `python main.py /home/project --verbose`   |
| `-c`, `--color`    | Enable colorful output in the terminal.                         | `python main.py /home/project -c`          |

## Examples

1. **Display the Directory Structure**

   ```bash
   python main.py /home/project
   ```

2. **Export to Markdown**

   ```bash
   python main.py /home/project --export-md
   ```

3. **Limit Depth to 2 Levels**

   ```bash
   python main.py /home/project --depth 2
   ```

4. **Enable Verbose Logging**

   ```bash
   python main.py /home/project --verbose
   ```

5. **Enable Colorful Output**

   ```bash
   python main.py /home/project -c
   ```

6. **Combine Options**

   ```bash
   python main.py /home/project --export-md --depth 3 -c
   ```

### Notes

- **Colorful Output**: The `-c` or `--color` switch enables colorful terminal output using `colorama`. Without this switch, the output will be plain text.
- **Depth Limiting**: Use the `--depth` option to control how many levels deep the directory tree should be displayed.
- **Verbose Mode**: The `--verbose` option provides more detailed logging information during script execution.
- **Markdown Export**: The `--export-md` option saves the directory structure to a Markdown file for documentation purposes.

For any additional options or troubleshooting, please refer to the [Troubleshooting](#troubleshooting) section of this documentation.

### Troubleshooting

- Permission Errors: If you encounter permission errors, make sure you have the necessary permissions to access the directories and files.
- Invalid Directory Path: Ensure the specified directory path is correct and exists.

### License

This script is provided under the MIT License. See the LICENSE file for more information.

### Contributing

Feel free to submit issues, suggestions, or pull requests. Contributions are welcome!
