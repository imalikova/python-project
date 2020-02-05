
class SessionHelper:

    def __init__(self, app):
        self.app = app

    def test_login(self, username, password):
        wd = self.app.wd
        self.app.open_homepage()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector('div.logBox button').click()

    def test_logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Log Out").click()