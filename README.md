# Selenium automation for Updating JIO Router DNS server
JIO Fiber router DNS setting does not persist after router reboot, This script uses Selenium to run and update to user Defined DNS server

# Prerequisite
Google Chrome needs to be installed, Tested with Version 116.0.5845.96 (Official Build) (64-bit)
```BASH
pip install -r requirements.txt
```
# Settings

Create **.env** and add the following environment variables
```python
router_url = "http://192.168.29.1" #
user_name = "admin"
password = "password"
ipv4_dns_server1 = "1.1.1.1" #cloudflare dns, # change as per required
ipv4_dns_server2 = "1.0.0.1"
ipv6_dns_server1 = "2606:4700::1111"
ipv6_dns_server2 = "2606:4700:4700::1001"
update_interval_time=28800 # interval after script will run again
```


