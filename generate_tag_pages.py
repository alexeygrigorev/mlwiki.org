#!/usr/bin/env python3
"""
Script to generate tag pages for Jekyll site.
This creates individual tag pages that work with GitHub Pages.
"""

import os
import yaml
from pathlib import Path

def extract_tags_from_files():
    """Extract all unique tags from markdown files"""
    tags = set()
    
    # Look for markdown files in index.php directory
    index_php_dir = Path("index.php")
    if not index_php_dir.exists():
        print("index.php directory not found")
        return tags
    
    for md_file in index_php_dir.glob("*.md"):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract frontmatter
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 2:
                    frontmatter = yaml.safe_load(parts[1])
                    if frontmatter and 'tags' in frontmatter:
                        file_tags = frontmatter['tags']
                        if isinstance(file_tags, list):
                            tags.update(file_tags)
                        elif isinstance(file_tags, str):
                            tags.add(file_tags)
        except Exception as e:
            print(f"Error processing {md_file}: {e}")
    
    return sorted(tags)

def create_tag_page(tag):
    """Create a tag page for the given tag"""
    tag_dir = Path("tag")
    tag_dir.mkdir(exist_ok=True)
    
    tag_file = tag_dir / f"{tag}.html"
    
    content = f"""---
layout: tag
tag: {tag}
permalink: /tag/{tag}/
---
"""
    
    with open(tag_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created tag page: {tag_file}")

def main():
    print("Extracting tags from markdown files...")
    tags = extract_tags_from_files()
    
    print(f"Found {len(tags)} unique tags")
    
    print("Creating tag pages...")
    for tag in tags:
        create_tag_page(tag)
    
    print("Done!")
    print(f"Created {len(tags)} tag pages in the 'tag' directory")

if __name__ == "__main__":
    main()