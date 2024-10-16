#!/usr/bin/python3
"""
Script that takes an argument 2 strings
"""

import sys
import os
import markdown


def convert_markdown_2html(input_file, output_file):
    """
    Converts a Markdown file into an HTML file.

    Parameters:
    input_file (str): The path to the input Markdown file.
    output_file (str): The path to the output HTML file where the converted content will be saved.

    Returns:
    None
    """
    with open(input_file, 'r') as md_file:
        markdown_txt = md_file.read()

    html = markdown.markdown(markdown_txt)

    with open(output_file, 'w') as html_file:
        html_file.write(html)


if __name__ == "__main__":
    """
    Main entry point of the script.
    """
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        print(f"Missing '{input_file}'", file=sys.stderr)
        sys.exit(1)

    convert_markdown_2html(input_file, output_file)

    sys.exit(0)
