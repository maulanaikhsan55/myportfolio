#!/usr/bin/env python3
"""
Portfolio Content Updater
Replaces template content with your personal information
"""

import os
import re
from pathlib import Path

# Configuration
REPLACEMENTS = {
    # Email
    'mailto:uxmushfq@gmail.com': 'mailto:maulanamuhammadikhsanxap2@gmail.com',
    'uxmushfq@gmail.com': 'maulanamuhammadikhsanxap2@gmail.com',
    
    # Page Title
    'Portfolica - Personal Portfolio Website Template': 'Maulana Muhammad Ikhsan - Finance Automation & Full-Stack Developer',
    
    # Meta Description
    'Personal portfolio website, showcasing selected projects, case studies, and professional experience in design and development.': 
    'Finance automation specialist and full-stack developer. Building production-grade ERP integrations, reconciliation systems, and SaaS platforms. Laravel, React, TypeScript, Python.',
    
    # Calendar/Booking Link
    'https://cal.com': 'mailto:maulanamuhammadikhsanxap2@gmail.com',
    
    # Domain
    'https://portfolica.framer.website': 'https://maulanaikhsan.vercel.app',
    'portfolica.framer.website': 'maulanaikhsan.vercel.app',
}

def update_file(file_path):
    """Update a single file with replacements"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Apply all replacements
        for old, new in REPLACEMENTS.items():
            content = content.replace(old, new)
        
        # Only write if content changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error updating {file_path}: {e}")
        return False

def main():
    """Main function to update all HTML files"""
    base_dir = Path(__file__).parent
    
    # Files to update
    files_to_update = [
        'index.html',
        'about',
        'contact',
        'all-projects',
        'legal/privacy-policy',
        'legal/terms-conditions',
        'project-details/tomoro-bridging',
        'project-details/zeirec',
        'project-details/api-bank-reconcile',
        'project-details/duckcost',
        'project-details/agriduck',
        'project-details/cellupay',
    ]
    
    print("=" * 60)
    print("Portfolio Content Updater")
    print("=" * 60)
    print()
    
    updated_count = 0
    
    for file_path in files_to_update:
        full_path = base_dir / file_path
        if full_path.exists():
            if update_file(full_path):
                print(f"✓ Updated: {file_path}")
                updated_count += 1
            else:
                print(f"- No changes: {file_path}")
        else:
            print(f"✗ Not found: {file_path}")
    
    print()
    print("=" * 60)
    print(f"Summary: {updated_count} files updated")
    print("=" * 60)
    print()
    print("Next steps:")
    print("1. Review changes in your browser")
    print("2. Commit: git add . && git commit -m 'Update: Personal information'")
    print("3. Push: git push")
    print("4. Deploy to Vercel!")
    print()

if __name__ == '__main__':
    main()
