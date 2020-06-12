from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import get_user_model
from selenium import webdriver


chrome_options = webdriver.ChromeOptions()


class Chrome_Login_Logout_FunctionalTestCase(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        self.browser.get(self.live_server_url)
        self.browser.implicitly_wait(30)
        self.browser.maximize_window()

        User = get_user_model()
        User.objects.create_user(
            username="UsernameTest",
            password="PasswordTest2020"
        )

    def tearDown(self):
        self.browser.close()

    def test_user_can_connect_and_disconnect(self):
        self.browser.find_element_by_css_selector('#button-login').click()
        user = self.browser.find_element_by_css_selector('#id_username')
        user.send_keys("UsernameTest")
        password = self.browser.find_element_by_css_selector('#id_password')
        password.send_keys("PasswordTest2020")
        self.browser.find_element_by_css_selector('#button-submit').click()
        self.browser.find_element_by_css_selector('#button-logout').click()
        self.assertTemplateUsed('users/logout.html')
