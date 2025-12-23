#!/usr/bin/env python3
"""
ZAKI-LINUX V2.0: Comprehensive Linux Command Reference
Created by: Zuciya Zaki
Purpose: Complete Linux command database - 170+ commands!
Day 26 - "I never go back on my word! That's my ninja way!"
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
    """Display Zuciya Zaki branded banner"""
    banner = f"""{Colors.YELLOW}
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║     ██╗     ██╗███╗   ██╗██╗   ██╗██╗  ██╗     ██████╗ ███╗   ███╗   ║
║     ██║     ██║████╗  ██║██║   ██║╚██╗██╔╝    ██╔════╝ ████╗ ████║   ║
║     ██║     ██║██╔██╗ ██║██║   ██║ ╚███╔╝     ██║      ██╔████╔██║   ║
║     ██║     ██║██║╚██╗██║██║   ██║ ██╔██╗     ██║      ██║╚██╔╝██║   ║
║     ███████╗██║██║ ╚████║╚██████╔╝██╔╝ ██╗    ╚██████╗ ██║ ╚═╝ ██║   ║
║     ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚═╝     ╚═╝   ║
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
║           LINUX COMMAND QUICK REFERENCE V1.0                         ║
║              📁 Files | 🌐 Network | ⚙️ Process | 📝 Text            ║
╚══════════════════════════════════════════════════════════════════════╝{Colors.RESET}
"""
    print(banner)

# Simple command database - Name, Description, Common Usage
COMMANDS = {
    # File System Commands
    'ls': {
        'category': 'filesystem',
        'description': 'List directory contents',
        'common': 'ls -la (list all with details)'
    },
    'cd': {
        'category': 'filesystem',
        'description': 'Change directory',
        'common': 'cd /path or cd .. (up one level)'
    },
    'pwd': {
        'category': 'filesystem',
        'description': 'Print working directory (current location)',
        'common': 'pwd'
    },
    'mkdir': {
        'category': 'filesystem',
        'description': 'Make new directory',
        'common': 'mkdir dirname or mkdir -p path/to/dir'
    },
    'rm': {
        'category': 'filesystem',
        'description': 'Remove files or directories',
        'common': 'rm file or rm -rf directory (CAREFUL!)'
    },
    'cp': {
        'category': 'filesystem',
        'description': 'Copy files or directories',
        'common': 'cp file1 file2 or cp -r dir1 dir2'
    },
    'mv': {
        'category': 'filesystem',
        'description': 'Move or rename files',
        'common': 'mv oldname newname'
    },
    'find': {
        'category': 'filesystem',
        'description': 'Search for files',
        'common': 'find . -name "*.txt"'
    },
    'chmod': {
        'category': 'filesystem',
        'description': 'Change file permissions',
        'common': 'chmod +x file or chmod 755 file'
    },
    'chown': {
        'category': 'filesystem',
        'description': 'Change file owner',
        'common': 'chown user:group file'
    },
    # Terminal Management / Session Management
'screen': {
    'category': 'terminal',
    'description': 'Terminal multiplexer - manage multiple sessions in one window',
    'common': 'screen -S sessionname (start named session)'
},
'screen_new': {
    'category': 'terminal',
    'description': 'Start new Screen session',
    'common': 'screen OR screen -S name (named session)'
},
'screen_list': {
    'category': 'terminal',
    'description': 'List all Screen sessions',
    'common': 'screen -ls'
},
'screen_reattach': {
    'category': 'terminal',
    'description': 'Reattach to detached Screen session',
    'common': 'screen -r OR screen -r sessionname'
},
'screen_detach_reattach': {
    'category': 'terminal',
    'description': 'Detach elsewhere and reattach here',
    'common': 'screen -d -r sessionname'
},
'screen_kill': {
    'category': 'terminal',
    'description': 'Kill a Screen session',
    'common': 'screen -X -S sessionname quit'
},
'screen_create_window': {
    'category': 'terminal',
    'description': 'Create new window (inside Screen)',
    'common': 'Ctrl+A then C'
},
'screen_next_window': {
    'category': 'terminal',
    'description': 'Switch to next window',
    'common': 'Ctrl+A then N'
},
'screen_previous_window': {
    'category': 'terminal',
    'description': 'Switch to previous window',
    'common': 'Ctrl+A then P'
},
'screen_list_windows': {
    'category': 'terminal',
    'description': 'List all windows in session',
    'common': 'Ctrl+A then "'
},
'screen_switch_window': {
    'category': 'terminal',
    'description': 'Switch to specific window number',
    'common': 'Ctrl+A then 0-9 (window number)'
},
'screen_rename_window': {
    'category': 'terminal',
    'description': 'Rename current window',
    'common': 'Ctrl+A then A'
},
'screen_detach': {
    'category': 'terminal',
    'description': 'Detach from current session (keeps running)',
    'common': 'Ctrl+A then D'
},
'screen_kill_window': {
    'category': 'terminal',
    'description': 'Kill current window',
    'common': 'Ctrl+A then K (confirm with y)'
},
'screen_kill_all': {
    'category': 'terminal',
    'description': 'Kill all windows and exit Screen',
    'common': 'Ctrl+A then \\ (backslash, confirm with y)'
},
'screen_help': {
    'category': 'terminal',
    'description': 'Show Screen help and commands',
    'common': 'Ctrl+A then ?'
},
'screen_copy_mode': {
    'category': 'terminal',
    'description': 'Enter copy/scrollback mode',
    'common': 'Ctrl+A then [ (use arrows to scroll, Space to mark, Enter to copy)'
},
'screen_split_horizontal': {
    'category': 'terminal',
    'description': 'Split screen horizontally',
    'common': 'Ctrl+A then S'
},
'screen_split_vertical': {
    'category': 'terminal',
    'description': 'Split screen vertically',
    'common': 'Ctrl+A then | (pipe)'
},
'screen_switch_region': {
    'category': 'terminal',
    'description': 'Switch between split regions',
    'common': 'Ctrl+A then Tab'
},
'screen_remove_region': {
    'category': 'terminal',
    'description': 'Remove current split region',
    'common': 'Ctrl+A then X'
},
'screen_only_region': {
    'category': 'terminal',
    'description': 'Remove all regions except current',
    'common': 'Ctrl+A then Q'
},
# ============================================
    # TMUX - Terminal Multiplexer (Modern Alternative to Screen)
    # NOTE: Commands below reflect ZAKI'S CUSTOM CONFIG (~/.tmux.conf)
    # Prefix changed from Ctrl+B to Ctrl+A, custom splits, mouse enabled
    # ============================================
    
    # Session Management
    'tmux_new': {
        'category': 'terminal',
        'description': 'Start new tmux session',
        'common': 'tmux OR tmux new -s sessionname (named session)'
    },
    'tmux_list': {
        'category': 'terminal',
        'description': 'List all tmux sessions',
        'common': 'tmux ls OR tmux list-sessions'
    },
    'tmux_attach': {
        'category': 'terminal',
        'description': 'Attach to existing session',
        'common': 'tmux attach OR tmux a -t sessionname'
    },
    'tmux_detach': {
        'category': 'terminal',
        'description': 'Detach from current session (keeps running)',
        'common': 'Ctrl+A then D',
        'default': 'Ctrl+B then D'
    },
    'tmux_kill_session': {
        'category': 'terminal',
        'description': 'Kill specific session',
        'common': 'tmux kill-session -t sessionname'
    },
    'tmux_kill_all': {
        'category': 'terminal',
        'description': 'Kill all sessions',
        'common': 'tmux kill-server'
    },
    'tmux_rename_session': {
        'category': 'terminal',
        'description': 'Rename current session',
        'common': 'Ctrl+A then $',
        'default': 'Ctrl+B then $'
    },
    'tmux_switch_session': {
        'category': 'terminal',
        'description': 'Switch between sessions interactively',
        'common': 'Ctrl+A then S',
        'default': 'Ctrl+B then S'
    },
    
    # Window Management (like tabs)
    'tmux_new_window': {
        'category': 'terminal',
        'description': 'Create new window',
        'common': 'Ctrl+A then C',
        'default': 'Ctrl+B then C'
    },
    'tmux_next_window': {
        'category': 'terminal',
        'description': 'Switch to next window',
        'common': 'Ctrl+A then N',
        'default': 'Ctrl+B then N'
    },
    'tmux_previous_window': {
        'category': 'terminal',
        'description': 'Switch to previous window',
        'common': 'Ctrl+A then P',
        'default': 'Ctrl+B then P'
    },
    'tmux_list_windows': {
        'category': 'terminal',
        'description': 'List all windows',
        'common': 'Ctrl+A then W',
        'default': 'Ctrl+B then W'
    },
    'tmux_switch_window_number': {
        'category': 'terminal',
        'description': 'Switch to window by number',
        'common': 'Ctrl+A then 0-9',
        'default': 'Ctrl+B then 0-9'
    },
    'tmux_rename_window': {
        'category': 'terminal',
        'description': 'Rename current window',
        'common': 'Ctrl+A then , (comma)',
        'default': 'Ctrl+B then ,'
    },
    'tmux_kill_window': {
        'category': 'terminal',
        'description': 'Kill current window',
        'common': 'Ctrl+A then &',
        'default': 'Ctrl+B then &'
    },
    'tmux_last_window': {
        'category': 'terminal',
        'description': 'Toggle to last active window',
        'common': 'Ctrl+A then L',
        'default': 'Ctrl+B then L'
    },
    'tmux_find_window': {
        'category': 'terminal',
        'description': 'Search for window by name',
        'common': 'Ctrl+A then F',
        'default': 'Ctrl+B then F'
    },
    
    # Pane Management (split windows) - CUSTOM BINDINGS
    'tmux_split_horizontal': {
        'category': 'terminal',
        'description': 'Split pane horizontally (top/bottom) - CUSTOM',
        'common': 'Ctrl+A then - (dash)',
        'default': 'Ctrl+B then "'
    },
    'tmux_split_vertical': {
        'category': 'terminal',
        'description': 'Split pane vertically (left/right) - CUSTOM',
        'common': 'Ctrl+A then | (pipe)',
        'default': 'Ctrl+B then %'
    },
    'tmux_navigate_panes': {
        'category': 'terminal',
        'description': 'Navigate between panes',
        'common': 'Ctrl+A then arrow keys',
        'default': 'Ctrl+B then arrow keys'
    },
    'tmux_cycle_panes': {
        'category': 'terminal',
        'description': 'Cycle through panes',
        'common': 'Ctrl+A then O',
        'default': 'Ctrl+B then O'
    },
    'tmux_select_pane_number': {
        'category': 'terminal',
        'description': 'Select pane by number (shows numbers)',
        'common': 'Ctrl+A then Q, then number',
        'default': 'Ctrl+B then Q, then number'
    },
    'tmux_kill_pane': {
        'category': 'terminal',
        'description': 'Kill current pane',
        'common': 'Ctrl+A then X OR type exit',
        'default': 'Ctrl+B then X'
    },
    'tmux_zoom_pane': {
        'category': 'terminal',
        'description': 'Toggle pane zoom (full screen)',
        'common': 'Ctrl+A then Z',
        'default': 'Ctrl+B then Z'
    },
    'tmux_resize_pane': {
        'category': 'terminal',
        'description': 'Resize current pane',
        'common': 'Ctrl+A then Ctrl+arrow',
        'default': 'Ctrl+B then Ctrl+arrow'
    },
    'tmux_swap_pane': {
        'category': 'terminal',
        'description': 'Swap current pane with next',
        'common': 'Ctrl+A then { or }',
        'default': 'Ctrl+B then { or }'
    },
    'tmux_break_pane': {
        'category': 'terminal',
        'description': 'Break pane into new window',
        'common': 'Ctrl+A then !',
        'default': 'Ctrl+B then !'
    },
    'tmux_rotate_panes': {
        'category': 'terminal',
        'description': 'Rotate pane positions',
        'common': 'Ctrl+A then Ctrl+O',
        'default': 'Ctrl+B then Ctrl+O'
    },
    'tmux_even_horizontal': {
        'category': 'terminal',
        'description': 'Arrange panes evenly horizontal',
        'common': 'Ctrl+A then Alt+1',
        'default': 'Ctrl+B then Alt+1'
    },
    'tmux_even_vertical': {
        'category': 'terminal',
        'description': 'Arrange panes evenly vertical',
        'common': 'Ctrl+A then Alt+2',
        'default': 'Ctrl+B then Alt+2'
    },
    'tmux_main_horizontal': {
        'category': 'terminal',
        'description': 'Main pane on top, others below',
        'common': 'Ctrl+A then Alt+3',
        'default': 'Ctrl+B then Alt+3'
    },
    'tmux_main_vertical': {
        'category': 'terminal',
        'description': 'Main pane left, others right',
        'common': 'Ctrl+A then Alt+4',
        'default': 'Ctrl+B then Alt+4'
    },
    'tmux_tiled_layout': {
        'category': 'terminal',
        'description': 'Tile all panes evenly',
        'common': 'Ctrl+A then Alt+5',
        'default': 'Ctrl+B then Alt+5'
    },
    
    # Copy Mode & Scrolling
    'tmux_copy_mode': {
        'category': 'terminal',
        'description': 'Enter copy/scrollback mode',
        'common': 'Ctrl+A then [ (arrows/PgUp/PgDn, Space to select, Enter to copy)',
        'default': 'Ctrl+B then ['
    },
    'tmux_paste': {
        'category': 'terminal',
        'description': 'Paste from tmux buffer',
        'common': 'Ctrl+A then ]',
        'default': 'Ctrl+B then ]'
    },
    'tmux_show_buffer': {
        'category': 'terminal',
        'description': 'Show paste buffer contents',
        'common': 'tmux show-buffer'
    },
    'tmux_list_buffers': {
        'category': 'terminal',
        'description': 'List all paste buffers',
        'common': 'Ctrl+A then # OR tmux list-buffers',
        'default': 'Ctrl+B then #'
    },
    'tmux_choose_buffer': {
        'category': 'terminal',
        'description': 'Choose which buffer to paste',
        'common': 'Ctrl+A then =',
        'default': 'Ctrl+B then ='
    },
    'tmux_save_buffer': {
        'category': 'terminal',
        'description': 'Save buffer to file',
        'common': 'tmux save-buffer filename.txt'
    },
    
    # Help & Information
    'tmux_help': {
        'category': 'terminal',
        'description': 'Show tmux help and all keybindings',
        'common': 'Ctrl+A then ? (press Q to exit)',
        'default': 'Ctrl+B then ?'
    },
    'tmux_clock': {
        'category': 'terminal',
        'description': 'Display clock (fun easter egg!)',
        'common': 'Ctrl+A then T',
        'default': 'Ctrl+B then T'
    },
    'tmux_show_messages': {
        'category': 'terminal',
        'description': 'Show tmux message log',
        'common': 'Ctrl+A then ~',
        'default': 'Ctrl+B then ~'
    },
    'tmux_command_prompt': {
        'category': 'terminal',
        'description': 'Enter tmux command prompt',
        'common': 'Ctrl+A then :',
        'default': 'Ctrl+B then :'
    },
    
    # Configuration & Customization - CUSTOM RELOAD
    'tmux_reload_config': {
        'category': 'terminal',
        'description': 'Reload tmux config file - CUSTOM BINDING',
        'common': 'Ctrl+A then R',
        'default': 'tmux source-file ~/.tmux.conf (manual)'
    },
    'tmux_show_options': {
        'category': 'terminal',
        'description': 'Show all tmux options',
        'common': 'tmux show-options -g'
    },
    'tmux_set_option': {
        'category': 'terminal',
        'description': 'Set tmux option',
        'common': 'tmux set-option -g option-name value'
    },
    
    # Advanced Session Management
    'tmux_new_session_attach': {
        'category': 'terminal',
        'description': 'Create or attach to named session',
        'common': 'tmux new-session -A -s sessionname (creates if not exists)'
    },
    'tmux_send_keys': {
        'category': 'terminal',
        'description': 'Send commands to specific window/pane',
        'common': 'tmux send-keys -t sessionname:0 "command" Enter'
    },
    'tmux_capture_pane': {
        'category': 'terminal',
        'description': 'Capture pane contents to file',
        'common': 'tmux capture-pane -t sessionname:0 -p > output.txt'
    },
    'tmux_pipe_pane': {
        'category': 'terminal',
        'description': 'Log all pane output to file',
        'common': 'tmux pipe-pane -o "cat >> ~/tmux-output.log"'
    },
    'tmux_respawn_pane': {
        'category': 'terminal',
        'description': 'Restart command in pane',
        'common': 'Ctrl+A then : then respawn-pane',
        'default': 'Ctrl+B then :'
    },
    
    # Mouse Support - ENABLED IN YOUR CONFIG
    'tmux_mouse_support': {
        'category': 'terminal',
        'description': 'Mouse support (ENABLED in your config)',
        'common': 'Click panes to switch, drag borders to resize, scroll to navigate history'
    },
    'tmux_mouse_toggle': {
        'category': 'terminal',
        'description': 'Toggle mouse support on/off',
        'common': 'tmux set -g mouse on (or off)'
    },
    
    # Text Processing
    'cat': {
        'category': 'text',
        'description': 'Display file contents',
        'common': 'cat file.txt'
    },
    'grep': {
        'category': 'text',
        'description': 'Search text for patterns',
        'common': 'grep "error" file.log or grep -i "ERROR" file'
    },
    'awk': {
        'category': 'text',
        'description': 'Pattern scanning and text processing',
        'common': 'awk \'{print $1}\' file (print first column)'
    },
    'sed': {
        'category': 'text',
        'description': 'Stream editor for text manipulation',
        'common': 'sed \'s/old/new/g\' file'
    },
    'head': {
        'category': 'text',
        'description': 'Display first lines of file',
        'common': 'head -n 20 file.txt'
    },
    'tail': {
        'category': 'text',
        'description': 'Display last lines of file',
        'common': 'tail -f file.log (follow in real-time)'
    },
    'less': {
        'category': 'text',
        'description': 'View file contents page by page',
        'common': 'less file.txt (q to quit)'
    },
    'wc': {
        'category': 'text',
        'description': 'Count lines, words, characters',
        'common': 'wc -l file.txt (count lines)'
    },
    'sort': {
        'category': 'text',
        'description': 'Sort lines of text',
        'common': 'sort file.txt'
    },
    'uniq': {
        'category': 'text',
        'description': 'Remove duplicate lines',
        'common': 'sort file | uniq'
    },
    'cut': {
        'category': 'text',
        'description': 'Extract sections from lines',
        'common': 'cut -d: -f1 /etc/passwd'
    },
    
    # Networking
    'ifconfig': {
        'category': 'networking',
        'description': 'Configure network interfaces (legacy)',
        'common': 'ifconfig'
    },
    'ip': {
        'category': 'networking',
        'description': 'Modern network configuration tool',
        'common': 'ip addr or ip route'
    },
    'ping': {
        'category': 'networking',
        'description': 'Test network connectivity',
        'common': 'ping -c 4 google.com'
    },
    'netstat': {
        'category': 'networking',
        'description': 'Network statistics and connections',
        'common': 'netstat -tulpn (listening ports)'
    },
    'ss': {
        'category': 'networking',
        'description': 'Socket statistics (modern netstat)',
        'common': 'ss -tulpn'
    },
    'nmap': {
        'category': 'networking',
        'description': 'Network scanner',
        'common': 'nmap -sV 192.168.1.1'
    },
    'curl': {
        'category': 'networking',
        'description': 'Transfer data from URLs',
        'common': 'curl http://example.com'
    },
    'wget': {
        'category': 'networking',
        'description': 'Download files from web',
        'common': 'wget http://example.com/file.txt'
    },
    'nc': {
        'category': 'networking',
        'description': 'Netcat - network Swiss army knife',
        'common': 'nc -l -p 4444 (listen on port)'
    },
    'tcpdump': {
        'category': 'networking',
        'description': 'Capture network packets',
        'common': 'tcpdump -i eth0'
    },
    
    # Process Management
    'ps': {
        'category': 'process',
        'description': 'Display running processes',
        'common': 'ps aux'
    },
    'top': {
        'category': 'process',
        'description': 'Real-time process monitor',
        'common': 'top (press q to quit)'
    },
    'htop': {
        'category': 'process',
        'description': 'Interactive process viewer (better than top)',
        'common': 'htop'
    },
    'kill': {
        'category': 'process',
        'description': 'Send signal to process',
        'common': 'kill PID or kill -9 PID (force)'
    },
    'killall': {
        'category': 'process',
        'description': 'Kill processes by name',
        'common': 'killall firefox'
    },
    'bg': {
        'category': 'process',
        'description': 'Send process to background',
        'common': 'command & (start in background)'
    },
    'fg': {
        'category': 'process',
        'description': 'Bring process to foreground',
        'common': 'fg'
    },
    'nohup': {
        'category': 'process',
        'description': 'Run command immune to hangups',
        'common': 'nohup ./script.sh &'
    },
    
    # Security & System
    'sudo': {
        'category': 'security',
        'description': 'Execute command as superuser',
        'common': 'sudo command'
    },
    'su': {
        'category': 'security',
        'description': 'Switch user',
        'common': 'su - (become root)'
    },
    'ssh': {
        'category': 'security',
        'description': 'Secure shell remote login',
        'common': 'ssh user@192.168.1.100'
    },
    'scp': {
        'category': 'security',
        'description': 'Secure copy over SSH',
        'common': 'scp file.txt user@host:/path'
    },
    'passwd': {
        'category': 'security',
        'description': 'Change user password',
        'common': 'passwd'
    },
    'whoami': {
        'category': 'security',
        'description': 'Display current username',
        'common': 'whoami'
    },
    'id': {
        'category': 'security',
        'description': 'Display user identity',
        'common': 'id'
    },
    'last': {
        'category': 'security',
        'description': 'Show last logged in users',
        'common': 'last'
    },
    'history': {
        'category': 'security',
        'description': 'Show command history',
        'common': 'history | grep ssh'
    },
    
    # System Info
    'uname': {
        'category': 'system',
        'description': 'Print system information',
        'common': 'uname -a'
    },
    'hostname': {
        'category': 'system',
        'description': 'Show system hostname',
        'common': 'hostname'
    },
    'df': {
        'category': 'system',
        'description': 'Display disk space usage',
        'common': 'df -h'
    },
    'du': {
        'category': 'system',
        'description': 'Estimate file space usage',
        'common': 'du -sh *'
    },
    'free': {
        'category': 'system',
        'description': 'Display memory usage',
        'common': 'free -h'
    },
    'uptime': {
        'category': 'system',
        'description': 'Show how long system has been running',
        'common': 'uptime'
    },
    'date': {
        'category': 'system',
        'description': 'Display system date/time',
        'common': 'date'
    },
    
    # Package Management
    'apt': {
        'category': 'package',
        'description': 'Package manager for Debian/Ubuntu',
        'common': 'apt update, apt install package'
    },
    'apt-get': {
        'category': 'package',
        'description': 'Legacy APT package manager',
        'common': 'apt-get install package'
    },
    'dpkg': {
        'category': 'package',
        'description': 'Low-level package manager',
        'common': 'dpkg -i package.deb or dpkg -l'
    },
    
    # Compression
    'tar': {
        'category': 'compression',
        'description': 'Archive files',
        'common': 'tar -czf file.tar.gz dir/ or tar -xzf file.tar.gz'
    },
    'gzip': {
        'category': 'compression',
        'description': 'Compress files',
        'common': 'gzip file.txt'
    },
    'gunzip': {
        'category': 'compression',
        'description': 'Decompress gzip files',
        'common': 'gunzip file.txt.gz'
    },
    'zip': {
        'category': 'compression',
        'description': 'Package and compress files',
        'common': 'zip -r archive.zip directory/'
    },
    'unzip': {
        'category': 'compression',
        'description': 'Extract zip archives',
        'common': 'unzip archive.zip'
    },
    
    # Misc Useful
    'man': {
        'category': 'help',
        'description': 'Display manual pages',
        'common': 'man ls'
    },
    'which': {
        'category': 'help',
        'description': 'Locate a command',
        'common': 'which python'
    },
    'whereis': {
        'category': 'help',
        'description': 'Locate binary/source/manual',
        'common': 'whereis ls'
    },
    'alias': {
        'category': 'help',
        'description': 'Create command shortcuts',
        'common': 'alias ll="ls -la"'
    },
    'echo': {
        'category': 'help',
        'description': 'Display text or variables',
        'common': 'echo "Hello" or echo $PATH'
    },
    'clear': {
        'category': 'help',
        'description': 'Clear terminal screen',
        'common': 'clear (or Ctrl+L)'
    },
    'exit': {
        'category': 'help',
        'description': 'Exit shell or close terminal',
        'common': 'exit (or Ctrl+D)'
    },
    
    # Security & Forensics
    'strings': {
        'category': 'security',
        'description': 'Extract printable strings from files',
        'common': 'strings binary_file'
    },
    'md5sum': {
        'category': 'security',
        'description': 'Calculate MD5 hash',
        'common': 'md5sum file.txt'
    },
    'sha256sum': {
        'category': 'security',
        'description': 'Calculate SHA-256 hash',
        'common': 'sha256sum file.txt'
    },
    'sha1sum': {
        'category': 'security',
        'description': 'Calculate SHA-1 hash',
        'common': 'sha1sum file.txt'
    },
    'file': {
        'category': 'security',
        'description': 'Determine file type',
        'common': 'file unknown_file'
    },
    'lsof': {
        'category': 'security',
        'description': 'List open files',
        'common': 'lsof -i :80'
    },
    'strace': {
        'category': 'security',
        'description': 'Trace system calls',
        'common': 'strace -p PID'
    },
    'ltrace': {
        'category': 'security',
        'description': 'Trace library calls',
        'common': 'ltrace ./program'
    },
    
    # System Services
    'systemctl': {
        'category': 'system',
        'description': 'Control systemd services',
        'common': 'systemctl status service'
    },
    'service': {
        'category': 'system',
        'description': 'Run init script',
        'common': 'service apache2 restart'
    },
    'journalctl': {
        'category': 'system',
        'description': 'Query systemd logs',
        'common': 'journalctl -f or journalctl -u service'
    },
    'crontab': {
        'category': 'system',
        'description': 'Schedule periodic tasks',
        'common': 'crontab -e or crontab -l'
    },
    'dmesg': {
        'category': 'system',
        'description': 'Print kernel messages',
        'common': 'dmesg | tail'
    },
    'reboot': {
        'category': 'system',
        'description': 'Reboot system',
        'common': 'sudo reboot'
    },
    'shutdown': {
        'category': 'system',
        'description': 'Shutdown system',
        'common': 'sudo shutdown -h now'
    },
    'init': {
        'category': 'system',
        'description': 'Change runlevel',
        'common': 'init 6 or init 0'
    },
    
    # Networking Advanced
    'dig': {
        'category': 'networking',
        'description': 'DNS lookup tool',
        'common': 'dig example.com'
    },
    'nslookup': {
        'category': 'networking',
        'description': 'Query DNS servers',
        'common': 'nslookup example.com'
    },
    'host': {
        'category': 'networking',
        'description': 'DNS lookup',
        'common': 'host example.com'
    },
    'arp': {
        'category': 'networking',
        'description': 'View ARP cache',
        'common': 'arp -a'
    },
    'route': {
        'category': 'networking',
        'description': 'Show routing table',
        'common': 'route -n'
    },
    'traceroute': {
        'category': 'networking',
        'description': 'Trace route to host',
        'common': 'traceroute google.com'
    },
    'whois': {
        'category': 'networking',
        'description': 'Domain registration info',
        'common': 'whois example.com'
    },
    'iptables': {
        'category': 'networking',
        'description': 'Firewall configuration',
        'common': 'iptables -L'
    },
    'telnet': {
        'category': 'networking',
        'description': 'Connect to remote host',
        'common': 'telnet host port'
    },
    'ftp': {
        'category': 'networking',
        'description': 'FTP client',
        'common': 'ftp hostname'
    },
    'sftp': {
        'category': 'networking',
        'description': 'Secure FTP',
        'common': 'sftp user@host'
    },
    
    # File Operations Advanced
    'touch': {
        'category': 'filesystem',
        'description': 'Create file or update timestamp',
        'common': 'touch newfile.txt'
    },
    'ln': {
        'category': 'filesystem',
        'description': 'Create links',
        'common': 'ln -s /path/to/file linkname'
    },
    'diff': {
        'category': 'filesystem',
        'description': 'Compare files',
        'common': 'diff file1 file2'
    },
    'locate': {
        'category': 'filesystem',
        'description': 'Find files by name',
        'common': 'locate filename'
    },
    'stat': {
        'category': 'filesystem',
        'description': 'Display file status',
        'common': 'stat file.txt'
    },
    'tree': {
        'category': 'filesystem',
        'description': 'Display directory tree',
        'common': 'tree or tree -L 2'
    },
    'dd': {
        'category': 'filesystem',
        'description': 'Convert and copy files',
        'common': 'dd if=input of=output'
    },
    'rsync': {
        'category': 'filesystem',
        'description': 'Remote file sync',
        'common': 'rsync -avz source/ dest/'
    },
    
    # User Management
    'useradd': {
        'category': 'users',
        'description': 'Create new user',
        'common': 'sudo useradd -m username'
    },
    'userdel': {
        'category': 'users',
        'description': 'Delete user',
        'common': 'sudo userdel -r username'
    },
    'usermod': {
        'category': 'users',
        'description': 'Modify user',
        'common': 'sudo usermod -aG group user'
    },
    'groupadd': {
        'category': 'users',
        'description': 'Create group',
        'common': 'sudo groupadd groupname'
    },
    'groupdel': {
        'category': 'users',
        'description': 'Delete group',
        'common': 'sudo groupdel groupname'
    },
    'w': {
        'category': 'users',
        'description': 'Show who is logged in',
        'common': 'w'
    },
    'who': {
        'category': 'users',
        'description': 'Show logged in users',
        'common': 'who'
    },
    'users': {
        'category': 'users',
        'description': 'Print logged in users',
        'common': 'users'
    },
    'groups': {
        'category': 'users',
        'description': 'Show user groups',
        'common': 'groups username'
    },
    'finger': {
        'category': 'users',
        'description': 'Display user info',
        'common': 'finger username'
    },
    
    # Shell & Environment
    'env': {
        'category': 'shell',
        'description': 'Display environment variables',
        'common': 'env'
    },
    'export': {
        'category': 'shell',
        'description': 'Set environment variables',
        'common': 'export VAR=value'
    },
    'source': {
        'category': 'shell',
        'description': 'Execute file commands',
        'common': 'source ~/.bashrc'
    },
    'set': {
        'category': 'shell',
        'description': 'Set shell options',
        'common': 'set'
    },
    'unset': {
        'category': 'shell',
        'description': 'Remove variable',
        'common': 'unset VARNAME'
    },
    'type': {
        'category': 'shell',
        'description': 'Describe command type',
        'common': 'type ls'
    },
    
    # Process Advanced
    'pgrep': {
        'category': 'process',
        'description': 'Find processes by name',
        'common': 'pgrep firefox'
    },
    'pkill': {
        'category': 'process',
        'description': 'Kill by name',
        'common': 'pkill firefox'
    },
    'nice': {
        'category': 'process',
        'description': 'Run with modified priority',
        'common': 'nice -n 10 command'
    },
    'renice': {
        'category': 'process',
        'description': 'Change process priority',
        'common': 'renice -n 5 -p PID'
    },
    'jobs': {
        'category': 'process',
        'description': 'List active jobs',
        'common': 'jobs'
    },
    'watch': {
        'category': 'process',
        'description': 'Execute periodically',
        'common': 'watch -n 2 "command"'
    },
    
    # Text Advanced
    'tr': {
        'category': 'text',
        'description': 'Translate characters',
        'common': 'echo "HELLO" | tr A-Z a-z'
    },
    'tee': {
        'category': 'text',
        'description': 'Write to stdout and file',
        'common': 'command | tee output.txt'
    },
    'nl': {
        'category': 'text',
        'description': 'Number lines',
        'common': 'nl file.txt'
    },
    'more': {
        'category': 'text',
        'description': 'View file page by page',
        'common': 'more file.txt'
    },
    'xargs': {
        'category': 'text',
        'description': 'Build commands from stdin',
        'common': 'find . -name "*.txt" | xargs rm'
    },
    'comm': {
        'category': 'text',
        'description': 'Compare sorted files',
        'common': 'comm file1 file2'
    },
    'paste': {
        'category': 'text',
        'description': 'Merge lines',
        'common': 'paste file1 file2'
    },
    'join': {
        'category': 'text',
        'description': 'Join lines on common field',
        'common': 'join file1 file2'
    },
    'column': {
        'category': 'text',
        'description': 'Format into columns',
        'common': 'column -t file.txt'
    },
    
    # Compression Advanced
    'bzip2': {
        'category': 'compression',
        'description': 'Compress with bzip2',
        'common': 'bzip2 file.txt'
    },
    'bunzip2': {
        'category': 'compression',
        'description': 'Decompress bzip2',
        'common': 'bunzip2 file.txt.bz2'
    },
    'xz': {
        'category': 'compression',
        'description': 'Compress with xz',
        'common': 'xz file.txt'
    },
    '7z': {
        'category': 'compression',
        'description': '7-Zip compression',
        'common': '7z a archive.7z files/'
    },
    'rar': {
        'category': 'compression',
        'description': 'Create RAR',
        'common': 'rar a archive.rar files/'
    },
    'unrar': {
        'category': 'compression',
        'description': 'Extract RAR',
        'common': 'unrar x archive.rar'
    },
    
    # Disk & Mount
    'mount': {
        'category': 'disk',
        'description': 'Mount filesystem',
        'common': 'sudo mount /dev/sdb1 /mnt'
    },
    'umount': {
        'category': 'disk',
        'description': 'Unmount filesystem',
        'common': 'sudo umount /mnt'
    },
    'fdisk': {
        'category': 'disk',
        'description': 'Partition table tool',
        'common': 'sudo fdisk -l'
    },
    'lsblk': {
        'category': 'disk',
        'description': 'List block devices',
        'common': 'lsblk'
    },
    'blkid': {
        'category': 'disk',
        'description': 'Display block device attributes',
        'common': 'sudo blkid'
    },
    'parted': {
        'category': 'disk',
        'description': 'Partition tool',
        'common': 'sudo parted -l'
    },
    
    # Hardware Info
    'lscpu': {
        'category': 'hardware',
        'description': 'Display CPU info',
        'common': 'lscpu'
    },
    'lspci': {
        'category': 'hardware',
        'description': 'List PCI devices',
        'common': 'lspci'
    },
    'lsusb': {
        'category': 'hardware',
        'description': 'List USB devices',
        'common': 'lsusb'
    },
    'dmidecode': {
        'category': 'hardware',
        'description': 'Display hardware info',
        'common': 'sudo dmidecode'
    },
    'hdparm': {
        'category': 'hardware',
        'description': 'Hard disk parameters',
        'common': 'sudo hdparm -I /dev/sda'
    },
    
    # Editors
    'nano': {
        'category': 'editor',
        'description': 'Simple text editor',
        'common': 'nano file.txt'
    },
    'vi': {
        'category': 'editor',
        'description': 'Classic editor',
        'common': 'vi file.txt'
    },
    'vim': {
        'category': 'editor',
        'description': 'Vi IMproved',
        'common': 'vim file.txt'
    },
    'emacs': {
        'category': 'editor',
        'description': 'GNU Emacs',
        'common': 'emacs file.txt'
    },
    
    # Terminal
    'screen': {
        'category': 'terminal',
        'description': 'Terminal multiplexer',
        'common': 'screen -S sessionname'
    },
    'tmux': {
        'category': 'terminal',
        'description': 'Modern multiplexer',
        'common': 'tmux new -s sessionname'
    },
    
    # Scheduling
    'at': {
        'category': 'scheduling',
        'description': 'Schedule one-time task',
        'common': 'echo "cmd" | at 10:00 AM'
    },
    'batch': {
        'category': 'scheduling',
        'description': 'Execute when load permits',
        'common': 'echo "cmd" | batch'
    },
    
    # Permissions
    'umask': {
        'category': 'permissions',
        'description': 'Set default permissions',
        'common': 'umask 022'
    },
    'getfacl': {
        'category': 'permissions',
        'description': 'Get ACLs',
        'common': 'getfacl file.txt'
    },
    'setfacl': {
        'category': 'permissions',
        'description': 'Set ACLs',
        'common': 'setfacl -m u:user:rwx file'
    },
    
    # Misc
    'bc': {
        'category': 'misc',
        'description': 'Calculator',
        'common': 'echo "2+2" | bc'
    },
    'cal': {
        'category': 'misc',
        'description': 'Display calendar',
        'common': 'cal'
    },
    'time': {
        'category': 'misc',
        'description': 'Time command execution',
        'common': 'time command'
    },
    'sleep': {
        'category': 'misc',
        'description': 'Delay',
        'common': 'sleep 5'
    },
    'yes': {
        'category': 'misc',
        'description': 'Output string repeatedly',
        'common': 'yes | command'
    },
    'printenv': {
        'category': 'misc',
        'description': 'Print environment',
        'common': 'printenv or printenv PATH'
    }
}

# Category names
CATEGORIES = {
    'filesystem': 'File System',
    'text': 'Text Processing',
    'networking': 'Networking',
    'process': 'Process Management',
    'security': 'Security & Forensics',
    'system': 'System Information',
    'package': 'Package Management',
    'compression': 'Compression',
    'help': 'Helpful Commands',
    'users': 'User Management',
    'shell': 'Shell & Environment',
    'disk': 'Disk & Mount',
    'hardware': 'Hardware Info',
    'editor': 'Text Editors',
    'terminal': 'Terminal Tools',
    'scheduling': 'Task Scheduling',
    'permissions': 'Permissions & ACL',
    'misc': 'Miscellaneous'
}

def show_main_menu():
    """Display main menu"""
    print(f"\n{Colors.CYAN}╔════════════════════════════════════════╗")
    print(f"║           MAIN MENU                    ║")
    print(f"╚════════════════════════════════════════╝{Colors.RESET}\n")
    print(f"{Colors.GREEN}[1]{Colors.RESET} Search Commands")
    print(f"{Colors.GREEN}[2]{Colors.RESET} Browse by Category")
    print(f"{Colors.GREEN}[3]{Colors.RESET} Show All Commands")
    print(f"{Colors.GREEN}[4]{Colors.RESET} Exit")
    print()

def search_commands(query):
    """Search commands by name or description"""
    query = query.lower()
    results = []
    
    for cmd, info in COMMANDS.items():
        if (query in cmd.lower() or 
            query in info['description'].lower() or
            query in info['common'].lower()):
            results.append((cmd, info))
    
    if not results:
        print(f"\n{Colors.RED}No commands found matching '{query}'{Colors.RESET}")
        return
    
    print(f"\n{Colors.CYAN}╔════════════════════════════════════════════════════════════════════╗")
    print(f"║  Found {len(results)} command(s) matching '{query}'")
    print(f"╚════════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    for cmd, info in results:
        display_command(cmd, info)
        print()

def display_command(cmd, info):
    """Display single command - ZAKI PREMIUM EDITION"""
    print(f"\n{Colors.CYAN}{'─' * 70}{Colors.RESET}")
    
    # Add 🦁 for CUSTOM commands
    custom_badge = " 🦁" if "CUSTOM" in info['description'] else ""
    print(f"{Colors.BOLD}{Colors.YELLOW}▶ {cmd}{custom_badge}{Colors.RESET}")
    
    print(f"  {Colors.WHITE}👉🏾 {info['description']}{Colors.RESET}")
    print(f"  {Colors.CYAN}💻 {Colors.GREEN}{info['common']}{Colors.RESET}")
    if 'default' in info:
        print(f"  {Colors.CYAN}📋 Default: {Colors.RESET}{info['default']}")

def browse_by_category():
    """Browse commands by category"""
    print(f"\n{Colors.CYAN}╔════════════════════════════════════════╗")
    print(f"║        COMMAND CATEGORIES              ║")
    print(f"╚════════════════════════════════════════╝{Colors.RESET}\n")
    
    # Group commands by category
    categories = {}
    for cmd, info in COMMANDS.items():
        cat = info['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append((cmd, info))
    
    # Display categories
    cat_list = list(categories.keys())
    for i, cat in enumerate(cat_list, 1):
        count = len(categories[cat])
        cat_name = CATEGORIES.get(cat, cat)
        print(f"{Colors.GREEN}[{i}]{Colors.RESET} {cat_name} ({count} commands)")
    
    print(f"{Colors.GREEN}[0]{Colors.RESET} Back")
    
    choice = input(f"\n{Colors.YELLOW}Select category: {Colors.RESET}").strip()
    
    if choice == '0':
        return
    
    try:
        choice_num = int(choice) - 1
        selected_cat = cat_list[choice_num]
        cat_name = CATEGORIES.get(selected_cat, selected_cat)
        
        print(f"\n{Colors.CYAN}╔════════════════════════════════════════════════════════════════════╗")
        print(f"║  {cat_name}")
        print(f"╚════════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
        
        for cmd, info in sorted(categories[selected_cat]):
            display_command(cmd, info)
            print()
    except (ValueError, IndexError):
        print(f"{Colors.RED}Invalid selection{Colors.RESET}")

def show_all_commands():
    """Display all commands alphabetically"""
    print(f"\n{Colors.CYAN}╔════════════════════════════════════════════════════════════════════╗")
    print(f"║           ALL COMMANDS ({len(COMMANDS)} total)")
    print(f"╚════════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    for cmd, info in sorted(COMMANDS.items()):
        display_command(cmd, info)
        print()

def main():
    """Main program loop"""
    print_banner()
    
    while True:
        show_main_menu()
        choice = input(f"{Colors.YELLOW}Select option (1-4): {Colors.RESET}").strip()
        
        if choice == '1':
            query = input(f"\n{Colors.YELLOW}Search: {Colors.RESET}").strip()
            if query:
                search_commands(query)
            else:
                print(f"{Colors.RED}Please enter a search term{Colors.RESET}")
        
        elif choice == '2':
            browse_by_category()
        
        elif choice == '3':
            show_all_commands()
        
        elif choice == '4':
            print(f"\n{Colors.YELLOW}{'═' * 70}")
            print(f"  Thanks for using ZAKI-LINUX!")
            print(f"  Keep going, BELIEVE! ")
            print(f"  \"I never go back on my word - that's my ninja way!\"")
            print(f"{'═' * 70}{Colors.RESET}\n")
            sys.exit(0)
        
        else:
            print(f"{Colors.RED}Invalid option{Colors.RESET}")
        
        input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.RESET}")
        os.system('clear' if os.name == 'posix' else 'cls')
        print_banner()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Exiting... Stay strong! {Colors.RESET}\n")
        sys.exit(0)