# ServicePanel
### Web panel with your services for the home lab
## Installation

Install ServicePanel in Ubuntu server

### Download
```bash
  cd /home/<your username>/
  git clone https://github.com/Sp0ge/ServicePanel.git
```
    
### Config setup


```bash
  sudo nano /home/<your username>/ServicePanel/config.conf
```
Config file:
```bash
[postgres]
url = <ip or domain>
port = <port>
db = <database name>
user = <your database username>
password = <your database password>
```

### Setup server

```bash
  cd /home/<your username>
  cp /ServicePanel/startfiles/update_app.sh .
  sudo chmod 777 update_app.sh
```

### Server run and setup requirements
```bash
sudo bash update_app.sh
```
