import sys
import pathlib
import mwparserfromhell
import xml.etree.ElementTree as ET
import re
import markdownify
from pygments.lexers import guess_lexer
from pygments.util import ClassNotFound

# Ensure an argument is provided
if len(sys.argv) < 2:
    print("Usage: python convert_wiki_to_md.py <path_to_wiki_dump.xml>")
    sys.exit(1)

# Input file from CLI
XML_DUMP_FILE = pathlib.Path(sys.argv[1])

# Output directory (ensuring `index.php` directory structure)
OUTPUT_DIR = pathlib.Path("index.php")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def sanitize_filename(title):
    """Sanitize filenames by replacing spaces with underscores and removing invalid characters."""
    return title.replace(" ", "_").replace("/", "_").replace(":", "_")


LANGUAGE_PATTERNS = {
    "python": [r"def\s+\w+\(", r"import\s+\w+", r"print\("],
    "java": [r"public\s+class\s+\w+", r"System\.out\.println\(", r"import\s+java\.", r"public\s+void"],
    "javascript": [r"function\s+\w+\(", r"console\.log\(", r"var\s+\w+"],
    "c": [r"#include\s+<stdio.h>", r"int\s+main\("],
    "cpp": [r"#include\s+<iostream>", r"std::cout\s*<<", r"using\s+namespace\s+std"],
    "html": [r"<!DOCTYPE html>", r"<html>", r"<body>"],
    "css": [r"color:", r"background:", r"font-size:"],
    "sql": [r"SELECT\s+.*\s+FROM", r"INSERT\s+INTO", r"UPDATE\s+\w+"],
    "bash": [r"#!/bin/bash", r"echo\s+", r"ls\s+"],
    "json": [r"^\s*\{", r"^\s*\[", r"\":\s*\""]
}

def detect_language(code):
    """Detect programming language using regex patterns, explicit hints, and fallback to guess_lexer."""
    code_sample = "\n".join(code.strip().split("\n")[:5])  # First 5 lines only

    # 1️⃣ Check regex patterns
    for lang, patterns in LANGUAGE_PATTERNS.items():
        if any(re.search(pattern, code_sample) for pattern in patterns):
            return lang

    # 2️⃣ Try Pygments' guess_lexer() as a last resort
    try:
        lexer = guess_lexer(code_sample)
        return lexer.name.lower()
    except ClassNotFound:
        return "text"  # Default if nothing matches


def process_nested_lists(text):
    """Convert MediaWiki lists (*, #) into properly formatted Markdown lists."""
    lines = text.split("\n")
    output = []
    
    for line in lines:
        match = re.match(r"^([\*#]+)\s*(.*)", line)
        # match = re.match(r"^([\*]+)\s*(.*)", line)
        if match:
            markers, content = match.groups()
            level = len(markers)  # Depth of nesting
            bullet = "-" if "*" in markers else "1."
            output.append(f"{'  ' * (level - 1)}{bullet} {content}")
        else:
            output.append(line)

    return "\n".join(output)

def process_headers(text):
    """Convert MediaWiki headers (== Title ==) into proper Markdown headers (# Title)."""
    text = re.sub(r"^(=+)\s*(.*?)\s*\1$", lambda m: f"{'#' * len(m.group(1))} {m.group(2)}", text, flags=re.MULTILINE)
    return text

def process_code_blocks(text):
    """Convert <pre> and {{code|lang|...}} into GitHub-Flavored Markdown fenced code blocks."""
    
    # Convert <pre>...</pre> to fenced code blocks with language detection
    def replace_pre(match):
        code = match.group(1).strip()
        lang = detect_language(code)
        return f"```{lang}\n{code}\n```"
    
    text = re.sub(r"<pre>(.*?)</pre>", replace_pre, text, flags=re.DOTALL)

    # Convert {{code|lang|...}} to ```lang ... ```
    def replace_code_template(match):
        lang = match.group(1).strip().lower()
        code = match.group(2).strip()
        return f"```{lang}\n{code}\n```"
    
    text = re.sub(r"{{code\|([^|]+)\|(.*?)}}", replace_code_template, text, flags=re.DOTALL)
    
    return text

def process_tables(text):
    """Convert MediaWiki tables into Markdown tables."""
    text = re.sub(r"{\|.*?\n", "", text)  # Remove opening table tag
    text = re.sub(r"\|-(.*?)\n", "", text)  # Remove row separators
    text = re.sub(r"\|}.*?\n", "", text)  # Remove closing table tag
    text = re.sub(r"!(.*?)\n", lambda m: f"| {' | '.join(m.group(1).split('||'))} |", text)  # Headers
    text = re.sub(r"\|(.*?)\n", lambda m: f"| {' | '.join(m.group(1).split('||'))} |", text)  # Rows
    return text

def process_links_and_images(text):
    """Convert internal links, external links, and image links correctly."""
    # Convert [[Page]] to [Page](Page) (without .md)
    text = re.sub(r"\[\[([^\]|]+)\]\]", lambda m: f"[{m.group(1)}]({sanitize_filename(m.group(1))})", text)
    
    # Convert [[Page|Display]] to [Display](Page)
    text = re.sub(r"\[\[([^|]+)\|([^\]]+)\]\]", lambda m: f"[{m.group(2)}]({sanitize_filename(m.group(1))})", text)
    
    # Convert external links [http://example.com Description] → [Description](http://example.com)
    text = re.sub(r"\[http[s]?://([^\s]+) (.*?)\]", r"[\2](http://\1)", text)

    # Convert image URLs (only if they end with an image extension)
    text = re.sub(
        r"(http[s]?://[^\s]+?\.(?:png|jpg|jpeg|gif|svg))",
        lambda m: f'<img src="{m.group(1)}" alt="Image">',
        text
    )

    return text

def process_math(text):
    """Convert MediaWiki math tags into LaTeX-style Markdown math expressions."""
    text = text.replace("<math>", "$").replace("</math>", "$")
    return text

def wiki_to_md(wiki_text):
    """Convert MediaWiki markup to GitHub-Flavored Markdown."""

    # **First process lists so they don't interfere with headers**
    text = process_nested_lists(wiki_text)

    # **Then process headers**
    text = process_headers(text)

    # Now parse with mwparserfromhell
    wikicode = mwparserfromhell.parse(text)
    text = str(wikicode)

    # Apply other transformations
    text = process_links_and_images(text)
    text = process_math(text)
    text = process_tables(text)
    text = process_code_blocks(text)

    return text

def parse_wiki_dump(xml_file):
    """Parse MediaWiki XML dump and convert pages to Markdown."""
    tree = ET.parse(xml_file)
    root = tree.getroot()

    ns = {"mw": "http://www.mediawiki.org/xml/export-0.10/"}
    for page in root.findall("mw:page", ns):
        title = page.find("mw:title", ns).text
        revision = page.find(".//mw:revision", ns)
        text = revision.find("mw:text", ns).text if revision is not None else ""

        if text:
            md_content = wiki_to_md(text)
            filename = OUTPUT_DIR / f"{sanitize_filename(title)}.md"
            
            # Jekyll front matter
            front_matter = f"""---
title: {title}
layout: default
permalink: /index.php/{sanitize_filename(title)}
---
"""

            with filename.open("w", encoding="utf-8") as f:
                f.write(front_matter + "\n" + f"# {title}\n\n" + md_content)
            
            print(f"Saved: {filename}")

# Run the script
parse_wiki_dump(XML_DUMP_FILE)

print("\n✅ Conversion completed! Markdown files are in:", OUTPUT_DIR)
