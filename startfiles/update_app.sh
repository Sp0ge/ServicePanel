sudo systemctl stop ServicePanel.service
sudo fuser -k 443/tcp
echo site kill
mkdir -p site_files
sudo rm -rf ServicePanel
echo remove ServicePanel dir
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv screen -y
sudo git clone https://Sp0ge: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@github.com/Sp0ge/ServicePanel.git
cd ServicePanel
sudo python3 -m venv venv
sudo python3 -m pip install --upgrade pip
sudo python3 -m pip uninstall -r requirements.txt -y
sudo python3 -m pip install -r requirements.txt
echo pip intalled
sudo export FLASK_APP=wsgi.py
sudo python3 -m flask db init
sudo python3 -m flask db stamp head
sudo python3 -m flask db upgrade
sudo python3 -m flask db migrate
echo db loaded
echo starting
cp /home/limb/ServicePanel/startfiles/ServicePanel.service /etc/systemd/system/ServicePanel.service
cd /home/limb/
sudo chmod -R 777 ServicePanel/

sudo systemctl daemon-reload

sudo systemctl start ServicePanel
sudo systemctl enable ServicePanel