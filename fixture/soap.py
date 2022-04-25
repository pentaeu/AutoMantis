from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:
    def __init__(self, app):
        self.app = app
        self.wd = self.app.wd

    def can_login(self, username, password):
        config = self.app.config
        client = Client(config["soap"]["host"])
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects_list(self):
        project_list = []
        config = self.app.config
        client = Client(config['soap']["host"])
        projects = client.service.mc_projects_get_user_accessible(config['webadmin']['username'],
                                                                  config['webadmin']['password'])
        for row in projects:
            project_list.append(Project(id=row.id, name=row.name, description=row.description))
        return project_list