# 🛡️ Zaki Security Tools

**Custom Python security tools for penetration testing, CTF challenges, and Security+ exam preparation.**

[![License: MIT](https://img.shields.io/badge/License-MIT-emerald.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Maintained](https://img.shields.io/badge/Maintained-Yes-green.svg)](https://github.com/zuciyazaki/zaki-security-tools)

> *"I never go back on my word. That's the Zaki way!"*  
> — Zuciya Zaki (Dominic Metz)

---

## 📋 Overview

This collection of Python CLI tools was developed during my journey from maritime work to cybersecurity. These tools solve real problems I encountered while completing 65+ TryHackMe rooms, preparing for Security+ certification, and building practical penetration testing skills.

**Purpose:** These are personal productivity tools I built for my own use and am sharing with others embarking on the same journey. They're designed to provide quick references, automate repetitive tasks, and accelerate learning in cybersecurity.

---

## 🔧 Tools Included

### 1. **zaki-john.py** - Hash Cracking Reference
**Purpose:** Quick reference for John the Ripper hash cracking workflows

**Features:**
- Hash type identification (MD5, NTLM, SHA-1, SHA-256, SHA-512, bcrypt, etc.)
- Ready-to-use John the Ripper commands
- TryHackMe-focused scenarios (hashdump, shadow files, Responder captures)
- File format conversion (zip2john, ssh2john, etc.)
- Wordlist recommendations (rockyou.txt, SecLists)
- Post-crack usage guidance

**Use case:** You find a hash dump during a CTF or pentest lab - this tool tells you exactly how to crack it.

**Example:**
```bash
python zaki-john.py
# Navigate through hash types
# Get exact commands to crack hashes
```

---

### 2. **zaki-msf.py** - Metasploit Framework Quick Reference
**Purpose:** Fast access to Metasploit exploits with TryHackMe-optimized workflows

**Features:**
- 30+ curated exploits (Excellent/Great rank only)
- Category browsing (Windows, Linux, Web, Services)
- Port-based attack vectors
- Payload selection guidance (Meterpreter vs cmd/shell)
- Post-exploitation command reference
- Flag hunting strategies for CTF challenges
- Command generator (auto-creates ready-to-paste msfconsole commands)

**Use case:** You've identified an open SMB port - this tool shows you EternalBlue, gives you the exact exploit command, and tells you what to do after getting a shell.

**Example:**
```bash
python zaki-msf.py
# Browse by service or port
# Get complete exploit workflow
# Copy-paste commands directly into msfconsole
```

---

### 3. **zaki-linux.py** - Linux Command Reference
**Purpose:** Comprehensive reference for 170+ essential Linux commands

**Features:**
- Categorized commands (File Management, Networking, Security, etc.)
- Real-world usage examples
- Common flags and options
- Penetration testing focused (nmap, netcat, curl, grep, find, etc.)
- Quick search functionality
- Cheat sheet format

**Use case:** You're in a reverse shell and need to find SUID binaries or enumerate the system - this tool gives you the exact commands.

**Example:**
```bash
python zaki-linux.py
# Search for specific commands
# Browse by category
# See practical examples
```

---

### 4. **zaki-cert-mastery.py** - Adaptive Security+ Learning System
**Purpose:** Intelligent study tool for Security+ certification preparation

**Features:**
- Adaptive difficulty system (tracks your performance)
- 500+ practice questions across all Security+ domains
- Spaced repetition algorithm
- Performance analytics and weak area identification
- Domain-specific practice (Threats, Architecture, Implementation, etc.)
- Progress tracking and study streaks
- Detailed explanations for answers

**Use case:** You're studying for Security+, this tool focuses on your weak areas and tracks your improvement over time.

**Example:**
```bash
python zaki-cert-mastery.py
# Answer questions
# System adapts to your level
# Track progress toward certification
```

---

### 5. **zaki-quiz.py** - General Cybersecurity Quiz Tool
**Purpose:** Quick knowledge testing and review

**Features:**
- Multiple choice questions
- Covers general cybersecurity topics
- Instant feedback
- Score tracking
- Great for quick reviews before labs

**Use case:** Quick 5-minute knowledge refresher before diving into TryHackMe rooms.

**Example:**
```bash
python zaki-quiz.py
# Take quick quizzes
# Test your knowledge
# Immediate feedback
```

---

## 📁 Quick Guides Directory

The `/quick-guides` folder contains condensed reference materials for rapid lookup during CTF challenges and penetration testing scenarios.

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- No external dependencies required (uses standard library only)

### Setup
```bash
# Clone the repository
git clone https://github.com/zuciyazaki/zaki-security-tools.git
cd zaki-security-tools

# Verify file integrity (optional but recommended)
# On Linux/Mac:
sha256sum -c SHA256SUMS

# On Windows (PowerShell):
Get-FileHash zaki-john.py -Algorithm SHA256
# Compare with SHA256SUMS file

# Run any tool
python zaki-john.py
```

### No Installation Required!
These are standalone Python scripts with no dependencies. Just run them!

---

## 🔐 File Integrity Verification

**Always verify checksums before running tools downloaded from the internet!**

### Expected SHA-256 Checksums:

See the `SHA256SUMS` file in this repository for current checksums.

### Verify on Linux/Mac:
```bash
sha256sum -c SHA256SUMS
```

### Verify on Windows (PowerShell):
```powershell
Get-FileHash zaki-john.py -Algorithm SHA256
# Compare output with SHA256SUMS file
```

All checksums should match. If they don't, **do not run the tools** and verify you downloaded from the official repository.

---

## 💡 Development Transparency

**These tools were developed for my personal use and workflow optimization.** I'm sharing them with the cybersecurity community because they might help others on the same journey.

### Development Process:
- **Tools were built iteratively** based on real challenges I encountered in TryHackMe labs and Security+ study sessions
- **I used Claude (Anthropic's AI assistant) extensively** to help with coding, debugging, and structure
- **All code was tested** in real penetration testing labs and CTF scenarios
- **Continuous refinement** based on practical use over 50+ days of daily cybersecurity training

### Why This Matters:
I believe in transparency. These aren't tools I claim to have coded entirely from scratch - they're the result of my learning process, problem-solving approach, and strategic use of available resources (including AI assistance). 

**What matters is:**
- ✅ They solve real problems
- ✅ They work in actual use cases
- ✅ I understand how they work (and can explain every line)
- ✅ They demonstrate my problem-solving approach
- ✅ I'm honest about the development process

In modern cybersecurity, knowing HOW to solve problems and WHEN to leverage tools (including AI) is more important than doing everything manually. These tools represent my approach: strategic, practical, and effective.

---

## 🎯 Use Cases

### For TryHackMe Users:
- Quick reference during CTF challenges
- Avoid context-switching to Google/documentation
- Learn by seeing practical examples
- Speed up common tasks (hash cracking, exploit selection)

### For Security+ Students:
- Adaptive practice questions
- Track weak areas
- Focused study sessions
- Real-world command examples

### For Penetration Testers:
- Fast exploit lookup
- Post-exploitation command reference
- Hash identification and cracking workflow
- Linux enumeration commands

---

## ⚠️ Legal & Ethical Use

**These tools are for:**
- ✅ Educational purposes
- ✅ Authorized penetration testing (with written permission)
- ✅ CTF challenges and training labs
- ✅ Personal security research
- ✅ Certification preparation

**These tools are NOT for:**
- ❌ Unauthorized access to systems
- ❌ Malicious purposes
- ❌ Any illegal activity
- ❌ Attacking systems without explicit permission

**By using these tools, you agree to:**
- Use them only on systems you own or have explicit written permission to test
- Comply with all applicable laws and regulations
- Accept full responsibility for your actions

**I am not responsible for misuse of these tools. Use them responsibly and ethically.**

See [SECURITY.md](SECURITY.md) for more information on responsible use and security considerations.

---

## 🛠️ Contributing

While these are personal tools, I welcome:
- Bug reports
- Feature suggestions
- Documentation improvements
- Your own tool additions (with proper attribution)

**To contribute:**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 Changelog

### v1.0.0 - Initial Release (December 2024)
- Released zaki-john.py (hash cracking reference)
- Released zaki-msf.py (Metasploit reference)
- Released zaki-linux.py (170+ Linux commands)
- Released zaki-cert-mastery.py (adaptive Security+ learning)
- Released zaki-quiz.py (general cybersecurity quiz)
- Added SHA256SUMS for file integrity verification
- Added comprehensive documentation

---

## 🔗 Related Projects

**Portfolio & Tools:**
- 🌐 [zuciyazaki.com](https://zuciyazaki.com) - Personal portfolio
- 🛠️ [tools.zuciyazaki.com](https://tools.zuciyazaki.com) - Web-based security tools (Password Analyzer, Hash Identifier, etc.)
- 💼 [LinkedIn](https://www.linkedin.com/in/dominic-metz-642519266/)
- 🎯 [TryHackMe Profile](https://tryhackme.com/p/ZuciyaZaki) - Top 8% globally

---

## 🦁 About Zuciya Zaki (Dominic Metz)

I'm a cybersecurity specialist in training, transitioning from maritime work to SOC Analyst roles. I maintain a 50+ day unbroken learning streak on TryHackMe (top 6% globally) while working full-time.

**My approach:**
- **Build, don't just consume** - I create tools to solve problems I encounter
- **Strategic problem solver** - Think systematically about root causes and solutions
- **Transparent learner** - Honest about my process, including using AI assistance
- **Consistent executor** - 50+ days without missing a day of cybersecurity study

**Philosophy:** *"I never go back on my word. That's my ninja way!"*

---

## 📧 Contact

**Dominic Metz (Zuciya Zaki)**
- 📧 Email: dominicmetz@me.com
- 💼 LinkedIn: [dominic-metz-642519266](https://www.linkedin.com/in/dominic-metz-642519266/)
- 🔧 Portfolio: [zuciyazaki.com](https://zuciyazaki.com)
- 💻 GitHub: [zuciyazaki](https://github.com/zuciyazaki)

**For security issues:** See [SECURITY.md](SECURITY.md) for responsible disclosure process.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**TL;DR:** You can use, modify, and distribute these tools freely. Just include the original license and don't hold me liable for anything.

---

## 🙏 Acknowledgments

- **Anthropic's Claude** - AI assistance in development and debugging
- **TryHackMe** - Practical labs that inspired many of these tools
- **The cybersecurity community** - For sharing knowledge and tools freely
- **You** - For taking the time to check out these tools!

---

## 📊 Stats

- **Development Time:** 50+ days of active cybersecurity training
- **Tools Built:** 5 Python CLI tools + web-based toolkit
- **TryHackMe Rooms Completed:** 65+
- **Coffee Consumed:** Immeasurable ☕

---

## 🔥 Star This Repository!

If these tools helped you on your cybersecurity journey, consider:
- ⭐ Starring this repository
- 🔄 Sharing it with others learning cybersecurity
- 💬 Opening an issue with feedback or suggestions
- 🤝 Contributing improvements

**Every star motivates me to keep building and sharing!**

---

**Built with dedication. Shared with the community. One day at a time.** 🦁

**BELIEVE IT!** 🔥

---

*Last updated: December 2025*
