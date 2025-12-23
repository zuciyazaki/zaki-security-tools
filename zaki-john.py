#!/usr/bin/env python3
"""
JOHN-QUICK V1.0: John the Ripper Quick Reference Tool
Created by: Zuciya Zaki
Purpose: Fast hash identification and cracking for TryHackMe/CTF challenges
Day 26 - "I never go back on my word! That's my ninja way!"

Features:
- 🔍 Hash Type Identification
- 💥 Exact Crack Commands
- 🚩 Post-Crack Guidance
- 📚 TryHackMe Scenarios
"""

import sys
import os

# Color definitions
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'

def print_banner():
    """Display Zuciya Zaki branded banner with lion"""
    banner = f"""{Colors.YELLOW}
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║                    ███████╗██╗   ██╗ ██████╗██╗██╗   ██╗ █████╗      ║
║                    ╚══███╔╝██║   ██║██╔════╝██║╚██╗ ██╔╝██╔══██╗     ║
║                      ███╔╝ ██║   ██║██║     ██║ ╚████╔╝ ███████║     ║
║                     ███╔╝  ██║   ██║██║     ██║  ╚██╔╝  ██╔══██║     ║
║                    ███████╗╚██████╔╝╚██████╗██║   ██║   ██║  ██║     ║
║                    ╚══════╝ ╚═════╝  ╚═════╝╚═╝   ╚═╝   ╚═╝  ╚═╝     ║
║                                                                      ║
║               ███████╗ █████╗ ██╗  ██╗██╗                            ║
║               ╚══███╔╝██╔══██╗██║ ██╔╝██║                            ║
║                 ███╔╝ ███████║█████╔╝ ██║                            ║
║                ███╔╝  ██╔══██║██╔═██╗ ██║                            ║
║               ███████╗██║  ██║██║  ██╗██║                            ║
║               ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝                            ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
{Colors.RESET}
{Colors.CYAN}╔══════════════════════════════════════════════════════════════════════╗
║           JOHN THE RIPPER QUICK REFERENCE TOOL V1.0                  ║
║           🔍 Identify | 💥 Crack | 🚩 Use Password                   ║
╚══════════════════════════════════════════════════════════════════════╝{Colors.RESET}
"""
    print(banner)

