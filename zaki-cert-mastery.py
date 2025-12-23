#!/usr/bin/env python3
"""
ZAKI-CERT-MASTER V1.0: Ultimate Certification Preparation Platform
Created by: Zuciya Zaki (Dominic Metz)
Purpose: Adaptive learning system for Security 101, Security+, Network+ and beyond
Day 33+ - "I never go back on my word! That's my ninja way!"

FEATURES:
🎯 Confidence-Based Learning - Rate your certainty, focus on weak spots
🧠 Spaced Repetition (SM-2) - Scientific memory optimization
📚 Multi-Format Questions - Test concepts from every angle
🎮 Real SOC Scenarios - Practical incident response situations
💡 Mistake Pattern Analysis - AI-driven weakness detection
⚡ Exam Simulation Modes - Practice, Timed, Nightmare difficulty
📊 Advanced Analytics - Track improvement over time
🔗 Tool Integration - Links to zaki-john, zaki-msf, study guide
"""

import sys
import os
import json
import random
import time
from datetime import datetime, timedelta
from collections import defaultdict
import math

# ============================================================================
# COLOR DEFINITIONS
# ============================================================================

class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    UNDERLINE = '\033[4m'
    
    # Standard colors
    BLACK = '\033[30m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    
    # Background colors
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'

# ============================================================================
# BANNER
# ============================================================================

def print_banner():
    """Display Zuciya Zaki branded banner"""
    banner = f"""{Colors.YELLOW}
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║      ███████╗ █████╗ ██╗  ██╗██╗    ██████╗███████╗██████╗ ████████╗║
║      ╚══███╔╝██╔══██╗██║ ██╔╝██║   ██╔════╝██╔════╝██╔══██╗╚══██╔══╝║
║        ███╔╝ ███████║█████╔╝ ██║   ██║     █████╗  ██████╔╝   ██║   ║
║       ███╔╝  ██╔══██║██╔═██╗ ██║   ██║     ██╔══╝  ██╔══██╗   ██║   ║
║      ███████╗██║  ██║██║  ██╗██║   ╚██████╗███████╗██║  ██║   ██║   ║
║      ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝    ╚═════╝╚══════╝╚═╝  ╚═╝   ╚═╝   ║
║                                                                      ║
║              ███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗    ║
║              ████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗   ║
║              ██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝   ║
║              ██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗   ║
║              ██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║   ║
║              ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝   ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
{Colors.RESET}
{Colors.CYAN}╔══════════════════════════════════════════════════════════════════════╗
║         CERTIFICATION PREPARATION MASTER PLATFORM V1.0               ║
║    🎯 Adaptive Learning | 🧠 Spaced Repetition | 📊 Analytics        ║
╚══════════════════════════════════════════════════════════════════════╝{Colors.RESET}
"""
    print(banner)

# ============================================================================
# QUESTION DATABASE - Security 101 Questions
# ============================================================================

