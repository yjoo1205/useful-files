import os

project_name = "my_project"

directories = [
    f"{project_name}/",
    f"{project_name}/{project_name}/",
    f"{project_name}/tests/",  # Changed from tests_files to tests
]

files = {
    f"{project_name}/{project_name}/": ["__init__.py", "module1.py", "module2.py"],
    f"{project_name}/tests/": ["__init__.py", "test_module1.py", "test_module2.py"],  # Changed as well
}

for directory in directories:
    os.makedirs(directory, exist_ok=True)

for directory, file_list in files.items():
    for file_name in file_list:
        with open(os.path.join(directory, file_name), 'w') as f:
            if file_name == "__init__.py":
                f.write("# This file makes Python treat the directories as containing packages\n")
            else:
                f.write("# Placeholder for module or test\n")

print("Project structure created successfully.")