# Hash type database with TryHackMe focus
HASH_TYPES = {
    'ntlm': {
        'name': 'NTLM (Windows Hash)',
        'john_format': 'NT',
        'length': '32 hex characters',
        'example': 'aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0',
        'visual_id': 'Two 32-char hashes separated by colon (LM:NTLM)',
        'purpose': 'When you run hashdump in Meterpreter or dump Windows SAM database',
        'identify_cmd': 'Look for format: [username]:[RID]:[LM]:[NTLM]:::\nExample: Administrator:500:aad3b...:31d6c...',
        'prep_file': 'Save just the NTLM part (after 3rd colon) to hash.txt',
        'crack_cmd': 'john --format=NT hash.txt --wordlist=/usr/share/wordlists/rockyou.txt',
        'show_cmd': 'john --show --format=NT hash.txt',
        'after_crack': 'Use password with: PSExec, RDP (xfreerdp), SMB shares, evil-winrm, WinRM',
        'speed': 'VERY FAST (millions/sec)',
        'notes': 'Most common Windows hash! LM part often empty (aad3b...). Focus on NTLM.'
    },
    'md5': {
        'name': 'MD5 (Unsalted)',
        'john_format': 'Raw-MD5',
        'length': '32 hex characters',
        'example': '5f4dcc3b5aa765d61d8327deb882cf99',
        'visual_id': 'Exactly 32 characters, only 0-9 and a-f',
        'purpose': 'When you find hashes in web app databases, config files, or password dumps',
        'identify_cmd': 'hashid <hash> OR echo <hash> | hash-identifier',
        'prep_file': 'echo "5f4dcc3b5aa765d61d8327deb882cf99" > hash.txt',
        'crack_cmd': 'john --format=Raw-MD5 hash.txt --wordlist=/usr/share/wordlists/rockyou.txt',
        'show_cmd': 'john --show --format=Raw-MD5 hash.txt',
        'after_crack': 'Use for: Web application login, database access, admin panels',
        'speed': 'VERY FAST (millions/sec)',
        'notes': 'Very weak, cracks quickly. Common in old web apps and databases.'
    },
    'sha1': {
        'name': 'SHA-1 (Unsalted)',
        'john_format': 'Raw-SHA1',
        'length': '40 hex characters',
        'example': '5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8',
        'visual_id': 'Exactly 40 characters, only 0-9 and a-f',
        'purpose': 'When you find SHA-1 hashes in databases or config files',
        'identify_cmd': 'hashid <hash> (will detect SHA-1)',
        'prep_file': 'echo "5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8" > hash.txt',
        'crack_cmd': 'john --format=Raw-SHA1 hash.txt --wordlist=/usr/share/wordlists/rockyou.txt',
        'show_cmd': 'john --show --format=Raw-SHA1 hash.txt',
        'after_crack': 'Use for: Web login, API keys, application passwords',
        'speed': 'FAST (millions/sec)',
        'notes': 'Longer than MD5, but still weak. Common in web applications.'
    },
    'sha256': {
        'name': 'SHA-256 (Unsalted)',
        'john_format': 'Raw-SHA256',
        'length': '64 hex characters',
        'example': '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8',
        'visual_id': 'Exactly 64 characters, only 0-9 and a-f',
        'purpose': 'When you find SHA-256 hashes in modern applications or databases',
        'identify_cmd': 'hashid <hash> (will detect SHA-256)',
        'prep_file': 'echo "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8" > hash.txt',
        'crack_cmd': 'john --format=Raw-SHA256 hash.txt --wordlist=/usr/share/wordlists/rockyou.txt',
        'show_cmd': 'john --show --format=Raw-SHA256 hash.txt',
        'after_crack': 'Use for: Modern web apps, cryptocurrency wallets, secure storage',
        'speed': 'MODERATE (thousands/sec)',
        'notes': 'Stronger than MD5/SHA1, takes longer to crack.'
    },
    'shadow_sha512': {
        'name': 'Linux Shadow (SHA-512)',
        'john_format': 'sha512crypt (auto-detected)',
        'length': 'Starts with $6$',
        'example': '$6$rounds=5000$salt$hash...',
        'visual_id': 'Starts with $6$ (SHA-512) or $5$ (SHA-256)',
        'purpose': 'When you read /etc/shadow file on Linux systems',
        'identify_cmd': 'Look for $6$ prefix in /etc/shadow\n$6$ = SHA-512\n$5$ = SHA-256\n$1$ = MD5\n$y$ = yescrypt',
        'prep_file': 'Copy entire line from /etc/shadow to file:\nroot:$6$xyz$hashhashash...:18760:0:99999:7:::',
        'crack_cmd': 'john shadow.txt --wordlist=/usr/share/wordlists/rockyou.txt',
        'show_cmd': 'john --show shadow.txt',
        'after_crack': 'Use password for: SSH login, su/sudo commands, system access',
        'speed': 'SLOW (hundreds/sec) - designed to be slow!',
        'notes': 'John auto-detects format. Very common in Linux privilege escalation!'
    },
    'shadow_md5': {
        'name': 'Linux Shadow (MD5)',
        'john_format': 'md5crypt (auto-detected)',
        'length': 'Starts with $1$',
        'example': '$1$salt$hash...',
        'visual_id': 'Starts with $1$ in /etc/shadow',
        'purpose': 'When you find older Linux /etc/shadow with MD5 hashes',
        'identify_cmd': 'Look for $1$ prefix',
        'prep_file': 'Copy entire shadow line to file',
        'crack_cmd': 'john shadow.txt --wordlist=/usr/share/wordlists/rockyou.txt',
        'show_cmd': 'john --show shadow.txt',
        'after_crack': 'Use for: SSH, su, sudo access on Linux',
        'speed': 'MODERATE (thousands/sec)',
        'notes': 'Weaker than SHA-512, found on older Linux systems.'
    },
    'ntlmv2': {
        'name': 'NTLMv2 (Network Authentication)',
        'john_format': 'netntlmv2',
        'length': 'Very long, contains username and challenge',
        'example': 'user::domain:challenge:response:response',
        'visual_id': 'Contains :: and multiple colons, captured from network traffic',
        'purpose': 'When you capture authentication with Responder or Inveigh',
        'identify_cmd': 'Captured from Responder.py during LLMNR/NBT-NS poisoning',
        'prep_file': 'Responder saves to /usr/share/responder/logs/*.txt automatically',
        'crack_cmd': 'john --format=netntlmv2 hash.txt --wordlist=/usr/share/wordlists/rockyou.txt',
        'show_cmd': 'john --show --format=netntlmv2 hash.txt',
        'after_crack': 'Use cleartext password (NOT the hash) for SMB, WinRM, RDP',
        'speed': 'SLOW (hundreds/sec)',
        'notes': 'Common in network attacks. Responder captures these automatically.'
    },
    'bcrypt': {
        'name': 'bcrypt (Modern Web Apps)',
        'john_format': 'bcrypt (auto-detected)',
        'length': 'Starts with $2a$, $2b$, or $2y$',
        'example': '$2a$10$rounds$saltsaltsalthash...',
        'visual_id': 'Starts with $2a$, $2b$, or $2y$ followed by cost factor',
        'purpose': 'When you find hashes in modern web app databases (very secure)',
        'identify_cmd': 'hashid will identify as bcrypt',
        'prep_file': 'echo "$2a$10$..." > hash.txt',
        'crack_cmd': 'john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt',
        'show_cmd': 'john --show hash.txt',
        'after_crack': 'Use for: Web application login, admin access',
        'speed': 'VERY SLOW (tens/sec) - designed to be VERY slow!',
        'notes': 'Very secure! May take hours/days. Try common passwords first.'
    },
    'ssh_key': {
        'name': 'SSH Private Key (id_rsa)',
        'john_format': 'SSH (after conversion)',
        'length': 'Multi-line RSA PRIVATE KEY format',
        'example': '-----BEGIN RSA PRIVATE KEY-----\nProc-Type: 4,ENCRYPTED...',
        'visual_id': 'File contains "BEGIN RSA PRIVATE KEY" and "ENCRYPTED"',
        'purpose': 'When you find encrypted SSH private key (id_rsa) file',
        'identify_cmd': 'Look for "Proc-Type: 4,ENCRYPTED" in key file',
        'prep_file': 'ssh2john id_rsa > hash.txt (converts key to john format)',
        'crack_cmd': 'john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt',
        'show_cmd': 'john --show hash.txt',
        'after_crack': 'Use password to decrypt key:\nopenssl rsa -in id_rsa -out id_rsa_decrypted\nThen: ssh -i id_rsa_decrypted user@target',
        'speed': 'MODERATE',
        'notes': 'Must convert with ssh2john first! Very common in TryHackMe.'
    },
    'zip': {
        'name': 'ZIP Archive Password',
        'john_format': 'ZIP (after conversion)',
        'length': 'N/A (password-protected file)',
        'example': 'secret.zip (password protected)',
        'visual_id': 'ZIP file that asks for password when extracting',
        'purpose': 'When you find password-protected ZIP files',
        'identify_cmd': 'Try: unzip secret.zip (asks for password = protected)',
        'prep_file': 'zip2john secret.zip > hash.txt',
        'crack_cmd': 'john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt',
        'show_cmd': 'john --show hash.txt',
        'after_crack': 'Use password to extract:\nunzip secret.zip (enter password)\nOR: 7z x secret.zip -p<password>',
        'speed': 'FAST',
        'notes': 'Must convert with zip2john first! Common for hidden files.'
    },
    'rar': {
        'name': 'RAR Archive Password',
        'john_format': 'RAR (after conversion)',
        'length': 'N/A (password-protected file)',
        'example': 'secret.rar (password protected)',
        'visual_id': 'RAR file that asks for password',
        'purpose': 'When you find password-protected RAR archives',
        'identify_cmd': 'Try: unrar e secret.rar (asks for password = protected)',
        'prep_file': 'rar2john secret.rar > hash.txt',
        'crack_cmd': 'john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt',
        'show_cmd': 'john --show hash.txt',
        'after_crack': 'Use password to extract:\nunrar x secret.rar (enter password)',
        'speed': 'MODERATE',
        'notes': 'Must convert with rar2john first!'
    },
    'keepass': {
        'name': 'KeePass Database',
        'john_format': 'KeePass (after conversion)',
        'length': 'N/A (.kdbx file)',
        'example': 'passwords.kdbx',
        'visual_id': 'File extension .kdbx (KeePass database)',
        'purpose': 'When you find KeePass password database files',
        'identify_cmd': 'Look for .kdbx file extension',
        'prep_file': 'keepass2john passwords.kdbx > hash.txt',
        'crack_cmd': 'john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt',
        'show_cmd': 'john --show hash.txt',
        'after_crack': 'Use password to open:\nkeepassxc passwords.kdbx (enter password)\nAll stored passwords revealed!',
        'speed': 'SLOW',
        'notes': 'Jackpot if cracked - contains all user passwords!'
    }
}

