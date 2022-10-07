import os

# directory structure we want to setup for ML project
dirs = [
    os.path.join("data", "raw"),
    os.path.join("data", "processed"),
    "notebooks",
    "saved_models",
    "src"
]

# loop-in and create above directory structure we agreed upon for ML project
for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    # create a .gitkeep file in every directory we will create using for loop
    # This will be helpful to track empty directories in Git
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:
        pass
# .gitignore is also used to list files that should be ignored by Git when looking for untracked files.
files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src", "__init__.py")
]

for file_ in files:
    with open(file_, "w") as f:
        pass

# data_given dir is nothing but remote repo for input data for model build
