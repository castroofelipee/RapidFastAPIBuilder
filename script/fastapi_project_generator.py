import os
import click

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def create_file(file_path, content=""):
    with open(file_path, "w") as file:
        file.write(content)

@click.command()
@click.argument('project_name', default='my_fastapi_project', required=False)
def generate_fastapi_project(project_name):
    structure = {
        project_name: [
            'main.py',
            'requirements.txt',
            'tests',
            'docs',
            'scripts',
            'api',
            'api/__init__.py',
            'routers',
            'routers/__init__.py',
            '.env',
            'templates',
            'templates/index.html'
        ]
    }

    create_directory(project_name)

    for item in structure[project_name]:
        item_path = os.path.join(project_name, item)

        if '.' in item:  
            if item.endswith('.html'):
                create_file(item_path, "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>Welcome to RapidFastAPIBuilder</title>\n</head>\n<body>\n    <h1>Welcome to RapidFastAPIBuilder</h1>\n    <p>This is your FastAPI project generated with RapidFastAPIBuilder.</p>\n</body>\n</html>")
            else:
                create_file(item_path)
        else:
            create_directory(item_path)

if __name__ == '__main__':
    generate_fastapi_project()