QUESTION_BANK = {
    # NETWORKING FUNDAMENTALS
    "SEC101_NET_001": {
        "metadata": {
            "category": "networking_fundamentals",
            "difficulty": "easy",
            "tags": ["ssh", "ports", "remote_access"]
        },
        "questions": {
            "primary": {
                "type": "multiple_choice",
                "text": "Which port does SSH use by default?",
                "options": ["21", "22", "23", "25"],
                "answer": "22"
            },
            "variants": [
                {
                    "type": "scenario",
                    "text": "You see 50 failed login attempts on port 22 in your SIEM logs. What service is being targeted?",
                    "answer": "SSH",
                    "keywords": ["ssh", "secure shell"]
                }
            ]
        },
        "learning": {
            "explanation": "SSH (Secure Shell) uses port 22 by default for encrypted remote access. This is one of the most important ports as it's commonly targeted for brute force attacks.",
            "mnemonic": "Two Twos = 22 (SSH has two S's, port has two 2's)",
            "study_guide": "Section 1: Networking Fundamentals - Ports",
            "soc_relevance": "SOC analysts monitor port 22 for SSH brute force attacks. Multiple failed attempts indicate password guessing.",
            "tools": ["nmap -p22 <target>", "auxiliary/scanner/ssh/ssh_login (from zaki-msf.py)"]
        }
    },
    
    "SEC101_NET_002": {
        "metadata": {
            "category": "networking_fundamentals",
            "difficulty": "easy",
            "tags": ["tcp", "udp", "protocols"]
        },
        "questions": {
            "primary": {
                "type": "multiple_choice",
                "text": "Which protocol is connection-oriented and guarantees delivery?",
                "options": ["UDP", "TCP", "ICMP", "ARP"],
                "answer": "TCP"
            },
            "variants": [
                {
                    "type": "short_answer",
                    "text": "What is the main difference between TCP and UDP?",
                    "answer": "TCP is connection-oriented and reliable, UDP is connectionless and faster but unreliable",
                    "keywords": ["tcp", "reliable", "connection", "udp", "fast", "connectionless"]
                }
            ]
        },
        "learning": {
            "explanation": "TCP (Transmission Control Protocol) is connection-oriented with a 3-way handshake (SYN, SYN-ACK, ACK) and guarantees packet delivery. UDP is connectionless and faster but doesn't guarantee delivery.",
            "mnemonic": "TCP = Takes Care of Packets | UDP = Usually Drops Packets",
            "study_guide": "Section 1: Networking Fundamentals - TCP vs UDP",
            "soc_relevance": "Understanding TCP vs UDP helps SOC analysts identify attack types. TCP SYN floods are different from UDP amplification attacks.",
            "tools": []
        }
    },
    
    "SEC101_NET_003": {
        "metadata": {
            "category": "networking_fundamentals",
            "difficulty": "medium",
            "tags": ["osi_model", "layers"]
        },
        "questions": {
            "primary": {
                "type": "multiple_choice",
                "text": "At which OSI layer do routers operate?",
                "options": ["Layer 2 (Data Link)", "Layer 3 (Network)", "Layer 4 (Transport)", "Layer 7 (Application)"],
                "answer": "Layer 3 (Network)"
            },
            "variants": [
                {
                    "type": "short_answer",
                    "text": "Name all 7 layers of the OSI Model from bottom to top.",
                    "answer": "Physical, Data Link, Network, Transport, Session, Presentation, Application",
                    "keywords": ["physical", "data link", "network", "transport", "session", "presentation", "application"]
                }
            ]
        },
        "learning": {
            "explanation": "Routers operate at Layer 3 (Network) using IP addresses to route traffic between different networks. Switches operate at Layer 2 using MAC addresses.",
            "mnemonic": "Please Do Not Throw Sausage Pizza Away (Physical, Data Link, Network, Transport, Session, Presentation, Application)",
            "study_guide": "Section 1: Networking Fundamentals - OSI Model",
            "soc_relevance": "Understanding OSI layers helps identify attack types: Layer 2 = ARP spoofing, Layer 3 = IP spoofing, Layer 7 = HTTP attacks.",
            "tools": []
        }
    },
    
    "SEC101_NET_004": {
        "metadata": {
            "category": "networking_fundamentals",
            "difficulty": "easy",
            "tags": ["dns", "domain_names"]
        },
        "questions": {
            "primary": {
                "type": "short_answer",
                "text": "What does DNS do?",
                "answer": "Translates domain names to IP addresses",
                "keywords": ["translate", "domain", "name", "ip", "address"]
            },
            "variants": []
        },
        "learning": {
            "explanation": "DNS (Domain Name System) is the internet's phone book - it converts human-readable domain names (google.com) into IP addresses (142.250.80.46) that computers use.",
            "mnemonic": "Don't Need to remember Server addresses",
            "study_guide": "Section 1: Networking Fundamentals - DNS",
            "soc_relevance": "SOC analysts monitor DNS for malicious domains, DNS tunneling (using DNS for data exfiltration), and command & control communication.",
            "tools": ["nslookup", "dig", "DNS logs in SIEM"]
        }
    },
    
    "SEC101_NET_005": {
        "metadata": {
            "category": "networking_fundamentals",
            "difficulty": "easy",
            "tags": ["http", "https", "ports"]
        },
        "questions": {
            "primary": {
                "type": "multiple_choice",
                "text": "Which port does HTTPS use by default?",
                "options": ["80", "443", "8080", "8443"],
                "answer": "443"
            },
            "variants": [
                {
                    "type": "short_answer",
                    "text": "What is the main difference between HTTP and HTTPS?",
                    "answer": "HTTPS is encrypted with TLS/SSL, HTTP is unencrypted plaintext",
                    "keywords": ["https", "encrypted", "tls", "ssl", "http", "plaintext", "unencrypted"]
                }
            ]
        },
        "learning": {
            "explanation": "HTTPS uses port 443 for encrypted web traffic using TLS/SSL. HTTP uses port 80 for unencrypted plaintext communication.",
            "mnemonic": "4-4-3 = For Fortress Security | H-T-80 for HTTP",
            "study_guide": "Section 1: Networking Fundamentals - HTTP vs HTTPS",
            "soc_relevance": "SOC analysts flag HTTP on sensitive pages (login/payment). Credentials sent over HTTP are visible in plaintext to attackers.",
            "tools": ["Wireshark to capture HTTP vs HTTPS traffic"]
        }
    },
    
    # SECURITY FUNDAMENTALS
    "SEC101_SEC_001": {
        "metadata": {
            "category": "security_fundamentals",
            "difficulty": "easy",
            "tags": ["cia_triad", "confidentiality", "integrity", "availability"]
        },
        "questions": {
            "primary": {
                "type": "short_answer",
                "text": "What does the CIA Triad stand for in security?",
                "answer": "Confidentiality, Integrity, Availability",
                "keywords": ["confidentiality", "integrity", "availability"]
            },
            "variants": [
                {
                    "type": "scenario",
                    "text": "A ransomware attack encrypts all files on a server. Which parts of the CIA Triad are violated?",
                    "answer": "Integrity and Availability",
                    "keywords": ["integrity", "availability", "both"]
                }
            ]
        },
        "learning": {
            "explanation": "The CIA Triad represents three pillars of information security: Confidentiality (only authorized access), Integrity (data hasn't been tampered), Availability (accessible when needed).",
            "mnemonic": "Can I Access? Is It Intact? Always Accessible?",
            "study_guide": "Section 2: Security Fundamentals - CIA Triad",
            "soc_relevance": "SOC analysts classify incidents by CIA impact to determine severity. Data breach = Confidentiality, file corruption = Integrity, DDoS = Availability.",
            "tools": []
        }
    },
    
    "SEC101_SEC_002": {
        "metadata": {
            "category": "security_fundamentals",
            "difficulty": "medium",
            "tags": ["authentication", "authorization"]
        },
        "questions": {
            "primary": {
                "type": "multiple_choice",
                "text": "What is the difference between authentication and authorization?",
                "options": [
                    "Authentication is WHO you are, Authorization is WHAT you can do",
                    "They are the same thing",
                    "Authentication is WHAT you can do, Authorization is WHO you are",
                    "Authorization happens before authentication"
                ],
                "answer": "Authentication is WHO you are, Authorization is WHAT you can do"
            },
            "variants": []
        },
        "learning": {
            "explanation": "Authentication verifies identity (username/password = WHO are you?). Authorization determines permissions (WHAT can you access?). Authentication always happens BEFORE authorization.",
            "mnemonic": "Authentication = WHO, Authorization = WHAT",
            "study_guide": "Section 2: Security Fundamentals - AAA Framework",
            "soc_relevance": "SOC analysts investigate both authentication failures (failed logins) and authorization violations (privilege escalation, unauthorized access attempts).",
            "tools": ["Active Directory logs", "SIEM correlation rules"]
        }
    },
    
    "SEC101_SEC_003": {
        "metadata": {
            "category": "security_fundamentals",
            "difficulty": "medium",
            "tags": ["ids", "ips"]
        },
        "questions": {
            "primary": {
                "type": "multiple_choice",
                "text": "What is the key difference between IDS and IPS?",
                "options": [
                    "IDS detects and alerts, IPS detects and blocks",
                    "IDS blocks attacks, IPS only alerts",
                    "They are the same thing",
                    "IDS is hardware, IPS is software"
                ],
                "answer": "IDS detects and alerts, IPS detects and blocks"
            },
            "variants": []
        },
        "learning": {
            "explanation": "IDS (Intrusion Detection System) passively monitors and alerts on threats. IPS (Intrusion Prevention System) actively blocks threats inline. IDS = Security camera, IPS = Security guard.",
            "mnemonic": "IDS = I Detect Suspicious | IPS = I Prevent Suspicious",
            "study_guide": "Section 7: Security Tools - IDS vs IPS",
            "soc_relevance": "SOC analysts monitor IDS alerts for threats and tune IPS to prevent false positives from blocking legitimate traffic.",
            "tools": ["Snort (IDS/IPS)", "Suricata", "SIEM integration"]
        }
    },
    
    "SEC101_SEC_004": {
        "metadata": {
            "category": "security_fundamentals",
            "difficulty": "easy",
            "tags": ["mfa", "2fa", "authentication"]
        },
        "questions": {
            "primary": {
                "type": "short_answer",
                "text": "What are the three factors in Multi-Factor Authentication (MFA)?",
                "answer": "Something you KNOW, something you HAVE, something you ARE",
                "keywords": ["know", "have", "are", "password", "token", "biometric"]
            },
            "variants": [
                {
                    "type": "multiple_choice",
                    "text": "Which of the following is an example of 'something you HAVE' in MFA?",
                    "options": ["Password", "Phone/token", "Fingerprint", "Username"],
                    "answer": "Phone/token"
                }
            ]
        },
        "learning": {
            "explanation": "MFA uses 2+ verification methods from different factor types: KNOW (password/PIN), HAVE (phone/token/card), ARE (fingerprint/face/biometric).",
            "mnemonic": "Multiple Factors = Awesome security | KNOW-HAVE-ARE",
            "study_guide": "Section 2: Security Fundamentals - MFA",
            "soc_relevance": "SOC analysts monitor MFA bypass attempts, fatigue attacks (spamming push notifications), and enforce MFA on critical systems.",
            "tools": []
        }
    },
    
    "SEC101_SEC_005": {
        "metadata": {
            "category": "security_fundamentals",
            "difficulty": "easy",
            "tags": ["least_privilege"]
        },
        "questions": {
            "primary": {
                "type": "short_answer",
                "text": "What is the principle of Least Privilege?",
                "answer": "Give users minimum permissions needed for their job, nothing more",
                "keywords": ["minimum", "permissions", "needed", "least", "necessary"]
            },
            "variants": []
        },
        "learning": {
            "explanation": "Least Privilege means giving users only the minimum access/permissions they need to do their job. Don't give admin rights unless absolutely necessary.",
            "mnemonic": "Least = Minimum needed, nothing more",
            "study_guide": "Section 4: System Security - Least Privilege",
            "soc_relevance": "SOC analysts review accounts with excessive permissions, investigate privilege escalation, and conduct regular access reviews.",
            "tools": ["Active Directory permission audits", "SIEM privilege monitoring"]
        }
    },
    
    # WEB SECURITY
    "SEC101_WEB_001": {
        "metadata": {
            "category": "web_security",
            "difficulty": "medium",
            "tags": ["xss", "cross_site_scripting"]
        },
        "questions": {
            "primary": {
                "type": "short_answer",
                "text": "What is Cross-Site Scripting (XSS)?",
                "answer": "Web vulnerability where attacker injects malicious JavaScript into pages that other users view",
                "keywords": ["javascript", "inject", "malicious", "script", "users", "browser"]
            },
            "variants": [
                {
                    "type": "multiple_choice",
                    "text": "Which type of XSS is most dangerous?",
                    "options": ["Reflected XSS", "Stored XSS", "DOM-based XSS", "All are equally dangerous"],
                    "answer": "Stored XSS"
                }
            ]
        },
        "learning": {
            "explanation": "XSS allows attackers to inject malicious JavaScript that executes in victim browsers. Stored XSS (saved in database) is most dangerous as it affects all users who view the page.",
            "mnemonic": "X = Cross-site, SS = Scripting Scare",
            "study_guide": "Section 3: Web Security - XSS",
            "soc_relevance": "SOC analysts monitor WAF logs for XSS injection attempts, looking for <script> tags and JavaScript payloads in web requests.",
            "tools": ["WAF logs", "Burp Suite", "XSS detection rules in SIEM"]
        }
    },
    
    "SEC101_WEB_002": {
        "metadata": {
            "category": "web_security",
            "difficulty": "medium",
            "tags": ["sql_injection"]
        },
        "questions": {
            "primary": {
                "type": "short_answer",
                "text": "What is SQL Injection?",
                "answer": "Injecting malicious SQL commands into input fields to manipulate database queries",
                "keywords": ["sql", "inject", "database", "query", "commands"]
            },
            "variants": [
                {
                    "type": "multiple_choice",
                    "text": "What does the SQL comment symbol '--' do in SQL injection?",
                    "options": [
                        "Comments out the rest of the query",
                        "Executes the command",
                        "Creates a new database",
                        "Nothing, it's ignored"
                    ],
                    "answer": "Comments out the rest of the query"
                }
            ]
        },
        "learning": {
            "explanation": "SQL Injection exploits poor input validation to inject SQL code, potentially reading/modifying/deleting database data. Example: ' OR 1=1-- bypasses login by making the query always true.",
            "mnemonic": "Sneaky Query Launched",
            "study_guide": "Section 3: Web Security - SQL Injection",
            "soc_relevance": "SOC analysts monitor for SQL keywords (UNION, DROP, SELECT) in web application logs and investigate database errors that indicate injection attempts.",
            "tools": ["WAF alerts", "Database logs", "sqlmap for testing"]
        }
    },
    
    "SEC101_WEB_003": {
        "metadata": {
            "category": "web_security",
            "difficulty": "hard",
            "tags": ["csrf", "cross_site_request_forgery"]
        },
        "questions": {
            "primary": {
                "type": "short_answer",
                "text": "What is CSRF (Cross-Site Request Forgery)?",
                "answer": "Tricks authenticated user into executing unwanted actions on a web application",
                "keywords": ["authenticated", "user", "unwanted", "action", "trick", "request"]
            },
            "variants": []
        },
        "learning": {
            "explanation": "CSRF tricks an authenticated user's browser into sending forged requests. Example: User logged into bank.com visits malicious site that sends hidden request to transfer money.",
            "mnemonic": "Cross-Site Request Fakery",
            "study_guide": "Section 3: Web Security - CSRF",
            "soc_relevance": "SOC analysts look for state-changing requests without CSRF tokens and investigate unusual authenticated actions from suspicious sources.",
            "tools": ["WAF CSRF protection", "Session monitoring"]
        }
    },
    
    # CRYPTOGRAPHY
    "SEC101_CRY_001": {
        "metadata": {
            "category": "cryptography",
            "difficulty": "medium",
            "tags": ["symmetric", "asymmetric", "encryption"]
        },
        "questions": {
            "primary": {
                "type": "multiple_choice",
                "text": "What is the main difference between symmetric and asymmetric encryption?",
                "options": [
                    "Symmetric uses same key for encrypt/decrypt, Asymmetric uses public/private key pair",
                    "Symmetric is slower than Asymmetric",
                    "They are the same thing",
                    "Symmetric is newer than Asymmetric"
                ],
                "answer": "Symmetric uses same key for encrypt/decrypt, Asymmetric uses public/private key pair"
            },
            "variants": [
                {
                    "type": "multiple_choice",
                    "text": "Which encryption type is faster?",
                    "options": ["Symmetric", "Asymmetric", "Same speed", "Depends on key size"],
                    "answer": "Symmetric"
                }
            ]
        },
        "learning": {
            "explanation": "Symmetric encryption uses ONE shared key (AES, DES). Asymmetric uses public/private key pair (RSA, ECC). Symmetric is MUCH faster but requires secure key exchange.",
            "mnemonic": "Same Secret Shared vs A key for All (public), a key for me (private)",
            "study_guide": "Section 5: Cryptography - Symmetric vs Asymmetric",
            "soc_relevance": "Understanding encryption helps SOC analysts identify encrypted traffic, detect weak encryption usage, and investigate data exfiltration attempts.",
            "tools": []
        }
    },
    
    "SEC101_CRY_002": {
        "metadata": {
            "category": "cryptography",
            "difficulty": "medium",
            "tags": ["hashing", "encryption"]
        },
        "questions": {
            "primary": {
                "type": "multiple_choice",
                "text": "What is the key difference between hashing and encryption?",
                "options": [
                    "Hashing is one-way (cannot be reversed), Encryption is two-way (can be decrypted)",
                    "They are the same thing",
                    "Hashing is two-way, Encryption is one-way",
                    "Hashing is faster than encryption"
                ],
                "answer": "Hashing is one-way (cannot be reversed), Encryption is two-way (can be decrypted)"
            },
            "variants": [
                {
                    "type": "multiple_choice",
                    "text": "Should passwords be hashed or encrypted?",
                    "options": ["Hashed", "Encrypted", "Either is fine", "Neither"],
                    "answer": "Hashed"
                }
            ]
        },
        "learning": {
            "explanation": "Hashing creates a one-way fingerprint (can't be reversed) - use for passwords. Encryption is two-way (can be decrypted with key) - use for data protection.",
            "mnemonic": "Hash = Hamburger through grinder (can't un-grind), Encrypt = Lock and key (reversible)",
            "study_guide": "Section 5: Cryptography - Hashing vs Encryption",
            "soc_relevance": "SOC analysts verify password storage uses hashing (bcrypt, Argon2), not encryption. If passwords are encrypted, attackers with the key can decrypt ALL passwords.",
            "tools": ["Check zaki-john.py for hash identification"]
        }
    },
    
    "SEC101_CRY_003": {
        "metadata": {
            "category": "cryptography",
            "difficulty": "easy",
            "tags": ["aes"]
        },
        "questions": {
            "primary": {
                "type": "short_answer",
                "text": "What does AES stand for?",
                "answer": "Advanced Encryption Standard",
                "keywords": ["advanced", "encryption", "standard"]
            },
            "variants": [
                {
                    "type": "multiple_choice",
                    "text": "AES is what type of encryption?",
                    "options": ["Symmetric", "Asymmetric", "Hash function", "Digital signature"],
                    "answer": "Symmetric"
                }
            ]
        },
        "learning": {
            "explanation": "AES (Advanced Encryption Standard) is the current symmetric encryption standard. Available in 128, 192, or 256-bit key sizes. Used in VPNs, WiFi (WPA2/WPA3), HTTPS, disk encryption.",
            "mnemonic": "Amazing Encryption Standard",
            "study_guide": "Section 5: Cryptography - AES",
            "soc_relevance": "SOC analysts check encryption strength in configurations. AES-256 is recommended for sensitive data. Deprecated algorithms like DES should trigger alerts.",
            "tools": []
        }
    },
    
    # ATTACKS
    "SEC101_ATK_001": {
        "metadata": {
            "category": "attacks",
            "difficulty": "easy",
            "tags": ["ddos", "denial_of_service"]
        },
        "questions": {
            "primary": {
                "type": "short_answer",
                "text": "What does DDoS stand for?",
                "answer": "Distributed Denial of Service",
                "keywords": ["distributed", "denial", "service"]
            },
            "variants": [
                {
                    "type": "scenario",
                    "text": "Your web server receives 100,000 requests per second from 5,000 different IP addresses, causing it to crash. What attack is this?",
                    "answer": "DDoS",
                    "keywords": ["ddos", "distributed denial of service"]
                }
            ]
        },
        "learning": {
            "explanation": "DDoS (Distributed Denial of Service) overwhelms a target with traffic from MANY sources (distributed), making services unavailable. Different from DoS which comes from one source.",
            "mnemonic": "Distributed = Many sources attacking at once",
            "study_guide": "Section 9: Security+ Exam Focus - Attack Types",
            "soc_relevance": "SOC analysts detect DDoS by monitoring traffic spikes, connection counts, and service performance. Response involves rate limiting, blocking source IPs, and using DDoS mitigation services.",
            "tools": ["Traffic analysis tools", "Firewall connection limits", "Cloudflare/Akamai DDoS protection"]
        }
    },
    
    "SEC101_ATK_002": {
        "metadata": {
            "category": "attacks",
            "difficulty": "medium",
            "tags": ["mitm", "man_in_the_middle"]
        },
        "questions": {
            "primary": {
                "type": "short_answer",
                "text": "What is a Man-in-the-Middle (MITM) attack?",
                "answer": "Attacker intercepts communication between two parties, can read or modify messages",
                "keywords": ["intercept", "between", "communication", "two", "parties"]
            },
            "variants": []
        },
        "learning": {
            "explanation": "MITM puts the attacker between two communicating parties, allowing eavesdropping or tampering. Like intercepting mail between two people. Prevention: HTTPS, VPN, certificate verification.",
            "mnemonic": "Man Intercepting The Messages",
            "study_guide": "Section 9: Security+ Exam Focus - Attack Types",
            "soc_relevance": "SOC analysts detect MITM by monitoring for certificate warnings, ARP spoofing, unexpected network routes, and SSL/TLS downgrade attempts.",
            "tools": ["Wireshark", "ARP monitoring", "Certificate transparency logs"]
        }
    },
    
    "SEC101_ATK_003": {
        "metadata": {
            "category": "attacks",
            "difficulty": "medium",
            "tags": ["phishing", "social_engineering"]
        },
        "questions": {
            "primary": {
                "type": "short_answer",
                "text": "What is phishing?",
                "answer": "Fake emails or messages designed to steal credentials or trick users into clicking malicious links",
                "keywords": ["fake", "email", "steal", "credentials", "malicious", "link", "trick"]
            },
            "variants": [
                {
                    "type": "multiple_choice",
                    "text": "What is 'spear phishing'?",
                    "options": [
                        "Targeted phishing aimed at specific individuals",
                        "Phishing using fishing metaphors",
                        "Phishing that uses spear weapons",
                        "Mass phishing campaigns"
                    ],
                    "answer": "Targeted phishing aimed at specific individuals"
                }
            ]
        },
        "learning": {
            "explanation": "Phishing uses fake emails/messages to steal credentials or deliver malware. Spear phishing targets specific people. Whaling targets executives. Vishing = voice phishing (phone calls).",
            "mnemonic": "Fishing for credentials",
            "study_guide": "Section 9: Security+ Exam Focus - Attack Types",
            "soc_relevance": "SOC analysts monitor email gateways for phishing indicators (suspicious links, spoofed senders), investigate reported phishing emails, and run security awareness training.",
            "tools": ["Email security gateway", "URL analysis tools", "VirusTotal"]
        }
    },
    
    # LINUX BASICS
    "SEC101_LNX_001": {
        "metadata": {
            "category": "linux_basics",
            "difficulty": "easy",
            "tags": ["commands", "file_permissions"]
        },
        "questions": {
            "primary": {
                "type": "multiple_choice",
                "text": "What does 'chmod 755 filename' do?",
                "options": [
                    "Owner: rwx, Group: r-x, Others: r-x",
                    "Owner: rwx, Group: rwx, Others: rwx",
                    "Owner: r-x, Group: rwx, Others: r-x",
                    "Everyone gets full permissions"
                ],
                "answer": "Owner: rwx, Group: r-x, Others: r-x"
            },
            "variants": [
                {
                    "type": "short_answer",
                    "text": "What command changes file permissions in Linux?",
                    "answer": "chmod",
                    "keywords": ["chmod"]
                }
            ]
        },
        "learning": {
            "explanation": "chmod changes file permissions. 755 = 7(rwx) for owner, 5(r-x) for group, 5(r-x) for others. Numbers: r=4, w=2, x=1.",
            "mnemonic": "7=rwx (4+2+1), 5=r-x (4+0+1), 0=no permissions",
            "study_guide": "Section 4: System Security - Linux File Permissions",
            "soc_relevance": "SOC analysts monitor for suspicious permission changes, especially world-writable files (777) or SUID/SGID bits that could indicate privilege escalation.",
            "tools": ["Check zaki-linux.py for Linux commands"]
        }
    },
    
    "SEC101_LNX_002": {
        "metadata": {
            "category": "linux_basics",
            "difficulty": "easy",
            "tags": ["commands", "sudo"]
        },
        "questions": {
            "primary": {
                "type": "short_answer",
                "text": "What does the 'sudo' command do?",
                "answer": "Execute command as superuser/root with elevated privileges",
                "keywords": ["superuser", "root", "elevated", "privileges", "admin"]
            },
            "variants": []
        },
        "learning": {
            "explanation": "sudo (superuser do) allows authorized users to run commands with root privileges. Safer than logging in as root directly. Logs all sudo usage for auditing.",
            "mnemonic": "SuperUser DO",
            "study_guide": "Linux Command Reference (zaki-linux.py)",
            "soc_relevance": "SOC analysts monitor sudo logs (/var/log/auth.log) for unauthorized privilege escalation, unusual sudo commands, and failed sudo attempts.",
            "tools": ["sudo logs", "auditd", "SIEM correlation rules"]
        }
    },
    
    # TOOLS & TECHNIQUES
    "SEC101_TOOL_001": {
        "metadata": {
            "category": "tools_techniques",
            "difficulty": "medium",
            "tags": ["nmap", "scanning"]
        },
        "questions": {
            "primary": {
                "type": "command_line",
                "text": "Write the nmap command to scan port 445 on target 10.10.10.50",
                "answer": "nmap -p445 10.10.10.50",
                "acceptable": ["nmap -p 445 10.10.10.50", "nmap -p445 10.10.10.50", "nmap -p 445 10.10.10.50"]
            },
            "variants": [
                {
                    "type": "multiple_choice",
                    "text": "What does the '-sV' flag do in nmap?",
                    "options": [
                        "Service version detection",
                        "Verbose output",
                        "Virtual scan",
                        "Save results"
                    ],
                    "answer": "Service version detection"
                }
            ]
        },
        "learning": {
            "explanation": "nmap is a network scanner. Common flags: -p (port), -sV (service version), -sS (SYN scan), -A (aggressive scan with OS detection).",
            "mnemonic": "Network Map maker",
            "study_guide": "Section 7: Security Tools - Nmap",
            "soc_relevance": "SOC analysts detect unauthorized port scans by monitoring for rapid connection attempts to multiple ports from single source IPs.",
            "tools": ["nmap", "Check zaki-msf.py for exploitation after scanning"]
        }
    },
    
    "SEC101_TOOL_002": {
        "metadata": {
            "category": "tools_techniques",
            "difficulty": "medium",
            "tags": ["metasploit", "exploitation"]
        },
        "questions": {
            "primary": {
                "type": "scenario",
                "text": "You have a Meterpreter session on a Windows box with standard user privileges. What command attempts automatic privilege escalation to SYSTEM?",
                "answer": "getsystem",
                "keywords": ["getsystem"]
            },
            "variants": [
                {
                    "type": "short_answer",
                    "text": "After getting SYSTEM privileges via Meterpreter, what command dumps Windows password hashes?",
                    "answer": "hashdump",
                    "keywords": ["hashdump"]
                }
            ]
        },
        "learning": {
            "explanation": "getsystem attempts automatic privilege escalation to SYSTEM. After success, hashdump extracts password hashes from SAM database. Then use zaki-john.py to crack them!",
            "mnemonic": "getsystem = Get SYSTEM privileges | hashdump = dump all hashes",
            "study_guide": "Check zaki-msf.py - Meterpreter Commands section",
            "soc_relevance": "SOC analysts detect privilege escalation by monitoring process creation, token manipulation, and sudden elevation to SYSTEM. They also watch for hashdump attempts via LSASS access.",
            "tools": ["Use zaki-msf.py for complete Meterpreter reference", "Use zaki-john.py to crack dumped hashes"]
        }
    },
    
    "SEC101_TOOL_003": {
        "metadata": {
            "category": "tools_techniques",
            "difficulty": "hard",
            "tags": ["hash_cracking", "john"]
        },
        "questions": {
            "primary": {
                "type": "multiple_choice",
                "text": "What John the Ripper format is used for Windows NTLM hashes?",
                "options": ["NTLM", "NT", "Windows", "LM"],
                "answer": "NT"
            },
            "variants": [
                {
                    "type": "scenario",
                    "text": "You ran hashdump in Meterpreter and got: Administrator:500:aad3b...:31d6c... What part should you save to crack with John?",
                    "answer": "The NTLM hash (4th field after 3rd colon)",
                    "keywords": ["ntlm", "hash", "fourth", "field", "colon"]
                }
            ]
        },
        "learning": {
            "explanation": "John the Ripper format for NTLM is '--format=NT' (NOT NTLM!). The hashdump output format is username:RID:LM_hash:NTLM_hash - save the 4th field (NTLM hash) to crack.",
            "mnemonic": "NT format for NTLM hashes (common mistake!)",
            "study_guide": "Check zaki-john.py - Hash Types section",
            "soc_relevance": "SOC analysts use hash analysis to identify compromised credentials, detect pass-the-hash attacks, and investigate credential theft incidents.",
            "tools": ["Use zaki-john.py for complete John the Ripper reference and exact crack commands!"]
        }
    },
    
    # INCIDENT RESPONSE
    "SEC101_IR_001": {
        "metadata": {
            "category": "incident_response",
            "difficulty": "medium",
            "tags": ["incident_response", "phases"]
        },
        "questions": {
            "primary": {
                "type": "short_answer",
                "text": "What are the 6 phases of the Incident Response process in order?",
                "answer": "Preparation, Detection, Identification, Containment, Recovery, Lessons Learned",
                "keywords": ["preparation", "detection", "identification", "containment", "recovery", "lessons"]
            },
            "variants": [
                {
                    "type": "multiple_choice",
                    "text": "What comes immediately AFTER Containment in the IR process?",
                    "options": ["Recovery", "Detection", "Lessons Learned", "Identification"],
                    "answer": "Recovery"
                }
            ]
        },
        "learning": {
            "explanation": "The 6 IR phases: Preparation (ready before incidents), Detection (identify breach), Identification (scope/severity), Containment (stop spread), Recovery (restore), Lessons Learned (improve).",
            "mnemonic": "PDICRL = Please Don't Interrupt Cyber Response Leaders",
            "study_guide": "Section 6: Incident Response & SIEM - Incident Response Process",
            "soc_relevance": "SOC analysts follow IR playbooks through all 6 phases. Most time is spent in Detection and Identification. Documentation is critical for Lessons Learned.",
            "tools": ["SIEM", "IR playbooks", "Ticketing systems"]
        }
    },
    
    "SEC101_IR_002": {
        "metadata": {
            "category": "incident_response",
            "difficulty": "easy",
            "tags": ["ioc", "indicators"]
        },
        "questions": {
            "primary": {
                "type": "short_answer",
                "text": "What does IOC stand for?",
                "answer": "Indicator of Compromise",
                "keywords": ["indicator", "compromise"]
            },
            "variants": [
                {
                    "type": "multiple_choice",
                    "text": "Which of these is an example of an IOC?",
                    "options": [
                        "Malicious IP address or file hash",
                        "User's password",
                        "Firewall rule",
                        "Network diagram"
                    ],
                    "answer": "Malicious IP address or file hash"
                }
            ]
        },
        "learning": {
            "explanation": "IOC (Indicator of Compromise) is evidence that a system has been breached. Examples: suspicious IPs, malicious file hashes, unusual domains, registry changes, new user accounts.",
            "mnemonic": "Infection Obvious Clue",
            "study_guide": "Section 6: Incident Response & SIEM - IOC",
            "soc_relevance": "SOC analysts search for known IOCs in their environment, subscribe to threat intelligence feeds for new IOCs, and create detection rules based on IOCs.",
            "tools": ["Threat intelligence feeds", "SIEM IOC searches", "VirusTotal"]
        }
    },
    
    # COMPLIANCE
    "SEC101_COMP_001": {
        "metadata": {
            "category": "compliance",
            "difficulty": "easy",
            "tags": ["pci_dss", "compliance"]
        },
        "questions": {
            "primary": {
                "type": "short_answer",
                "text": "What does PCI-DSS stand for?",
                "answer": "Payment Card Industry Data Security Standard",
                "keywords": ["payment", "card", "industry", "data", "security", "standard"]
            },
            "variants": []
        },
        "learning": {
            "explanation": "PCI-DSS is the security standard for organizations that handle credit card data. Requires encryption, access controls, monitoring, and regular testing.",
            "mnemonic": "Pay Card Industry Data Security Standard",
            "study_guide": "Section 8: Compliance & Frameworks - PCI-DSS",
            "soc_relevance": "SOC analysts monitor systems that process card data for PCI-DSS compliance, investigate violations, and prepare for quarterly audits.",
            "tools": ["PCI scanning tools", "Compliance dashboards"]
        }
    },
}

