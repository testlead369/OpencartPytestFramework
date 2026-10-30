from playwright.sync_api import Page


class HomePage:
    def __init__(self,page:Page):
        self.page = page
        self.title = page.title()
        self.logo=page.locator("img[title='naveenopencart']")
        self.currency_dropdown=page.locator(".pull-left")
        self.currency_dropdown_values=page.locator(".pull-left>form>div>ul>li")
        self.currency_dropdown_names=page.locator(".pull-left>form>div>ul>li>button")
        self.phone_number=page.get_by_text("123456789")
        self.my_account=page.get_by_text("My Account").nth(0)
        self.login_link=page.get_by_role("link", name="Login")


    def check_logo(self):
        return self.logo

    def get_title(self):
        return self.title

    def currency_dropdown_click(self):
        self.currency_dropdown.click()

    def currency_dropdown__options_click(self):
        for i in range( self.currency_dropdown_names.count()):
            self.currency_dropdown.click()
            expected_currency=self.currency_dropdown_names.nth(i).inner_text().split(" ")[0].strip()
            self.currency_dropdown_names.nth(i).click()
            Actual_currency = self.currency_dropdown.inner_text().split(" ")[0].strip()
            assert expected_currency== Actual_currency

    def Phone_number_display(self):
        return self.phone_number

    def my_account_click(self):
        self.my_account.click()

    def login_link_click(self):
        self.login_link.click()