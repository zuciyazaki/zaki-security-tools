# 🦁 JOHN-QUICK V1.0 - Hash Cracking Made Easy!

## 🚀 Quick Start

### Installation
```bash
# Download to Kali Linux
cd ~
chmod +x john-quick.py

# Run it!
./john-quick.py
```

## ✨ What's Inside

### **15+ Hash Types Covered:**
- ✅ NTLM (Windows passwords from hashdump)
- ✅ Linux Shadow (SHA-512, SHA-256, MD5)
- ✅ MD5, SHA-1, SHA-256 (web/database)
- ✅ NTLMv2 (Responder captures)
- ✅ bcrypt (modern web apps)
- ✅ SSH Private Keys (encrypted id_rsa)
- ✅ ZIP/RAR archives
- ✅ KeePass databases
- ✅ And more!

### **6 TryHackMe Scenarios:**
1. Got Meterpreter → Ran hashdump
2. Found /etc/shadow File
3. Found Hashes in Database Dump
4. Captured NTLMv2 with Responder
5. Found Encrypted SSH Key
6. Found Password-Protected ZIP

### **Complete Workflow:**
- 🔍 Identify hash type
- 💥 Get exact crack command
- 🚩 Know what to do with password

---

## 📖 How to Use

### **Menu Option 1: Quick Hash Identification**

**Use when:** You have a hash and don't know what type it is

```bash
./john-quick.py
[1] Quick Hash Identification
> Paste hash: 5f4dcc3b5aa765d61d8327deb882cf99

Output:
✅ Detected: MD5 (32 hex chars)
💥 Crack: john --format=Raw-MD5 hash.txt --wordlist=/usr/share/wordlists/rockyou.txt
🚩 After Crack: Use for web application login
```

---

### **Menu Option 2: Browse Hash Types**

**Use when:** You want to explore all available hash types

Shows organized by category:
- **Windows**: NTLM, NTLMv2
- **Linux**: Shadow files (all variants)
- **Web/Database**: MD5, SHA-1, SHA-256, bcrypt
- **Files**: SSH keys, ZIP, RAR, KeePass

---

### **Menu Option 3: Common TryHackMe Scenarios** ⭐ **MOST USEFUL!**

**Use when:** You're stuck and need step-by-step guidance

**Example: You ran hashdump in Meterpreter**

```bash
[3] Common TryHackMe Scenarios
[1] Got Meterpreter → Ran hashdump

Shows:
Typical Output:
Administrator:500:aad3b...:31d6c...:::

Step-by-Step:
1. Copy output to file: hashdump.txt
2. Extract NTLM hashes:
   cut -d: -f4 hashdump.txt > hashes.txt
3. Crack with John:
   john --format=NT hashes.txt --wordlist=/usr/share/wordlists/rockyou.txt
4. Show cracked:
   john --show --format=NT hashes.txt
5. Use password with PSExec or RDP!
```

**Every scenario = Complete walkthrough!** 🎯

---

### **Menu Option 4: Wordlist Reference**

**Use when:** You need to know which wordlist to use

Shows:
- **rockyou.txt** - DEFAULT (14M passwords) ← Use 99% of the time
- **fasttrack.txt** - Quick test (222 passwords)
- **SecLists** - Specialized lists
- **Custom with Crunch** - Generate your own

---

### **Menu Option 5: Generate Crack Command** ⭐ **SUPER USEFUL!**

**Use when:** You know the hash type and want exact commands

```bash
[5] Generate Crack Command
[Select hash type] NTLM
Hash filename: hashes.txt
Wordlist: (default rockyou.txt)

Output:
═══════════════════════════════════════
  COPY AND PASTE THESE COMMANDS
═══════════════════════════════════════

# Crack the hash
john --format=NT hashes.txt --wordlist=/usr/share/wordlists/rockyou.txt

# Show cracked passwords
john --show --format=NT hashes.txt

═══════════════════════════════════════
🚩 After Success: Use password with PSExec, RDP, SMB shares, WinRM
💡 Expected Speed: VERY FAST (millions/sec)
```

---

### **Menu Option 6: Useful Commands Cheat Sheet**

**Use when:** You need quick reference for conversion tools

Shows commands for:
- hashid / hash-identifier
- ssh2john, zip2john, rar2john, keepass2john
- Extracting hashes from hashdump
- John resume, rules, masks
- And more!

---

## 🎯 Real TryHackMe Workflow Examples

### **Example 1: Windows Box - Got Meterpreter**

**Step 1: Dump hashes**
```bash
meterpreter > hashdump
Administrator:500:aad3b...:31d6c...:::
user:1001:aad3b...:e52ca...:::
```

**Step 2: Check JOHN-QUICK**
```bash
./john-quick.py
[3] Common TryHackMe Scenarios
[1] Got Meterpreter → Ran hashdump
```

**Step 3: Follow the steps shown**
```bash
# Extract NTLM hashes
cut -d: -f4 hashdump.txt > hashes.txt

# Crack
john --format=NT hashes.txt --wordlist=/usr/share/wordlists/rockyou.txt

# Show results
john --show --format=NT hashes.txt
# user:Password123
```

**Step 4: Use password**
```bash
# Tool told you: "Use with PSExec or RDP"
psexec.py user:Password123@10.10.10.40
# Got SYSTEM shell! 🎉
```

---

### **Example 2: Linux Box - Found /etc/shadow**

**Step 1: Got shadow file**
```bash
cat /etc/shadow
root:$6$xyz$longhash...:18760:0:99999:7:::
```

**Step 2: Check JOHN-QUICK**
```bash
./john-quick.py
[1] Quick Hash Identification
> Paste: $6$xyz$longhash...

Detected: Linux Shadow SHA-512
```

