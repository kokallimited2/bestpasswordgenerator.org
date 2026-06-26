#!/usr/bin/env python3
"""
Add affiliate links to blog posts on bestpasswordgenerator.org.
Processes each file, identifies content area before CTA, inserts natural recommendation paragraph.
"""
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))

# Affiliate link snippets
NORD = '<a href="https://go.nordpass.io/aff_c?offer_id=488&aff_id=34741&url=https://www.nordpass.com/" target="_blank" rel="nofollow sponsored noopener">NordPass</a>'

KASP = '<a href="https://dhwnh.com/g/f6b07970c6ca5cdc7c0be5a65aad3a/?erid=5jtCeReLm1S3Xx3LfA8QF84" target="_blank" rel="nofollow sponsored noopener">Kaspersky Premium</a>'

HIDE = '<a href="https://codeaven.com/g/d6ig17yj38ca5cdc7c0bcfba9fca8a/" target="_blank" rel="nofollow sponsored noopener">Hide My Name VPN</a>'

TURBO = '<a href="https://grfpr.com/g/exe221unkpca5cdc7c0bddf84d4c0b/" target="_blank" rel="nofollow sponsored noopener">Turbo VPN</a>'

TREK = '<a href="https://tsygg.com/g/p5lrcr1ak1ca5cdc7c0bce5d089991/" target="_blank" rel="nofollow sponsored noopener">TrekMail</a>'

ONEP = '<a href="https://1password.com/" target="_blank" rel="nofollow sponsored noopener">1Password</a>'

BITW = '<a href="https://bitwarden.com/" target="_blank" rel="nofollow sponsored noopener">Bitwarden</a>'


def get_link_tuple(link_type, filepath):
    """Return (paragraph_html, link_snippet) based on context"""
    if link_type == 'nord':
        para = f'<p>For a reliable and feature-rich password manager that works across all your devices, consider {NORD}. It combines strong encryption with an intuitive interface, making it easy to generate and store unique passwords for every account.</p>'
        return para
    elif link_type == 'nord_short':
        para = f'<p>Using a password manager like {NORD} is the easiest way to generate and store strong, unique passwords for every account without having to memorise them.</p>'
        return para
    elif link_type == 'nord_auth':
        para = f'<p>Pair your authenticator app with a password manager like {NORD} for complete account security — it generates and stores strong passwords while you handle 2FA codes separately.</p>'
        return para
    elif link_type == 'nord_mfa':
        para = f'<p>Combine MFA with a dedicated password manager like {NORD} to ensure every account has a unique, strong password alongside your second-factor protection.</p>'
        return para
    elif link_type == 'nord_third':
        para = f'<p>If you are still evaluating your options, {NORD} is another excellent choice worth considering — it offers a polished user experience, strong security architecture, and affordable family plans.</p>'
        return para
    elif link_type == 'nord_breach':
        para = f'<p>After any data breach, using a password manager like {NORD} to generate and store unique passwords for every account is the single most effective step you can take to prevent credential reuse attacks.</p>'
        return para
    elif link_type == 'nord_browser':
        para = f'<p>For users who want more than what browser managers offer, a dedicated solution like {NORD} provides security audits, encrypted sharing, and cross-platform support that built-in managers simply cannot match.</p>'
        return para
    elif link_type == 'nord_pass':
        para = f'<p>For most users, the best approach is to use a password manager like {NORD} to generate and store strong passphrases — combining memorability with the convenience of automatic password management.</p>'
        return para
    elif link_type == 'nord_create':
        para = f'<p>The easiest way to ensure all your passwords meet these standards is to use a password manager like {NORD}, which can generate and store cryptographically strong passwords for every account automatically.</p>'
        return para
    elif link_type == 'kasp':
        para = f'<p>To stay protected against evolving threats like infostealer malware and credential theft, consider a comprehensive security suite like {KASP}. It includes advanced malware protection, password monitoring, and breach alerts that help you detect compromised credentials early.</p>'
        return para
    elif link_type == 'kasp_short':
        para = f'<p>Running a full security scan with a trusted suite like {KASP} can help detect and remove infostealer malware before it compromises your saved passwords.</p>'
        return para
    elif link_type == 'kasp_phish':
        para = f'<p>To defend against AI-powered phishing attacks, a comprehensive security suite like {KASP} provides real-time phishing detection, malicious link blocking, and credential theft protection across your devices.</p>'
        return para
    elif link_type == 'kasp_bitlocker':
        para = f'<p>For complete endpoint protection beyond BitLocker, consider a security suite like {KASP} that includes ransomware protection, vulnerability scanning, and advanced threat detection alongside full-disk encryption management.</p>'
        return para
    elif link_type == 'kasp_edge':
        para = f'<p>If you are concerned about how your browser stores passwords, a dedicated password manager combined with a security suite like {KASP} provides encrypted storage, breach monitoring, and real-time threat protection that browser-native solutions lack.</p>'
        return para
    elif link_type == 'nord_edge':
        para = f'<p>For truly secure password storage, switch to a dedicated password manager like {NORD} that stores your credentials with zero-knowledge encryption — meaning even the service provider cannot access your passwords.</p>'
        return para
    elif link_type == 'nord_audit':
        para = f'<p>Using a password manager like {NORD} makes it easy to act on audit findings — you can quickly update weak or reused passwords and enable two-factor authentication for every account from one dashboard.</p>'
        return para
    elif link_type == 'nord_host':
        para = f'<p>Regardless of which hosting provider you choose, securing user accounts with a password manager like {NORD} is essential — it ensures every admin, editor, and contributor uses strong, unique passwords that are stored securely.</p>'
        return para
    elif link_type == 'nord_list':
        para = f'<p>Avoid every password on this list by using a password manager like {NORD} to generate and store strong, unique passwords that are impossible to crack — it handles the complexity so you do not have to.</p>'
        return para
    elif link_type == 'nord_compare':
        para = f'<p>For users still evaluating their options, {NORD} is another strong contender worth considering — it combines modern security architecture with an intuitive interface and competitive pricing.</p>'
        return para
    elif link_type == 'nord_compare2':
        para = f'<p>If you are still deciding, {NORD} offers a compelling middle ground with strong security, an intuitive interface, and affordable family plans that make it easy to secure everyone in your household.</p>'
        return para
    elif link_type == 'nord_compare3':
        para = f'<p>For users looking for a simpler all-in-one solution, {NORD} combines password management with a clean interface and strong security at a competitive price point.</p>'
        return para
    elif link_type == 'nord_twofactor':
        para = f'<p>Beyond authenticator apps, a password manager like {NORD} can complement your 2FA setup by generating and storing strong passwords that work alongside your second-factor codes for complete account protection.</p>'
        return para
    elif link_type == 'nord_small':
        para = f'<p>A password manager like {NORD} is essential for any small business — it enables secure password sharing among team members, enforces strong password policies, and provides centralised security oversight without burdening employees.</p>'
        return para
    elif link_type == 'nord_short_common':
        para = f'<p>The best way to avoid weak passwords is to use a password manager like {NORD} to generate and store strong, unique credentials for every account automatically.</p>'
        return para
    else:
        return f'<p>Using a password manager like {NORD} is the best way to generate and store strong, unique passwords for every account.</p>'