# ============================================================================
# SPACED REPETITION SYSTEM (SM-2 Algorithm)
# ============================================================================

class SpacedRepetition:
    """
    SM-2 Algorithm for optimal review scheduling
    Questions you know well are shown less frequently
    Questions you struggle with are shown more frequently
    """
    
    def __init__(self):
        self.min_easiness = 1.3
        self.default_easiness = 2.5
    
    def calculate_next_review(self, question_id, performance_history):
        """
        Calculate when to show this question again based on performance
        
        Performance ratings:
        5 = Perfect (knew instantly, 100% confident)
        4 = Correct with hesitation (75% confident)
        3 = Correct with difficulty (50% confident)
        2 = Incorrect but close (recognized concept)
        1 = Incorrect, no idea (need to study)
        """
        
        if not performance_history:
            return 1  # Show tomorrow if new question
        
        last_performance = performance_history[-1]
        repetition_count = len([p for p in performance_history if p >= 3])
        
        # Calculate easiness factor
        easiness = self.default_easiness
        for perf in performance_history:
            easiness = easiness + (0.1 - (5 - perf) * (0.08 + (5 - perf) * 0.02))
            easiness = max(easiness, self.min_easiness)
        
        # Calculate interval in days
        if repetition_count == 0:
            interval = 1
        elif repetition_count == 1:
            interval = 3
        else:
            prev_interval = self.get_previous_interval(performance_history)
            interval = round(prev_interval * easiness)
        
        # Adjust based on last performance
        if last_performance < 3:
            interval = 1  # Reset if got it wrong
        
        return interval
    
    def get_previous_interval(self, history):
        """Get the interval from last review"""
        if len(history) < 2:
            return 1
        return 3  # Simplified for now
    
    def get_performance_rating(self, was_correct, confidence_level):
        """
        Convert correctness + confidence to performance rating
        
        Confidence levels:
        - 'instant': Knew it immediately (100%)
        - 'confident': Pretty sure (75%)
        - 'guess': Lucky guess (50%)
        - 'no_idea': Complete guess
        """
        
        if was_correct:
            confidence_map = {
                'instant': 5,
                'confident': 4,
                'guess': 3
            }
            return confidence_map.get(confidence_level, 3)
        else:
            # Wrong answer
            confidence_map = {
                'confident': 2,  # Thought you knew but was wrong
                'guess': 1,
                'no_idea': 1
            }
            return confidence_map.get(confidence_level, 1)

