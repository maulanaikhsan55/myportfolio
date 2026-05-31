#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
COMPLETE PORTFOLIO CONTENT REPLACEMENT
Replaces ALL Framer template content with professional CV content
Based on Maulana Muhammad Ikhsan's CV
"""

import os
import re
from pathlib import Path

# ============================================================================
# PROFESSIONAL CONTENT FROM CV
# ============================================================================

REPLACEMENTS = {
    # ========== NAMES ==========
    r'\bAlex\s+Morgan\b': 'Maulana Ikhsan',
    r'\bAlex\b(?!\s*Morgan)': 'Maulana',
    r'\bMorgan\b(?<!Alex\s)': 'Ikhsan',
    r'"Alex"': '"Maulana"',
    r'"Morgan"': '"Ikhsan"',
    r'>Alex<': '>Maulana<',
    r'>Morgan<': '>Ikhsan<',
    
    # ========== PROFESSIONAL TITLES ==========
    r'Product Designer': 'Finance Automation Developer',
    r'UI/UX Designer': 'Finance Automation Developer',
    r'Creative Designer': 'Finance Automation Developer',
    r'Visual designer': 'Finance Automation Developer',
    r'Digital Designer': 'Finance Automation Developer',
    
    # ========== HERO SECTION ==========
    r'I build digital experiences that drive real growth for your business\. Let\'s partner to create work that gets results\.': 
        'Accounting Information Systems student (GPA 3.81/4.00) with hands-on experience delivering production-grade finance automation systems, ERP integrations, and reconciliation workflows.',
    
    r'I build digital experiences that drive real growth for your business\.':
        'I build production-grade finance automation systems and ERP integrations.',
    
    r'Helped 120\+ businesses & counting':
        'GPA 3.81/4.00 - Telkom University',
    
    r'4\.9\s*/\s*5':
        '3.81/4.00',
    
    r'4\.9/5':
        '3.81/4.00',
    
    # ========== ABOUT SECTION ==========
    r'who builds digital experiences\s*that drive real growth':
        'specializing in finance automation systems and ERP integrations',
    
    # ========== CONTACT ==========
    r'uxmushfq@gmail\.com': 'maulanamuhammadikhsanxap2@gmail.com',
    r'Book a 30 min call': 'Email Me',
    r'https://cal\.com': 'mailto:maulanamuhammadikhsanxap2@gmail.com',
    
    # ========== PROJECT NAMES ==========
    r'\bConnecto\b': 'Tomoro Bridging Internal',
    r'\bEdunova\b': 'Zeirec',
    r'\bMedilink\b': 'API Bank Reconcile',
    r'\bPaynest\b': 'DuckCost',
    r'\bShopora\b': 'AgriDuck',
    r'\bTravelio\b': 'CelluPay',
    
    # ========== GENERIC FRAMER CONTENT ==========
    r'Portfolica': 'Maulana Ikhsan',
    r'This is a Framer template': 'Professional Portfolio',
    
    # ========== DESCRIPTIONS - Remove generic design content ==========
    r'digital experiences': 'finance automation systems',
    r'design solutions': 'automation solutions',
    r'creative work': 'technical solutions',
    
    # ========== STATS ==========
    r'120\+': '7+',
    r'businesses': 'projects',
    
    # ========== CAREER/EXPERIENCE ==========
    r'Healthcare': 'Finance',
    r'E-commerce': 'ERP Systems',
    r'Education': 'Accounting',
    r'Finance': 'Finance Automation',
    r'Travel': 'Banking',
    
    # ========== SKILLS - Remove design-related, add tech ==========
    r'Figma': 'Laravel',
    r'Sketch': 'React',
    r'Adobe XD': 'TypeScript',
    r'Photoshop': 'PostgreSQL',
    r'Illustrator': 'Python',
    
    # ========== TESTIMONIALS - Remove or replace ==========
    r'Working with Alex was amazing': 'Professional finance automation developer',
    r'Alex delivered': 'Delivered',
    r'highly recommend Alex': 'highly skilled developer',
    
    # ========== PROCESS/METHODOLOGY ==========
    r'Design thinking': 'Agile development',
    r'User research': 'Requirements analysis',
    r'Wireframing': 'System design',
    r'Prototyping': 'Development',
    r'Usability testing': 'QA testing',
    
    # ========== CALL TO ACTION ==========
    r'Start a Project': 'Contact Me',
    r'Let\'s work together': 'Let\'s discuss your project',
    r'Get in touch': 'Email me',
    
    # ========== FOOTER/NEWSLETTER ==========
    r'design discounts': 'project updates',
    r'design tips': 'tech insights',
    
    # ========== SOCIAL LINKS - Keep generic ones ==========
    r'https://dribbble\.com': 'https://github.com/maulanaikhsan55',
    r'https://behance\.net': 'https://linkedin.com/in/maulanamuhammadikhsan',
    
    # ========== PLACEHOLDER TEXT ==========
    r'Jane Smith': 'Your Name',
    r'jane@brand\.com': 'your.email@example.com',
    r'Tell us about your next project': 'Tell me about your project',
    
    # ========== AWARDS/RECOGNITION ==========
    r'Awwwards': 'Innovillage 2024',
    r'CSS Design Awards': 'National Finalist',
    r'FWA': 'Top 165/750+',
    
    # ========== YEARS OF EXPERIENCE ==========
    r'10\+ years': '2+ years',
    r'8\+ years': '2+ years',
    r'5\+ years': '2+ years',
    
    # ========== CLIENT/COMPANY NAMES - Generic ones ==========
    r'Google': 'PT Pengembang Sistem Manajemen',
    r'Apple': 'Bank Mandiri',
    r'Microsoft': 'Telkom University',
    r'Amazon': 'Tomoro Coffee',
    
    # ========== SERVICES ==========
    r'Brand Identity': 'ERP Integration',
    r'Web Design': 'Web Development',
    r'Mobile Design': 'API Development',
    r'UI/UX Design': 'Finance Automation',
    
    # ========== PROCESS STEPS ==========
    r'Discovery': 'Requirements',
    r'Strategy': 'Planning',
    r'Design': 'Development',
    r'Development': 'Implementation',
    r'Launch': 'Deployment',
    
    # ========== METRICS ==========
    r'100%': '100%',  # Keep percentages
    r'\$1M\+': 'Rp14,000,000',
    r'\$500K': 'Production systems',
    
    # ========== EDUCATION/CREDENTIALS ==========
    r'Bachelor of Design': 'Diploma 3 in Accounting Information Systems',
    r'Master of Arts': 'Telkom University',
    
    # ========== TOOLS/SOFTWARE ==========
    r'After Effects': 'FastAPI',
    r'Principle': 'PostgreSQL',
    r'InVision': 'Postman',
    r'Zeplin': 'Railway',
    
    # ========== INDUSTRY TERMS ==========
    r'user experience': 'system integration',
    r'user interface': 'API development',
    r'visual design': 'backend development',
    r'interaction design': 'workflow automation',
    
    # ========== PORTFOLIO SPECIFIC ==========
    r'Case Study': 'Project Details',
    r'View Project': 'View Details',
    r'See More Work': 'See All Projects',
    
    # ========== TESTIMONIAL SOURCES ==========
    r'CEO at TechCorp': 'Finance Team Lead',
    r'Founder of StartupX': 'Project Manager',
    r'Director of Design': 'Technical Lead',
    
    # ========== LOCATION ==========
    r'San Francisco': 'Bandung',
    r'New York': 'Jakarta',
    r'Los Angeles': 'Indonesia',
    r'London': 'Bandung',
    
    # ========== TIME/DURATION ==========
    r'2020 - Present': '2023 - Present',
    r'2018 - 2020': '2024 - 2026',
    
    # ========== CONTACT FORM ==========
    r'What\'s your budget\?': 'What type of project?',
    r'What\'s your timeline\?': 'When do you need it?',
    
    # ========== FAQ CONTENT ==========
    r'How do we get started\?': 'How do we get started?',
    r'Can you redesign my existing website or app\?': 'Can you help with ERP integration?',
    r'Do you offer frontend development or just design\?': 'What technologies do you use?',
    r'What tools do you use for design\?': 'What is your tech stack?',
    
    # ========== PRICING/PACKAGES ==========
    r'Starting at \$5,000': 'Contact for pricing',
    r'Starting at \$10,000': 'Contact for pricing',
    r'\$\d+': 'Contact for quote',
    
    # ========== AVAILABILITY ==========
    r'Available for freelance': 'Open to opportunities',
    r'Currently booked': 'Available',
    r'Taking on new clients': 'Open for projects',
}

# ============================================================================
# ADDITIONAL SPECIFIC CONTENT REPLACEMENTS
# ============================================================================

SPECIFIC_REPLACEMENTS = {
    # Hero descriptions that need complete replacement
    'digital experiences that drive real growth for your business': 
        'production-grade finance automation systems, ERP integrations, and reconciliation workflows',
    
    # About section
    'passionate about creating beautiful and functional designs':
        'specialized in building finance automation systems and ERP integrations',
    
    'help businesses grow through design':
        'help businesses automate their finance operations',
    
    # Services
    'I offer a range of design services':
        'I offer finance automation and development services',
    
    # Process
    'My design process':
        'My development process',
    
    # CTA
    'Ready to start your project':
        'Ready to automate your finance operations',
    
    # Footer
    'Subscribe to get early access to special offers, design discounts':
        'Subscribe to get updates on finance automation and tech insights',
}

# ============================================================================
# FILE PROCESSING
# ============================================================================

def apply_replacements(content):
    """Apply all replacements to content"""
    # First apply regex replacements
    for pattern, replacement in REPLACEMENTS.items():
        content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
    
    # Then apply specific string replacements (case-insensitive)
    for old_text, new_text in SPECIFIC_REPLACEMENTS.items():
        # Case-insensitive replacement
        content = re.sub(re.escape(old_text), new_text, content, flags=re.IGNORECASE)
    
    return content

def process_file(file_path):
    """Process a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        content = apply_replacements(content)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8', newline='') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def find_html_files(base_dir):
    """Find all HTML files including those without extension"""
    html_files = []
    
    # Find .html files
    html_files.extend(Path(base_dir).rglob('*.html'))
    
    # Find HTML files without extension
    for item in Path(base_dir).rglob('*'):
        if item.is_file() and not item.suffix:
            try:
                with open(item, 'r', encoding='utf-8') as f:
                    first_line = f.readline().lower()
                    if '<!doctype html>' in first_line or '<html' in first_line:
                        html_files.append(item)
            except:
                pass
    
    return html_files

# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    print("=" * 80)
    print("COMPLETE PORTFOLIO CONTENT REPLACEMENT")
    print("Replacing ALL Framer content with CV-based professional content")
    print("=" * 80)
    print()
    
    base_dir = Path(__file__).parent
    print(f"Base directory: {base_dir}")
    print()
    
    # Find all HTML files
    print("Finding HTML files...")
    html_files = find_html_files(base_dir)
    print(f"Found {len(html_files)} HTML files")
    print()
    
    # Process each file
    print("Processing files...")
    print("-" * 80)
    updated_files = []
    
    for html_file in html_files:
        print(f"Processing: {html_file.name}")
        if process_file(html_file):
            updated_files.append(str(html_file))
            print(f"  ✓ Updated")
        else:
            print(f"  - No changes")
    
    print()
    print("=" * 80)
    print("REPLACEMENT COMPLETE")
    print("=" * 80)
    print(f"Total files updated: {len(updated_files)}")
    print()
    
    if updated_files:
        print("Updated files:")
        for file in updated_files:
            print(f"  - {Path(file).name}")
    
    print()
    print("✓ All Framer template content replaced with professional CV content")
    print("✓ Names: Alex Morgan → Maulana Ikhsan")
    print("✓ Title: Product Designer → Finance Automation Developer")
    print("✓ Descriptions: Design → Finance Automation")
    print("✓ Projects: Updated to real projects from CV")
    print("✓ Contact: Updated email and links")
    print("✓ Skills: Updated to technical skills")
    print("✓ All generic content removed/replaced")
    print()
    print("Next steps:")
    print("1. Test locally: http://localhost/portfolica.framer.website")
    print("2. Hard refresh: Ctrl + Shift + R")
    print("3. Check all pages: Home, About, Projects, Contact")
    print("4. Verify all content is professional and accurate")
    print("5. Commit and push to GitHub")
    print()

if __name__ == "__main__":
    main()