# File categorization: (filepath, link_type)
files_config = [
    # === Security breach / malware / threat news → Kaspersky Premium ===
    ('blog/149-million-credentials-leaked-unsecured-database-2026.html', 'kasp'),
    ('blog/184-million-passwords-leaked-plain-text-apple-google-government-accounts-exposed.html', 'kasp'),
    ('blog/6-billion-passwords-stolen-by-malware-2025-specops-report.html', 'kasp_short'),
    ('blog/ai-found-record-security-bugs-may-2026-patch-guide.html', 'kasp'),
    ('blog/ai-phishing-attacks-surge-1265-percent-2026.html', 'kasp_phish'),
    ('blog/canvas-breach-275-million-students-password-safety.html', 'kasp'),
    ('blog/congress-investigates-canvas-breach-instructure-paid-ransom.html', 'kasp'),
    ('blog/cushman-wakefield-breach-500k-records-stolen-by.html', 'kasp'),
    ('blog/fast16-malware-sabotaged-nuclear-weapons-tests.html', 'kasp'),
    ('blog/first-ai-generated-zero-day-exploit-google-2026.html', 'kasp'),
    ('blog/github-hacked-3800-repos-stolen-poisoned-vs-code-extension-teampcp-2026.html', 'kasp'),
    ('blog/kaspersky-md5-password-hashes-crackable-2026-study.html', 'kasp'),
    ('blog/medtronic-hacked-medical-device-giant-hit-by.html', 'kasp'),
    ('blog/microsoft-bitlocker-encryption-bypassed-your-encrypted.html', 'kasp_bitlocker'),
    ('blog/microsoft-edge-stores-passwords-plaintext-security-risk.html', 'kasp_edge'),
    ('blog/passkey-phishing-2026.html', 'kasp'),
    ('blog/password-breach-statistics-2026.html', 'kasp'),
    ('blog/verizon-dbir-2026-vulnerability-exploitation-overtakes-credential-theft.html', 'kasp'),
    ('blog/what-is-credential-stuffing.html', 'kasp'),
    ('blog/yellowkey-bitlocker-bypass-zero-day-microsoft-2026.html', 'kasp_bitlocker'),

    # === Password manager / security guides → NordPass ===
    ('blog/best-password-managers-2026.html', 'nord'),
    ('blog/are-browser-password-managers-safe-2026.html', 'nord_browser'),
    ('blog/bitwarden-vs-1password-2026.html', 'nord_third'),
    ('blog/browser-password-manager-vs-dedicated-password-manager-2026.html', 'nord_browser'),
    ('blog/how-to-create-strong-passwords-2026.html', 'nord_create'),
    ('blog/how-to-perform-personal-password-security-audit-2026.html', 'nord_audit'),
    ('blog/most-common-passwords-2026-list.html', 'nord_list'),
    ('blog/nist-password-guidelines-2026-changes.html', 'nord'),
    ('blog/password-generator-vs-password-manager.html', 'nord_short'),
    ('blog/password-managers-vs-passkeys-2026.html', 'nord'),
    ('blog/password-vs-passphrase-which-is-more-secure.html', 'nord_pass'),

    # === 2FA / Authenticator posts → NordPass ===
    ('blog/best-authenticator-apps-2026.html', 'nord_auth'),
    ('blog/google-authenticator-vs-duo-mobile-2026.html', 'nord_auth'),
    ('blog/google-authenticator-vs-microsoft-authenticator-2026.html', 'nord_twofactor'),
    ('blog/mfa-guide-2026.html', 'nord_mfa'),
    ('blog/security-key-vs-authenticator-app-2026.html', 'nord_auth'),
    ('blog/two-factor-authentication-statistics-2026.html', 'nord_mfa'),

    # === Hosting → NordPass ===
    ('blog/best-secure-wordpress-hosting-in-2026-7-providers.html', 'nord_host'),

    # === blog/posts/ files ===
    ('blog/posts/2fa-app-comparison-google-authenticator-vs-authy-vs-microsoft-authenticator.html', 'nord_auth'),
    ('blog/posts/how-long-would-it-take-to-crack-your-password.html', 'nord_short'),
    ('blog/posts/password-manager-vs-browser-password-saving-which-is-safer.html', 'nord_browser'),
    ('blog/posts/securing-your-small-business-password-policies-that-actually-work.html', 'nord_small'),
    ('blog/posts/the-top-10-most-common-passwords-and-why-you-must-avoid-them.html', 'nord_short_common'),
    ('blog/posts/two-factor-authentication-the-extra-lock-on-your-digital-life.html', 'nord_mfa'),
]

