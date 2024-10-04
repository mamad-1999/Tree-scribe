<p align="center">
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-blue"></a>
  <a href="https://github.com/mamad-1999/Tree-scribe/issues"><img src="https://img.shields.io/github/issues/mamad-1999/Tree-scribe"></a>
  <a href="https://github.com/mamad-1999/Tree-scribe/blob/master/LICENSE"><img src="https://img.shields.io/github/license/mamad-1999/Tree-scribe"></a>
</p>
<h4 align="center">This script generates a visual representation of the directory structure of a specified root directory. It supports exporting the structure to a Markdown file and offers various options to customize the output.</h4>
<p align="center">
  <a href="#installation"><img src="https://img.shields.io/badge/Install-blue?style=for-the-badge" alt="Install"></a>
  <a href="#usage"><img src="https://img.shields.io/badge/Usage-green?style=for-the-badge" alt="Usage"></a>
  <a href="#commands"><img src="https://img.shields.io/badge/Commands-red?style=for-the-badge" alt="Commands"></a>
  <a href="#output"><img src="https://img.shields.io/badge/Output-orange?style=for-the-badge" alt="Output"></a>
  <a href="#troubleshooting"><img src="https://img.shields.io/badge/Troubleshooting-aqua?style=for-the-badge" alt="Troubleshooting"></a>
  <a href="#contributing"><img src="https://img.shields.io/badge/Contributing-yellow?style=for-the-badge" alt="Contributing"></a>
</p>

### Output

```
├── .env
├── .gitignore
├── README.md
├── config/
│   ├── env.go
├── data/
│   ├── found-url.json
│   ├── url.txt
├── db/
│   ├── db.go
├── directory_structure.md
├── go.mod
├── go.sum
├── main.go
├── rss/
│   ├── fetch.go
├── telegram/
│   ├── telegram.go
├── utils/
    ├── http.go
    ├── utils.go
```

### Installation

1.  Ensure you have Python installed (version 3.6 or later recommended).
2.  Install the required Python packages:
   ```bash
   pip install colorama
```
> [!NOTE]
> Just need in -c switch for colorful, you don't need install package for run the script
    

### Commands

| Switch/Option            | Description                                                     | Example Usage                       |
| ------------------------ | --------------------------------------------------------------- | ----------------------------------- |
| `<directory-path>`       | Path to the root directory whose structure you want to display. | `python main.py /home/project`      |
| `-md`, `--export-md`     | Export the directory structure to a Markdown file.              | `python main.py /home/project -md`  |
| `-d`, `--depth <number>` | Limit the depth of directory traversal.                         | `python main.py /home/project -d 2` |
| `-c`, `--color`          | Enable colorful output in the terminal.                         | `python main.py /home/project -c`   |

### Usage

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
4. **Enable Colorful Output**

   ```bash
   python main.py /home/project -c
   ```

5. **Combine Options**

   ```bash
   python main.py /home/project --export-md --depth 3 -c
   ```
> [!NOTE]
> - **Colorful Output**: The `-c` or `--color` switch enables colorful terminal output using `colorama`. Without this switch, the output will be plain text.
> - **Depth Limiting**: Use the `--depth` option to control how many levels deep the directory tree should be displayed.
> - **Markdown Export**: The `--export-md` option saves the directory structure to a Markdown file for documentation purposes.
> 
> For any additional options or troubleshooting, please refer to the [Troubleshooting](#troubleshooting) section of this documentation.

### Troubleshooting

- Permission Errors: If you encounter permission errors, make sure you have the necessary permissions to access the directories and files.
- Invalid Directory Path: Ensure the specified directory path is correct and exists.

### Contributing

Feel free to submit issues, suggestions, or pull requests. Contributions are welcome!

> [!TIP]
> ### Summary of Additions
> - **Customizing Filters**: Instructions for modifying the `filters.py` file to include or exclude specific directories from the output.
> - **Adding/Removing Folders**: Clear steps on how to update the `EXCLUDED_DIRECTORIES` list.


