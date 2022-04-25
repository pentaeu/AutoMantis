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
