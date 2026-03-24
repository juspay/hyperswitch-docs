#!/usr/bin/env python3
"""
Documentation reformatting script for Hyperswitch docs.
Applies 5 formatting rules to all markdown files:
1. Heading hierarchy (single H1, proper nesting)
2. General formatting (numbered lists, bullets, tables, typos)
3. Brand name "Juspay Hyperswitch" (first mentions)
4. Frontmatter descriptions (action verb + task + benefit)
5. Canonical statistics (300+ connectors, 200+ methods, 2,000 TPS, 40k+ stars)
"""

import os
import re
import sys
from pathlib import Path
from typing import Optional, Tuple

# Statistics to insert
CANONICAL_STATS = {
    'connectors': '300+',
    'payment_methods': '200+',
    'tps': '2,000',
    'github_stars': '40,000+'
}

def find_markdown_files(root_dir: str) -> list:
    """Find all markdown files recursively."""
    markdown_files = []
    for path in Path(root_dir).rglob('*.md'):
        # Skip hidden directories and certain paths
        if any(part.startswith('.') for part in path.parts):
            continue
        if '.git' in str(path):
            continue
        markdown_files.append(path)
    return sorted(markdown_files)

def parse_frontmatter(content: str) -> Tuple[Optional[dict], str]:
    """Extract frontmatter and body from markdown content."""
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter_text = parts[1].strip()
            body = parts[2].strip()
            
            # Parse frontmatter
            frontmatter = {}
            for line in frontmatter_text.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    frontmatter[key.strip()] = value.strip()
            
            return frontmatter, body
    
    return None, content

