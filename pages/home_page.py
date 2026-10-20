from playwright.sync_api import Page


class HomePage:
    def __init__(self,page:Page):
        self.logo=page.get_by_alt_text("naveenopencart")
        self.title=page.title()

    def check_logo(self):
        return self.logo

    def get_title(self):
        return self.title