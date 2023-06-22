sudo apt update
sudo apt install python3.5
sudo rm /usr/bin/python3
sudo ln -s /usr/bin/python3.5 /usr/bin/python3
sudo pip3 install gunicorn
sudo pip3 install django==2.1
sudo python3 -m pip install mysqlclient

sudo /etc/init.d/mysql start
mysql -uroot -e "create database stepic_web;"
mysql -uroot -e "GRANT ALL PRIVILEGES ON stepic_web.* TO 'box'@'localhost' WITH GRANT OPTION;"
source ./venv/bin/activate
cd ask
python3 manage.py makemigrations
python3 manage.py migrate
cd ..

sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default

gunicorn --bind='0.0.0.0:8080' hello:application &
cd ask
gunicorn --bind='0.0.0.0:8000' ask.wsgi &

sudo /etc/init.d/nginx restart
