from model.project import Project


def test_add_project_soap(app, json_projects):
    project = json_projects
    old_projects = app.soap.get_projects_list()
    app.project.create_project(project)
    old_projects.append(project)
    new_projects = app.soap.get_projects_list()
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


# def test_add_project_db(app, db, json_projects):
#     project = json_projects
#     old_projects = db.get_project_list()
#     app.project.create_project(project)
#     old_projects.append(project)
#     new_projects = db.get_project_list()
#     assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
