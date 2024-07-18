from pathlib import Path
import os

project_name = "US_Visa"

list_of_files = [

    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",  
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipline/__init__.py",
    f"{project_name}/pipline/training_pipeline.py",
    f"{project_name}/pipline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml",

]

# Loop through each filepath in the list of files
for filepath in list_of_files:
    # Convert the filepath to a Path object for easier manipulation
    filepath = Path(filepath)
    
    # Split the filepath into the directory part and the filename part
    filedir, filename = os.path.split(filepath)
    
    # If the directory part is not empty (i.e., the file is not in the current directory)
    if filedir != "":
        # Create the directory (and any intermediate directories) if they do not already exist
        os.makedirs(filedir, exist_ok=True)
    
    # Check if the file does not exist or if its size is 0 bytes
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # Open the file in write mode, which creates an empty file
        with open(filepath, "w") as f:
            pass
    else:
        # If the file already exists and is not empty, print a message indicating its presence
        print(f"file is already present at: {filepath}")

