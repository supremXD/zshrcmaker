import os

def install():
	os.system("git clone https://github.com/amstrad/oh-my-matrix ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/oh-my-matrix")
	os.system("git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions")
	os.system("git clone https://github.com/zdharma-continuum/fast-syntax-highlighting ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/fast-syntax-highlighting")
	os.system("git clone https://github.com/zsh-users/zsh-history-substring-search ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-history-substring-search")
	os.system("echo alias pythonserver='python3 -m http.server 8080' >> .zshrc")
	os.system("echo alias cls='clear' >> .zshrc")
	os.system("echo alias bat='batcat' >> .zshrc")
	os.system("echo alias cat='/usr/bin/cat' >> .zshrc")
	os.system("echo alias intensenmap='sudo nmap -sS -min-rate 5000 -n -Pn -v' >> .zshrc")
	os.system("echo alias networkrestart='sudo systemctl restart NetworkManager.service && sudo ifdown -a && sudo ifup -a' >> .zshrc")
	os.system("echo alias cptoserver='python3 /home/suprem/Documents/commandsshortucts/cptoserver.py' >> .zshrc")
	os.system("echo alias mvtoserver='python3 /home/suprem/Documents/commandsshortucts/mvtoserver.py' >> .zshrc")
	os.system("echo alias apacheup='sudo service apache2 start' >> .zshrc")
	os.system("echo alias apachedown='sudo service apache2 stop' >> .zshrc")
	os.system("echo alias wichsystem='python3 /home/suprem/Documents/commandsshortucts/whichsystem.py' >> .zshrc")
	os.system("echo alias debinstall='sudo dpkg -i' >> .zshrc")
	os.system("alias autoserver='bash /home/suprem/Documents/commandsshortucts/autoserveranddownloading/autoserver/autoserver.sh'")
	os.system("alias autodownload='bash /home/suprem/Documents/commandsshortucts/autoserveranddownloading/autodownload/autodownload.sh'")
	os.system("clear")
	print("")
	print("Add this to the plugins part in the /home/suprem(.zshrc file: oh-my-matrix zsh-autosuggestions fast-syntax-highlighting zsh-history-substring-search web-search")
	while True:
		exit()

install()
