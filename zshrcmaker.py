import os, sys



home_dir = os.path.expanduser("~")
current_dir = os.getcwd()

if os.path.abspath(current_dir) != os.path.abspath(home_dir):
    print("Copy this file to your /home/ directory and try again.")
    sys.exit(1)



banner = """

|___  /  ___| | | | ___ /  __ \ |  \/  |/ _ \| | / |  ___| ___ |
   / /\ `--.| |_| | |_/ | /  \/ | .  . / /_\ | |/ /| |__ | |_/ /
  / /  `--. |  _  |    /| |     | |\/| |  _  |    \|  __||    / 
./ /__/\__/ | | | | |\ \| \__/\_| |  | | | | | |\  | |___| |\ \ 
\_____\____/\_| |_\_| \_|\____(_\_|  |_\_| |_\_| \_\____/\_| \_|                                               

"""



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
	if x == "2":
		termux()
	if x == "3":
		other()
	if x == "4":
		exit()
	


def kali():
    os.system("git clone https://github.com/amstrad/oh-my-matrix ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/oh-my-matrix")
    os.system("git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions")
    os.system("git clone https://github.com/zdharma-continuum/fast-syntax-highlighting ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/fast-syntax-highlighting")
    os.system("git clone https://github.com/zsh-users/zsh-history-substring-search ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-history-substring-search")
    os.system("git clone https://github.com/supremXD/commandshortcuts")
    os.system("mkdir -p ~/Documents/commandshortcuts")
    os.system("mv commandshortcuts/* ~/Documents/commandshortcuts/")
    os.system("rm -rf commandshortcuts")
    os.system("sudo chmod +x ~/Documents/commandshortcuts/autoserveranddownloading/autoserver/autoserver.sh")
    os.system("sudo chmod +x ~/Documents/commandshortcuts/autoserveranddownloading/autoserver/autoserver.sh")
    aliases = [
        'alias pythonserver="python3 -m http.server 8080"',
        'alias cls="clear"',
        'alias bat="batcat"',
        'alias cat="/usr/bin/cat"',
        'alias cptoserver="python3 ~/Documents/commandshortcuts/cptoserver.py"',
        'alias mvtoserver="python3 ~/Documents/commandshortcuts/mvtoserver.py"',
        'alias apacheup="sudo service apache2 start"',
        'alias apachedown="sudo service apache2 stop"',
        'alias wichsystem="python3 ~/Documents/commandshortcuts/whichsystem.py"',
        'alias debinstall="sudo dpkg -i"',
        'alias autoserver="bash ~/Documents/commandshortcuts/autoserveranddownloading/autoserver/autoserver.sh"',
        'alias autodownload="bash ~/Documents/commandshortcuts/autoserveranddownloading/autodownload/autodownload.sh"',
        'alias temp="touch temp"',
        'alias mtemp="nano temp"',
        'alias rm%="rm -f temp"',
		'alias macfinder="python3 ~/Documents/commandshortcuts/macfinder.py"',
		'alias autonmap="python3 ~/Documents/commandshortcuts/autonmap.py"',
		'alias autosclose="python3 ~/Documents/commandshortcuts//autoserveranddownloading/autoserverclose.py"'
    ]
    for alias in aliases:
        os.system(f"echo '{alias}' >> ~/.zshrc")
    os.system("clear")
    print("")
    print("Add this to the plugins line in the ~/.zshrc file:")
    print("")
    print("oh-my-matrix")
    print("zsh-autosuggestions")
    print("fast-syntax-highlighting")
    print("zsh-history-substring-search")
    print("web-search")
    exit()