**Step 3: Generate command**
```bash
[5] Generate Crack Command
[Select] Linux Shadow (SHA-512)

# Crack (John auto-detects format)
john shadow.txt --wordlist=/usr/share/wordlists/rockyou.txt

# Show cracked
john --show shadow.txt
# root:admin123
```

**Step 4: Use password**
```bash
# Tool told you: "Use for SSH or su/sudo"
ssh root@10.10.10.40
Password: admin123
# Root access! 🎉
```

---

### **Example 3: Found Encrypted SSH Key**

**Step 1: Found key but it's encrypted**
```bash
cat id_rsa
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
...
```

**Step 2: Check JOHN-QUICK**
```bash
./john-quick.py
[3] Common TryHackMe Scenarios
[5] Found Encrypted SSH Key
```

**Step 3: Follow exact steps**
```bash
# Convert to john format
ssh2john id_rsa > id_rsa.hash

# Crack
john id_rsa.hash --wordlist=/usr/share/wordlists/rockyou.txt

# Show password
john --show id_rsa.hash
# id_rsa:password123

# Decrypt key
openssl rsa -in id_rsa -out id_rsa_decrypted
# Enter password: password123

# Use for SSH
chmod 600 id_rsa_decrypted
ssh -i id_rsa_decrypted user@10.10.10.40
# SSH access! 🎉
```

---

## 💡 Pro Tips

### **Tip 1: Always Use Quick Identification First**
```bash
[1] Quick Hash Identification
> Paste any hash
# Tool tells you EXACTLY what it is
```

### **Tip 2: Scenarios Are Your Best Friend**
- Stuck? → [3] Common TryHackMe Scenarios
- Pick the scenario that matches your situation
- Get step-by-step walkthrough!

### **Tip 3: Generate Commands, Don't Memorize**
- Don't try to remember john syntax
- Use [5] Generate Crack Command
- Copy/paste = no typos!

### **Tip 4: rockyou.txt Solves 90% of TryHackMe**
- Always try rockyou.txt first
- It cracks most passwords in seconds/minutes
- Don't overthink wordlist choice!

### **Tip 5: Pay Attention to "After Crack"**
- Tool tells you WHAT TO DO with the password
- PSExec? RDP? SSH? It's right there!
- No more "I cracked it... now what?"

---

## 🔥 What Makes JOHN-QUICK Special

### **Problem It Solves:**

**Before JOHN-QUICK:**
1. Find hashes ✅
2. Google "what hash type is this" ❌
3. Google "john the ripper ntlm format" ❌
4. Try random commands ❌
5. Syntax error ❌
6. Google more ❌
7. Finally crack it ✅
8. Google "what to do with cracked ntlm" ❌
9. Use password ✅

**Total time: 30-60 minutes** 😫

---

**After JOHN-QUICK:**
1. Find hashes ✅
2. `./john-quick.py` [1] Identify ✅
3. [5] Generate command ✅
4. Copy/paste & crack ✅
5. Read "After Crack" guidance ✅
6. Use password ✅

**Total time: 5 minutes** 🎯

**85% TIME SAVED!** ⚡

---

## 📚 Hash Types Cheat Sheet

### **By Length:**
- **32 chars** = MD5 or NTLM
- **40 chars** = SHA-1
- **64 chars** = SHA-256

### **By Prefix:**
- **$6$** = Linux Shadow SHA-512
- **$5$** = Linux Shadow SHA-256
- **$1$** = Linux Shadow MD5
- **$2a$/$2b$/$2y$** = bcrypt
- **user::domain:** = NTLMv2

### **By Format:**
- **Contains colons** = Windows hashdump format
- **Multi-line with BEGIN** = Encrypted file
- **.kdbx file** = KeePass database
- **.zip/.rar with password** = Archive

---

## 🦁 The Zuciya Zaki Philosophy

**"Never waste time googling what you can automate"**

**This tool:**
- ✅ Identifies hashes instantly
- ✅ Generates exact commands
- ✅ Tells you what to do after
- ✅ Saves you 30+ minutes per room

**You built this workflow once.**  
**Now it serves you forever.**

**That's the ninja way!** 🍜

---

## 🚀 Quick Command Reference

### **Most Common TryHackMe Hashes:**

```bash
# NTLM (Windows hashdump)
john --format=NT hash.txt --wordlist=/usr/share/wordlists/rockyou.txt

# Linux Shadow (auto-detects)
john shadow.txt --wordlist=/usr/share/wordlists/rockyou.txt

# MD5 (web/database)
john --format=Raw-MD5 hash.txt --wordlist=/usr/share/wordlists/rockyou.txt

# SSH Key (must convert first)
ssh2john id_rsa > hash.txt
john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt

# ZIP File (must convert first)
zip2john secret.zip > hash.txt
john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt
```

---

## 💪 Day 26 Achievement Unlocked

**You now have TWO professional tools:**

1. **MSF-QUICK** - Metasploit exploit reference
2. **JOHN-QUICK** - Hash cracking guide

**Together they cover:**
- 🎯 Exploitation (MSF-Quick)
- 🔓 Privilege Escalation (John-Quick)
- 🚩 Flag Hunting (both tools)

**You're building a complete toolkit!** 🛠️

---

## 🎯 Next Steps

1. **Download to Kali**
2. **Make executable:** `chmod +x john-quick.py`
3. **Run it:** `./john-quick.py`
4. **Try Option [3]** - Common Scenarios
5. **Bookmark it** - You'll use this CONSTANTLY!

---

**Now go crack those hashes and find those flags! #ZuciyaZaki!** 🦁🔥

**BELIEVE IT!!!** 🍜🌀
