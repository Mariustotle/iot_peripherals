


## Network Configuration

```bash
# Get dynamic IP details
ip route

# List wireless connections (Grab NAME from connection)
nmcli connection show

# Configure the network
sudo nmcli connection modify "preconfigured" ipv4.addresses 10.5.10.233/24
sudo nmcli connection modify "preconfigured" ipv4.gateway 10.5.10.1
sudo nmcli connection modify "preconfigured" ipv4.dns "10.5.10.1,8.8.8.8"
sudo nmcli connection modify "preconfigured" ipv4.method manual

# Restart Connection
sudo nmcli connection down "preconfigured" && sudo nmcli connection up "preconfigured"

# Show updated connection
ip addr show wlan0

```
To wrap up, open browser and make sure internet is still working

## SSH Configuration

Prerequisists
- SSH Key Pair Files
  

```bash
# Show SSH Status
sudo systemctl status ssh

# Enable SSH (If needed)
sudo systemctl enable ssh
sudo systemctl start ssh

# Configure SSH Connection file
#Open SSH connection to PI e.g. `ssh {user}@{address}`
# Create SSH Folder on the Pi (Will complain if already exist)
sudo mkdir ~/.ssh

# Edit the SSH Authorization file
sudo nano ~/.ssh/authorized_keys

# Copy paste from **id_rsa.pub** (Public Key) file >> Cntr+O (Save) Cntr+X (Exit)
 
# Fix ownership (make sure pi owns its own .ssh folder)
sudo chown -R pi:pi /home/pi/.ssh

# Fix folder permissions
chmod 700 /home/pi/.ssh
chmod 700 ~/.ssh

# Fix file permissions (if they exist)
chmod 600 /home/pi/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys

# View SSH auth options
grep -i auth /etc/ssh/sshd_config

```
