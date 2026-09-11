# BookBot

A Python command-line tool that analyzes a `.txt` file and reports word count and character frequency statistics.

> Built while completing [Boot.dev](https://www.boot.dev)'s Python fundamentals course. This is a guided learning project, not an original analysis.

## What it does
- Reads a `.txt` file from a `Books/` subfolder
- Counts the total number of words in the file
- Tallies the frequency of each letter (case-insensitive) and sorts results from most to least common
- Outputs a formatted report to the console

## Tools
Python (standard library only — no external dependencies)

## What I practiced
- File I/O and reading text data
- Functions and control flow
- Working with dictionaries for frequency counts
- Sorting and formatting output for readability
- Basic project structure (separating logic across files)

## How to run
1. Place a `.txt` file inside a `Books/` folder in the project directory
2. Run the script, passing the filename:
```bash
python3 main.py Books/your_file.txt
```
3. View the word count and character frequency report printed to the console

## Repo Structure
```
├── Books/          # place .txt files here (not included in repo)
├── main.py
├── stats.py
└── README.md
```
