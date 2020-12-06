from selenium import webdriver
from mock_site.models import Session
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time


class TestHomePage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('Functional_test/chromedriver')

    def tearDown(self):
        self.browser.close()

    def test_login(self):
        self.browser.get(self.live_server_url)
        time.sleep(2)
        self.browser.find_element_by_xpath(
            "//*[contains(text(),'Register with us to start mock interviews with your buddy!')]").is_displayed()

        self.browser.find_element_by_link_text('Login').click()
        time.sleep(2)

        self.browser.find_element_by_id('id_username').send_keys('test1')
        time.sleep(2)
        text: str = 'rdjmvebiaamntxxg'
        self.browser.find_element_by_id('id_password').send_keys(text)
        time.sleep(1)
        self.browser.find_element_by_xpath("//*[@class='btn btn-dark' and @type='submit']").click()
        time.sleep(10)

    def test_register(self):
        self.browser.get(self.live_server_url)
        time.sleep(2)

        self.browser.find_element_by_link_text('Register').click()
        time.sleep(2)

        self.browser.find_element_by_id('id_username').send_keys('qitest')
        time.sleep(2)
        self.browser.find_element_by_id('id_email').send_keys('qiwang922@gmail.com')
        time.sleep(2)
        self.browser.find_element_by_id('id_password1').send_keys('testme922')
        time.sleep(2)
        self.browser.find_element_by_id('id_password2').send_keys('testme922')
        self.browser.find_element_by_xpath("//*[@class='btn btn-dark' and @type='submit']").click()
        time.sleep(10)

    def test_login_wrongpassword(self):
        self.browser.get(self.live_server_url)
        time.sleep(2)

        self.browser.find_element_by_link_text('Login').click()
        time.sleep(2)

        self.browser.find_element_by_id('id_username').send_keys('testtest')
        time.sleep(2)
        self.browser.find_element_by_id('id_password').send_keys("qi")#should display "Please enter a correct username and password. Note that both fields may be case-sensitive#
        time.sleep(1)
        self.browser.find_element_by_xpath("//*[@class='btn btn-dark' and @type='submit']").click()
        time.sleep(10)

    def test_newsession(self):
        self.browser.get(self.live_server_url)
        time.sleep(2)
        self.test_login()
        self.browser.find_element_by_id('session-creation').click()
        time.sleep(2)

    def test_previoussessions(self):
        self.browser.get(self.live_server_url)
        time.sleep(2)
        self.test_login()
        self.browser.find_element_by_id('session-creation').click()
        self.self.browser.find_element_by_link_text('Previous Sessions').click()#make sure display the content of previous session#

    def test_profile(self):
        self.browser.get(self.live_server_url)
        time.sleep(2)
        self.test_login()
        self.browser.find_element_by_class_name('requiredField').send_keys('test1')
        self.browser.find_element_by_xpath("//*[@class='emailinput form-control' and @type='email']").send_keys('fangle0121@gmail.com')
        self.browser.find_element_by_id('id_programming_language').click()
        self.browser.find_element_by_xpath("//*[@class='btn btn-dark' and @type='submit']").click()
        time.sleep(2)

    def test_googlesignin(self):
        self.browser.get(self.live_server_url)
        time.sleep(2)
        self.browser.find_element_by_link_text('Login').click()
        time.sleep(2)
        self.browser.find_element_by_link_text('Sign in with Google').click()
        time.sleep(2)

    def test_facebooksignin(self):
        self.browser.get(self.live_server_url)
        time.sleep(2)
        self.browser.find_element_by_link_text('Login').click()
        time.sleep(2)
        self.browser.find_element_by_link_text('Sign in with Facebook').click()
        time.sleep(2)

    def test_githubsignin(self):
         self.browser.get(self.live_server_url)
         time.sleep(2)
         self.browser.find_element_by_link_text('Login').click()
         time.sleep(2)
         self.browser.find_element_by_link_text('Sign in with Github').click()
         time.sleep(2)

    def linkedin_signin(self):
        self.browser.get(self.live_server_url)
        time.sleep(2)
        self.browser.find_element_by_link_text('Login').click()
        time.sleep(2)
        self.browser.find_element_by_link_text('Sign in with Linkedin').click()
        time.sleep(2)




























