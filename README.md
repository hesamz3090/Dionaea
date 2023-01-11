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
sudo apt install python-pip python2 python3 python2.7-dev git perl sslscan snapd -y
sudo apt install wapiti whatweb nmap dnsrecon fierce dnswalk whois dnsenum dmitry nikto dnsmap dirb wafw00f -y
sudo apt install python3-pip
sudo apt install python-pip
sudo apt install python3-virtualenv
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
sudo git clone https://github.com/golismero/golismero
sudo git clone https://github.com/epsylon/xsser
sudo git clone https://github.com/laramies/theHarvester
sudo git clone https://github.com/poerschke/Uniscan
sudo git clone https://github.com/cldrn/davtest
```


Install Uniscan:
```
sudo chmod +x Uniscan/install-modules.sh
sudo ./Uniscan/install-modules.sh
cd --
```


Install App's Requirements:

```
pip2 install -r /opt/golismero/requirements.txt
pip2 install -r /opt/golismero/requirements_unix.txt
pip3 install -r /opt/theHarvester/requirements/dev.txt
pip3 install -r /opt/theHarvester/requirements/base.txt
```

Link Apps Command:

```
sudo ln -s /usr/bin/python3 /usr/bin/python
sudo ln -s /opt/golismero/golismero.py /usr/bin/golismero
sudo ln -s /opt/xsser/xsser /usr/bin/xsser
sudo ln -s /opt/theHarvester/theHarvester.py /usr/bin/theHarvester
sudo ln -s /opt/Uniscan/uniscan.pl /usr/bin/uniscan
sudo ln -s /opt/davtest/davtest.pl /usr/bin/davtest
```

Install And Run Dionaea :

````
sudo git clone https://github.com/hesamz3090/Dionaea
virtualenv Dionaea/venv
Dionaea/venv/bin/local/pip install -r Dionaea/requirements.txt
````

### Usage :
````
Dionaea/venv/local/bin/python3 Dionaea/manage.py runserver
````

