# INSTALLATION.
+ Instalation for Debian based OS.
```bash
git clone https://github.com/supremXD/zshrcmaker
sudo apt update
sudo apt install zsh wget git python3 -y
sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
mv zshrcmaker/zshrcmaker.py .
python3 zshrcmaker.py
```
+ Instalation for Termux.
```bash
git clone https://github.com/supremXD/zshrcmaker
apt update
apt install zsh wget git python3 -y
sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
mv zshrcmaker/zshrcmaker.py .
python3 zshrcmaker.py
```
After last command, follow the instructions given in the output of the zshrcmaker.py, and make sure to change the alias
directories to your owns.
