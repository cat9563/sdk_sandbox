import dtlpy as dl
import os

if dl.token_expired():
    dl.login()


selected_project_name = 'Crystals_Demos'
project = dl.projects.get(project_name=selected_project_name)
new_dataset = 'lanes-demo4-createdByCLI-Script'


def create_dataset(project, dataset_name):
    """
    creates a dataset in the selected project name. 
    """
    dataset = dataset_name
    get_dataset = project.datasets.get(dataset_name=dataset)
    project.datasets.create(dataset_name=dataset_name)
    
    return get_dataset

create_dataset(project, new_dataset)