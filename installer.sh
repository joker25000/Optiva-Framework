#!/bin/bash
# author : Joker-Security 
# Tested on Kali Linux / Parrot Os / Archman / ArcoLinux / Termux
# Simple script for Install Optiva-Framework
#Colors
cyan='\e[0;36m'
green='\e[0;32m'
lightgreen='\e[1;32m'
white='\e[1;37m'
red='\e[1;31m'
yellow='\e[1;33m'
blue='\e[1;34m'
#Options
path=`pwd` # Path
name="\e[1;34mOptiva-Framework" #Name
VeR="\e[1;31mV1.0.4" # Version
#Check root exist
#[[ `id -u` -eq 0 ]] > /dev/null 2>&1 || { echo  $red "You must be root to run the script"; exit 1; }
#banner head
function main_menu()
{
    while :
    do
echo -e """
 ██████╗ ██████╗ ████████╗██╗██╗   ██╗ █████╗                                     
██╔═══██╗██╔══██╗╚══██╔══╝██║██║   ██║██╔══██╗                                    
██║   ██║██████╔╝   ██║   ██║██║   ██║███████║                                    
██║   ██║██╔═══╝    ██║   ██║╚██╗ ██╔╝██╔══██║                                    
╚██████╔╝██║        ██║   ██║ ╚████╔╝ ██║  ██║                                    
 ╚═════╝ ╚═╝        ╚═╝   ╚═╝  ╚═══╝  ╚═╝  ╚═╝                                    
                                                                                  
    ███████╗██████╗  █████╗ ███╗   ███╗███████╗██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗
    ██╔════╝██╔══██╗██╔══██╗████╗ ████║██╔════╝██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝
    █████╗  ██████╔╝███████║██╔████╔██║█████╗  ██║ █╗ ██║██║   ██║██████╔╝█████╔╝ 
    ██╔══╝  ██╔══██╗██╔══██║██║╚██╔╝██║██╔══╝  ██║███╗██║██║   ██║██╔══██╗██╔═██╗ 
    ██║     ██║  ██║██║  ██║██║ ╚═╝ ██║███████╗╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗
    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
                        Setup Script for $name $VeR                                                                         
"""
echo -e $yellow "Systems Available : "
echo -e "$lightgreen 1) $red ✔ Kali Linux / Parrot-Os / Ubuntu "
echo -e "$lightgreen 2) $red ✔ Black Arch / Arch Linux / Archman"
echo -e "$lightgreen 3) $red ✔ Termux(Android)"
echo -e "$lightgreen 0) $red ✔ Exit"
echo -n -e "$lightgreen Select Your System : $red"
read -e joker
case $joker in
'1')
echo -e $green "[*] Loading... "
sudo apt-get update
sudo apt-get install python-pip
echo "[*] installing requirements...."
pip2 install -r requirements.txt
pip2 install mechanize
pip2 install requests
pip2 install termcolor
pip2 install --upgrade html5lib
pip2 install --upgrade beautifulsoup4
echo -e $green "[*] Moving Optiva-Framework folder "
mkdir /usr/share/optiva
cp -r ico /usr/share/optiva
cp -r core /usr/share/optiva
cp -r modules /usr/share/optiva
cp -r plugins /usr/share/optiva
cp installer.sh /usr/share/optiva
cp requirements.txt /usr/share/optiva
cp optiva.py /usr/share/optiva
echo -e $blue "[ ✔ ]Done"
echo -e $red "[*] Creating Icons Dirctory"
cp -r $path/ico/optiva.desktop /usr/share/applications/optiva.desktop
cp -r $path/ico/optiva.png /usr/share/icons/optiva.png
echo -e $yellow "[*] Creating shortcut command $red Optiva-Framework"
echo "#!/bin/sh" >> /usr/bin/optiva
echo "cd /usr/share/optiva" >> /usr/bin/optiva
echo "exec python2 optiva.py \"\$@\"" >> /usr/bin/optiva
chmod +x /usr/bin/optiva
echo -e $green ""
echo "------------------------------------" 
echo "| [ ✔ ]installation completed[ ✔ ] |" 
echo "------------------------------------" 
echo
echo -e $green "#####################################"
echo -e $blue "|Now Just Type In Terminal (optiva)|"
echo -e $green "#####################################"
echo -e $green "【!】 Main Menu【!】"
read -p "pess any key to return ..."
clear
;;
'2')
echo -e $green "[*] Loading... "
sudo pacman -Syy
sudo pacman -S python2-pip
echo "[*] installing requirements...."
pip2 install -r requirements.txt
pip2 install mechanize
pip2 install requests
pip2 install termcolor
pip2 install --upgrade html5lib
pip2 install --upgrade beautifulsoup4
echo -e $green "[*] Moving $red Optiva-Framework folder "
mkdir /usr/share/optiva
cp -r ico /usr/share/optiva
cp -r core /usr/share/optiva
cp -r modules /usr/share/optiva
cp -r plugins /usr/share/optiva
cp installer.sh /usr/share/optiva
cp requirements.txt /usr/share/optiva
cp optiva.py /usr/share/optiva
echo -e $blue "[ ✔ ]Done"
echo -e $red "[*] Creating Icons Dirctory"
cp -r $path/ico/optiva.desktop /usr/share/applications/optiva.desktop
cp -r $path/ico/optiva.png /usr/share/icons/optiva.png
echo -e $yellow "[*] Creating shortcut command Optiva-Framework"
echo "#!/bin/sh" >> /usr/bin/optiva
echo "cd /usr/share/optiva" >> /usr/bin/optiva
echo "exec python2 optiva.py \"\$@\"" >> /usr/bin/optiva
chmod +x /usr/bin/optiva
echo -e $green ""
echo "------------------------------------" 
echo "| [ ✔ ]installation completed[ ✔ ] |" 
echo "------------------------------------" 
echo
echo -e $green "#####################################"
echo -e $blue "|Now Just Type In Terminal (optiva)|"
echo -e $green "#####################################"
echo -e $green "【!】 Main Menu【!】"
read -p "pess any key to return ..."
clear
;;
'3')
echo -e $green "[*] Loading... "
apt install python2
echo "[*] installing requirements...."
pip2 install -r requirements.txt
pip2 install mechanize
pip2 install requests
pip2 install termcolor
pip2 install --upgrade html5lib
pip2 install --upgrade beautifulsoup4
echo -e $blue "[ ✔ ]Done"
echo -e $green ""
echo "------------------------------------" 
echo "| [ ✔ ]installation completed[ ✔ ] |" 
echo "------------------------------------" 
echo
echo "------------------------------------" 
echo "| [ ✔ ]Run python2 optiva.py[ ✔ ] |" 
echo "------------------------------------" 
echo -e $green "#########################################"
echo -e $blue "| Thanks For Installing Optiva-Framework |"
echo -e $green "#########################################"
echo -e $green "【!】 Main Menu【!】"
read -p "pess any key to return ..."
clear

;;
'0')
  echo -e $red " Good Bye !!"
  echo
  exit 0
  ;;
       esac
    done
}
main_menu                                                              
