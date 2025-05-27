#!/bin/bash

apt update
apt install zsh wget git python3 -y
sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
exit
