sudo apt install python2 python3 python2.7-dev python-pip python3-pip git perl nmap sslscan
sudo apt install wapiti whatweb nmap dnsrecon fierce dnswalk whois dnsenum dmitry nikto dnsmap dirb wafw00f

pip install --upgrade pip setuptools wheel
sudo pip3 install bs4 pygeoip gobject cairocffi selenium sslyze

sudo snap install amass

cd /opt
sudo git clone https://github.com/golismero/golismero.git
sudo git clone https://github.com/epsylon/xsser
sudo git clone https://github.com/laramies/theHarvester
sudo git clone https://github.com/poerschke/Uniscan
sudo git clone https://github.com/cldrn/davtest

sudo chmod +x Uniscan/install-modules.sh

pip2 install -r golismero/requirements.txt
pip2 install -r golismero/requirements_unix.txt
pip3 -m pip install -r theHarvester/requirements/dev.txt
pip3 -m pip install -r theHarvester/requirements/base.txt
./Uniscan/install-modules.sh

sudo ln -s ${PWD}/golismero/golismero.py /usr/bin/golismero
sudo ln -s ${PWD}/xsser/xsser /usr/bin/xsser
sudo ln -s ${PWD}/theHarvester/theHarvester.py /usr/bin/theHarvester
sudo ln -s ${PWD}/Uniscan/uniscan.pl /usr/bin/uniscan
sudo ln -s ${PWD}/Uniscan/davtest.pl /usr/bin/davtest

