


## 2. Configure Networking

Once booted and connected to your Wi-Fi, you could also do this through your DHCP then you do not need to log into the device OS.

```bash
# View OS Version (the network file might vary)
cat /etc/os-release

# View current IP address
hostname -I

# Show WiFi connections
nmcli connection show

# (Optional) Set a static IP for stability
sudo nano /etc/NetworkManager/system-connections/{connection_name}.nmconnection

```

```ini
[ipv4]
method=manual
addresses=X.X.X.X/24
gateway=X.X.X.X
dns=8.8.8.8;
```
Nano commands: Cntr+O (Save) then Cntr+X (Exit)

```bash
sudo nmcli connection reload
sudo nmcli connection up "{connection_name}"
```

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