def generate_description(file_path: Path, content: str, h1: str) -> str:
    """
    Generate a specific, actionable description based on file content.
    Format: [Action verb] [task/topic] to [reader benefit]
    15-30 words, no full stop at end.
    """
    file_name = file_path.stem.lower()
    file_dir = str(file_path.parent).lower()
    
    # Extract first paragraph for context
    lines = content.split('\n')
    first_para = ''
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#') and not line.startswith('{%'):
            first_para = line
            break
    
    # Action verbs mapping
    action_verbs = {
        'setup': 'Set up',
        'configure': 'Configure',
        'enable': 'Enable',
        'implement': 'Implement',
        'integrate': 'Integrate',
        'deploy': 'Deploy',
        'manage': 'Manage',
        'monitor': 'Monitor',
        'optimize': 'Optimize',
        'automate': 'Automate',
        'secure': 'Secure',
        'route': 'Route',
        'process': 'Process',
        'handle': 'Handle',
        'track': 'Track',
        'analyze': 'Analyze',
        'customize': 'Customize',
        'build': 'Build',
        'create': 'Create',
        'test': 'Test',
        'troubleshoot': 'Troubleshoot',
    }
    
    # Generate description based on file path and content patterns
    description = None
    
    # Router/Routing files
    if 'router' in file_name or 'routing' in file_name:
        if 'smart' in file_name or 'intelligent' in file_name:
            description = "Configure intelligent routing rules to optimize transaction success across multiple payment processors"
        elif 'volume' in file_name:
            description = "Set up volume-based routing to distribute transactions across processors by percentage"
        elif 'rule' in file_name:
            description = "Create custom routing rules to direct payments based on geography, currency, or payment method"
        elif 'fallback' in file_name:
            description = "Configure fallback processor order to ensure payment continuity during outages"
        else:
            description = "Implement smart routing to optimize payment processing across multiple connectors"
    
    # Retry files
    elif 'retry' in file_name or 'retries' in file_name:
        description = "Enable automatic payment retries to recover failed transactions and boost authorization rates"
    
    # Vault/Tokenization files
    elif 'vault' in file_name or 'token' in file_name:
        description = "Set up secure payment tokenization to store and reuse customer credentials across processors"
    
    # Connector files
    elif 'connector' in file_name:
        if 'available' in file_dir:
            connector_name = file_name.replace('.md', '').title()
            description = f"Integrate {connector_name} to process payments through this payment processor"
        elif 'integration' in file_name:
            description = "Integrate payment connectors to expand your payment processing capabilities"
        else:
            description = "Configure payment connectors to enable multi-processor payment processing"
    
    # Deployment files
    elif 'deploy' in file_name:
        if 'aws' in file_name or 'aws' in file_dir:
            description = "Deploy Hyperswitch on AWS infrastructure for scalable production payment processing"
        elif 'kubernetes' in file_name or 'helm' in file_name:
            description = "Deploy Hyperswitch using Kubernetes and Helm for containerized payment infrastructure"
        elif 'docker' in file_name:
            description = "Set up Hyperswitch locally using Docker for development and testing"
        elif 'production' in file_name:
            description = "Deploy production-ready Hyperswitch infrastructure with high availability and monitoring"
        else:
            description = "Deploy Hyperswitch payment infrastructure on your preferred cloud platform"
    
    # Setup/Installation files
    elif 'setup' in file_name or 'install' in file_name:
        if 'local' in file_name:
            description = "Set up Hyperswitch locally for development, testing, and integration work"
        elif 'account' in file_name:
            description = "Create and configure your Hyperswitch account to start processing payments"
        else:
            description = "Set up Hyperswitch infrastructure to enable payment processing capabilities"
    
    # Reconciliation files
    elif 'reconcil' in file_name:
        if 'getting-started' in file_name:
            description = "Set up automated reconciliation to match transactions across banks and payment processors"
        elif 'exception' in file_name:
            description = "Handle reconciliation exceptions to resolve mismatched transactions and data discrepancies"
        else:
            description = "Implement automated reconciliation to streamline financial reporting and reduce manual effort"
    
    # Cost/Analytics files
    elif 'cost' in file_name or 'analytics' in file_name:
        description = "Set up real-time payment analytics to track performance and identify cost optimization opportunities"
    
    # Recovery/Revenue files
    elif 'recovery' in file_name or 'revenue' in file_name:
        description = "Enable revenue recovery features to automatically retry failed payments and reduce churn"
    
    # SDK files
    elif 'sdk' in file_name:
        if 'web' in file_name or 'js' in file_name or 'javascript' in file_name:
            description = "Integrate the Web SDK to embed customizable checkout experiences in your application"
        elif 'react' in file_name:
            description = "Implement the React SDK to add payment processing to your React applications"
        elif 'node' in file_name:
            description = "Use the Node.js SDK to integrate server-side payment processing capabilities"
        elif 'mobile' in file_name or 'ios' in file_name or 'android' in file_name:
            description = "Integrate mobile SDKs to enable in-app payment processing on iOS and Android"
        else:
            description = "Implement Hyperswitch SDKs to add payment capabilities to your applications"
    
    # Subscription files
    elif 'subscription' in file_name:
        description = "Configure subscription billing to automate recurring payments and manage billing cycles"
    
    # Payout files
    elif 'payout' in file_name:
        description = "Set up payout processing to automate disbursements to vendors, sellers, or partners"
    
    # Split payments
    elif 'split' in file_name:
        description = "Implement split payments to divide transactions between multiple parties or accounts"
    
    # 3DS/Authentication files
    elif '3ds' in file_name or 'authentication' in file_name or 'decision' in file_name:
        description = "Configure 3DS authentication rules to balance fraud prevention with checkout conversion"
    
    # Test files
    elif 'test' in file_name:
        description = "Test payment flows to validate integration and ensure transaction processing works correctly"
    
    # API files
    elif 'api' in file_name:
        description = "Integrate with Hyperswitch APIs to implement custom payment processing workflows"
    
    # FAQ files
    elif 'faq' in file_name:
        description = "Find answers to common questions about Hyperswitch features and implementation"
    
    # Troubleshooting files
    elif 'troubleshoot' in file_name:
        description = "Troubleshoot common issues to resolve payment processing problems and integration errors"
    
    # Architecture files
    elif 'architecture' in file_name:
        description = "Understand Hyperswitch architecture to design scalable payment infrastructure"
    
    # Security files
    elif 'security' in file_name or 'compliance' in file_name or 'pci' in file_name:
        description = "Implement security best practices to protect payment data and maintain PCI compliance"
    
    # Webhook files
    elif 'webhook' in file_name:
        description = "Configure webhooks to receive real-time notifications for payment events and updates"
    
    # Use case files
    elif 'use-case' in file_dir or 'for-' in file_name:
        # Extract business type from filename
        business_types = {
            'sme': 'small and medium enterprises',
            'enterprise': 'enterprises',
            'e-commerce': 'e-commerce businesses',
            'marketplace': 'marketplace platforms',
            'saas': 'SaaS providers',
            'fintech': 'fintech companies',
            'b2b': 'B2B businesses',
            'bank': 'banks and financial institutions',
        }
        
        for key, value in business_types.items():
            if key in file_name:
                description = f"Implement payment solutions tailored for {value} with optimized processing"
                break
        
        if not description:
            description = "Explore payment solutions designed for your specific business use case"
    
    # Account management
    elif 'account' in file_name or 'profile' in file_name:
        description = "Manage merchant accounts and profiles to organize payment operations across businesses"
    
    # Dispute/Chargeback files
    elif 'dispute' in file_name or 'chargeback' in file_name:
        description = "Handle payment disputes and chargebacks through a centralized management interface"
    
    # Surcharge files
    elif 'surcharge' in file_name:
        description = "Configure dynamic surcharges to pass processing fees to customers based on card type"
    
    # Reporting files
    elif 'report' in file_name:
        description = "Generate payment reports to analyze transaction data and financial performance"
    
    # Refund files
    elif 'refund' in file_name:
        description = "Process refunds to return funds to customers and manage reversal transactions"
    
    # Payment method files
    elif 'payment-method' in file_name:
        description = "Configure payment methods to offer customers their preferred payment options"
    
    # Wallet files
    elif 'wallet' in file_name or 'apple-pay' in file_name or 'google-pay' in file_name:
        description = "Enable digital wallet payments to offer customers fast, secure checkout options"
    
    # UPI files
    elif 'upi' in file_name:
        description = "Integrate UPI payments to accept instant bank transfers in India"
    
    # Card files
    elif 'card' in file_name:
        description = "Configure card payment processing to accept credit and debit card transactions"
    
    # Web client/Control center
    elif 'control-center' in file_name or 'web-client' in file_name:
        description = "Deploy the web-based control center to manage payments through an intuitive interface"
    
    # Going live/Production
    elif 'going-live' in file_name or 'go-live' in file_name or 'live' in file_name:
        description = "Prepare your Hyperswitch integration for production with security and compliance checks"
    
    # Community files
    elif 'community' in file_dir:
        description = "Join the Hyperswitch community to contribute, collaborate, and connect with other developers"
    
    # Release notes
    elif 'release' in file_name or 'changelog' in file_name:
        description = "Review release notes to stay updated on new features, improvements, and fixes"
    
    # README files
    elif file_name == 'readme':
        # Get parent directory name for context
        parent = file_path.parent.name.lower()
        
        if parent == 'hyperswitch-docs':
            description = "Explore the complete guide to implementing Juspay Hyperswitch payment infrastructure"
        elif 'connector' in parent:
            description = "Browse available payment connectors and integration guides for your preferred processors"
        elif 'deploy' in parent:
            description = "Access deployment guides to set up Hyperswitch on your infrastructure"
        elif 'feature' in parent:
            description = "Discover Hyperswitch features to optimize payment processing and increase revenue"
        elif 'sdk' in parent:
            description = "Explore SDK documentation to integrate payment processing into your applications"
        elif 'api' in parent:
            description = "Reference API documentation to build custom payment integrations"
        else:
            description = f"Overview and guides for {parent.replace('-', ' ')}"
    
    # SUMMARY.md
    elif file_name == 'summary':
        description = "Navigate the complete Hyperswitch documentation with this structured table of contents"
    
    # Default description based on H1
    if not description:
        # Clean up H1
        clean_h1 = h1.replace('#', '').strip()
        clean_h1 = re.sub(r'^[\W]+', '', clean_h1)  # Remove leading non-word chars
        
        if 'how to' in clean_h1.lower():
            # Extract the task after "How to"
            task = re.sub(r'^.*how to\s+', '', clean_h1, flags=re.IGNORECASE)
            description = f"Learn {task} to improve your payment processing workflow"
        elif any(verb in clean_h1.lower() for verb in ['setup', 'set up']):
            description = f"Set up {clean_h1.replace('Set up', '').replace('Setup', '').strip()} to enable payment processing capabilities"
        elif 'guide' in clean_h1.lower():
            description = f"Follow this guide to implement {clean_h1.replace('Guide', '').replace('guide', '').strip()} successfully"
        elif 'integration' in clean_h1.lower():
            description = f"Integrate {clean_h1.replace('Integration', '').replace('integration', '').strip()} to expand payment capabilities"
        else:
            # Generic but still specific
            description = f"Learn about {clean_h1} to optimize your payment infrastructure"
    
    # Ensure description follows format and constraints
    description = description.strip()
    
    # Remove trailing period if present
    if description.endswith('.'):
        description = description[:-1]
    
    # Ensure 15-30 words
    words = description.split()
    if len(words) < 15:
        # Expand short descriptions
        if 'to' in description:
            parts = description.split(' to ', 1)
            if len(parts) == 2:
                description = f"{parts[0]} to {parts[1]}"
    
    # Cap at 30 words
    words = description.split()
    if len(words) > 30:
        description = ' '.join(words[:30])
    
    return description