stats = {'success': 0, 'skipped_redirect': 0, 'skipped_has_link': 0, 'not_found': 0, 'error': 0}

for relpath, link_type in files_config:
    filepath = os.path.join(BASE, relpath)

    if not os.path.exists(filepath):
        print(f"NOT FOUND: {relpath}")
        stats['not_found'] += 1
        continue

    with open(filepath, 'r') as f:
        content = f.read()

    # Skip redirect pages
    if 'http-equiv="refresh"' in content:
        print(f"SKIP (redirect): {relpath}")
        stats['skipped_redirect'] += 1
        continue

    # Skip if already has affiliate links
    if 'nofollow sponsored' in content:
        print(f"SKIP (has links): {relpath}")
        stats['skipped_has_link'] += 1
        continue

    # Generate the paragraph to insert
    new_para = get_link_tuple(link_type, relpath)

    # Find insertion point: before the CTA button div
    cta_marker = '<div style="text-align:center">'
    related_marker = '<div class="related"'

    # First try: insert before CTA div
    insert_idx = content.find(cta_marker)
    if insert_idx == -1:
        # Try before related articles
        insert_idx = content.find(related_marker)
        if insert_idx == -1:
            # Try before closing post-container
            insert_idx = content.find('</div>\n</main>')
            if insert_idx == -1:
                print(f"ERROR: No insertion point found in {relpath}")
                stats['error'] += 1
                continue

    # Insert the paragraph with a blank line separator
    new_content = content[:insert_idx] + '\n' + new_para + '\n\n' + content[insert_idx:]

    with open(filepath, 'w') as f:
        f.write(new_content)

    print(f"OK: {relpath} ({link_type})")
    stats['success'] += 1

print(f"\n=== Summary ===")
print(f"Success: {stats['success']}")
print(f"Skipped (redirect): {stats['skipped_redirect']}")
print(f"Skipped (has links): {stats['skipped_has_link']}")
print(f"Not found: {stats['not_found']}")
print(f"Error: {stats['error']}")
print(f"Total processed: {stats['success'] + stats['skipped_redirect'] + stats['skipped_has_link'] + stats['not_found'] + stats['error']}")