# Common TryHackMe scenarios
SCENARIOS = {
    'meterpreter_hashdump': {
        'title': 'Got Meterpreter → Ran hashdump',
        'hash_type': 'ntlm',
        'typical_output': '''
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
user:1001:aad3b435b51404eeaad3b435b51404ee:e52cac67419a9a224a3b108f3fa6cb6d:::
        ''',
        'steps': [
            '1. Copy the output to a file: hashdump.txt',
            '2. Extract just NTLM hashes (after 3rd colon):',
            '   cut -d: -f4 hashdump.txt > hashes.txt',
            '3. Crack with John:',
            '   john --format=NT hashes.txt --wordlist=/usr/share/wordlists/rockyou.txt',
            '4. Show cracked:',
            '   john --show --format=NT hashes.txt',
            '5. Use password with PSExec or RDP!'
        ]
    },
    'found_shadow': {
        'title': 'Found /etc/shadow File',
        'hash_type': 'shadow_sha512',
        'typical_output': 'root:$6$xyz$longhash...:18760:0:99999:7:::',
        'steps': [
            '1. Copy shadow file content to local machine',
            '2. Save to file: shadow.txt',
            '3. Crack (John auto-detects format):',
            '   john shadow.txt --wordlist=/usr/share/wordlists/rockyou.txt',
            '4. Show cracked:',
            '   john --show shadow.txt',
            '5. Use password for SSH or su/sudo!'
        ]
    },
    'database_dump': {
        'title': 'Found Hashes in Database Dump',
        'hash_type': 'md5',
        'typical_output': '''
admin:5f4dcc3b5aa765d61d8327deb882cf99
user:098f6bcd4621d373cade4e832627b4f6
        ''',
        'steps': [
            '1. Identify hash type with hashid',
            '2. Save hashes to file: hashes.txt',
            '3. Crack with appropriate format:',
            '   john --format=Raw-MD5 hashes.txt --wordlist=/usr/share/wordlists/rockyou.txt',
            '4. Show cracked:',
            '   john --show --format=Raw-MD5 hashes.txt',
            '5. Use credentials for web login!'
        ]
    },
    'responder_capture': {
        'title': 'Captured NTLMv2 with Responder',
        'hash_type': 'ntlmv2',
        'typical_output': 'user::DOMAIN:1122334455667788:response:response',
        'steps': [
            '1. Responder saves automatically to:',
            '   /usr/share/responder/logs/SMB-NTLMv2-*.txt',
            '2. Crack the capture file:',
            '   john --format=netntlmv2 SMB-NTLMv2-*.txt --wordlist=/usr/share/wordlists/rockyou.txt',
            '3. Show cracked:',
            '   john --show --format=netntlmv2 SMB-NTLMv2-*.txt',
            '4. Use CLEARTEXT password (not hash) for SMB/WinRM!'
        ]
    },
    'encrypted_key': {
        'title': 'Found Encrypted SSH Key (id_rsa)',
        'hash_type': 'ssh_key',
        'typical_output': '-----BEGIN RSA PRIVATE KEY-----\nProc-Type: 4,ENCRYPTED',
        'steps': [
            '1. Convert key to john format:',
            '   ssh2john id_rsa > id_rsa.hash',
            '2. Crack:',
            '   john id_rsa.hash --wordlist=/usr/share/wordlists/rockyou.txt',
            '3. Show password:',
            '   john --show id_rsa.hash',
            '4. Decrypt key:',
            '   openssl rsa -in id_rsa -out id_rsa_decrypted',
            '5. Use for SSH:',
            '   chmod 600 id_rsa_decrypted',
            '   ssh -i id_rsa_decrypted user@target'
        ]
    },
    'zip_file': {
        'title': 'Found Password-Protected ZIP',
        'hash_type': 'zip',
        'typical_output': 'secret.zip (password required)',
        'steps': [
            '1. Convert to john format:',
            '   zip2john secret.zip > zip.hash',
            '2. Crack:',
            '   john zip.hash --wordlist=/usr/share/wordlists/rockyou.txt',
            '3. Show password:',
            '   john --show zip.hash',
            '4. Extract with password:',
            '   unzip secret.zip',
            '   (enter the cracked password)'
        ]
    }
}

