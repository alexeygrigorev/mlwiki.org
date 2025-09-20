#!/usr/bin/env python3
"""
Script to extract all unique tags from YAML frontmatter in markdown files.
"""

import os
import re
from pathlib import Path

def extract_tags_from_file(file_path):
    """Extract tags from a single markdown file's YAML frontmatter."""
    tags = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Look for tags section in frontmatter
        in_frontmatter = False
        in_tags_section = False
        
        for line in lines:
            line = line.strip()
            
            # Start of frontmatter
            if line == '---' and not in_frontmatter:
                in_frontmatter = True
                continue
            
            # End of frontmatter
            if line == '---' and in_frontmatter:
                break
            
            # Found tags section
            if in_frontmatter and line == 'tags:':
                in_tags_section = True
                continue
            
            # If we're in tags section and line starts with '- '
            if in_frontmatter and in_tags_section and line.startswith('- '):
                tag = line[2:].strip()  # Remove '- ' prefix
                if tag and re.match(r'^[a-zA-Z0-9\-_]+$', tag):
                    tags.append(tag)
            
            # If we encounter another YAML key, we're out of tags section
            if in_frontmatter and in_tags_section and ':' in line and not line.startswith('- '):
                in_tags_section = False
    
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
    
    return tags

def main():
    """Extract all unique tags from all markdown files in index.php directory."""
    index_php_dir = Path("c:/Users/alexe/git/mlwiki.org/index.php")
    
    if not index_php_dir.exists():
        print(f"Directory {index_php_dir} does not exist!")
        return
    
    all_tags = set()
    
    # Process all .md files
    md_files = list(index_php_dir.glob("*.md"))
    print(f"Found {len(md_files)} markdown files")
    
    for md_file in md_files:
        file_tags = extract_tags_from_file(md_file)
        all_tags.update(file_tags)
    
    # Sort tags alphabetically
    sorted_tags = sorted(all_tags)
    
    print(f"\nFound {len(sorted_tags)} unique tags:")
    print("\n".join(sorted_tags))
    
    return sorted_tags

if __name__ == "__main__":
    main()