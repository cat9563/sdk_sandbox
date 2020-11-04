import dtlpy as dl
import os

if dl.token_expired():
    dl.login()


selected_project_name = 'Crystals_Demos'
project = dl.projects.get(project_name=selected_project_name)
new_dataset = 'sdk_demo4-createdByPython-Script'
dataset_id='5fa173bb1c37a819112cd702'


def create_dataset(project, dataset_name):
    """
    creates a dataset in the selected project name. 
    """
    dataset = dataset_name
    project.datasets.create(dataset_name=dataset_name)
    get_dataset = project.datasets.get(dataset_name=dataset)
    
    print(f"dataset: {get_dataset} created successfully")
    return get_dataset
  
#create_dataset(project, new_dataset)
def clone_dataset(project, datasetID):
    cloned_dataset = project.datasets.get(dataset_id=datasetID)
    cloned_dataset.clone(clone_name='roofs_clone_example_with_sdk', filters=None,
    with_items_annotations=False, with_metadata=False,
              with_task_annotations_status=False)


create_dataset(project, new_dataset)
clone_dataset(project, dataset_id)