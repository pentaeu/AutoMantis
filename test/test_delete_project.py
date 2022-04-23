from model.project import Project
import random


def test_delete_some_project(app, db):
    if len(db.get_project_list()) == 0:
        app.project.create_project(Project(name='Project', description='Desc'))
    old_projects = db.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_name(project.name)
    assert len(old_projects) - 1 == len(db.get_project_list())
    new_projects = db.get_project_list()
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
