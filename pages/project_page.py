from pages.base_page import BasePage
from pages.credentials import projects_name_for_search_pro


class ProjectPage(BasePage):

    def create_invoice_button_click(self):
        self.page.get_by_test_id("payments-card-create-invoice--button").click()

    def existing_project_check(self):
        self.page.get_by_label("Existing project").check()

    def fill_search_project_field(self):
        # self.fill_the_field_by_role("textbox", "pro")
        self.page.get_by_role("textbox").click()
        self.page.get_by_role("textbox").fill("pro")

    def names_and_count_of_searched_projects(self):
        self.page.locator(".company-search-input__result-item-label.ng-binding").locator("nth=0").text_content()
        s = self.page.locator("ul.company-search-input__result-list.company-search-input__result-list--not-empty")
        number_of_projects = s.locator("li").count()
        projects_name = s.locator("li").all_text_contents()
        return {"projects_number": number_of_projects, "projects_name": projects_name}

    def check_number_projects_and_names(self):
        data = self.names_and_count_of_searched_projects()

        assert data["projects_number"] == 4, "The number of projects does not correspond to the existing"
        assert data["projects_name"] == projects_name_for_search_pro, "The names of projects does not correspond " \
                                                                      "to the existing"
