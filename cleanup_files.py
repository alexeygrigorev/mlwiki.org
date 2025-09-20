#!/usr/bin/env python3
"""
Script to clean up Jekyll markdown files:
1. Remove duplicate H1 titles that match frontmatter title
2. Convert MediaWiki-style categories to Jekyll tags
"""

import os
import re
import yaml
from pathlib import Path

def process_file(file_path):
    """Process a single markdown file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        print(f"  Encoding error, skipping: {file_path}")
        return False
    
    # Split frontmatter and content
    if not content.startswith('---'):
        return False
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False
    
    frontmatter_str = parts[1]
    body = parts[2]
    
    # Parse frontmatter
    try:
        frontmatter = yaml.safe_load(frontmatter_str)
    except yaml.YAMLError as e:
        print(f"  YAML error in {file_path}: {e}")
        return False
    
    if not frontmatter:
        frontmatter = {}
    
    # Get title from frontmatter
    title = frontmatter.get('title', '').strip('"\'')
    
    changed = False
    
    # 1. Remove duplicate H1 title
    if title:
        # Look for H1 that matches the title (allowing for some variation)
        h1_pattern = rf'^#\s+{re.escape(title)}\s*$'
        if re.search(h1_pattern, body, re.MULTILINE):
            body = re.sub(h1_pattern, '', body, count=1, flags=re.MULTILINE)
            body = body.lstrip('\n')  # Remove leading newlines
            changed = True
    
    # 2. Find and extract categories - improved pattern
    # Handle both Category_Name and Category:Name patterns
    category_patterns = [
        r'\[Category:([^\]]+)\]\(Category_[^\)]*\)',  # [Category:Name](Category_Name)
        r'\[Category:([^\]]+)\]\(Category[^\)]*\)',   # [Category:Name](Category)
    ]
    
    all_categories = []
    for pattern in category_patterns:
        categories = re.findall(pattern, body)
        all_categories.extend(categories)
        # Remove category links from body
        body = re.sub(pattern + r'\s*', '', body)
    
    if all_categories:
        body = body.rstrip('\n') + '\n'  # Clean up trailing whitespace
        
        # Convert categories to tags
        tags = []
        for cat in all_categories:
            # Clean up category names to be valid tags
            tag = cat.replace(' ', '-').replace('_', '-').lower()
            # Remove special characters but keep Cyrillic
            tag = re.sub(r'[^\w\-\u0400-\u04FF]', '', tag)
            if tag:  # Only add non-empty tags
                tags.append(tag)
        
        # Add tags to frontmatter (merge with existing if any)
        existing_tags = frontmatter.get('tags', [])
        if not isinstance(existing_tags, list):
            existing_tags = []
        
        all_tags = existing_tags + tags
        if all_tags:
            frontmatter['tags'] = sorted(list(set(all_tags)))  # Remove duplicates and sort
            changed = True
    
    # 3. Write back if changed
    if changed:
        # Reconstruct the file
        new_frontmatter = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True)
        new_content = f"---\n{new_frontmatter}---\n{body}"
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True
    else:
        return False

def main():
    """Main function to process all markdown files in index.php directory"""
    index_php_dir = Path('index.php')
    
    if not index_php_dir.exists():
        print("Error: index.php directory not found")
        return
    
    # Find all .md files
    md_files = list(index_php_dir.glob('*.md'))
    
    if not md_files:
        print("No markdown files found in index.php directory")
        return
    
    print(f"Processing {len(md_files)} markdown files...")
    
    updated_count = 0
    
    for md_file in md_files:
        try:
            if process_file(md_file):
                updated_count += 1
        except Exception as e:
            print(f"Error processing {md_file}: {e}")
    
    print(f"Updated {updated_count} out of {len(md_files)} files")

if __name__ == "__main__":
    main()