#!/bin/sh

sudo apt-get install iceweasel
sudo apt-get install xvfb
sudo apt-get install xserver-xephyr
sudo pip3 install selenium==2.53.6
sudo pip3 install pyvirtualdisplay
sudo pip3 install pytest
wget https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-arm7hf.tar.gz
tar -xf geckodriver-v0.19.1-arm7hf.tar.gz
rm geckodriver-v0.19.1-arm7hf.tar.gz
sudo chmod a+x geckodriver
sudo mv geckodriver /usr/local/bin/