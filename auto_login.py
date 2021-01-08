from selenium import webdriver
from getpass import getpass
from time import sleep


def interface():
    print('')
    print("Caleb's Auto-Login Program")
    print('')
    print('Sites:')
    count = 1
    for site in valid_site:
        print(f'{count}. {site.title()}')
        count += 1
    print('')


def facebook(username, password):
    driver.get('https://www.facebook.com/')
    sleep(1)

    driver.find_element_by_xpath('//input[@name="email"]').send_keys(username)
    driver.find_element_by_xpath('//input[@name="pass"]').send_keys(password)
    driver.find_element_by_xpath('//button[@name="login"]').click()
    sleep(1)


def instagram(username, password):
    driver.get('https://www.instagram.com/')
    sleep(1)

    driver.find_element_by_xpath(
        '//input[@name="username"]').send_keys(username)
    driver.find_element_by_xpath(
        '//input[@name="password"]').send_keys(password)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    sleep(4)

    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/div/div/div/button').click()  # pop-up #1
    sleep(1)

    # driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click() # pop-up #2
    # sleep(1)


def twitter(username, password):
    driver.get('https://twitter.com/login')
    sleep(1)

    driver.find_element_by_xpath(
        '//input[@name="session[username_or_email]"]').send_keys(username)
    driver.find_element_by_xpath(
        '//input[@name="session[password]"]').send_keys(password)
    driver.find_element_by_xpath(
        '//div[@data-testid="LoginForm_Login_Button"]').click()
    sleep(1)


def stackoverflow(username, password):
    driver.get('https://stackoverflow.com/users/login')

    driver.find_element_by_xpath('//input[@name="email"]').send_keys(username)
    driver.find_element_by_xpath(
        '//input[@name="password"]').send_keys(password)
    driver.find_element_by_xpath('//button[@name="submit-button"]').click()
    sleep(1)


valid_site = ['instagram', 'facebook', 'twitter', 'stack overflow']
function = {'instagram': instagram, 'facebook': facebook,
            'twitter': twitter, 'stack overflow': stackoverflow}

interface()

# login variables
while True:
    site = input('enter site: ').lower()
    if site not in valid_site:
        print('invalid platform')
    else:
        break

while True:
    my_username = input('username or email: ')
    my_password = getpass('password: ')

    confirmation = input('Confirm? (y/n): ').lower()
    if confirmation == 'y':
        break

# create instance of web driver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(chrome_options=options)

# call function
function[site](my_username, my_password)