# Wordlist reference
WORDLISTS = {
    'rockyou': {
        'name': 'rockyou.txt',
        'path': '/usr/share/wordlists/rockyou.txt',
        'size': '14 million passwords',
        'when_to_use': 'DEFAULT - use for 99% of TryHackMe challenges',
        'extract': 'sudo gunzip /usr/share/wordlists/rockyou.txt.gz (if compressed)',
        'notes': 'Most common passwords from real breach. Try this FIRST always!'
    },
    'fasttrack': {
        'name': 'fasttrack.txt',
        'path': '/usr/share/wordlists/fasttrack.txt',
        'size': '222 passwords',
        'when_to_use': 'Quick test - most common passwords only',
        'extract': 'Usually pre-installed with Kali',
        'notes': 'Fast but limited. Good for initial test before rockyou.'
    },
    'seclists': {
        'name': 'SecLists Passwords',
        'path': '/usr/share/seclists/Passwords/',
        'size': 'Various sizes',
        'when_to_use': 'Specialized wordlists (years, names, etc.)',
        'extract': 'sudo apt install seclists',
        'notes': 'Contains themed lists - years, months, common-passwords, etc.'
    },
    'custom': {
        'name': 'Custom with Crunch',
        'path': 'Generated on demand',
        'size': 'Variable',
        'when_to_use': 'When you know password pattern (e.g., 8 chars, lowercase+numbers)',
        'extract': 'crunch <min> <max> <charset> -o wordlist.txt',
        'notes': 'Example: crunch 8 8 -t password@@@ (password + 3 numbers)'
    }
}

