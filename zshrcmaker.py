#Version 3.0

import os, sys

# Banner.
banner = """
|___  /  ___| | | | ___ /  __ \ |  \/  |/ _ \| | / |  ___| ___ |
   / /\ `--.| |_| | |_/ | /  \/ | .  . / /_\ | |/ /| |__ | |_/ /
  / /  `--. |  _  |    /| |     | |\/| |  _  |    \|  __||    / 
./ /__/\__/ | | | | |\ \| \__/\_| |  | | | | | |\  | |___| |\ \ 
\_____\____/\_| |_\_| \_|\____(_\_|  |_\_| |_\_| \_\____/\_| \_|                                               
"""

# Function to add the plugins in .zshrc.
def add_plugins_to_zshrc():
    zshrc_path = os.path.expanduser("~/.zshrc")
    plugins_to_add = [
        "oh-my-matrix",
        "zsh-autosuggestions",
        "fast-syntax-highlighting",
        "zsh-history-substring-search",
        "web-search"
    ]

    if not os.path.exists(zshrc_path):
        print("[!] ~/.zshrc not found. Creating new file...")
        with open(zshrc_path, "w") as f:
            f.write("# ~/.zshrc generated automatically\n")

    with open(zshrc_path, "r") as f:
        lines = f.readlines()

    new_lines = []
    found_plugins = False

    for line in lines:
        if line.strip().startswith("plugins=("):
            found_plugins = True
            start = line.find("(")
            end = line.find(")")
            current_plugins = line[start + 1:end].split()
            
            for plugin in plugins_to_add:
                if plugin not in current_plugins:
                    current_plugins.append(plugin)

            new_line = f"plugins=({' '.join(current_plugins)})\n"
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    if not found_plugins:
        new_lines.append("\nplugins=(" + " ".join(plugins_to_add) + ")\n")

    with open(zshrc_path, "w") as f:
        f.writelines(new_lines)

    print("[✔] Plugins added successfully to ~/.zshrc!")

# Main menu.
def menu():
    os.system("clear")
    print(banner)
    print("              |                    1 -->> Install for Kali Linux")
    print("              |                    2 -->> Install for Termux")
    print("              |                    3 -->> Install for other debian based OS")
    print("              |                    4 -->> Exit")
    x = input("              ↳ ")
    if x == "1":
        kali()
    elif x == "2":
        termux()
    elif x == "3":
        other()
    else:
        exit()

# Instalation for kali linux.
def kali():
    os.system('sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"')
    os.system("git clone https://github.com/amstrad/oh-my-matrix ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/oh-my-matrix")
    os.system("git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions")
    os.system("git clone https://github.com/zdharma-continuum/fast-syntax-highlighting ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/fast-syntax-highlighting")
    os.system("git clone https://github.com/zsh-users/zsh-history-substring-search ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-history-substring-search")
    os.system("git clone https://github.com/supremXD/commandshortcuts")
    os.system("mkdir -p ~/.commandshortcuts")
    os.system("mv commandshortcuts/* ~/.commandshortcuts/")
    os.system("rm -rf commandshortcuts")
  
    aliases = [
        'alias pythonserver="python3 -m http.server 8080"',
        'alias cls="clear"',
        'alias bat="batcat"',
        'alias cat="/usr/bin/cat"',
        'alias cptoserver="python3 ~/.commandshortcuts/cptoserver.py"',
        'alias mvtoserver="python3 ~/.commandshortcuts/mvtoserver.py"',
        'alias apacheup="sudo service apache2 start"',
        'alias apachedown="sudo service apache2 stop"',
        'alias wichsystem="python3 ~/.commandshortcuts/whichsystem.py"',
        'alias debinstall="sudo dpkg -i"',
        'alias autoserver="python3 ~/.commandshortcuts/autoserveranddownloading/autoserver.py"',
        'alias autodownload="python3 ~/.commandshortcuts/autoserveranddownloading/autodownload.py"',
        'alias temp="touch temp"',
        'alias mtemp="nano temp"',
        'alias rm%="rm -f temp"',
        'alias macfinder="python3 ~/.commandshortcuts/macfinder.py"',
        'alias autonmap="python3 ~/.commandshortcuts/autonmap.py"',
        'alias autosclose="python3 ~/.commandshortcuts/autoserveranddownloading/autoserverclose.py"'
        'alias pdfconverter="python3 ~/.commandshortcuts/pdfconverter.py"'
    ]
    for alias in aliases:
        os.system(f"echo '{alias}' >> ~/.zshrc")

    os.system("clear")
    add_plugins_to_zshrc()
    print("\n[✔] Installation for Kali completed!\n")
    exit()

