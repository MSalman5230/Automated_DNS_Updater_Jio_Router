from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
from os import getenv
from time import sleep
from ipaddress import ip_address

load_dotenv()


# Variables
url = getenv("router_url")
username = getenv("user_name")
password = getenv("password")
ipv4_dns_server1 = getenv("ipv4_dns_server1")
ipv4_dns_server2 = getenv("ipv4_dns_server2")
ipv6_dns_server1 = getenv("ipv6_dns_server1")
ipv6_dns_server2 = getenv("ipv6_dns_server2")
update_interval_time = int(getenv("update_interval_time"))


def display_settings():
    print("Router IP:", url)
    print("user_name:", username)
    print("ipv4_dns_server1:", ipv4_dns_server1)
    print("ipv4_dns_server2:", ipv4_dns_server2)
    print("ipv6_dns_server1:", ipv6_dns_server1)
    print("ipv6_dns_server2:", ipv6_dns_server2)
    print("update_interval_time:", update_interval_time)


def check_DNS_IPs():
    try:
        ip_address(ipv4_dns_server1)
        ip_address(ipv4_dns_server2)
        ip_address(ipv6_dns_server1)
        ip_address(ipv6_dns_server2)
        print("DNS IPs are in valid format")
        return True
    except:
        print("DNS servers IP's not valid: exiting")
        exit()


def create_web_driver():
    try:
        print("Creating Webdriver")
        # Create a Chrome WebDriver instance
        options = Options()
        # options.add_experimental_option("detach", True)
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        
        print("Successful")
        return driver
    except Exception as e:
        print("Failed to create web driver: ", e)
        exit()


def login_jio_router(driver):
    try:
        print("Logging In ....")
        driver.get(url)
        username_field = driver.find_element("xpath", '//input[@name="users.username"]')
        password_field = driver.find_element("xpath", '//input[@name="users.password"]')
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Find the login button and click it
        login_button = driver.find_element("xpath", '//button[@class="loginBtn"]')
        login_button.click()
        print("Successful")
        return driver
    except Exception as e:
        print("Failed to login: ", e)
        exit()


def open_lan_setting_page(driver):
    try:
        print("Opening LAN setting page ....")
        lan_setting = driver.find_element("xpath", '//a[@id="tf1_network_lanIPv4Config"]')
        driver.execute_script("arguments[0].click();", lan_setting)
        print("Successful")
        return driver
    except Exception as e:
        print("Failed to Open lan setting page: ", e)
        exit()


def change_ipv4_dns_setting(driver):
    try:
        print("Changing ipv4 DNS settings ....")
        # Select Dropdown
        ipv4_dns_dropdown = driver.find_element("xpath", '//select[@id="tf1_DnsSvrs"]')
        select = Select(ipv4_dns_dropdown)
        select.select_by_value("3")

        ipv4_dns_1 = driver.find_element("xpath", '//input[@id="tf1_priDnsServer"]')
        ipv4_dns_2 = driver.find_element("xpath", '//input[@id="tf1_secDnsServer"]')

        ipv4_dns_1.clear()
        ipv4_dns_2.clear()
        ipv4_dns_1.send_keys(ipv4_dns_server1)
        ipv4_dns_2.send_keys(ipv4_dns_server2)

        save_ipv4 = driver.find_element("xpath", '//input[@name="button.config.lanIPv4Config.lanIPv4Config.-1"]')
        driver.execute_script("arguments[0].click();", save_ipv4)
        print("Successful")
        return driver

    except Exception as e:
        print("Failed to change ipv4 dns settings: ", e)
        exit()


def change_ipv6_dns_setting(driver):
    try:
        print("Changing ipv6 DNS settings ....")

        # find IPv6 Setting page
        ipv6_dns_setting = driver.find_element("xpath", '//a[contains(text(), "LAN IPv6 Configuration")]')
        driver.execute_script("arguments[0].click();", ipv6_dns_setting)

        ipv6_dns_dropdown = driver.find_element("xpath", '//select[@id="tf1_DnsSvrs"]')
        select = Select(ipv6_dns_dropdown)
        select.select_by_value("3")
        ipv6_dns_1 = driver.find_element("xpath", '//input[@id="tf1_ipv6_PriDnsServer"]')
        ipv6_dns_2 = driver.find_element("xpath", '//input[@id="tf1_ipv6_SecDnsServer"]')

        ipv6_dns_1.clear()
        ipv6_dns_2.clear()
        ipv6_dns_1.send_keys(ipv6_dns_server1)
        ipv6_dns_2.send_keys(ipv6_dns_server2)

        save_ipv6 = driver.find_element("xpath", '//input[@name="button.ipv6Config.lanIPv6Config.lanIPv6Config"]')
        driver.execute_script("arguments[0].click();", save_ipv6)
        print("Successful")
        return driver

    except Exception as e:
        print("Failed to change ipv6 dns settings: ", e)
        exit()


def logout(driver):
    try:
        print("Logging Out ....")
        logout_url = f"{url}/platform.cgi?page=index.html"
        driver.get(logout_url)
        print("Successful")
        return driver
    except Exception as e:
        print("Failed to Log Out: ", e)
        exit()


def main():
    while True:
        if url and username and password and ipv4_dns_server1 and ipv4_dns_server2 and ipv6_dns_server1 and ipv6_dns_server2 and update_interval_time:
            display_settings()
            check_DNS_IPs()
            driver = create_web_driver()
            driver = login_jio_router(driver)
            driver = open_lan_setting_page(driver)
            driver = change_ipv4_dns_setting(driver)
            driver = change_ipv6_dns_setting(driver)
            driver = logout(driver)
            driver.quit()
            print("---Completed---")
            print(f"Sleeping for {update_interval_time} seconds or {update_interval_time / 3600} hours")
            sleep(update_interval_time)
        else:
            print("Some env variable missing")
            print("exiting program")
            exit()


if __name__ == "__main__":
    main()