def show_main_menu():
    """Display main menu"""
    print(f"\n{Colors.CYAN}╔════════════════════════════════════════╗")
    print(f"║           MAIN MENU                    ║")
    print(f"╚════════════════════════════════════════╝{Colors.RESET}\n")
    print(f"{Colors.GREEN}[1]{Colors.RESET} Quick Hash Identification")
    print(f"{Colors.GREEN}[2]{Colors.RESET} Browse Hash Types")
    print(f"{Colors.GREEN}[3]{Colors.RESET} Common TryHackMe Scenarios")
    print(f"{Colors.GREEN}[4]{Colors.RESET} Wordlist Reference")
    print(f"{Colors.GREEN}[5]{Colors.RESET} Generate Crack Command")
    print(f"{Colors.GREEN}[6]{Colors.RESET} Useful Commands Cheat Sheet")
    print(f"{Colors.GREEN}[7]{Colors.RESET} Exit")
    print()

def quick_identify():
    """Quick hash identification helper"""
    print(f"\n{Colors.CYAN}╔════════════════════════════════════════════════════════════════════╗")
    print(f"║          QUICK HASH IDENTIFICATION                                ║")
    print(f"╚════════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    print(f"{Colors.YELLOW}Paste your hash (or first few characters):{Colors.RESET}")
    hash_input = input("> ").strip()
    
    if not hash_input:
        print(f"{Colors.RED}No input provided{Colors.RESET}")
        return
    
    # Visual identification based on patterns
    hash_len = len(hash_input.split()[0])  # First part if multiple fields
    
    matches = []
    
    # Check by length and pattern
    if hash_len == 32 and all(c in '0123456789abcdefABCDEF' for c in hash_input[:32]):
        matches.append(('md5', 'MD5 (32 hex chars)'))
        if ':' in hash_input:
            matches.append(('ntlm', 'NTLM (32:32 format with colons)'))
    elif hash_len == 40 and all(c in '0123456789abcdefABCDEF' for c in hash_input[:40]):
        matches.append(('sha1', 'SHA-1 (40 hex chars)'))
    elif hash_len == 64 and all(c in '0123456789abcdefABCDEF' for c in hash_input[:64]):
        matches.append(('sha256', 'SHA-256 (64 hex chars)'))
    elif hash_input.startswith('$6$'):
        matches.append(('shadow_sha512', 'Linux Shadow SHA-512'))
    elif hash_input.startswith('$5$'):
        matches.append(('shadow_sha512', 'Linux Shadow SHA-256'))
    elif hash_input.startswith('$1$'):
        matches.append(('shadow_md5', 'Linux Shadow MD5'))
    elif hash_input.startswith('$2a$') or hash_input.startswith('$2b$') or hash_input.startswith('$2y$'):
        matches.append(('bcrypt', 'bcrypt'))
    elif '::' in hash_input and hash_input.count(':') >= 5:
        matches.append(('ntlmv2', 'NTLMv2 (network capture)'))
    elif 'BEGIN RSA PRIVATE KEY' in hash_input or 'ENCRYPTED' in hash_input:
        matches.append(('ssh_key', 'Encrypted SSH Private Key'))
    
    if not matches:
        print(f"{Colors.YELLOW}Could not auto-identify. Try these tools:{Colors.RESET}")
        print(f"  • hashid {hash_input[:32]}")
        print(f"  • hash-identifier")
        print(f"  • Search in option [2] Browse Hash Types")
        return
    
    print(f"\n{Colors.GREEN}Possible matches:{Colors.RESET}\n")
    for i, (key, name) in enumerate(matches, 1):
        print(f"{Colors.YELLOW}[{i}]{Colors.RESET} {name}")
    
    if len(matches) == 1:
        print(f"\n{Colors.GREEN}Showing details for: {matches[0][1]}{Colors.RESET}\n")
        display_hash_type(matches[0][0], HASH_TYPES[matches[0][0]])
    else:
        choice = input(f"\n{Colors.YELLOW}Select hash type (1-{len(matches)}) or press Enter to skip: {Colors.RESET}").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(matches):
            selected = matches[int(choice) - 1]
            display_hash_type(selected[0], HASH_TYPES[selected[0]])

def display_hash_type(key, hash_info):
    """Display detailed hash type information"""
    print(f"{Colors.BOLD}{Colors.GREEN}{hash_info['name']}{Colors.RESET}")
    print(f"{Colors.CYAN}John Format:{Colors.RESET} --format={hash_info['john_format']}")
    print(f"{Colors.CYAN}Length/Pattern:{Colors.RESET} {hash_info['length']}")
    print(f"{Colors.CYAN}Example:{Colors.RESET} {hash_info['example'][:60]}...")
    print(f"{Colors.MAGENTA}🎯 When to Use:{Colors.RESET} {Colors.BOLD}{hash_info['purpose']}{Colors.RESET}")
    print(f"{Colors.BLUE}🔍 Identify:{Colors.RESET} {hash_info['visual_id']}")
    print(f"{Colors.YELLOW}📝 Prep File:{Colors.RESET} {hash_info['prep_file']}")
    print(f"{Colors.GREEN}💥 Crack Command:{Colors.RESET}\n   {Colors.BOLD}{hash_info['crack_cmd']}{Colors.RESET}")
    print(f"{Colors.GREEN}📺 Show Cracked:{Colors.RESET}\n   {hash_info['show_cmd']}")
    print(f"{Colors.MAGENTA}🚩 After Crack:{Colors.RESET} {hash_info['after_crack']}")
    print(f"{Colors.CYAN}⚡ Speed:{Colors.RESET} {hash_info['speed']}")
    print(f"{Colors.YELLOW}Notes:{Colors.RESET} {hash_info['notes']}")

def browse_hash_types():
    """Browse all hash types by category"""
    print(f"\n{Colors.CYAN}╔════════════════════════════════════════════════════════════════════╗")
    print(f"║                    ALL HASH TYPES                                  ║")
    print(f"╚════════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    categories = {
        'Windows': ['ntlm', 'ntlmv2'],
        'Linux': ['shadow_sha512', 'shadow_md5'],
        'Web/Database': ['md5', 'sha1', 'sha256', 'bcrypt'],
        'Files': ['ssh_key', 'zip', 'rar', 'keepass']
    }
    
    for category, hash_keys in categories.items():
        print(f"{Colors.BOLD}{Colors.YELLOW}{category}:{Colors.RESET}")
        for i, key in enumerate(hash_keys, 1):
            print(f"  {Colors.GREEN}[{key}]{Colors.RESET} {HASH_TYPES[key]['name']}")
        print()
    
    selection = input(f"{Colors.YELLOW}Enter hash type key to see details (or press Enter to go back): {Colors.RESET}").strip().lower()
    
    if selection in HASH_TYPES:
        print()
        display_hash_type(selection, HASH_TYPES[selection])

def show_scenarios():
    """Show common TryHackMe scenarios"""
    print(f"\n{Colors.CYAN}╔════════════════════════════════════════════════════════════════════╗")
    print(f"║              COMMON TRYHACKME SCENARIOS                            ║")
    print(f"╚════════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    for i, (key, scenario) in enumerate(SCENARIOS.items(), 1):
        print(f"{Colors.GREEN}[{i}]{Colors.RESET} {scenario['title']}")
    
    print(f"{Colors.GREEN}[0]{Colors.RESET} Back to Main Menu")
    
    choice = input(f"\n{Colors.YELLOW}Select scenario (0-{len(SCENARIOS)}): {Colors.RESET}").strip()
    
    if choice == '0':
        return
    
    try:
        scenario = list(SCENARIOS.values())[int(choice) - 1]
        print(f"\n{Colors.BOLD}{Colors.CYAN}{scenario['title']}{Colors.RESET}\n")
        print(f"{Colors.YELLOW}Typical Output:{Colors.RESET}")
        print(f"{Colors.WHITE}{scenario['typical_output']}{Colors.RESET}\n")
        print(f"{Colors.GREEN}Step-by-Step:{Colors.RESET}\n")
        for step in scenario['steps']:
            print(f"  {step}")
        print(f"\n{Colors.MAGENTA}💡 Related Hash Type: {HASH_TYPES[scenario['hash_type']]['name']}{Colors.RESET}")
    except (ValueError, IndexError):
        print(f"{Colors.RED}Invalid selection{Colors.RESET}")

def show_wordlists():
    """Display wordlist reference"""
    print(f"\n{Colors.CYAN}╔════════════════════════════════════════════════════════════════════╗")
    print(f"║                    WORDLIST REFERENCE                              ║")
    print(f"╚════════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    for name, wl in WORDLISTS.items():
        print(f"{Colors.BOLD}{Colors.GREEN}{wl['name']}{Colors.RESET}")
        print(f"{Colors.CYAN}Path:{Colors.RESET} {wl['path']}")
        print(f"{Colors.CYAN}Size:{Colors.RESET} {wl['size']}")
        print(f"{Colors.MAGENTA}🎯 When to Use:{Colors.RESET} {wl['when_to_use']}")
        print(f"{Colors.YELLOW}Setup:{Colors.RESET} {wl['extract']}")
        print(f"{Colors.WHITE}Notes:{Colors.RESET} {wl['notes']}")
        print(f"{Colors.YELLOW}{'─' * 70}{Colors.RESET}\n")

def generate_command():
    """Generate crack command based on user input"""
    print(f"\n{Colors.CYAN}╔════════════════════════════════════════════════════════════════════╗")
    print(f"║                 GENERATE CRACK COMMAND                             ║")
    print(f"╚════════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    print(f"{Colors.YELLOW}Select hash type:{Colors.RESET}\n")
    hash_list = list(HASH_TYPES.keys())
    for i, key in enumerate(hash_list, 1):
        print(f"{Colors.GREEN}[{i}]{Colors.RESET} {HASH_TYPES[key]['name']}")
    
    choice = input(f"\n{Colors.YELLOW}Select (1-{len(hash_list)}): {Colors.RESET}").strip()
    
    try:
        selected_key = hash_list[int(choice) - 1]
        hash_info = HASH_TYPES[selected_key]
        
        print(f"\n{Colors.GREEN}Selected: {hash_info['name']}{Colors.RESET}\n")
        
        # Get filename
        filename = input(f"{Colors.YELLOW}Hash filename (default: hash.txt): {Colors.RESET}").strip() or "hash.txt"
        
        # Get wordlist
        wordlist = input(f"{Colors.YELLOW}Wordlist (default: rockyou.txt): {Colors.RESET}").strip() or "/usr/share/wordlists/rockyou.txt"
        
        # Generate command
        print(f"\n{Colors.GREEN}{'═' * 70}")
        print(f"  COPY AND PASTE THESE COMMANDS")
        print(f"{'═' * 70}{Colors.RESET}\n")
        
        # Prep command if needed
        if 'ssh2john' in hash_info['prep_file'] or 'zip2john' in hash_info['prep_file'] or 'rar2john' in hash_info['prep_file'] or 'keepass2john' in hash_info['prep_file']:
            print(f"{Colors.CYAN}# Step 1: Convert file to john format{Colors.RESET}")
            print(f"{hash_info['prep_file']}")
            print()
        
        # Crack command
        print(f"{Colors.CYAN}# {'Step 2: ' if 'john' in hash_info['prep_file'] else ''}Crack the hash{Colors.RESET}")
        if hash_info['john_format'] == 'sha512crypt (auto-detected)' or hash_info['john_format'] == 'md5crypt (auto-detected)' or hash_info['john_format'] == 'bcrypt (auto-detected)':
            crack_cmd = f"john {filename} --wordlist={wordlist}"
        else:
            crack_cmd = f"john --format={hash_info['john_format']} {filename} --wordlist={wordlist}"
        print(f"{Colors.BOLD}{crack_cmd}{Colors.RESET}")
        print()
        
        # Show command
        print(f"{Colors.CYAN}# Show cracked passwords{Colors.RESET}")
        if hash_info['john_format'] == 'sha512crypt (auto-detected)' or hash_info['john_format'] == 'md5crypt (auto-detected)' or hash_info['john_format'] == 'bcrypt (auto-detected)':
            show_cmd = f"john --show {filename}"
        else:
            show_cmd = f"john --show --format={hash_info['john_format']} {filename}"
        print(f"{Colors.BOLD}{show_cmd}{Colors.RESET}")
        
        print(f"\n{Colors.GREEN}{'═' * 70}{Colors.RESET}")
        print(f"{Colors.MAGENTA}🚩 After Success:{Colors.RESET} {hash_info['after_crack']}")
        print(f"{Colors.YELLOW}💡 Expected Speed:{Colors.RESET} {hash_info['speed']}\n")
        
    except (ValueError, IndexError):
        print(f"{Colors.RED}Invalid selection{Colors.RESET}")

def show_cheat_sheet():
    """Display useful commands cheat sheet"""
    print(f"\n{Colors.CYAN}╔════════════════════════════════════════════════════════════════════╗")
    print(f"║                  USEFUL COMMANDS CHEAT SHEET                       ║")
    print(f"╚════════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    commands = [
        ("Identify hash type", "hashid <hash>\nhash-identifier (then paste hash)"),
        ("Extract NTLM from hashdump", "cut -d: -f4 hashdump.txt > hashes.txt"),
        ("Convert SSH key", "ssh2john id_rsa > id_rsa.hash"),
        ("Convert ZIP", "zip2john secret.zip > zip.hash"),
        ("Convert RAR", "rar2john secret.rar > rar.hash"),
        ("Convert KeePass", "keepass2john passwords.kdbx > keepass.hash"),
        ("Show john formats", "john --list=formats | grep -i <keyword>"),
        ("Resume cracking session", "john --restore"),
        ("Use rules for mutations", "john hash.txt --wordlist=rockyou.txt --rules"),
        ("Crack with mask (pattern)", "john --mask='?l?l?l?l?d?d?d' hash.txt"),
        ("Show all cracked passwords", "john --show <hashfile>"),
        ("Remove hash from john.pot", "john --pot=john.pot --show hash.txt")
    ]
    
    for cmd_name, cmd in commands:
        print(f"{Colors.GREEN}{cmd_name}:{Colors.RESET}")
        print(f"  {Colors.CYAN}{cmd}{Colors.RESET}\n")

def main():
    """Main program loop"""
    print_banner()
    
    while True:
        show_main_menu()
        choice = input(f"{Colors.YELLOW}Select option (1-7): {Colors.RESET}").strip()
        
        if choice == '1':
            quick_identify()
        
        elif choice == '2':
            browse_hash_types()
        
        elif choice == '3':
            show_scenarios()
        
        elif choice == '4':
            show_wordlists()
        
        elif choice == '5':
            generate_command()
        
        elif choice == '6':
            show_cheat_sheet()
        
        elif choice == '7':
            print(f"\n{Colors.YELLOW}{'═' * 70}")
            print(f"  Thanks for using ZAKI-JOHN!")
            print(f"  Keep cracking, Zuciya Zaki! 🦁")
            print(f"  \"I never go back on my word - that's my ninja way!\"")
            print(f"{'═' * 70}{Colors.RESET}\n")
            sys.exit(0)
        
        else:
            print(f"{Colors.RED}Invalid option. Please select 1-7{Colors.RESET}")
        
        input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.RESET}")
        # Clear screen
        os.system('clear' if os.name == 'posix' else 'cls')
        print_banner()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Exiting... You WILL make it happen, BELIEVE IT! {Colors.RESET}\n")
        sys.exit(0)
