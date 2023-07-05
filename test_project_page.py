from pages.project_page import ProjectPage


class TestProjectPage:

    def test_list_of_projects(self, page, login):
        """The test verifies that the number and names of projects shown by the search word correspond
                to existing projects ."""
        project_page = ProjectPage(page, page.url)
        project_page.create_invoice_button_click()
        project_page.existing_project_check()
        project_page.fill_search_project_field()
        project_page.check_number_projects_and_names()

