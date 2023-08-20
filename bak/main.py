from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

ipv4_dns_server1="1.1.1.1"
ipv4_dns_server2="1.0.0.1"
ipv6_dns_server1="2606:4700::1111"
ipv6_dns_server2="2606:4700:4700::1001"

username = 'admin'
password = 'G!o1k1u1'
url = 'http://192.168.11.1'

# Set the path to the ChromeDriver executable
#chromedriver_path = 'chromedriver.exe'  # Replace with the actual path

# Create a Chrome WebDriver instance
options = Options()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options = options)



# Open a webpage
 # Replace with the desired URL
driver.get(url)
#driver.maximize_window()
username_field = driver.find_element("xpath",'//input[@name="users.username"]')
password_field = driver.find_element("xpath",'//input[@name="users.password"]')



username_field.send_keys(username)
password_field.send_keys(password)

# Find the login button and click it
login_button = driver.find_element("xpath",'//button[@class="loginBtn"]')
login_button.click()
#driver.execute_script("arguments[0].click();", login_button)

lan_setting = driver.find_element("xpath",'//a[@id="tf1_network_lanIPv4Config"]')
driver.execute_script("arguments[0].click();", lan_setting)
#id="tf1_DnsSvrs"
#lan_setting.click()
#ipv4
ipv4_dns_dropdown=driver.find_element("xpath",'//select[@id="tf1_DnsSvrs"]')
select = Select(ipv4_dns_dropdown)
select.select_by_value('3')
#id="tf1_priDnsServer"
ipv4_dns_1=driver.find_element("xpath",'//input[@id="tf1_priDnsServer"]')
ipv4_dns_2=driver.find_element("xpath",'//input[@id="tf1_secDnsServer"]')

ipv4_dns_1.clear()
ipv4_dns_2.clear()

ipv4_dns_1.send_keys(ipv4_dns_server1)
ipv4_dns_2.send_keys(ipv4_dns_server2)
# name="button.config.lanIPv4Config.lanIPv4Config.-1"
save_ipv4 = driver.find_element("xpath",'//input[@name="button.config.lanIPv4Config.lanIPv4Config.-1"]')
driver.execute_script("arguments[0].click();", save_ipv4)

# //a[@onclick="gotoLinks('lanIPv6Config.html')"]

ipv6_dns_setting=driver.find_element("xpath", '//a[contains(text(), "LAN IPv6 Configuration")]')
driver.execute_script("arguments[0].click();", ipv6_dns_setting)

ipv6_dns_dropdown=driver.find_element("xpath",'//select[@id="tf1_DnsSvrs"]')
select = Select(ipv6_dns_dropdown)
select.select_by_value('3')
#id="tf1_priDnsServer"
ipv6_dns_1=driver.find_element("xpath",'//input[@id="tf1_ipv6_PriDnsServer"]')
ipv6_dns_2=driver.find_element("xpath",'//input[@id="tf1_ipv6_SecDnsServer"]')

ipv6_dns_1.clear()
ipv6_dns_2.clear()

ipv6_dns_1.send_keys(ipv6_dns_server1)
ipv6_dns_2.send_keys(ipv6_dns_server2)
# name="button.config.lanIPv4Config.lanIPv4Config.-1"
save_ipv6 = driver.find_element("xpath",'//input[@name="button.ipv6Config.lanIPv6Config.lanIPv6Config"]')
driver.execute_script("arguments[0].click();", save_ipv6)




print("DONE")