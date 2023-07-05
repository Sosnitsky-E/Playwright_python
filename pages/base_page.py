class BasePage:
    def __init__(self, page, url):
        self.page = page
        self.url = url

    def open_web_page(self):
        self.page.goto(self.url)

    def fill_the_field_by_locator(self, element, text):
        self.page.locator(element).click()
        self.page.locator(element).fill_search_project_field(text)

    def fill_the_field_by_role(self, element, text):
        self.page.get_by_role(element).click()
        self.page.get_by_role(element).fill_search_project_field(text)


