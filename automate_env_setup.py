import dtlpy as dl
import os

########################################################################
#   The Goal of this script is demonstrate how we can use              #
#   dataloops sdk package to quickly automate settings up a            #
#   users environmnet.                                                 #  
#                                                                      #
#   Author: Crystal Ramirez                                            #
########################################################################

# Puesdo 

# goal 1) Create the environment 
# goal 2) Add users to the environment 
# goal 3) Create the data sets 
# goal 4) Clone Recipe/Ontology if possible 
# goal 5) transfer images 



if dl.token_expired():
    dl.login()


selected_project_name = 'Crystals_Sandbox' 
project = dl.projects.get(project_name=selected_project_name)
 
new_dataset = 'lanes-demo3-createdByCLI-Script'

# get recipe by id 
get_dataset = 'Lanes-Demo2'
dataset = project.datasets.get(dataset_name=get_dataset)
recipe = dataset.recipes.list()[0]

print(recipe)



#goal 1) Create the environment 
def create_project(new_project):
    """
    creates the new project and returns projects it created to stdout for verfication
    """
    dl.projects.create(project_name=new_project)
    get_project = dl.projects.get(project_name=new_project)
    return get_project

# goal 2) Add users to the environment (hardcoded version)
def add_project_contributors(project, email_account, roles):
    """
    adds contributors to the project and selects the role. 
    """
    project.add_member(email=email_account, role=roles)
    print(f"member {email_account} added with role {roles}")

# goal 3) Create the data sets 
def create_dataset(project, dataset_name):
    """
    creates a dataset in the selected project name. 
    """
    dataset = dataset_name
    get_dataset = project.datasets.get(dataset_name=dataset)
    project.datasets.create(dataset_name=dataset_name)
    
    return get_dataset

# goal 4) Clone Recipe/Ontology 



#create_dataset(project, new_dataset)