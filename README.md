# NFTicketHub-app
# Flask API Project

This is a simple Flask API project that demonstrates how to create and use a RESTful API. The project includes a basic setup with a few routes and uses a virtual environment (venv) for dependency management.

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Setup

1. Clone this repository:

```bash
git clone https://github.com/yourusername/flask-api-project.git
cd flask-api-project

### Create a virtual environment:
```python -m venv venv```

### Activate the virtual environment:
For Windows:
```venv\Scripts\activate```

For macOS/Linux:
```source venv/bin/activate```

Install the required packages:
```pip install -r requirements.txt```

If you add new dependencies to your project, make sure to update the requirements.txt file using pip freeze > requirements.txt.

## Running the Flask API
Ensure that the virtual environment is active. If not, activate it as described in the "Setup" section.
Run the Flask application:
```python app.py```
Test the API using a tool like curl or Postman.

## Deactivating the Virtual Environment
When you're done working on your project, deactivate the virtual environment:
```deactivate```

### Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