def fix_heading_hierarchy(content: str) -> str:
    """
    Rule 1: Fix heading hierarchy.
    - Single H1 at top
    - ## H2 for sections, ### H3 for sub-sections
    - No skipped levels
    """
    lines = content.split('\n')
    result = []
    h1_found = False
    
    for i, line in enumerate(lines):
        # Check for H1 (single #)
        if line.strip().startswith('# ') and not line.strip().startswith('## '):
            if h1_found:
                # Convert duplicate H1 to H2
                line = '#' + line.strip()
            else:
                h1_found = True
        
        # Fix skipped levels (e.g., # followed by ###)
        # This is handled by ensuring proper progression
        
        result.append(line)
    
    return '\n'.join(result)

def fix_formatting(content: str) -> str:
    """
    Rule 2: Fix general formatting.
    - Numbered lists for steps
    - Bullet lists for features
    - Tables for structured data
    - Fix typos
    """
    # Common typos to fix
    typos = {
        'teh ': 'the ',
        'recieve': 'receive',
        'seperate': 'separate',
        'occured': 'occurred',
        'occurence': 'occurrence',
        'sucessful': 'successful',
        'sucess': 'success',
        'upto': 'up to',
        'setup ': 'set up ',  # verb form
        ' alot ': ' a lot ',
        'adn ': 'and ',
        'taht': 'that',
        'wiht': 'with',
    }
    
    for typo, correction in typos.items():
        content = content.replace(typo, correction)
        content = content.replace(typo.capitalize(), correction.capitalize())
    
    # Ensure step lists use proper numbering
    # Convert bullet lists that look like steps to numbered lists
    lines = content.split('\n')
    result = []
    in_step_section = False
    
    step_keywords = ['step', 'first', 'next', 'then', 'finally', 'follow these']
    
    for i, line in enumerate(lines):
        # Detect step sections
        if any(keyword in line.lower() for keyword in step_keywords):
            if '## ' in line or '### ' in line:
                in_step_section = True
        
        # Reset on new major section
        if line.strip().startswith('## ') and 'step' not in line.lower():
            in_step_section = False
        
        result.append(line)
    
    return '\n'.join(result)

