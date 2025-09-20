import sys
import pathlib
import mwparserfromhell
import xml.etree.ElementTree as ET
import re
import markdownify
import unicodedata
from transliterate import translit
from pygments.lexers import get_lexer_by_name, guess_lexer
from pygments.util import ClassNotFound

# Ensure an argument is provided
if len(sys.argv) < 2:
    print("Usage: python transfer.py <path_to_wiki_dump.xml>")
    sys.exit(1)

# Input file from CLI
XML_DUMP_FILE = pathlib.Path(sys.argv[1])

# Output directory (ensuring `index.php` directory structure)
OUTPUT_DIR = pathlib.Path("index.php")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def sanitize_filename(title):
    """Sanitize and transliterate filenames to be ASCII-safe."""
    # Transliterate Cyrillic (or other scripts) to Latin
    title = translit(title, 'ru', reversed=True) if any(ord(c) > 127 for c in title) else title

    # Replace spaces with underscores and remove invalid characters
    title = unicodedata.normalize("NFKD", title)
    title = re.sub(r"[^\w\-_.]", "_", title)  # Keep alphanumeric, _, -, and .
    
    return title

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

    # Check regex patterns first
    for lang, patterns in LANGUAGE_PATTERNS.items():
        if any(re.search(pattern, code_sample) for pattern in patterns):
            return lang

    # Try Pygments' guess_lexer() as a fallback
    try:
        lexer = guess_lexer(code_sample)
        return lexer.name.lower()
    except ClassNotFound:
        return "text"  # Default if no match

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
        
        # Validate language
        try:
            get_lexer_by_name(lang)
        except ClassNotFound:
            lang = "text"  # Fallback if invalid
        
        return f"```{lang}\n{code}\n```"
    
    text = re.sub(r"{{code\|([^|]+)\|(.*?)}}", replace_code_template, text, flags=re.DOTALL)
    
    return text

def wiki_to_md(wiki_text):
    """Convert MediaWiki markup to GitHub-Flavored Markdown."""
    text = process_code_blocks(wiki_text)
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
            safe_filename = sanitize_filename(title)
            filename = OUTPUT_DIR / f"{safe_filename}.md"
            
            # Jekyll front matter
            front_matter = f"""---
title: "{title}"
layout: default
permalink: /index.php/{safe_filename}
---
"""

            with filename.open("w", encoding="utf-8") as f:
                f.write(front_matter + "\n" + md_content)
            
            print(f"Saved: {filename}")

# Run the script
parse_wiki_dump(XML_DUMP_FILE)

print("\n✅ Conversion completed! Markdown files are in:", OUTPUT_DIR)