# Instalation for termux.
def termux():
    os.system('sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"')
    os.system("git clone https://github.com/amstrad/oh-my-matrix ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/oh-my-matrix")
    os.system("git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions")
    os.system("git clone https://github.com/zdharma-continuum/fast-syntax-highlighting ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/fast-syntax-highlighting")
    os.system("git clone https://github.com/zsh-users/zsh-history-substring-search ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-history-substring-search")
    os.system("git clone https://github.com/supremXD/commandshortcuts")
    os.system("mkdir -p ~/things/commandshortcuts")
    os.system("mv commandshortcuts/* ~/things/commandshortcuts/")
    os.system("rm -rf commandshortcuts")

    aliases = [
        'alias pythonserver="python3 -m http.server 8080"',
        'alias cls="clear"',
        'alias bat="batcat"',
        'alias cat="/usr/bin/cat"',
        'alias autoserver="python3 ~/.commandshortcuts/autoserveranddownloading/autoserver.py"',
        'alias autodownload="python3 ~/.commandshortcuts/autoserveranddownloading/autodownload.py"',
        'alias temp="touch temp"',
        'alias mtemp="nano temp"',
        'alias rm%="rm -f temp"',
        'alias autosclose="python3 ~/things/commandshortcuts/autoserveranddownloading/autoserverclose.py"'
    ]
    for alias in aliases:
        os.system(f"echo '{alias}' >> ~/.zshrc")

    os.system("clear")
    add_plugins_to_zshrc()
    print("\n[✔] Installation for Termux completed!\n")
    exit()

# Instalation for other OS based in debian.
def other():
    os.system('sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"')
    os.system("git clone https://github.com/amstrad/oh-my-matrix ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/oh-my-matrix")
    os.system("git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions")
    os.system("git clone https://github.com/zdharma-continuum/fast-syntax-highlighting ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/fast-syntax-highlighting")
    os.system("git clone https://github.com/zsh-users/zsh-history-substring-search ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-history-substring-search")
    os.system("git clone https://github.com/supremXD/commandshortcuts")
    os.system("mkdir -p ~/.commandshortcuts")
    os.system("mv commandshortcuts/* ~/.commandshortcuts/")
    os.system("rm -rf commandshortcuts")
    os.system("sudo chmod +x ~/.commandshortcuts/ip.sh")
    os.system("sudo chmod +x ~/.commandshortcuts/copy_ip.sh")
    os.system("rm -f ~/.commandshortcuts/autonmap.py")
    os.system("rm -f ~/.commandshortcuts/extractPorts.sh")
    os.system("rm -f ~/.commandshortcuts/macfinder.py")
    os.system("rm -f ~/.commandshortcuts/whichsystem.py")
    aliases = [
        'alias pythonserver="python3 -m http.server 8080"',
        'alias cls="clear"',
        'alias bat="batcat"',
        'alias cat="/usr/bin/cat"',
        'alias cptoserver="python3 ~/.commandshortcuts/cptoserver.py"',
        'alias mvtoserver="python3 ~/.commandshortcuts/mvtoserver.py"',
        'alias apacheup="sudo service apache2 start"',
        'alias apachedown="sudo service apache2 stop"',
        'alias debinstall="sudo dpkg -i"',
        'alias autoserver="python3 ~/.commandshortcuts/autoserveranddownloading/autoserver.py"',
        'alias autodownload="python3 ~/.commandshortcuts/autoserveranddownloading/autodownload.py"',
        'alias temp="touch temp"',
        'alias mtemp="nano temp"',
        'alias rm%="rm -f temp"',
        'alias autosclose="python3 ~/.commandshortcuts/autoserveranddownloading/autoserverclose.py"',
        'alias copyip="bash ~/.commandshortcuts/copy_ip.sh"',
        'alias contar="python3 ~/.commandshortcuts/contar.py"',
        'alias txttopdf="python3 ~/.commandshortcuts/txttopdf.py"'
        'alias pdfconverter="python3 ~/.commandshortcuts/pdfconverter.py"'
    ]
    for alias in aliases:
        os.system(f"echo '{alias}' >> ~/.zshrc")

    os.system("clear")
    add_plugins_to_zshrc()
    print("\n[✔] Installation for Debian completed!\n")
    exit()

# Start zshrcmaker
menu()
