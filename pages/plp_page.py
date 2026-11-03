class PLPPage:
    def __init__(self, page):
        self.page = page
        self.sortby_dropdown=page.locator("#input-sort")
        self.sortby_dropdown_values=page.locator("#input-sort option")
        self.listed_products=page.locator("#content>div:nth-child(7)>div>div>div:nth-child(2)>div:nth-child(1)>h4>a")

    def get_sortby_dropdown_values(self):
        return self.sortby_dropdown_values.all_inner_texts()

    def get_listed_products(self):
        return self.listed_products.all_inner_texts()

    def select_name_sort_option(self):
        self.sortby_dropdown.select_option("Name (A - Z)")