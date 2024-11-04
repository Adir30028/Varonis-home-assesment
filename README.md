Varonis Home Assessment Project

This project is a Flask web application designed to interact with Azure DevOps for managing Work Items. The application provides the following key functionalities:

Retrieve Recent Work Items: Fetches all Work Items created in the past 3 days.
Update Work Item Titles: Appends the current date to the titles of PBIs, Features, and Bugs.
Create Child Work Items: Generates child tasks for each Product Backlog Item (PBI).
Features
Retrieve Recent Work Items
Fetch all Work Items created in the last 3 days.
Update Work Item Titles
Automatically append the current date to titles of PBIs, Features, and Bugs.
Create Child Work Items
Generate child tasks for each Product Backlog Item (PBI).
Setup Instructions
Prerequisites
Python 3.9 or later
Azure DevOps Personal Access Token (PAT)
Docker (optional, for containerized deployment)
Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/Adir30028/Varonis-home-assesment.git
cd Varonis-home-assesment
Create and Activate a Virtual Environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Environment Variables
Create a .env file in the root directory to store sensitive information, such as your Azure DevOps Personal Access Token:
plaintext
Copy code
PERSONAL_ACCESS_TOKEN=your_personal_access_token_here
Note: Ensure the .env file is added to .gitignore to prevent it from being committed to the repository.
Running the Application
Start the Flask App:
bash
Copy code
python app.py
The application will be accessible at: http://127.0.0.1:5000
Usage
View Recent Work Items: Navigate to /get_recent_work_items.
Update Work Item Titles: Use /update_work_items to modify titles of PBIs, Features, and Bugs.
Create Child Work Items: Access /create_child_items to generate child tasks for PBIs.
Docker Deployment (Optional)
Build the Docker Image:
bash
Copy code
docker build -t azure-devops-flask-app .
Run the Docker Container:
bash
Copy code
docker run -p 5000:5000 azure-devops-flask-app
Security Notice
Do Not Share Your .env File: Keep sensitive information, like your Personal Access Token, secure.
Token Management: It is recommended to periodically regenerate your Personal Access Token and keep it confidential.
License
This project is licensed under the MIT License. See the LICENSE file for more information.
