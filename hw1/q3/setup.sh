#!/usr/bin/bash

# 3.2

sudo apt update
sudo apt install --no-install-recommends r-base -y
sudo add-apt-repository ppa:c2d4u.team/c2d4u4.0+ -y
sudo apt install --no-install-recommends r-cran-rstan -y
sudo apt install git -y
sudo apt install python3-pip -y
# 3.3
sudo pip3 install pandas
sudo pip3 install numpy
sudo pip3 install ipython
sudo pip3 install ipython
sudo pip3 install jupyter
sudo pip3 install scikit-learn
sudo pip3 install flask
sudo pip3 install sqlite3

# 3.4
wget https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh
bash Anaconda3-2019.10-Linux-x86_64.sh

# 3.5
source ~/.bashrc
conda install -c conda-forge keras -y
conda install -c pytorch pytorch -y
conda install -c conda-forge tensorflow -y
#etc.