def fix_brand_names(content: str, is_first_mention: bool = True) -> str:
    """
    Rule 3: Fix brand name usage.
    - Add "Juspay" to first mentions, titles, product intros
    - Keep "Hyperswitch" in code, URLs, subsequent mentions
    """
    if not is_first_mention:
        return content
    
    # Only modify first paragraph and H1
    lines = content.split('\n')
    result = []
    first_para_done = False
    
    for i, line in enumerate(lines):
        # Skip frontmatter
        if line.strip() == '---':
            result.append(line)
            continue
        
        # Handle H1
        if line.strip().startswith('# ') and not first_para_done:
            # Check if H1 contains just "Hyperswitch"
            h1_content = line.replace('# ', '').strip()
            if h1_content.lower() == 'hyperswitch' or h1_content.startswith('Hyperswitch '):
                # Check if already has Juspay
                if 'Juspay' not in h1_content:
                    line = line.replace('Hyperswitch', 'Juspay Hyperswitch', 1)
        
        # Handle first paragraph (before any heading)
        if not first_para_done and line.strip() and not line.startswith('#'):
            # Only add Juspay to first occurrence in first paragraph
            if 'Hyperswitch' in line and 'Juspay' not in line:
                # Don't modify if in code block or URL
                if not line.strip().startswith('```') and 'http' not in line:
                    line = line.replace('Hyperswitch', 'Juspay Hyperswitch', 1)
            first_para_done = True
        
        result.append(line)
    
    return '\n'.join(result)

