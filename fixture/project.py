from selenium.webdriver.common.by import By


class ProjectHelper:

    def __init__(self, app):
        self.app = app
        self.wd = self.app.wd

    def open_project_page(self):
        self.wd.find_element(By.XPATH, '//a[@href="/mantisbt-1.2.20/manage_overview_page.php"]').click()
        self.wd.find_element(By.XPATH, '//a[@href="/mantisbt-1.2.20/manage_proj_page.php"]').click()

    def create_project(self, project):
        self.open_project_page()
        # Create New Project
        self.wd.find_element(By.XPATH, "//input[@value='Create New Project']").click()
        self.fill_project_form(project)
        # Add Project
        self.wd.find_element(By.XPATH, "//input[@value='Add Project']").click()
        self.open_project_page()
        self.project_cache = None

    def select_project_by_name(self, name):
        self.wd.find_element(By.LINK_TEXT, name).click()

    def delete_project_by_name(self, name):
        self.open_project_page()
        self.select_project_by_name(name)
        self.wd.find_element(By.XPATH, "//input[@value='Delete Project']").click()
        self.wd.find_element(By.XPATH, "//input[@value='Delete Project']").click()
        self.open_project_page()
        self.project_cache = None

    project_cache = None

    def fill_project_form(self, project):
        self.edit_field_value("name", project.name)
        self.edit_field_value("description", project.description)

    def edit_field_value(self, field_name, text):
        if text is not None:
            self.wd.find_element(By.NAME, field_name).click()
            self.wd.find_element(By.NAME, field_name).clear()
            self.wd.find_element(By.NAME, field_name).send_keys(text)

