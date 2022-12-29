# Dionaea
Cloud Security Service

### Install :

Update And Upgrade OS :

```
sudo apt update -y
sudo apt upgrade -y
```

Install requirements :

```
sudo apt install python2 python3 python2.7-dev python-pip python3-pip git perl nmap sslscan
sudo apt install wapiti whatweb nmap dnsrecon fierce dnswalk whois dnsenum dmitry nikto dnsmap dirb wafw00f
```

Upgrade Pip And Install Requirements :

```
sudo -H pip3 install --upgrade pip
sudo pip3 install bs4 pygeoip gobject cairocffi selenium sslyze setuptools wheel
```

Install Snap's Apps :

```
sudo snap install amass
```

Clone Github's Apps :

```
cd /opt
sudo git clone https://github.com/golismero/golismero.git
sudo git clone https://github.com/epsylon/xsser
sudo git clone https://github.com/laramies/theHarvester
sudo git clone https://github.com/poerschke/Uniscan
sudo git clone https://github.com/cldrn/davtest
```

Make Some Files Executable:

```
./Uniscan/install-modules.sh
```

Install App's Requirements:

```
pip2 install -r golismero/requirements.txt
pip2 install -r golismero/requirements_unix.txt
pip3 -m pip install -r theHarvester/requirements/dev.txt
pip3 -m pip install -r theHarvester/requirements/base.txt
```

Make Apps Command:

```
sudo ln -s ${PWD}/golismero/golismero.py /usr/bin/golismero
sudo ln -s ${PWD}/xsser/xsser /usr/bin/xsser
sudo ln -s ${PWD}/theHarvester/theHarvester.py /usr/bin/theHarvester
sudo ln -s ${PWD}/Uniscan/uniscan.pl /usr/bin/uniscan
sudo ln -s ${PWD}/Uniscan/davtest.pl /usr/bin/davtest
```

Install And Run Dionaea :

````
git clone https://github.com/hesamz3090/Dionaea.git
virtualenv Dionaea/venv
Dionaea/venv/bin/pip install -r requirements.txt
````

### Usage :
````
Dionaea/venv/bin/python3 Dionaea/manage.py runserver
````