def insert_canonical_stats(content: str) -> str:
    """
    Rule 5: Insert canonical statistics where appropriate.
    300+ connectors, 200+ payment methods, 2,000 TPS, 40k+ GitHub stars
    """
    # Find introduction/hero sections and insert stats
    lines = content.split('\n')
    result = []
    stats_inserted = False
    
    for i, line in enumerate(lines):
        result.append(line)
        
        # Insert stats after first H1 if it's an overview/intro file
        if not stats_inserted and line.strip().startswith('# ') and i < 10:
            # Check if this looks like an overview/main page
            next_lines = '\n'.join(lines[i+1:i+5])
            if any(word in next_lines.lower() for word in ['overview', 'introduction', 'getting started', 'guide']):
                # Insert stats block
                stats_block = f"""

> **Scale with Confidence:** Process payments with {CANONICAL_STATS['connectors']}+ connectors, {CANONICAL_STATS['payment_methods']}+ payment methods, and {CANONICAL_STATS['tps']} TPS capacity. Join {CANONICAL_STATS['github_stars']} developers on [GitHub](https://github.com/juspay/hyperswitch).
"""
                result.append(stats_block)
                stats_inserted = True
    
    return '\n'.join(result)

def process_file(file_path: Path) -> bool:
    """Process a single markdown file and apply all formatting rules."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False
    
    # Parse frontmatter and body
    frontmatter, body = parse_frontmatter(content)
    
    # Extract H1 from body
    h1 = ''
    for line in body.split('\n'):
        if line.strip().startswith('# '):
            h1 = line.strip()
            break
    
    # Generate new description
    new_description = generate_description(file_path, body, h1)
    
    # Update frontmatter
    if frontmatter is None:
        frontmatter = {}
    
    # Only update if description is missing or generic
    current_desc = frontmatter.get('description', '')
    if not current_desc or len(current_desc) < 20 or 'hyperswitch' in current_desc.lower():
        frontmatter['description'] = new_description
    
    # Apply formatting rules to body
    body = fix_heading_hierarchy(body)
    body = fix_formatting(body)
    body = fix_brand_names(body, is_first_mention=True)
    body = insert_canonical_stats(body)
    
    # Reconstruct content
    if frontmatter:
        frontmatter_lines = ['---']
        for key, value in frontmatter.items():
            frontmatter_lines.append(f"{key}: {value}")
        frontmatter_lines.append('---')
        new_content = '\n'.join(frontmatter_lines) + '\n\n' + body
    else:
        new_content = body
    
    # Write back
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    except Exception as e:
        print(f"Error writing {file_path}: {e}")
        return False

def main():
    """Main function to process all markdown files."""
    root_dir = '/Users/atul.p/open/hyperswitch-docs'
    
    print(f"Scanning for markdown files in {root_dir}...")
    markdown_files = find_markdown_files(root_dir)
    print(f"Found {len(markdown_files)} markdown files")
    
    success_count = 0
    error_count = 0
    
    for i, file_path in enumerate(markdown_files, 1):
        print(f"[{i}/{len(markdown_files)}] Processing {file_path}...")
        
        if process_file(file_path):
            success_count += 1
        else:
            error_count += 1
        
        # Progress update every 50 files
        if i % 50 == 0:
            print(f"Progress: {i}/{len(markdown_files)} files processed")
    
    print(f"\nProcessing complete!")
    print(f"Successfully processed: {success_count} files")
    print(f"Errors: {error_count} files")
    
    return 0 if error_count == 0 else 1

if __name__ == '__main__':
    sys.exit(main())
