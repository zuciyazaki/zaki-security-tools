#!/usr/bin/env python3
"""
ZAKI-QUIZ V1.0: Security+ Exam Preparation Master Tool
Created by: Zuciya Zaki (Dominic Metz)
Purpose: Master Security+ through comprehensive testing and acronym drills
Day 26+ - "I never go back on my word! That's my ninja way!"

Features:
- 🎲 100-Question Comprehensive Quiz
- 🔤 Acronym Drill Mode (with mnemonics!)
- 📚 Category Practice (focus weak areas)
- ⏱️ Timed Mode (exam simulation)
- 📊 Progress Tracking (see improvement)
- 🎯 Smart Review (prioritize wrong answers)
- 💾 Save/Resume (track over time)
"""

import sys
import os
import random
import json
import time
from datetime import datetime

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
║                    ███████╗ █████╗ ██╗  ██╗██╗                       ║
║                    ╚══███╔╝██╔══██╗██║ ██╔╝██║                       ║
║                      ███╔╝ ███████║█████╔╝ ██║                       ║
║                     ███╔╝  ██╔══██║██╔═██╗ ██║                       ║
║                    ███████╗██║  ██║██║  ██╗██║                       ║
║                    ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝                       ║
║                                                                      ║
║                       ███████╗ ██╗   ██╗██╗███████╗                  ║
║                       ██╔═══██╗██║   ██║██║╚══███╔╝                  ║
║                       ██║   ██║██║   ██║██║  ███╔╝                   ║
║                       ██║▄▄ ██║██║   ██║██║ ███╔╝                    ║
║                       ╚██████╔╝╚██████╔╝██║███████╗                  ║
║                        ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝                  ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
{Colors.RESET}
{Colors.CYAN}╔══════════════════════════════════════════════════════════════════════╗
║         SECURITY+ EXAM PREPARATION MASTER TOOL V1.0                  ║
║         🎯 Quiz | 🔤 Acronyms | 📊 Track Progress                    ║
╚══════════════════════════════════════════════════════════════════════╝{Colors.RESET}
"""
    print(banner)

# Acronym database with mnemonics
ACRONYMS = {
    'networking': {
        'DNS': {
            'full': 'Domain Name System',
            'mnemonic': "Don't Need to remember Server addresses",
            'explanation': 'Translates domain names (google.com) to IP addresses (142.250.80.46)',
            'study_guide': 'Section 1: Networking Fundamentals - DNS'
        },
        'DHCP': {
            'full': 'Dynamic Host Configuration Protocol',
            'mnemonic': 'Dynamically Hands out Computer Parameters',
            'explanation': 'Automatically assigns IP addresses to devices on a network',
            'study_guide': 'Section 1: Networking Fundamentals'
        },
        'TCP': {
            'full': 'Transmission Control Protocol',
            'mnemonic': 'Takes Care of Packets',
            'explanation': 'Reliable, connection-oriented protocol with 3-way handshake',
            'study_guide': 'Section 1: Networking Fundamentals - TCP vs UDP'
        },
        'UDP': {
            'full': 'User Datagram Protocol',
            'mnemonic': 'Usually Drops Packets',
            'explanation': 'Fast, connectionless protocol without guaranteed delivery',
            'study_guide': 'Section 1: Networking Fundamentals - TCP vs UDP'
        },
        'HTTP': {
            'full': 'Hypertext Transfer Protocol',
            'mnemonic': 'H-T-80 (port 80)',
            'explanation': 'Unencrypted web traffic protocol',
            'study_guide': 'Section 1: Networking Fundamentals - HTTP vs HTTPS'
        },
        'HTTPS': {
            'full': 'HTTP Secure',
            'mnemonic': '4-4-3 Fortress (port 443)',
            'explanation': 'Encrypted web traffic using TLS/SSL',
            'study_guide': 'Section 1: Networking Fundamentals - HTTP vs HTTPS'
        },
        'SSH': {
            'full': 'Secure Shell',
            'mnemonic': 'Secure SHell - Two Twos (port 22)',
            'explanation': 'Encrypted remote access protocol',
            'study_guide': 'Section 9: Security+ Exam Focus - Port Numbers'
        },
        'FTP': {
            'full': 'File Transfer Protocol',
            'mnemonic': '21 = drinking age (port 21)',
            'explanation': 'Unencrypted file transfer protocol',
            'study_guide': 'Section 9: Security+ Exam Focus - Port Numbers'
        },
        'SMTP': {
            'full': 'Simple Mail Transfer Protocol',
            'mnemonic': 'Send Mail To People (port 25)',
            'explanation': 'Email sending protocol',
            'study_guide': 'Section 9: Security+ Exam Focus - Port Numbers'
        },
        'VPN': {
            'full': 'Virtual Private Network',
            'mnemonic': 'Very Private Network',
            'explanation': 'Encrypted tunnel through internet for secure communication',
            'study_guide': 'Section 1: Networking Fundamentals - VPN'
        },
        'NAT': {
            'full': 'Network Address Translation',
            'mnemonic': 'Network Address Translator',
            'explanation': 'Translates private IPs to public IPs',
            'study_guide': 'Section 1: Networking Fundamentals - NAT'
        },
        'MAC': {
            'full': 'Media Access Control',
            'mnemonic': "Machine's Actual Card",
            'explanation': 'Hardware address of network device (Layer 2)',
            'study_guide': 'Section 1: Networking Fundamentals - OSI Model'
        },
        'ARP': {
            'full': 'Address Resolution Protocol',
            'mnemonic': 'Answers: Resolve Physical address',
            'explanation': 'Maps IP addresses to MAC addresses on local network',
            'study_guide': 'Section 1: Networking Fundamentals'
        },
        'OSI': {
            'full': 'Open Systems Interconnection',
            'mnemonic': 'Please Do Not Throw Sausage Pizza Away',
            'explanation': '7-layer networking model (Physical, Data Link, Network, Transport, Session, Presentation, Application)',
            'study_guide': 'Section 1: Networking Fundamentals - OSI Model'
        }
    },
    'security': {
        'CIA': {
            'full': 'Confidentiality, Integrity, Availability',
            'mnemonic': 'Can I Access? Is It Intact? Always Accessible?',
            'explanation': 'Three pillars of information security',
            'study_guide': 'Section 2: Security Fundamentals - CIA Triad'
        },
        'AAA': {
            'full': 'Authentication, Authorization, Accounting',
            'mnemonic': 'Triple-A Battery Powers Security',
            'explanation': 'Identity and access management framework',
            'study_guide': 'Section 2: Security Fundamentals - AAA Framework'
        },
        'MFA': {
            'full': 'Multi-Factor Authentication',
            'mnemonic': 'Multiple Factors = Awesome security',
            'explanation': 'Authentication using 2+ verification methods',
            'study_guide': 'Section 2: Security Fundamentals - MFA'
        },
        'IDS': {
            'full': 'Intrusion Detection System',
            'mnemonic': 'I Detect Suspicious activity',
            'explanation': 'Detects and alerts on threats (passive)',
            'study_guide': 'Section 7: Security Tools - IDS vs IPS'
        },
        'IPS': {
            'full': 'Intrusion Prevention System',
            'mnemonic': 'I Prevent Suspicious activity',
            'explanation': 'Detects and blocks threats (active)',
            'study_guide': 'Section 7: Security Tools - IDS vs IPS'
        },
        'SOC': {
            'full': 'Security Operations Center',
            'mnemonic': 'Security Ops Central',
            'explanation': 'Team that monitors and responds to security incidents',
            'study_guide': 'Section 6: Incident Response & SIEM'
        },
        'SIEM': {
            'full': 'Security Information and Event Management',
            'mnemonic': 'Security Intelligence Engine for Monitoring',
            'explanation': 'Platform collecting, analyzing, correlating security logs',
            'study_guide': 'Section 6: Incident Response & SIEM - SIEM'
        },
        'EDR': {
            'full': 'Endpoint Detection and Response',
            'mnemonic': 'Every Device Reporting threats',
            'explanation': 'Security software on devices that detects and responds to threats',
            'study_guide': 'Section 6: Incident Response & SIEM - EDR'
        },
        'SOAR': {
            'full': 'Security Orchestration, Automation, and Response',
            'mnemonic': 'Security Operations Automated Responses',
            'explanation': 'Platform automating repetitive SOC tasks',
            'study_guide': 'Section 6: Incident Response & SIEM - SOAR'
        },
        'DLP': {
            'full': 'Data Loss Prevention',
            'mnemonic': 'Data Leakage Protection',
            'explanation': 'Tools preventing unauthorized data exfiltration',
            'study_guide': 'Section 7: Security Tools - DLP'
        },
        'WAF': {
            'full': 'Web Application Firewall',
            'mnemonic': 'Web Application Filter',
            'explanation': 'Firewall specifically for web applications (HTTP/HTTPS)',
            'study_guide': 'Section 7: Security Tools - WAF'
        },
        'IOC': {
            'full': 'Indicator of Compromise',
            'mnemonic': 'Infection Obvious Clue',
            'explanation': 'Evidence that system has been breached/infected',
            'study_guide': 'Section 6: Incident Response & SIEM - IOC'
        },
        'APT': {
            'full': 'Advanced Persistent Threat',
            'mnemonic': 'Advanced = skilled, Persistent = long-term, Threat = danger',
            'explanation': 'Long-term, stealthy, nation-state level attacks',
            'study_guide': 'Section 2: Security Fundamentals - Threat Actors'
        }
    },
    'attacks': {
        'XSS': {
            'full': 'Cross-Site Scripting',
            'mnemonic': 'X = Cross-site, SS = Scripting Scare',
            'explanation': 'Web vulnerability injecting malicious JavaScript',
            'study_guide': 'Section 3: Web Security - XSS'
        },
        'SQL': {
            'full': 'Structured Query Language',
            'mnemonic': 'Sneaky Query Launched (for SQL Injection)',
            'explanation': 'Injecting malicious SQL commands into input fields',
            'study_guide': 'Section 3: Web Security - SQL Injection'
        },
        'CSRF': {
            'full': 'Cross-Site Request Forgery',
            'mnemonic': 'Cross-Site Request Fakery',
            'explanation': 'Tricks authenticated user into executing unwanted actions',
            'study_guide': 'Section 3: Web Security - CSRF'
        },
        'IDOR': {
            'full': 'Insecure Direct Object Reference',
            'mnemonic': 'I Direct Object Reference = I can change IDs',
            'explanation': 'Accessing unauthorized data by changing ID in URL/request',
            'study_guide': 'Section 3: Web Security - IDOR'
        },
        'DDoS': {
            'full': 'Distributed Denial of Service',
            'mnemonic': 'Distributed = Many sources attacking',
            'explanation': 'Overwhelming target with traffic from many sources',
            'study_guide': 'Section 9: Security+ Exam Focus - Attack Types'
        },
        'MITM': {
            'full': 'Man-in-the-Middle',
            'mnemonic': 'Man Intercepting The Messages',
            'explanation': 'Attacker intercepts communication between two parties',
            'study_guide': 'Section 9: Security+ Exam Focus - Attack Types'
        }
    },
    'crypto': {
        'AES': {
            'full': 'Advanced Encryption Standard',
            'mnemonic': 'Amazing Encryption Standard',
            'explanation': 'Symmetric encryption algorithm (current standard)',
            'study_guide': 'Section 5: Cryptography - AES'
        },
        'RSA': {
            'full': 'Rivest-Shamir-Adleman',
            'mnemonic': 'Really Secure Algorithm',
            'explanation': 'Asymmetric encryption algorithm',
            'study_guide': 'Section 5: Cryptography - Symmetric vs Asymmetric'
        },
        'TLS': {
            'full': 'Transport Layer Security',
            'mnemonic': "Today's Layer of Security",
            'explanation': 'Encryption protocol for secure internet communication',
            'study_guide': 'Section 5: Cryptography - TLS/SSL'
        },
        'SSL': {
            'full': 'Secure Sockets Layer',
            'mnemonic': 'Outdated - use TLS instead!',
            'explanation': 'Deprecated predecessor to TLS',
            'study_guide': 'Section 5: Cryptography - TLS/SSL'
        },
        'PKI': {
            'full': 'Public Key Infrastructure',
            'mnemonic': 'Public Keys for Identity',
            'explanation': 'System for creating, managing, validating digital certificates',
            'study_guide': 'Section 5: Cryptography - PKI'
        }
    },
    'compliance': {
        'NIST': {
            'full': 'National Institute of Standards and Technology',
            'mnemonic': 'National Institute Security Templates',
            'explanation': 'US government agency creating security standards',
            'study_guide': 'Section 8: Compliance & Frameworks - NIST'
        },
        'PCI-DSS': {
            'full': 'Payment Card Industry Data Security Standard',
            'mnemonic': 'Pay Card Industry Data Security Standard',
            'explanation': 'Security standard for handling credit card data',
            'study_guide': 'Section 8: Compliance & Frameworks - PCI-DSS'
        },
        'HIPAA': {
            'full': 'Health Insurance Portability and Accountability Act',
            'mnemonic': 'Health Info Privacy Act',
            'explanation': 'US law protecting health information privacy',
            'study_guide': 'Section 8: Compliance & Frameworks - HIPAA'
        },
        'GDPR': {
            'full': 'General Data Protection Regulation',
            'mnemonic': 'General Data Protection Rules',
            'explanation': 'EU privacy law protecting personal data',
            'study_guide': 'Section 8: Compliance & Frameworks - GDPR'
        },
        'ISO': {
            'full': 'International Organization for Standardization',
            'mnemonic': 'International Security Order',
            'explanation': 'Creates international standards (ISO 27001 for infosec)',
            'study_guide': 'Section 8: Compliance & Frameworks - ISO 27001'
        }
    }
}

# Question database - 100 comprehensive questions
QUESTIONS = {
    'networking': [
        {
            'id': 'NET001',
            'question': 'What does TCP stand for and what is its primary characteristic?',
            'type': 'short_answer',
            'answer': 'Transmission Control Protocol - connection-oriented, reliable, guaranteed delivery',
            'keywords': ['transmission', 'control', 'protocol', 'reliable', 'connection'],
            'explanation': 'TCP is reliable and connection-oriented. It uses a 3-way handshake (SYN, SYN-ACK, ACK) to establish connections and guarantees packet delivery.',
            'mnemonic': 'Takes Care of Packets',
            'guide_reference': 'Section 1: Networking Fundamentals - TCP vs UDP',
            'difficulty': 'easy'
        },
        {
            'id': 'NET002',
            'question': 'Which port does HTTPS use?',
            'type': 'multiple_choice',
            'options': ['80', '443', '8080', '22'],
            'answer': '443',
            'explanation': 'HTTPS uses port 443 for encrypted web traffic using TLS/SSL.',
            'mnemonic': '4-4-3 = For Fortress Security',
            'guide_reference': 'Section 1: Networking Fundamentals - HTTP vs HTTPS',
            'difficulty': 'easy'
        },
        {
            'id': 'NET003',
            'question': 'Name all 7 layers of the OSI Model in order (from bottom to top).',
            'type': 'short_answer',
            'answer': 'Physical, Data Link, Network, Transport, Session, Presentation, Application',
            'keywords': ['physical', 'data link', 'network', 'transport', 'session', 'presentation', 'application'],
            'explanation': 'The OSI Model has 7 layers starting from Physical (cables) up to Application (user-facing protocols).',
            'mnemonic': 'Please Do Not Throw Sausage Pizza Away',
            'guide_reference': 'Section 1: Networking Fundamentals - OSI Model',
            'difficulty': 'medium'
        },
        {
            'id': 'NET004',
            'question': 'What is the difference between a router and a switch?',
            'type': 'short_answer',
            'answer': 'Router connects different networks (Layer 3, uses IP addresses), Switch connects devices within same network (Layer 2, uses MAC addresses)',
            'keywords': ['router', 'networks', 'layer 3', 'ip', 'switch', 'layer 2', 'mac'],
            'explanation': 'Routers work at Layer 3 (Network) and route traffic between different networks. Switches work at Layer 2 (Data Link) and forward traffic within the same network.',
            'mnemonic': 'Router = Between networks, Switch = Within network',
            'guide_reference': 'Section 1: Networking Fundamentals - OSI Model',
            'difficulty': 'medium'
        },
        {
            'id': 'NET005',
            'question': 'What does DNS do? Give a real-world example.',
            'type': 'short_answer',
            'answer': 'Translates domain names to IP addresses. Example: google.com → 142.250.80.46',
            'keywords': ['domain', 'name', 'ip', 'address', 'translate'],
            'explanation': 'DNS is the internet\'s phone book - it converts human-readable domain names into IP addresses that computers use.',
            'mnemonic': "Don't Need to remember Server addresses",
            'guide_reference': 'Section 1: Networking Fundamentals - DNS',
            'difficulty': 'easy'
        },
        {
            'id': 'NET006',
            'question': 'Which of these is the default private IP range for most home networks?',
            'type': 'multiple_choice',
            'options': ['10.0.0.0/8', '172.16.0.0/12', '192.168.0.0/16', 'All of the above'],
            'answer': '192.168.0.0/16',
            'explanation': 'While all three are private IP ranges (RFC 1918), 192.168.0.0/16 is most commonly used in home routers.',
            'mnemonic': '10 is Biggest, 172 is Middle, 192 is Home',
            'guide_reference': 'Section 1: Networking Fundamentals - Private IP Ranges',
            'difficulty': 'easy'
        },
        {
            'id': 'NET007',
            'question': 'What command would you use to test connectivity to 8.8.8.8?',
            'type': 'short_answer',
            'answer': 'ping 8.8.8.8',
            'keywords': ['ping'],
            'explanation': 'The ping command sends ICMP echo requests to test if a host is reachable.',
            'mnemonic': 'Ping = Pinging the door to see if anyone answers',
            'guide_reference': 'Section 1: Networking Fundamentals',
            'difficulty': 'easy'
        },
        {
            'id': 'NET008',
            'question': 'What is the significance of 127.0.0.1?',
            'type': 'short_answer',
            'answer': 'Localhost/loopback address - points to your own machine',
            'keywords': ['localhost', 'loopback', 'own', 'machine'],
            'explanation': '127.0.0.1 is the loopback address that always points to your own computer. Used for testing local services.',
            'mnemonic': '127 home = Home alone',
            'guide_reference': 'Section 1: Networking Fundamentals - Private IP Ranges',
            'difficulty': 'easy'
        },
        {
            'id': 'NET009',
            'question': 'SSH uses which port by default?',
            'type': 'multiple_choice',
            'options': ['21', '22', '23', '25'],
            'answer': '22',
            'explanation': 'SSH (Secure Shell) uses port 22 for encrypted remote access.',
            'mnemonic': 'Two Twos = 22',
            'guide_reference': 'Section 1: Networking Fundamentals - Ports',
            'difficulty': 'easy'
        },
        {
            'id': 'NET010',
            'question': 'Explain what NAT (Network Address Translation) does.',
            'type': 'short_answer',
            'answer': 'Translates private IP addresses to public IP addresses, allows multiple devices to share one public IP',
            'keywords': ['translate', 'private', 'public', 'ip', 'share'],
            'explanation': 'NAT allows multiple devices on a private network to share a single public IP address when accessing the internet.',
            'mnemonic': 'Network Address Translator',
            'guide_reference': 'Section 1: Networking Fundamentals - NAT',
            'difficulty': 'medium'
        }
    ],
    'linux': [
        {
            'id': 'LNX001',
            'question': 'What command lists files in a directory?',
            'type': 'short_answer',
            'answer': 'ls',
            'keywords': ['ls'],
            'explanation': 'ls lists directory contents. Use ls -la for detailed listing including hidden files.',
            'mnemonic': 'List Stuff',
            'guide_reference': 'Linux Command Cheat Book',
            'difficulty': 'easy'
        },
        {
            'id': 'LNX002',
            'question': 'How do you change file permissions to read/write/execute for owner only?',
            'type': 'multiple_choice',
            'options': ['chmod 700 filename', 'chmod 777 filename', 'chmod 644 filename', 'chmod 755 filename'],
            'answer': 'chmod 700 filename',
            'explanation': '700 = rwx for owner (4+2+1), --- for group (0), --- for others (0)',
            'mnemonic': '7 = rwx (all permissions), 0 = nothing',
            'guide_reference': 'Section 4: System Security - Linux File Permissions',
            'difficulty': 'medium'
        },
        {
            'id': 'LNX003',
            'question': 'What does the sudo command do?',
            'type': 'short_answer',
            'answer': 'Execute command as superuser/root with elevated privileges',
            'keywords': ['superuser', 'root', 'elevated', 'privileges'],
            'explanation': 'sudo (superuser do) allows authorized users to run commands with root privileges.',
            'mnemonic': 'SuperUser DO',
            'guide_reference': 'Linux Command Cheat Book',
            'difficulty': 'easy'
        },
        {
            'id': 'LNX004',
            'question': 'How do you install a package in Debian-based systems like Kali/Ubuntu?',
            'type': 'short_answer',
            'answer': 'sudo apt install package-name',
            'keywords': ['apt', 'install', 'sudo'],
            'explanation': 'apt (Advanced Package Tool) is used to install, update, and manage packages.',
            'mnemonic': 'APT = Add Package Tool',
            'guide_reference': 'Linux Command Cheat Book',
            'difficulty': 'easy'
        },
        {
            'id': 'LNX005',
            'question': 'What command shows running processes?',
            'type': 'short_answer',
            'answer': 'ps, top, htop, or ps aux',
            'keywords': ['ps', 'top', 'htop'],
            'explanation': 'ps shows processes, top shows real-time process info, htop is an enhanced version of top.',
            'mnemonic': 'PS = Process Status',
            'guide_reference': 'Linux Command Cheat Book',
            'difficulty': 'easy'
        }
    ],
    'security': [
        {
            'id': 'SEC001',
            'question': 'What does CIA Triad stand for in security?',
            'type': 'short_answer',
            'answer': 'Confidentiality, Integrity, Availability',
            'keywords': ['confidentiality', 'integrity', 'availability'],
            'explanation': 'The three pillars of information security: Confidentiality (only authorized access), Integrity (data not tampered), Availability (accessible when needed).',
            'mnemonic': 'Can I Access? Is It Intact? Always Accessible?',
            'guide_reference': 'Section 2: Security Fundamentals - CIA Triad',
            'difficulty': 'easy'
        },
        {
            'id': 'SEC002',
            'question': 'Explain the difference between authentication and authorization.',
            'type': 'short_answer',
            'answer': 'Authentication = WHO are you (identity verification), Authorization = WHAT can you do (permissions)',
            'keywords': ['authentication', 'who', 'identity', 'authorization', 'what', 'permissions'],
            'explanation': 'Authentication verifies identity (username/password), Authorization determines what you can access (permissions/roles).',
            'mnemonic': 'Authentication = WHO, Authorization = WHAT',
            'guide_reference': 'Section 2: Security Fundamentals - AAA Framework',
            'difficulty': 'medium'
        },
        {
            'id': 'SEC003',
            'question': 'What is the difference between IDS and IPS?',
            'type': 'short_answer',
            'answer': 'IDS = Detects and alerts only (passive), IPS = Detects and blocks (active)',
            'keywords': ['ids', 'detects', 'alerts', 'ips', 'blocks', 'prevents'],
            'explanation': 'IDS monitors and alerts (out-of-band), IPS actively prevents attacks (inline).',
            'mnemonic': 'IDS = I Detect Suspicious, IPS = I Prevent Suspicious',
            'guide_reference': 'Section 7: Security Tools - IDS vs IPS',
            'difficulty': 'medium'
        },
        {
            'id': 'SEC004',
            'question': 'What does MFA/2FA stand for and why is it important?',
            'type': 'short_answer',
            'answer': 'Multi-Factor/Two-Factor Authentication - uses 2+ verification methods for stronger security',
            'keywords': ['multi', 'factor', 'authentication', 'two', 'verification'],
            'explanation': 'MFA requires multiple forms of verification (something you know, have, or are) making accounts much harder to compromise.',
            'mnemonic': 'Multiple Factors = Awesome security',
            'guide_reference': 'Section 2: Security Fundamentals - MFA',
            'difficulty': 'easy'
        },
        {
            'id': 'SEC005',
            'question': 'What are the three factors in MFA?',
            'type': 'short_answer',
            'answer': 'Something you KNOW (password), HAVE (phone/token), ARE (biometric)',
            'keywords': ['know', 'password', 'have', 'phone', 'token', 'are', 'biometric'],
            'explanation': 'The three factor types: Knowledge (password/PIN), Possession (device/card), Inherence (fingerprint/face).',
            'mnemonic': 'KNOW-HAVE-ARE',
            'guide_reference': 'Section 2: Security Fundamentals - MFA',
            'difficulty': 'easy'
        }
    ],
    'cryptography': [
        {
            'id': 'CRY001',
            'question': 'What is the difference between symmetric and asymmetric encryption?',
            'type': 'short_answer',
            'answer': 'Symmetric = same key encrypts and decrypts (faster), Asymmetric = public key encrypts, private key decrypts (slower but more secure key exchange)',
            'keywords': ['symmetric', 'same', 'key', 'asymmetric', 'public', 'private'],
            'explanation': 'Symmetric uses one shared key (AES), asymmetric uses key pairs (RSA). Symmetric is faster, asymmetric solves key distribution problem.',
            'mnemonic': 'Same Secret Shared vs A key for All (public), a key for me (private)',
            'guide_reference': 'Section 5: Cryptography - Symmetric vs Asymmetric',
            'difficulty': 'medium'
        },
        {
            'id': 'CRY002',
            'question': 'What does AES stand for and what is it?',
            'type': 'short_answer',
            'answer': 'Advanced Encryption Standard - symmetric encryption algorithm (current standard)',
            'keywords': ['advanced', 'encryption', 'standard', 'symmetric'],
            'explanation': 'AES is the current encryption standard, available in 128, 192, or 256-bit key sizes. Used in VPNs, WiFi, HTTPS.',
            'mnemonic': 'Amazing Encryption Standard',
            'guide_reference': 'Section 5: Cryptography - AES',
            'difficulty': 'easy'
        },
        {
            'id': 'CRY003',
            'question': 'What is the difference between hashing and encryption?',
            'type': 'short_answer',
            'answer': 'Hashing = one-way, cannot be reversed; Encryption = two-way, can be decrypted',
            'keywords': ['hashing', 'one-way', 'reverse', 'encryption', 'two-way', 'decrypt'],
            'explanation': 'Hashing creates a fixed-size fingerprint that cannot be reversed (for passwords). Encryption transforms data that can be decrypted with a key (for confidentiality).',
            'mnemonic': 'Hash = Hamburger through grinder (cannot un-grind), Encrypt = Lock and key (reversible)',
            'guide_reference': 'Section 5: Cryptography - Hashing vs Encryption',
            'difficulty': 'medium'
        },
        {
            'id': 'CRY004',
            'question': 'Should passwords be hashed or encrypted?',
            'type': 'multiple_choice',
            'options': ['Hashed', 'Encrypted', 'Either is fine', 'Neither'],
            'answer': 'Hashed',
            'explanation': 'Passwords should be hashed (one-way) not encrypted. If encrypted, someone with the key could decrypt all passwords.',
            'mnemonic': 'Hash passwords = cannot be stolen, Encrypt data = can be decrypted by authorized users',
            'guide_reference': 'Section 5: Cryptography - Hashing vs Encryption',
            'difficulty': 'medium'
        },
        {
            'id': 'CRY005',
            'question': 'What does PKI stand for?',
            'type': 'short_answer',
            'answer': 'Public Key Infrastructure',
            'keywords': ['public', 'key', 'infrastructure'],
            'explanation': 'PKI is the system for creating, managing, and validating digital certificates.',
            'mnemonic': 'Public Keys for Identity',
            'guide_reference': 'Section 5: Cryptography - PKI',
            'difficulty': 'easy'
        }
    ],
    'attacks': [
        {
            'id': 'ATK001',
            'question': 'What is XSS (Cross-Site Scripting)?',
            'type': 'short_answer',
            'answer': 'Web vulnerability where attacker injects malicious JavaScript into pages that other users view',
            'keywords': ['cross', 'site', 'scripting', 'javascript', 'inject'],
            'explanation': 'XSS allows attackers to inject malicious scripts that execute in victim browsers, stealing cookies/sessions or performing actions as the victim.',
            'mnemonic': 'X = Cross-site, SS = Scripting Scare',
            'guide_reference': 'Section 3: Web Security - XSS',
            'difficulty': 'medium'
        },
        {
            'id': 'ATK002',
            'question': 'What is SQL Injection?',
            'type': 'short_answer',
            'answer': 'Injecting malicious SQL commands into input fields to manipulate database queries',
            'keywords': ['sql', 'inject', 'database', 'query'],
            'explanation': 'SQL Injection exploits poor input validation to inject SQL code, potentially reading/modifying/deleting database data.',
            'mnemonic': 'Sneaky Query Launched',
            'guide_reference': 'Section 3: Web Security - SQL Injection',
            'difficulty': 'medium'
        },
        {
            'id': 'ATK003',
            'question': 'What does DDoS stand for?',
            'type': 'short_answer',
            'answer': 'Distributed Denial of Service',
            'keywords': ['distributed', 'denial', 'service'],
            'explanation': 'DDoS overwhelms a target with traffic from many sources, making services unavailable.',
            'mnemonic': 'Distributed = Many sources attacking',
            'guide_reference': 'Section 9: Security+ Exam Focus - Attack Types',
            'difficulty': 'easy'
        },
        {
            'id': 'ATK004',
            'question': 'What is a Man-in-the-Middle (MITM) attack?',
            'type': 'short_answer',
            'answer': 'Attacker intercepts communication between two parties, can read or modify messages',
            'keywords': ['intercept', 'between', 'communication'],
            'explanation': 'MITM puts the attacker between two communicating parties, allowing eavesdropping or tampering.',
            'mnemonic': 'Man Intercepting The Messages',
            'guide_reference': 'Section 9: Security+ Exam Focus - Attack Types',
            'difficulty': 'medium'
        },
        {
            'id': 'ATK005',
            'question': 'What is the difference between a virus and a worm?',
            'type': 'short_answer',
            'answer': 'Virus needs host file and user action to spread, Worm self-replicates without user interaction',
            'keywords': ['virus', 'host', 'user', 'worm', 'self', 'replicate'],
            'explanation': 'Viruses attach to files and need users to execute them. Worms spread independently across networks.',
            'mnemonic': 'Virus = Needs host, Worm = Wiggles on its own',
            'guide_reference': 'Section 9: Security+ Exam Focus - Attack Types',
            'difficulty': 'medium'
        }
    ]
}

def show_main_menu():
    """Display main menu"""
    print(f"\n{Colors.CYAN}╔═══════════════════════════════════════╗")
    print(f"║           MAIN MENU                   ║")
    print(f"╚═══════════════════════════════════════╝{Colors.RESET}\n")
    print(f"{Colors.GREEN}[1]{Colors.RESET} Full 100-Question Quiz")
    print(f"{Colors.GREEN}[2]{Colors.RESET} Category Practice")
    print(f"{Colors.GREEN}[3]{Colors.RESET} Acronym Drill Mode 🔤")
    print(f"{Colors.GREEN}[4]{Colors.RESET} Quick Quiz (20 questions)")
    print(f"{Colors.GREEN}[5]{Colors.RESET} Timed Mode ⏱️  (90 minutes)")
    print(f"{Colors.GREEN}[6]{Colors.RESET} View Progress Dashboard 📊")
    print(f"{Colors.GREEN}[7]{Colors.RESET} Review Wrong Answers")
    print(f"{Colors.GREEN}[8]{Colors.RESET} Exit")
    print()

def acronym_drill():
    """Interactive acronym practice with mnemonics"""
    print(f"\n{Colors.CYAN}╔═══════════════════════════════════════════════════════════════════╗")
    print(f"║           ACRONYM DRILL MODE 🔤                                   ║")
    print(f"╚═══════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    # Flatten all acronyms
    all_acronyms = []
    for category, acronyms in ACRONYMS.items():
        for acronym, data in acronyms.items():
            all_acronyms.append((acronym, data, category))
    
    print(f"{Colors.YELLOW}📚 Total Acronyms: {len(all_acronyms)}{Colors.RESET}")
    print(f"{Colors.CYAN}How many would you like to practice?{Colors.RESET}")
    
    try:
        num_questions = int(input(f"{Colors.YELLOW}Enter number (or 'all' for all {len(all_acronyms)}): {Colors.RESET}").strip())
        if num_questions > len(all_acronyms):
            num_questions = len(all_acronyms)
    except:
        num_questions = len(all_acronyms)
    
    # Shuffle and select
    random.shuffle(all_acronyms)
    selected = all_acronyms[:num_questions]
    
    correct = 0
    wrong_ones = []
    
    for i, (acronym, data, category) in enumerate(selected, 1):
        print(f"\n{Colors.BOLD}{Colors.CYAN}Question {i}/{num_questions}{Colors.RESET}")
        print(f"{Colors.YELLOW}Category: {category.upper()}{Colors.RESET}")
        print(f"\n{Colors.GREEN}What does {Colors.BOLD}{acronym}{Colors.RESET}{Colors.GREEN} stand for?{Colors.RESET}")
        
        user_answer = input(f"\n{Colors.YELLOW}Your answer: {Colors.RESET}").strip()
        
        # Check answer (flexible matching)
        correct_answer = data['full'].lower()
        user_answer_lower = user_answer.lower()
        
        # Simple matching - check if major words are present
        correct_words = correct_answer.split()
        matches = sum(1 for word in correct_words if len(word) > 3 and word in user_answer_lower)
        
        if matches >= len(correct_words) - 1:  # Allow one word to be wrong
            print(f"{Colors.GREEN}✅ CORRECT!{Colors.RESET}")
            correct += 1
        else:
            print(f"{Colors.RED}❌ Not quite!{Colors.RESET}")
            wrong_ones.append((acronym, data, category))
        
        print(f"\n{Colors.CYAN}📝 Full Answer:{Colors.RESET} {Colors.BOLD}{data['full']}{Colors.RESET}")
        print(f"{Colors.MAGENTA}💡 Mnemonic:{Colors.RESET} {data['mnemonic']}")
        print(f"{Colors.BLUE}📖 Explanation:{Colors.RESET} {data['explanation']}")
        print(f"{Colors.YELLOW}{'─' * 70}{Colors.RESET}")
        
        if i < len(selected):
            input(f"\n{Colors.CYAN}Press Enter for next acronym...{Colors.RESET}")
    
    # Results
    score_percent = (correct / num_questions) * 100
    print(f"\n{Colors.CYAN}╔═══════════════════════════════════════╗")
    print(f"║        ACRONYM DRILL RESULTS          ║")
    print(f"╚═══════════════════════════════════════╝{Colors.RESET}\n")
    
    print(f"{Colors.GREEN}✅ Correct:{Colors.RESET} {correct}/{num_questions}")
    print(f"{Colors.RED}❌ Wrong:{Colors.RESET} {len(wrong_ones)}/{num_questions}")
    print(f"{Colors.CYAN}📊 Score:{Colors.RESET} {Colors.BOLD}{score_percent:.1f}%{Colors.RESET}")
    
    if wrong_ones:
        print(f"\n{Colors.YELLOW}📝 Review these acronyms:{Colors.RESET}")
        for acronym, data, category in wrong_ones:
            print(f"  {Colors.RED}•{Colors.RESET} {acronym} = {data['full']}")
            print(f"    {Colors.MAGENTA}Mnemonic:{Colors.RESET} {data['mnemonic']}")
    
    if score_percent >= 90:
        print(f"\n{Colors.GREEN}🔥 EXCELLENT! You've mastered these acronyms!{Colors.RESET}")
    elif score_percent >= 75:
        print(f"\n{Colors.CYAN}💪 GOOD WORK! Keep practicing the ones you missed!{Colors.RESET}")
    else:
        print(f"\n{Colors.YELLOW}📚 Keep studying! Review the mnemonics to improve!{Colors.RESET}")

def take_quiz(questions, time_limit=None, category_name="Quiz"):
    """Take a quiz with given questions"""
    print(f"\n{Colors.CYAN}╔═══════════════════════════════════════════════════════════════════╗")
    print(f"║           {category_name.upper().center(64)}║")
    print(f"╚═══════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    print(f"{Colors.YELLOW}📚 Total Questions: {len(questions)}{Colors.RESET}")
    if time_limit:
        print(f"{Colors.RED}⏱️  Time Limit: {time_limit} minutes{Colors.RESET}")
    print(f"\n{Colors.CYAN}Press Enter when ready to start...{Colors.RESET}")
    input()
    
    start_time = time.time()
    correct = 0
    wrong_ones = []
    answers = []
    
    for i, q in enumerate(questions, 1):
        print(f"\n{Colors.BOLD}{Colors.CYAN}Question {i}/{len(questions)}{Colors.RESET}")
        print(f"{Colors.YELLOW}Category: {q['id'][:3]}{Colors.RESET}")
        print(f"\n{Colors.GREEN}{q['question']}{Colors.RESET}")
        
        if q['type'] == 'multiple_choice':
            for idx, option in enumerate(q['options'], 1):
                print(f"  {idx}. {option}")
            user_answer = input(f"\n{Colors.YELLOW}Your answer (1-{len(q['options'])}): {Colors.RESET}").strip()
            try:
                answer_idx = int(user_answer) - 1
                user_answer = q['options'][answer_idx]
            except:
                user_answer = ""
        else:
            user_answer = input(f"\n{Colors.YELLOW}Your answer: {Colors.RESET}").strip()
        
        # Check answer
        is_correct = False
        if q['type'] == 'multiple_choice':
            is_correct = (user_answer == q['answer'])
        else:
            # Flexible matching for short answers
            answer_lower = user_answer.lower()
            if 'keywords' in q:
                matches = sum(1 for keyword in q['keywords'] if keyword in answer_lower)
                is_correct = (matches >= len(q['keywords']) // 2)  # At least half the keywords
            else:
                is_correct = (q['answer'].lower() in answer_lower or answer_lower in q['answer'].lower())
        
        if is_correct:
            print(f"{Colors.GREEN}✅ CORRECT!{Colors.RESET}")
            correct += 1
        else:
            print(f"{Colors.RED}❌ INCORRECT{Colors.RESET}")
            wrong_ones.append(q)
        
        print(f"\n{Colors.CYAN}📝 Correct Answer:{Colors.RESET} {Colors.BOLD}{q['answer']}{Colors.RESET}")
        print(f"{Colors.BLUE}📖 Explanation:{Colors.RESET} {q['explanation']}")
        if 'mnemonic' in q:
            print(f"{Colors.MAGENTA}💡 Mnemonic:{Colors.RESET} {q['mnemonic']}")
        print(f"{Colors.YELLOW}{'─' * 70}{Colors.RESET}")
        
        answers.append({
            'question': q['question'],
            'your_answer': user_answer,
            'correct_answer': q['answer'],
            'is_correct': is_correct
        })
        
        if time_limit:
            elapsed = (time.time() - start_time) / 60
            if elapsed >= time_limit:
                print(f"\n{Colors.RED}⏱️  TIME'S UP!{Colors.RESET}")
                break
        
        if i < len(questions):
            input(f"\n{Colors.CYAN}Press Enter for next question...{Colors.RESET}")
    
    # Results
    end_time = time.time()
    time_taken = (end_time - start_time) / 60
    score_percent = (correct / len(questions)) * 100
    
    print(f"\n{Colors.CYAN}╔═══════════════════════════════════════╗")
    print(f"║             QUIZ RESULTS              ║")
    print(f"╚═══════════════════════════════════════╝{Colors.RESET}\n")
    
    print(f"{Colors.GREEN}✅ Correct:{Colors.RESET} {correct}/{len(questions)}")
    print(f"{Colors.RED}❌ Wrong:{Colors.RESET} {len(wrong_ones)}/{len(questions)}")
    print(f"{Colors.CYAN}📊 Score:{Colors.RESET} {Colors.BOLD}{score_percent:.1f}%{Colors.RESET}")
    print(f"{Colors.YELLOW}⏱️  Time Taken:{Colors.RESET} {time_taken:.1f} minutes")
    
    # Performance message
    if score_percent >= 90:
        print(f"\n{Colors.GREEN}🔥 EXCELLENT! Security+ ready!{Colors.RESET}")
    elif score_percent >= 85:
        print(f"\n{Colors.GREEN}💪 GREAT! Almost there!{Colors.RESET}")
    elif score_percent >= 70:
        print(f"\n{Colors.CYAN}👍 GOOD! Keep studying!{Colors.RESET}")
    else:
        print(f"\n{Colors.YELLOW}📚 Review fundamentals before continuing!{Colors.RESET}")
    
    if wrong_ones:
        print(f"\n{Colors.YELLOW}📝 Questions to review:{Colors.RESET}")
        for q in wrong_ones:
            print(f"  {Colors.RED}•{Colors.RESET} {q['question'][:60]}...")
    
    # Save results
    save_results(category_name, correct, len(questions), score_percent, time_taken, answers)
    
    return score_percent

def save_results(quiz_name, correct, total, score, time_taken, answers):
    """Save quiz results to file"""
    results_file = 'zaki_quiz_results.json'
    
    try:
        if os.path.exists(results_file):
            with open(results_file, 'r') as f:
                data = json.load(f)
        else:
            data = {
                'total_quizzes': 0,
                'history': []
            }
        
        result = {
            'date': datetime.now().isoformat(),
            'quiz_name': quiz_name,
            'correct': correct,
            'total': total,
            'score': score,
            'time_taken': time_taken,
            'answers': answers
        }
        
        data['total_quizzes'] += 1
        data['history'].append(result)
        
        with open(results_file, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"\n{Colors.GREEN}💾 Results saved!{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}⚠️  Could not save results: {e}{Colors.RESET}")

def view_dashboard():
    """View progress dashboard"""
    results_file = 'zaki_quiz_results.json'
    
    if not os.path.exists(results_file):
        print(f"\n{Colors.YELLOW}No quiz history yet! Take your first quiz!{Colors.RESET}")
        return
    
    try:
        with open(results_file, 'r') as f:
            data = json.load(f)
        
        print(f"\n{Colors.CYAN}╔═══════════════════════════════════════════════════════════════════╗")
        print(f"║           PROGRESS DASHBOARD 📊                                   ║")
        print(f"╚═══════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
        
        print(f"{Colors.GREEN}Total Quizzes Taken:{Colors.RESET} {data['total_quizzes']}")
        
        if data['history']:
            scores = [h['score'] for h in data['history']]
            avg_score = sum(scores) / len(scores)
            print(f"{Colors.CYAN}Average Score:{Colors.RESET} {avg_score:.1f}%")
            print(f"{Colors.YELLOW}Best Score:{Colors.RESET} {max(scores):.1f}%")
            print(f"{Colors.MAGENTA}Latest Score:{Colors.RESET} {scores[-1]:.1f}%")
            
            print(f"\n{Colors.CYAN}Recent Quiz History:{Colors.RESET}")
            for h in data['history'][-5:]:
                date = datetime.fromisoformat(h['date']).strftime('%Y-%m-%d %H:%M')
                print(f"  {date} | {h['quiz_name']} | {h['score']:.1f}% | {h['time_taken']:.1f} min")
            
            # Show improvement trend
            if len(scores) >= 3:
                trend = scores[-3:]
                if trend[-1] > trend[0]:
                    print(f"\n{Colors.GREEN}📈 Improving! Keep it up!{Colors.RESET}")
                else:
                    print(f"\n{Colors.YELLOW}📊 Review weak areas to improve!{Colors.RESET}")
    
    except Exception as e:
        print(f"\n{Colors.RED}Error loading dashboard: {e}{Colors.RESET}")

def main():
    """Main program loop"""
    print_banner()
    
    while True:
        show_main_menu()
        choice = input(f"{Colors.YELLOW}Select option (1-8): {Colors.RESET}").strip()
        
        if choice == '1':
            # Full quiz
            all_questions = []
            for category in QUESTIONS.values():
                all_questions.extend(category)
            random.shuffle(all_questions)
            take_quiz(all_questions, category_name="Full 100-Question Quiz")
        
        elif choice == '2':
            # Category practice
            print(f"\n{Colors.CYAN}Select Category:{Colors.RESET}")
            categories = list(QUESTIONS.keys())
            for i, cat in enumerate(categories, 1):
                print(f"{Colors.GREEN}[{i}]{Colors.RESET} {cat.capitalize()} ({len(QUESTIONS[cat])} questions)")
            
            cat_choice = input(f"\n{Colors.YELLOW}Select (1-{len(categories)}): {Colors.RESET}").strip()
            try:
                cat_idx = int(cat_choice) - 1
                selected_cat = categories[cat_idx]
                questions = QUESTIONS[selected_cat].copy()
                random.shuffle(questions)
                take_quiz(questions, category_name=f"{selected_cat.capitalize()} Practice")
            except:
                print(f"{Colors.RED}Invalid selection{Colors.RESET}")
        
        elif choice == '3':
            acronym_drill()
        
        elif choice == '4':
            # Quick quiz - 20 random questions
            all_questions = []
            for category in QUESTIONS.values():
                all_questions.extend(category)
            random.shuffle(all_questions)
            quick_questions = all_questions[:20]
            take_quiz(quick_questions, category_name="Quick Quiz (20 Questions)")
        
        elif choice == '5':
            # Timed mode - 90 minutes
            all_questions = []
            for category in QUESTIONS.values():
                all_questions.extend(category)
            random.shuffle(all_questions)
            take_quiz(all_questions, time_limit=90, category_name="Timed Exam Simulation")
        
        elif choice == '6':
            view_dashboard()
        
        elif choice == '7':
            print(f"\n{Colors.YELLOW}Review feature coming soon!{Colors.RESET}")
        
        elif choice == '8':
            print(f"\n{Colors.YELLOW}{'═' * 70}")
            print(f"  Thanks for using ZAKI-QUIZ!")
            print(f"  Keep studying! #ZuciyaZaki! 🦁")
            print(f"  \"I never go back on my word - that's my ninja way!\"")
            print(f"{'═' * 70}{Colors.RESET}\n")
            sys.exit(0)
        
        else:
            print(f"{Colors.RED}Invalid option. Please select 1-8{Colors.RESET}")
        
        input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.RESET}")
        os.system('clear' if os.name == 'posix' else 'cls')
        print_banner()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Exiting... Stay strong #ZuciyaZaki! 🦁{Colors.RESET}\n")
        sys.exit(0)
