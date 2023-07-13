from pages.base_page import BasePage
from pages.credentials import projects_name_for_search_pro
from .locators import ProjectPageLocators


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

        assert data["projects_number"] == 1, "The number of projects does not correspond to the existing"
        assert data["projects_name"] == projects_name_for_search_pro, "The names of projects does not correspond " \
                                                                      "to the existing"

    def open_library_page(self):
        self.page.locator("#radix-1").click()
        self.page.locator("//span[normalize-space()='Library']").click()

    def upload_file(self):
        self.page.get_by_role("button", name="UPLOAD").click()
        self.page.on("filechooser", lambda file_chooser: file_chooser.set_files("Upload.txt"))
        self.page.locator(".nx-button.nx-button--small.ng-scope").click()
        self.page.wait_for_selector("#saveBtn").click()
        self.page.wait_for_selector(".nx-button.nx-button--small.ng-binding")

    def get_files_number(self):
        files_area = self.page.locator(".HBFileThumbnailstyles__ThumbnailsWrapper-sc-1dp5vxz-0.laFPyE")
        files_count = files_area.locator("li").count()
        files_names_list = files_area.locator(".HBFileThumbnailstyles__ThumbnailFileName-sc-1dp5vxz-6.jlzfgv").all_text_contents()
        return files_names_list

    def check_is_file_uploaded(self, files):
        num_files = len(files)
        actual_num_files = self.get_files_number()
        assert num_files + 1 == len(actual_num_files)