# ============================================================================
# MISTAKE PATTERN ANALYZER
# ============================================================================

class MistakeAnalyzer:
    """
    Analyzes patterns in user mistakes to provide targeted feedback
    """
    
    def __init__(self):
        self.patterns = {
            'reading_too_fast': {
                'name': 'Reading Too Fast',
                'indicators': [],
                'threshold': 3,
                'advice': 'SLOW DOWN - Read questions twice before answering. Look for keywords like "NOT", "EXCEPT", "LEAST".'
            },
            'category_weakness': {
                'name': 'Category Weakness',
                'indicators': [],
                'threshold': 0.5,  # 50% or lower
                'advice': 'Focus study time on weak categories. Review study guide sections.'
            },
            'confidence_mismatch': {
                'name': 'Confidence Calibration Issue',
                'indicators': [],
                'threshold': 3,
                'advice': 'Your confidence doesn\'t match results. Practice honesty in self-assessment.'
            },
            'port_confusion': {
                'name': 'Port Number Confusion',
                'indicators': [],
                'threshold': 2,
                'advice': 'Use port number mnemonics daily. Focus on 22(SSH), 80(HTTP), 443(HTTPS), 445(SMB), 3389(RDP).'
            }
        }
    
    def analyze(self, session_history):
        """
        Analyze a quiz session to detect patterns
        Returns list of detected issues with recommendations
        """
        
        detected_patterns = []
        
        # Check for reading too fast
        fast_answers = [q for q in session_history if q.get('time_taken', 999) < 10 and not q.get('correct')]
        if len(fast_answers) >= 3:
            detected_patterns.append({
                'pattern': 'reading_too_fast',
                'severity': 'high',
                'evidence': f'Answered {len(fast_answers)} questions wrong in under 10 seconds',
                'recommendation': self.patterns['reading_too_fast']['advice']
            })
        
        # Check for category weaknesses
        category_performance = defaultdict(lambda: {'correct': 0, 'total': 0})
        for q in session_history:
            cat = q.get('category', 'unknown')
            category_performance[cat]['total'] += 1
            if q.get('correct'):
                category_performance[cat]['correct'] += 1
        
        for cat, stats in category_performance.items():
            if stats['total'] >= 3:  # Need at least 3 questions
                accuracy = stats['correct'] / stats['total']
                if accuracy < 0.5:
                    detected_patterns.append({
                        'pattern': 'category_weakness',
                        'severity': 'high',
                        'category': cat,
                        'evidence': f'{cat}: {accuracy*100:.0f}% accuracy ({stats["correct"]}/{stats["total"]})',
                        'recommendation': f'Review study guide section on {cat.replace("_", " ").title()}'
                    })
        
        # Check for confidence mismatch
        confidence_mismatches = [
            q for q in session_history 
            if q.get('confidence') == 'confident' and not q.get('correct')
        ]
        if len(confidence_mismatches) >= 3:
            detected_patterns.append({
                'pattern': 'confidence_mismatch',
                'severity': 'medium',
                'evidence': f'High confidence but wrong on {len(confidence_mismatches)} questions',
                'recommendation': self.patterns['confidence_mismatch']['advice']
            })
        
        # Check for port number confusion
        port_questions_wrong = [
            q for q in session_history
            if 'port' in q.get('tags', []) and not q.get('correct')
        ]
        if len(port_questions_wrong) >= 2:
            detected_patterns.append({
                'pattern': 'port_confusion',
                'severity': 'medium',
                'evidence': f'Missed {len(port_questions_wrong)} port number questions',
                'recommendation': self.patterns['port_confusion']['advice']
            })
        
        return detected_patterns

