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
   
2. **Create a virtual environment and activate it**:

(bash)
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

Install dependencies:
