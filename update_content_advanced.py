#!/usr/bin/env python3
"""
Advanced Portfolio Content Updater
Replaces all template content including names, bios, and descriptions
"""

import os
import re
from pathlib import Path

# Comprehensive replacements
REPLACEMENTS = {
    # Names
    'Alex Morgan': 'Maulana Muhammad Ikhsan',
    'alex morgan': 'maulana muhammad ikhsan',
    
    # Professional titles
    'Product Designer': 'Finance Automation Developer',
    'UX/UI Designer': 'Full-Stack Developer',
    'Digital Designer': 'Finance Automation Specialist',
    
    # Bio/Description
    'I build digital experiences that drive real growth for your business': 
    'I build finance automation systems that bridge accounting knowledge with modern software engineering',
    
    "Let's partner to create work that gets results": 
    'Specializing in ERP integrations, reconciliation workflows, and multi-tenant SaaS platforms',
    
    'Helped 120+ businesses & counting': 
    'Delivered 7+ production-grade projects',
    
    # Project-related
    'Connecto': 'Tomoro Bridging Internal',
    'Edunova': 'Zeirec',
    'Medilink': 'API Bank Reconcile',
    'Paynest': 'DuckCost',
    'Shopora': 'AgriDuck',
    'Travelio': 'CelluPay',
    
    # Contact/Social (already done but double-check)
    'mailto:uxmushfq@gmail.com': 'mailto:maulanamuhammadikhsanxap2@gmail.com',
    'uxmushfq@gmail.com': 'maulanamuhammadikhsanxap2@gmail.com',
    
    # URLs
    'https://cal.com': 'mailto:maulanamuhammadikhsanxap2@gmail.com',
    'Book a 30 min call': 'Email Me',
    'Book a call': 'Email Me',
    
    # Meta
    'Portfolica - Personal Portfolio Website Template': 
    'Maulana Muhammad Ikhsan - Finance Automation & Full-Stack Developer',
    
    'Personal portfolio website, showcasing selected projects, case studies, and professional experience in design and development.':
    'Finance automation specialist and full-stack developer. Building production-grade ERP integrations, reconciliation systems, and SaaS platforms. Laravel, React, TypeScript, Python.',
}

def update_file(file_path):
    """Update a single file with replacements"""
    try:
        # Read file
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        original_content = content
        changes_made = []
        
        # Apply all replacements
        for old, new in REPLACEMENTS.items():
            if old in content:
                count = content.count(old)
                content = content.replace(old, new)
                changes_made.append(f"  - Replaced '{old[:50]}...' ({count}x)")
        
        # Only write if content changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, changes_made
        return False, []
    except Exception as e:
        print(f"Error updating {file_path}: {e}")
        return False, []

def main():
    """Main function to update all files"""
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
    
    print("=" * 70)
    print("Advanced Portfolio Content Updater")
    print("=" * 70)
    print()
    
    updated_count = 0
    total_changes = 0
    
    for file_path in files_to_update:
        full_path = base_dir / file_path
        if full_path.exists():
            updated, changes = update_file(full_path)
            if updated:
                print(f"✓ Updated: {file_path}")
                for change in changes:
                    print(change)
                updated_count += 1
                total_changes += len(changes)
            else:
                print(f"- No changes: {file_path}")
        else:
            print(f"✗ Not found: {file_path}")
        print()
    
    print("=" * 70)
    print(f"Summary: {updated_count} files updated, {total_changes} replacements made")
    print("=" * 70)
    print()
    print("✅ Content updated successfully!")
    print()
    print("Next steps:")
    print("1. Refresh browser: http://localhost/portfolica.framer.website")
    print("2. Check if name and bio are updated")
    print("3. Commit: git add . && git commit -m 'Update: All template content'")
    print("4. Push: git push")
    print("5. Deploy to Vercel!")
    print()

if __name__ == '__main__':
    main()