# ============================================================================
# PROGRESS TRACKER
# ============================================================================

class ProgressTracker:
    """
    Tracks user progress, scores, and improvement over time
    """
    
    def __init__(self, data_file='zaki_cert_progress.json'):
        self.data_file = data_file
        self.data = self.load_data()
    
    def load_data(self):
        """Load progress data from file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except:
                return self.create_new_data()
        return self.create_new_data()
    
    def create_new_data(self):
        """Create new progress data structure"""
        return {
            'user': {
                'name': 'Zuciya Zaki',
                'streak_start': datetime.now().isoformat(),
                'total_sessions': 0
            },
            'question_history': {},  # question_id -> list of performance ratings
            'review_schedule': {},   # question_id -> next_review_date
            'session_history': [],   # List of all quiz sessions
            'statistics': {
                'total_questions_answered': 0,
                'correct_answers': 0,
                'by_category': {}
            }
        }
    
    def save_data(self):
        """Save progress data to file"""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.data, f, indent=2)
        except Exception as e:
            print(f"{Colors.RED}Error saving progress: {e}{Colors.RESET}")
    
    def record_answer(self, question_id, correct, confidence, time_taken, category):
        """Record a question answer"""
        # Update question history
        if question_id not in self.data['question_history']:
            self.data['question_history'][question_id] = []
        
        # Calculate performance rating
        sr = SpacedRepetition()
        performance = sr.get_performance_rating(correct, confidence)
        
        self.data['question_history'][question_id].append({
            'performance': performance,
            'timestamp': datetime.now().isoformat(),
            'time_taken': time_taken,
            'correct': correct,
            'confidence': confidence
        })
        
        # Update review schedule
        history = [h['performance'] for h in self.data['question_history'][question_id]]
        days_until_review = sr.calculate_next_review(question_id, history)
        next_review = (datetime.now() + timedelta(days=days_until_review)).isoformat()
        self.data['review_schedule'][question_id] = next_review
        
        # Update statistics
        self.data['statistics']['total_questions_answered'] += 1
        if correct:
            self.data['statistics']['correct_answers'] += 1
        
        # Category stats
        if category not in self.data['statistics']['by_category']:
            self.data['statistics']['by_category'][category] = {'correct': 0, 'total': 0}
        self.data['statistics']['by_category'][category]['total'] += 1
        if correct:
            self.data['statistics']['by_category'][category]['correct'] += 1
    
    def get_due_questions(self, all_question_ids, max_questions=20):
        """Get questions that are due for review"""
        now = datetime.now()
        due = []
        new = []
        
        for qid in all_question_ids:
            if qid not in self.data['review_schedule']:
                new.append(qid)
            else:
                review_date = datetime.fromisoformat(self.data['review_schedule'][qid])
                if review_date <= now:
                    due.append(qid)
        
        # Prioritize due questions, then add new ones
        random.shuffle(due)
        random.shuffle(new)
        
        selected = due[:max_questions]
        if len(selected) < max_questions:
            selected.extend(new[:max_questions - len(selected)])
        
        return selected
    
    def get_weak_categories(self, threshold=0.7):
        """Get categories where performance is below threshold"""
        weak = []
        for cat, stats in self.data['statistics']['by_category'].items():
            if stats['total'] >= 3:  # Need at least 3 questions
                accuracy = stats['correct'] / stats['total']
                if accuracy < threshold:
                    weak.append((cat, accuracy, stats))
        return sorted(weak, key=lambda x: x[1])  # Sort by accuracy (worst first)
    
    def get_overall_stats(self):
        """Get overall performance statistics"""
        total = self.data['statistics']['total_questions_answered']
        if total == 0:
            return None
        
        correct = self.data['statistics']['correct_answers']
        accuracy = (correct / total) * 100
        
        # Get recent trend (last 50 questions)
        recent_sessions = self.data['session_history'][-5:] if self.data['session_history'] else []
        recent_scores = [s['score'] for s in recent_sessions if 'score' in s]
        
        trend = "stable"
        if len(recent_scores) >= 3:
            if recent_scores[-1] > recent_scores[0] + 10:
                trend = "improving"
            elif recent_scores[-1] < recent_scores[0] - 10:
                trend = "declining"
        
        return {
            'total_answered': total,
            'correct': correct,
            'accuracy': accuracy,
            'sessions': self.data['user']['total_sessions'],
            'trend': trend,
            'recent_scores': recent_scores
        }

# ============================================================================
# QUIZ ENGINE
# ============================================================================

class QuizEngine:
    """
    Core quiz delivery engine with multiple modes
    """
    
    def __init__(self):
        self.progress = ProgressTracker()
        self.mistake_analyzer = MistakeAnalyzer()
        self.current_session = []
    
    def get_question_variant(self, question_data, variant_type='primary'):
        """Get a specific variant of a question"""
        if variant_type == 'primary':
            return question_data['questions']['primary']
        else:
            variants = question_data['questions'].get('variants', [])
            if variants:
                return random.choice(variants)
            return question_data['questions']['primary']
    
    def ask_question(self, question_id, question_data, show_explanation=True):
        """
        Present a question and get answer with confidence rating
        Returns: (correct, confidence, time_taken)
        """
        
        # Choose question variant
        use_variant = random.random() < 0.3  # 30% chance of variant
        question = self.get_question_variant(question_data, 'variant' if use_variant else 'primary')
        
        print(f"\n{Colors.CYAN}{'='*70}{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.GREEN}{question['text']}{Colors.RESET}\n")
        
        start_time = time.time()
        
        # Handle different question types
        if question['type'] == 'multiple_choice':
            for i, option in enumerate(question['options'], 1):
                print(f"  {i}. {option}")
            
            while True:
                user_input = input(f"\n{Colors.YELLOW}Your answer (1-{len(question['options'])}): {Colors.RESET}").strip()
                try:
                    choice_idx = int(user_input) - 1
                    if 0 <= choice_idx < len(question['options']):
                        user_answer = question['options'][choice_idx]
                        break
                    else:
                        print(f"{Colors.RED}Please enter a number between 1 and {len(question['options'])}{Colors.RESET}")
                except ValueError:
                    print(f"{Colors.RED}Please enter a valid number{Colors.RESET}")
        
        elif question['type'] in ['short_answer', 'command_line', 'scenario']:
            user_answer = input(f"\n{Colors.YELLOW}Your answer: {Colors.RESET}").strip()
        
        else:  # true_false
            while True:
                user_answer = input(f"\n{Colors.YELLOW}Your answer (True/False): {Colors.RESET}").strip().lower()
                if user_answer in ['true', 'false', 't', 'f']:
                    user_answer = user_answer[0] == 't'
                    break
                print(f"{Colors.RED}Please enter True or False{Colors.RESET}")
        
        time_taken = time.time() - start_time
        
        # Check answer
        correct = self.check_answer(user_answer, question)
        
        # Get confidence rating
        if correct:
            print(f"\n{Colors.GREEN}{Colors.BOLD}✅ CORRECT!{Colors.RESET}")
        else:
            print(f"\n{Colors.RED}{Colors.BOLD}❌ INCORRECT{Colors.RESET}")
        
        confidence = self.get_confidence_rating(correct)
        
        # Show explanation
        if show_explanation:
            self.show_explanation(question_data, question, user_answer, correct)
        
        return correct, confidence, time_taken
    
    def check_answer(self, user_answer, question):
        """Check if answer is correct"""
        correct_answer = question['answer']
        
        if question['type'] == 'multiple_choice':
            return user_answer == correct_answer
        
        elif question['type'] == 'true_false':
            return user_answer == correct_answer
        
        elif question['type'] in ['short_answer', 'command_line', 'scenario']:
            # Check keywords or acceptable answers
            user_lower = str(user_answer).lower()
            
            # Check acceptable answers if provided
            if 'acceptable' in question:
                for acceptable in question['acceptable']:
                    if acceptable.lower() in user_lower or user_lower in acceptable.lower():
                        return True
            
            # Check keywords
            if 'keywords' in question:
                keywords = question['keywords']
                matches = sum(1 for keyword in keywords if keyword.lower() in user_lower)
                # Need at least half the keywords
                return matches >= len(keywords) // 2
            
            # Direct match
            return correct_answer.lower() in user_lower or user_lower in correct_answer.lower()
        
        return False
    
    def get_confidence_rating(self, was_correct):
        """
        Get user's confidence level
        This is KEY for spaced repetition effectiveness!
        """
        
        print(f"\n{Colors.CYAN}How confident were you?{Colors.RESET}")
        
        if was_correct:
            print(f"  {Colors.GREEN}1{Colors.RESET} - Instant recall (100% knew it)")
            print(f"  {Colors.GREEN}2{Colors.RESET} - Pretty confident (75%)")
            print(f"  {Colors.YELLOW}3{Colors.RESET} - Lucky guess (50%)")
        else:
            print(f"  {Colors.YELLOW}1{Colors.RESET} - Almost had it (knew concept)")
            print(f"  {Colors.RED}2{Colors.RESET} - Had a guess (25%)")
            print(f"  {Colors.RED}3{Colors.RESET} - No idea (complete guess)")
        
        while True:
            try:
                rating = int(input(f"\n{Colors.YELLOW}Confidence (1-3): {Colors.RESET}").strip())
                if 1 <= rating <= 3:
                    if was_correct:
                        confidence_map = {1: 'instant', 2: 'confident', 3: 'guess'}
                    else:
                        confidence_map = {1: 'confident', 2: 'guess', 3: 'no_idea'}
                    return confidence_map[rating]
                print(f"{Colors.RED}Please enter 1, 2, or 3{Colors.RESET}")
            except ValueError:
                print(f"{Colors.RED}Please enter a valid number{Colors.RESET}")
    
    def show_explanation(self, question_data, question, user_answer, correct):
        """Show detailed explanation after question"""
        learning = question_data['learning']
        
        print(f"\n{Colors.CYAN}{'─'*70}{Colors.RESET}")
        
        # Correct answer
        print(f"\n{Colors.CYAN}📝 Correct Answer:{Colors.RESET} {Colors.BOLD}{question['answer']}{Colors.RESET}")
        
        # Explanation
        print(f"\n{Colors.BLUE}📖 Explanation:{Colors.RESET}")
        print(f"  {learning['explanation']}")
        
        # Mnemonic
        if learning.get('mnemonic'):
            print(f"\n{Colors.MAGENTA}💡 Mnemonic:{Colors.RESET} {Colors.BOLD}{learning['mnemonic']}{Colors.RESET}")
        
        # Study guide reference
        if learning.get('study_guide'):
            print(f"\n{Colors.YELLOW}📚 Study Guide:{Colors.RESET} {learning['study_guide']}")
        
        # SOC relevance
        if learning.get('soc_relevance'):
            print(f"\n{Colors.GREEN}🎯 SOC Analyst Relevance:{Colors.RESET}")
            print(f"  {learning['soc_relevance']}")
        
        # Tool integration
        if learning.get('tools') and len(learning['tools']) > 0:
            print(f"\n{Colors.CYAN}🛠️  Related Tools/Commands:{Colors.RESET}")
            for tool in learning['tools']:
                print(f"  • {tool}")
        
        print(f"\n{Colors.CYAN}{'─'*70}{Colors.RESET}")
    
    def run_quiz_session(self, question_ids, mode='practice', time_limit=None):
        """
        Run a complete quiz session
        
        Modes:
        - practice: Relaxed, immediate feedback
        - timed: Time pressure, feedback after each
        - exam: Full exam simulation, feedback at end only
        - nightmare: Hardest questions, strict timing
        """
        
        print(f"\n{Colors.CYAN}╔══════════════════════════════════════════════════════════════════════╗")
        print(f"║                      QUIZ SESSION - {mode.upper().center(35)}║")
        print(f"╚══════════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
        
        print(f"{Colors.YELLOW}📚 Questions: {len(question_ids)}{Colors.RESET}")
        if time_limit:
            print(f"{Colors.RED}⏱️  Time Limit: {time_limit} minutes{Colors.RESET}")
        
        print(f"\n{Colors.CYAN}Press Enter when ready to start...{Colors.RESET}")
        input()
        
        session_start = time.time()
        self.current_session = []
        
        show_immediate_feedback = mode in ['practice', 'timed']
        
        for i, qid in enumerate(question_ids, 1):
            if qid not in QUESTION_BANK:
                continue
            
            question_data = QUESTION_BANK[qid]
            
            print(f"\n{Colors.BOLD}{Colors.CYAN}Question {i}/{len(question_ids)}{Colors.RESET}")
            print(f"{Colors.YELLOW}Category: {question_data['metadata']['category'].replace('_', ' ').title()}{Colors.RESET}")
            print(f"{Colors.YELLOW}Difficulty: {question_data['metadata']['difficulty'].upper()}{Colors.RESET}")
            
            # Check time limit
            if time_limit:
                elapsed = (time.time() - session_start) / 60
                remaining = time_limit - elapsed
                if remaining <= 0:
                    print(f"\n{Colors.RED}⏱️  TIME'S UP!{Colors.RESET}")
                    break
                print(f"{Colors.YELLOW}⏱️  Time remaining: {remaining:.1f} minutes{Colors.RESET}")
            
            correct, confidence, time_taken = self.ask_question(
                qid, 
                question_data,
                show_explanation=show_immediate_feedback
            )
            
            # Record answer
            self.progress.record_answer(
                qid,
                correct,
                confidence,
                time_taken,
                question_data['metadata']['category']
            )
            
            # Store in session
            self.current_session.append({
                'question_id': qid,
                'correct': correct,
                'confidence': confidence,
                'time_taken': time_taken,
                'category': question_data['metadata']['category'],
                'difficulty': question_data['metadata']['difficulty'],
                'tags': question_data['metadata']['tags']
            })
            
            if i < len(question_ids):
                input(f"\n{Colors.CYAN}Press Enter for next question...{Colors.RESET}")
                # Clear screen for next question
                os.system('clear' if os.name == 'posix' else 'cls')
                print_banner()
        
        # Show results
        self.show_session_results()
        
        # Save progress
        self.progress.data['user']['total_sessions'] += 1
        self.progress.data['session_history'].append({
            'timestamp': datetime.now().isoformat(),
            'mode': mode,
            'questions': len(self.current_session),
            'score': (sum(1 for q in self.current_session if q['correct']) / len(self.current_session) * 100) if self.current_session else 0,
            'time_taken': (time.time() - session_start) / 60
        })
        self.progress.save_data()
    
    def show_session_results(self):
        """Show detailed results after quiz session"""
        if not self.current_session:
            return
        
        total = len(self.current_session)
        correct = sum(1 for q in self.current_session if q['correct'])
        score = (correct / total) * 100
        
        print(f"\n{Colors.CYAN}╔══════════════════════════════════════════════════════════════════════╗")
        print(f"║                         SESSION RESULTS                              ║")
        print(f"╚══════════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
        
        print(f"{Colors.GREEN}✅ Correct:{Colors.RESET} {correct}/{total}")
        print(f"{Colors.RED}❌ Wrong:{Colors.RESET} {total - correct}/{total}")
        print(f"{Colors.CYAN}📊 Score:{Colors.RESET} {Colors.BOLD}{score:.1f}%{Colors.RESET}")
        
        # Performance message
        if score >= 90:
            print(f"\n{Colors.GREEN}🔥 EXCELLENT! You're exam-ready!{Colors.RESET}")
        elif score >= 80:
            print(f"\n{Colors.GREEN}💪 GREAT! Almost there!{Colors.RESET}")
        elif score >= 70:
            print(f"\n{Colors.CYAN}👍 GOOD! Keep studying!{Colors.RESET}")
        else:
            print(f"\n{Colors.YELLOW}📚 Review fundamentals and try again!{Colors.RESET}")
        
        # Category breakdown
        category_stats = defaultdict(lambda: {'correct': 0, 'total': 0})
        for q in self.current_session:
            cat = q['category']
            category_stats[cat]['total'] += 1
            if q['correct']:
                category_stats[cat]['correct'] += 1
        
        print(f"\n{Colors.CYAN}📊 Performance by Category:{Colors.RESET}\n")
        for cat, stats in sorted(category_stats.items()):
            accuracy = (stats['correct'] / stats['total']) * 100
            cat_name = cat.replace('_', ' ').title()
            bar_length = int(accuracy / 5)
            bar = '█' * bar_length + '░' * (20 - bar_length)
            
            color = Colors.GREEN if accuracy >= 80 else Colors.YELLOW if accuracy >= 60 else Colors.RED
            print(f"  {cat_name:30} {color}{bar}{Colors.RESET} {accuracy:5.1f}% ({stats['correct']}/{stats['total']})")
        
        # Mistake pattern analysis
        patterns = self.mistake_analyzer.analyze(self.current_session)
        if patterns:
            print(f"\n{Colors.YELLOW}🔍 Detected Issues:{Colors.RESET}\n")
            for pattern in patterns:
                severity_color = Colors.RED if pattern['severity'] == 'high' else Colors.YELLOW
                print(f"{severity_color}⚠️  {pattern.get('category', pattern['pattern']).replace('_', ' ').title()}{Colors.RESET}")
                print(f"   Evidence: {pattern['evidence']}")
                print(f"   💡 {pattern['recommendation']}\n")
        
        # Questions to review
        wrong_questions = [q for q in self.current_session if not q['correct']]
        if wrong_questions:
            print(f"{Colors.YELLOW}📝 Review These Topics:{Colors.RESET}\n")
            reviewed = set()
            for q in wrong_questions:
                cat = q['category'].replace('_', ' ').title()
                if cat not in reviewed:
                    print(f"  • {cat}")
                    reviewed.add(cat)

# ============================================================================
# MAIN MENU & MODES
# ============================================================================

def show_main_menu():
    """Display main menu"""
    print(f"\n{Colors.CYAN}╔══════════════════════════════════════════════════════════════════════╗")
    print(f"║                           MAIN MENU                                  ║")
    print(f"╚══════════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    print(f"{Colors.GREEN}[1]{Colors.RESET} 🎯 Smart Review (Spaced Repetition)")
    print(f"{Colors.GREEN}[2]{Colors.RESET} 📚 Practice by Category")
    print(f"{Colors.GREEN}[3]{Colors.RESET} 🎲 Random Practice (20 questions)")
    print(f"{Colors.GREEN}[4]{Colors.RESET} ⏱️ Timed Practice (30 min)")
    print(f"{Colors.GREEN}[5]{Colors.RESET} 🎓 Exam Simulation (Full exam mode)")
    print(f"{Colors.GREEN}[6]{Colors.RESET} 💀 Nightmare Mode (Hard questions only)")
    print(f"{Colors.GREEN}[7]{Colors.RESET} 🎯 Weak Area Focus (Target weaknesses)")
    print(f"{Colors.GREEN}[8]{Colors.RESET} 📊 Progress Dashboard")
    print(f"{Colors.GREEN}[9]{Colors.RESET} 🔤 Acronym Drill")
    print(f"{Colors.GREEN}[0]{Colors.RESET} 🚪 Exit")
    print()

def smart_review_mode(engine):
    """Spaced repetition mode - shows questions due for review"""
    all_qids = list(QUESTION_BANK.keys())
    due_questions = engine.progress.get_due_questions(all_qids, max_questions=20)
    
    if not due_questions:
        print(f"\n{Colors.GREEN}🎉 No questions due for review! You're caught up!{Colors.RESET}")
        print(f"{Colors.CYAN}Come back tomorrow for new reviews.{Colors.RESET}")
        return
    
    print(f"\n{Colors.CYAN}📚 You have {len(due_questions)} questions due for review{Colors.RESET}")
    engine.run_quiz_session(due_questions, mode='practice')

def category_practice(engine):
    """Practice specific category"""
    categories = {}
    for qid, qdata in QUESTION_BANK.items():
        cat = qdata['metadata']['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(qid)
    
    print(f"\n{Colors.CYAN}Select Category:{Colors.RESET}\n")
    cat_list = sorted(categories.keys())
    for i, cat in enumerate(cat_list, 1):
        cat_name = cat.replace('_', ' ').title()
        print(f"{Colors.GREEN}[{i}]{Colors.RESET} {cat_name} ({len(categories[cat])} questions)")
    
    try:
        choice = int(input(f"\n{Colors.YELLOW}Select category (1-{len(cat_list)}): {Colors.RESET}").strip())
        if 1 <= choice <= len(cat_list):
            selected_cat = cat_list[choice - 1]
            questions = categories[selected_cat].copy()
            random.shuffle(questions)
            
            engine.run_quiz_session(questions, mode='practice')
    except ValueError:
        print(f"{Colors.RED}Invalid selection{Colors.RESET}")

def random_practice(engine, num_questions=20):
    """Random practice mode"""
    all_qids = list(QUESTION_BANK.keys())
    random.shuffle(all_qids)
    selected = all_qids[:num_questions]
    
    engine.run_quiz_session(selected, mode='practice')

def timed_practice(engine):
    """Timed practice mode"""
    all_qids = list(QUESTION_BANK.keys())
    random.shuffle(all_qids)
    selected = all_qids[:30]  # 30 questions in 30 minutes
    
    engine.run_quiz_session(selected, mode='timed', time_limit=30)

def exam_simulation(engine):
    """Full exam simulation mode"""
    print(f"\n{Colors.CYAN}╔══════════════════════════════════════════════════════════════════════╗")
    print(f"║                      EXAM SIMULATION MODE                            ║")
    print(f"╚══════════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    print(f"{Colors.YELLOW}This simulates a real Security 101 exam:{Colors.RESET}")
    print(f"  • 45 questions")
    print(f"  • 60 minute time limit")
    print(f"  • No immediate feedback (results at end)")
    print(f"  • Passing score: 80%")
    
    confirm = input(f"\n{Colors.YELLOW}Ready to begin? (yes/no): {Colors.RESET}").strip().lower()
    if confirm not in ['yes', 'y']:
        return
    
    all_qids = list(QUESTION_BANK.keys())
    random.shuffle(all_qids)
    selected = all_qids[:45]
    
    engine.run_quiz_session(selected, mode='exam', time_limit=60)

def nightmare_mode(engine):
    """Nightmare mode - hardest questions only"""
    hard_questions = [
        qid for qid, qdata in QUESTION_BANK.items()
        if qdata['metadata']['difficulty'] in ['hard', 'medium']
    ]
    
    random.shuffle(hard_questions)
    selected = hard_questions[:25]
    
    print(f"\n{Colors.RED}💀 NIGHTMARE MODE 💀{Colors.RESET}")
    print(f"{Colors.YELLOW}Only medium and hard questions!{Colors.RESET}")
    print(f"{Colors.YELLOW}If you can pass this, the real exam will feel EASY!{Colors.RESET}\n")
    
    engine.run_quiz_session(selected, mode='nightmare', time_limit=25)

def weak_area_focus(engine):
    """Focus on weak categories"""
    weak_cats = engine.progress.get_weak_categories(threshold=0.7)
    
    if not weak_cats:
        print(f"\n{Colors.GREEN}🎉 No weak areas detected! Great job!{Colors.RESET}")
        return
    
    print(f"\n{Colors.YELLOW}🎯 Weak Areas Detected:{Colors.RESET}\n")
    for cat, accuracy, stats in weak_cats:
        cat_name = cat.replace('_', ' ').title()
        print(f"  • {cat_name}: {accuracy*100:.0f}% ({stats['correct']}/{stats['total']})")
    
    # Get questions from weak categories
    weak_qids = []
    for cat, _, _ in weak_cats:
        for qid, qdata in QUESTION_BANK.items():
            if qdata['metadata']['category'] == cat:
                weak_qids.append(qid)
    
    random.shuffle(weak_qids)
    selected = weak_qids[:20]
    
    print(f"\n{Colors.CYAN}Focusing on your weak areas...{Colors.RESET}")
    engine.run_quiz_session(selected, mode='practice')

def show_progress_dashboard(engine):
    """Display detailed progress dashboard"""
    stats = engine.progress.get_overall_stats()
    
    print(f"\n{Colors.CYAN}╔══════════════════════════════════════════════════════════════════════╗")
    print(f"║                      PROGRESS DASHBOARD 📊                           ║")
    print(f"╚══════════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    if not stats:
        print(f"{Colors.YELLOW}No quiz data yet! Take your first quiz to see stats.{Colors.RESET}")
        return
    
    print(f"{Colors.GREEN}Total Questions Answered:{Colors.RESET} {stats['total_answered']}")
    print(f"{Colors.GREEN}Correct Answers:{Colors.RESET} {stats['correct']}")
    print(f"{Colors.CYAN}Overall Accuracy:{Colors.RESET} {Colors.BOLD}{stats['accuracy']:.1f}%{Colors.RESET}")
    print(f"{Colors.YELLOW}Quiz Sessions:{Colors.RESET} {stats['sessions']}")
    
    # Trend
    trend_color = Colors.GREEN if stats['trend'] == 'improving' else Colors.YELLOW
    trend_icon = "📈" if stats['trend'] == 'improving' else "📊" if stats['trend'] == 'stable' else "📉"
    print(f"\n{trend_color}{trend_icon} Trend: {stats['trend'].upper()}{Colors.RESET}")
    
    # Recent scores
    if stats['recent_scores']:
        print(f"\n{Colors.CYAN}Recent Session Scores:{Colors.RESET}")
        for i, score in enumerate(stats['recent_scores'], 1):
            print(f"  Session {i}: {score:.1f}%")
    
    # Category performance
    print(f"\n{Colors.CYAN}Performance by Category:{Colors.RESET}\n")
    for cat, cat_stats in engine.progress.data['statistics']['by_category'].items():
        if cat_stats['total'] > 0:
            accuracy = (cat_stats['correct'] / cat_stats['total']) * 100
            cat_name = cat.replace('_', ' ').title()
            bar_length = int(accuracy / 5)
            bar = '█' * bar_length + '░' * (20 - bar_length)
            
            color = Colors.GREEN if accuracy >= 80 else Colors.YELLOW if accuracy >= 60 else Colors.RED
            print(f"  {cat_name:30} {color}{bar}{Colors.RESET} {accuracy:5.1f}% ({cat_stats['correct']}/{cat_stats['total']})")
    
    # Readiness assessment
    print(f"\n{Colors.CYAN}Exam Readiness:{Colors.RESET}")
    if stats['accuracy'] >= 85:
        print(f"{Colors.GREEN}🟢 READY! You should take the exam!{Colors.RESET}")
    elif stats['accuracy'] >= 75:
        print(f"{Colors.YELLOW}🟡 ALMOST READY! Focus on weak areas.{Colors.RESET}")
    else:
        print(f"{Colors.RED}🔴 NOT READY. Continue studying fundamentals.{Colors.RESET}")
    
    # Due for review
    all_qids = list(QUESTION_BANK.keys())
    due = engine.progress.get_due_questions(all_qids, max_questions=100)
    print(f"\n{Colors.YELLOW}Questions due for review:{Colors.RESET} {len(due)}")

def acronym_drill():
    """Acronym drill mode"""
    acronyms = {
        'TCP': 'Transmission Control Protocol',
        'UDP': 'User Datagram Protocol',
        'DNS': 'Domain Name System',
        'DHCP': 'Dynamic Host Configuration Protocol',
        'HTTP': 'Hypertext Transfer Protocol',
        'HTTPS': 'HTTP Secure',
        'SSH': 'Secure Shell',
        'FTP': 'File Transfer Protocol',
        'SMTP': 'Simple Mail Transfer Protocol',
        'CIA': 'Confidentiality, Integrity, Availability',
        'AAA': 'Authentication, Authorization, Accounting',
        'MFA': 'Multi-Factor Authentication',
        'IDS': 'Intrusion Detection System',
        'IPS': 'Intrusion Prevention System',
        'SIEM': 'Security Information and Event Management',
        'EDR': 'Endpoint Detection and Response',
        'SOAR': 'Security Orchestration, Automation, and Response',
        'DLP': 'Data Loss Prevention',
        'WAF': 'Web Application Firewall',
        'IOC': 'Indicator of Compromise',
        'APT': 'Advanced Persistent Threat',
        'XSS': 'Cross-Site Scripting',
        'CSRF': 'Cross-Site Request Forgery',
        'DDoS': 'Distributed Denial of Service',
        'MITM': 'Man-in-the-Middle',
        'AES': 'Advanced Encryption Standard',
        'RSA': 'Rivest-Shamir-Adleman',
        'TLS': 'Transport Layer Security',
        'SSL': 'Secure Sockets Layer',
        'PKI': 'Public Key Infrastructure',
        'NIST': 'National Institute of Standards and Technology',
        'PCI-DSS': 'Payment Card Industry Data Security Standard'
    }
    
    print(f"\n{Colors.CYAN}╔══════════════════════════════════════════════════════════════════════╗")
    print(f"║                        ACRONYM DRILL MODE 🔤                         ║")
    print(f"╚══════════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    items = list(acronyms.items())
    random.shuffle(items)
    
    num_questions = min(10, len(items))
    selected = items[:num_questions]
    
    correct = 0
    
    for i, (acronym, full_name) in enumerate(selected, 1):
        print(f"\n{Colors.BOLD}{Colors.CYAN}Question {i}/{num_questions}{Colors.RESET}")
        print(f"\n{Colors.GREEN}What does {Colors.BOLD}{acronym}{Colors.RESET}{Colors.GREEN} stand for?{Colors.RESET}")
        
        user_answer = input(f"\n{Colors.YELLOW}Your answer: {Colors.RESET}").strip()
        
        # Check answer (flexible matching)
        user_lower = user_answer.lower()
        correct_lower = full_name.lower()
        
        # Split into words and check
        user_words = user_lower.split()
        correct_words = correct_lower.split()
        
        matches = sum(1 for word in correct_words if len(word) > 2 and word in user_lower)
        
        if matches >= len(correct_words) - 1:
            print(f"{Colors.GREEN}✅ CORRECT!{Colors.RESET}")
            correct += 1
        else:
            print(f"{Colors.RED}❌ Not quite!{Colors.RESET}")
        
        print(f"\n{Colors.CYAN}📝 Full Answer:{Colors.RESET} {Colors.BOLD}{full_name}{Colors.RESET}")
        
        if i < num_questions:
            input(f"\n{Colors.CYAN}Press Enter for next acronym...{Colors.RESET}")
    
    # Results
    score = (correct / num_questions) * 100
    print(f"\n{Colors.CYAN}╔══════════════════════════════════════════════════════════════════════╗")
    print(f"║                        ACRONYM DRILL RESULTS                         ║")
    print(f"╚══════════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    print(f"{Colors.GREEN}✅ Correct:{Colors.RESET} {correct}/{num_questions}")
    print(f"{Colors.CYAN}📊 Score:{Colors.RESET} {Colors.BOLD}{score:.1f}%{Colors.RESET}")
    
    if score >= 90:
        print(f"\n{Colors.GREEN}🔥 EXCELLENT! Acronyms mastered!{Colors.RESET}")
    elif score >= 70:
        print(f"\n{Colors.CYAN}💪 GOOD! Keep practicing!{Colors.RESET}")
    else:
        print(f"\n{Colors.YELLOW}📚 Review your study guide mnemonics!{Colors.RESET}")

# ============================================================================
# MAIN PROGRAM
# ============================================================================

def main():
    """Main program loop"""
    print_banner()
    
    engine = QuizEngine()
    
    print(f"{Colors.GREEN}Welcome back, Zuciya Zaki! 🦁{Colors.RESET}")
    print(f"{Colors.CYAN}Day {engine.progress.data['user']['total_sessions'] + 1} of your certification journey!{Colors.RESET}")
    print(f"{Colors.YELLOW}\"I never go back on my word! That's my ninja way!\"{Colors.RESET}")
    
    while True:
        show_main_menu()
        choice = input(f"{Colors.YELLOW}Select option (0-9): {Colors.RESET}").strip()
        
        try:
            if choice == '1':
                smart_review_mode(engine)
            elif choice == '2':
                category_practice(engine)
            elif choice == '3':
                random_practice(engine, num_questions=20)
            elif choice == '4':
                timed_practice(engine)
            elif choice == '5':
                exam_simulation(engine)
            elif choice == '6':
                nightmare_mode(engine)
            elif choice == '7':
                weak_area_focus(engine)
            elif choice == '8':
                show_progress_dashboard(engine)
            elif choice == '9':
                acronym_drill()
            elif choice == '0':
                print(f"\n{Colors.YELLOW}{'═'*70}")
                print(f"  Thanks for studying with ZAKI-CERT-MASTER!")
                print(f"  Keep going! #ZuciyaZaki! 🦁")
                print(f"  \"I never go back on my word - that's my ninja way!\"")
                print(f"{'═'*70}{Colors.RESET}\n")
                sys.exit(0)
            else:
                print(f"{Colors.RED}Invalid option. Please select 0-9{Colors.RESET}")
            
            input(f"\n{Colors.CYAN}Press Enter to return to main menu...{Colors.RESET}")
            os.system('clear' if os.name == 'posix' else 'cls')
            print_banner()
            
        except KeyboardInterrupt:
            print(f"\n\n{Colors.YELLOW}Exiting... Stay strong! BELIEVE IT! 🔥{Colors.RESET}\n")
            sys.exit(0)
        except Exception as e:
            print(f"\n{Colors.RED}An error occurred: {e}{Colors.RESET}")
            input(f"{Colors.CYAN}Press Enter to continue...{Colors.RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Exiting... You WILL make it happen, BELIEVE IT! 🦁🔥{Colors.RESET}\n")
        sys.exit(0)