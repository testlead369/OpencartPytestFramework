from playwright.sync_api import Page


class LoginPage:
    def __init__(self,page:Page):
        self.page = page
        self.returning_customer_text=page.get_by_text("Returning Customer").nth(0)
        self.email_address=page.locator("#input-email")
        self.password=page.locator("#input-password")
        self.login_button=page.locator("input[value='Login']")


    def login_page_text_check(self):
        return self.returning_customer_text

    def successful_login(self,email,password):
        self.email_address.fill(email)
        self.password.fill(password)
        self.login_button.click()