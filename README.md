# Varonis Home Assessment Project

This project is a Flask web application that interacts with Azure DevOps to manage Work Items. It provides functionality to retrieve recent Work Items, update specific Work Item titles, and create child Work Items for Product Backlog Items (PBIs).

## Features
- **Retrieve Recent Work Items**: Fetch all Work Items created in the last 3 days.
- **Update Work Item Titles**: Append the current date to the title of PBIs, Features, and Bugs.
- **Create Child Work Items**: Create child tasks for each PBI.

## Setup Instructions

### Prerequisites
- Python 3.9 or later
- Azure DevOps Personal Access Token (PAT)
- Docker (optional for containerized deployment)

### Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Adir30028/Varonis-home-assesment.git
   cd Varonis-home-assesment
   ```

2. **Create a virtual environment and activate it**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Environment Variables
Create a `.env` file in the root directory of the project to store sensitive information, such as your Azure DevOps Personal Access Token:
```
PERSONAL_ACCESS_TOKEN=your_personal_access_token_here
```
*Note: Ensure the `.env` file is added to `.gitignore` to prevent it from being committed to the repository.*

### Running the Application
Start the Flask app:
```bash
python app.py
```
The application will be accessible at `http://127.0.0.1:5000`.

### Usage
- Navigate to `/get_recent_work_items` to view recent Work Items.
- Use `/update_work_items` to update the titles of PBIs, Features, and Bugs.
- Access `/create_child_items` to create child Work Items for PBIs.

### Docker Deployment (Optional)
1. **Build the Docker image**:
   ```bash
   docker build -t azure-devops-flask-app .
   ```

2. **Run the Docker container**:
   ```bash
   docker run -p 5000:5000 azure-devops-flask-app
   ```

### Security Notice
- Do not share your `.env` file or expose sensitive information like the Personal Access Token.
- It's recommended to regenerate your Personal Access Token periodically and keep it secure.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.
```
