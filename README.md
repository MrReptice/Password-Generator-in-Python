# Secure CLI Password Generator

A lightweight, zero-dependency command-line tool to generate cryptographically secure random passwords in Python. It uses Python's `random.SystemRandom()` to utilize OS-level entropy for maximum security.

## Features
* **Zero Dependencies:** Uses only built-in Python standard libraries (`random`, `string`, `argparse`).
* **Customizable Length:** Generate passwords of any length (default is 16).
* **Character Toggles:** Easily include or exclude special punctuation characters.

## Requirements
* Python 3.6+

## Usage

Run the script directly from your terminal. 

**Basic Run (Default 16 characters, includes special symbols):**
```bash
python password_gen.py
