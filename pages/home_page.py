from playwright.sync_api import Page


class HomePage:
    def __init__(self,page:Page):
        self.page = page
        self.title = page.title()
        self.logo=page.locator("img[title='naveenopencart']")
        self.currency_dropdown=page.locator(".pull-left")
        self.currency_dropdown_values=page.locator(".pull-left>form>div>ul>li")


    def check_logo(self):
        return self.logo

    def get_title(self):
        return self.title

    def currency_dropdown_click(self):
        self.currency_dropdown.click()

    def currency_dropdown__options_click(self):
        for i in range( self.currency_dropdown_values.count()):
            self.currency_dropdown_values.nth(i).click()
            self.currency_dropdown.click()