def termux():
    os.system("git clone https://github.com/amstrad/oh-my-matrix ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/oh-my-matrix")
    os.system("git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions")
    os.system("git clone https://github.com/zdharma-continuum/fast-syntax-highlighting ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/fast-syntax-highlighting")
    os.system("git clone https://github.com/zsh-users/zsh-history-substring-search ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-history-substring-search")
    os.system("mkdir -p things/commandshortcuts")
    os.system("git clone https://github.com/supremXD/commandshortcuts")
    os.system("mv commandshortcuts/* things/commandshortcuts")
    os.system("rm -rf commandshortcuts")
    os.system("chmod +x ~/things/commandshortcuts/autoserveranddownloading/autoserver/autoserver.sh")
    os.system("chmod +x ~/things/commandshortcuts/autoserveranddownloading/autodownload/autodownload.sh")
    aliases = [
        'alias pythonserver="python3 -m http.server 8080"',
        'alias cls="clear"',
        'alias bat="batcat"',
        'alias cat="/usr/bin/cat"',
        'alias autoserver="bash ~/things/commandshortcuts/autoserveranddownloading/autoserver/autoserver.sh"',
        'alias autodownload="bash ~/things/commandshortcuts/autoserveranddownloading/autodownload/autodownload.sh"',
        'alias temp="touch temp"',
        'alias mtemp="nano temp"',
        'alias rm%="rm -f temp"',
		'alias autosclose="python3 ~/things/commandshortcuts//autoserveranddownloading/autoserverclose.py"'
    ]
    for alias in aliases:
        os.system(f"echo '{alias}' >> ~/.zshrc")
    os.system("clear")
    print("")
    print("Add this to the plugins line in the ~/.zshrc file:")
    print("")
    print("oh-my-matrix")
    print("zsh-autosuggestions")
    print("fast-syntax-highlighting")
    print("zsh-history-substring-search")
    print("web-search")
    exit()



def other():
    os.system("git clone https://github.com/amstrad/oh-my-matrix ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/oh-my-matrix")
    os.system("git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions")
    os.system("git clone https://github.com/zdharma-continuum/fast-syntax-highlighting ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/fast-syntax-highlighting")
    os.system("git clone https://github.com/zsh-users/zsh-history-substring-search ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-history-substring-search")
    os.system("git clone https://github.com/supremXD/commandshortcuts")
    os.system("mkdir -p ~/Documents/commandshortcuts")
    os.system("mv commandshortcuts/* ~/Documents/commandshortcuts/")
    os.system("rm -rf commandshortcuts")
    os.system("sudo chmod +x ~/Documents/commandshortcuts/autoserveranddownloading/autoserver/autoserver.sh")
    os.system("sudo chmod +x ~/Documents/commandshortcuts/autoserveranddownloading/autoserver/autoserver.sh")
    aliases = [
        'alias pythonserver="python3 -m http.server 8080"',
        'alias cls="clear"',
        'alias bat="batcat"',
        'alias cat="/usr/bin/cat"',
        'alias cptoserver="python3 ~/Documents/commandshortcuts/cptoserver.py"',
        'alias mvtoserver="python3 ~/Documents/commandshortcuts/mvtoserver.py"',
        'alias apacheup="sudo service apache2 start"',
        'alias apachedown="sudo service apache2 stop"',
        'alias debinstall="sudo dpkg -i"',
        'alias autoserver="bash ~/Documents/commandshortcuts/autoserveranddownloading/autoserver/autoserver.sh"',
        'alias autodownload="bash ~/Documents/commandshortcuts/autoserveranddownloading/autodownload/autodownload.sh"',
        'alias temp="touch temp"',
        'alias mtemp="nano temp"',
        'alias rm%="rm -f temp"',
		'alias autosclose="python3 ~/Documents/commandshortcuts//autoserveranddownloading/autoserverclose.py"'
    ]
    for alias in aliases:
        os.system(f"echo '{alias}' >> ~/.zshrc")
    os.system("clear")
    print("")
    print("Add this to the plugins line in the ~/.zshrc file:")
    print("")
    print("oh-my-matrix")
    print("zsh-autosuggestions")
    print("fast-syntax-highlighting")
    print("zsh-history-substring-search")
    print("web-search")
    exit()



menu()
