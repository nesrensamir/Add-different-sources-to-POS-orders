#** ODOO 14 INSTALLATIONS STEPS **

sudo apt update && sudo apt upgrade -y
	
# Install python Dependencies
sudo apt install build-essential python3-dev python3-venv libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev libtiff5-dev libjpeg8-dev libopenjp2-7-dev zlib1g-dev libfreetype6-dev  liblcms2-dev libwebp-dev libharfbuzz-dev libfribidi-dev libxcb1-dev libpq-dev -y

# Install wget ,git ,postgresql
sudo apt install wget git postgresql -y

# Create database user
sudo su - postgres -c "createuser -s $USER"

#** Install Wkhtmltopdf **
wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.$(lsb_release -cs)_amd64.deb
sudo dpkg -i --force-depends wkhtmltox_0.12.5-1.$(lsb_release -cs)_amd64.deb

#Install missing dependencies
sudo apt install -f -y

#** Install Odoo **
mkdir odoo14
cd odoo14

sudo git clone https://www.github.com/odoo/odoo --depth 1 --branch 14.0

#Create Python Virtual Env
python3 -m venv odoo-venv

source odoo-venv/bin/activate

pip install wheel
pip install -r odoo/requirements.txt

# Create odoo configuration file will be located at /home/username
python3 odoo/odoo-bin -s --stop-after-init

sudo mv $HOME/.odoorc odoo14.conf

mkdir odoo_custom_addons ## add this path at oddo.conf 

python3 ./odoo/odoo-bin -c odoo14.conf
