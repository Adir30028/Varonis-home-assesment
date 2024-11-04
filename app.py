from flask import Flask, jsonify, render_template
from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
#push test
load_dotenv()
#workflow testing
app = Flask(__name__)

# Basic settings with your parameters
organization_url = 'https://dev.azure.com/Adir3001'
personal_access_token = os.getenv('PERSONAL_ACCESS_TOKEN')
project_name = 'Adir_Home_assesment'

# Connect to Azure DevOps
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)
wit_client = connection.clients.get_work_item_tracking_client()

# Function to get all Work Items created in the last 3 days
def get_recent_work_items():
    start_date = (datetime.now() - timedelta(days=3)).strftime('%Y-%m-%d')
    query = f"SELECT [System.Id], [System.Title], [System.WorkItemType] FROM workitems WHERE [System.CreatedDate] >= '{start_date}'"
    work_items = wit_client.query_by_wiql({"query": query}).work_items

    # Retrieve details for each Work Item
    work_item_details = [wit_client.get_work_item(item.id) for item in work_items]
    return work_item_details

# Route to get recent Work Items (Step 1)
@app.route('/get_recent_work_items', methods=['GET'])
def get_recent_work_items_route():
    work_items = get_recent_work_items()
    work_item_data = [{'id': wi.id, 'title': wi.fields['System.Title'], 'type': wi.fields['System.WorkItemType']} for wi in work_items]
    return render_template('get_recent_work_items.html', work_items=work_item_data)

# Route to update titles of PBIs, Features, and Bugs (Step 2)
@app.route('/update_work_items', methods=['GET'])
def update_work_items():
    work_items = get_recent_work_items()
    updated_items = []

    for wi in work_items:
        wi_type = wi.fields['System.WorkItemType']
        if wi_type in ['Product Backlog Item', 'Feature', 'Bug']:
            current_date = datetime.now().strftime('%Y-%m-%d')
            new_title = f"{wi.fields['System.Title']} - {current_date}"
            wit_client.update_work_item(
                document=[{
                    "op": "replace",
                    "path": "/fields/System.Title",
                    "value": new_title
                }],
                id=wi.id
            )
            updated_items.append({'id': wi.id, 'new_title': new_title})

    return render_template('update_work_items.html', updated_items=updated_items)

# Route to create child Work Items for each PBI (Step 3)
@app.route('/create_child_items', methods=['GET'])
def create_child_items():
    work_items = get_recent_work_items()
    created_items = []

    for wi in work_items:
        if wi.fields['System.WorkItemType'] == 'Product Backlog Item':
            child_work_item = wit_client.create_work_item(
                document=[{
                    "op": "add",
                    "path": "/fields/System.Title",
                    "value": "Child Work Item"
                }],
                project=project_name,
                type='Task'
            )
            created_items.append({'parent_id': wi.id, 'child_id': child_work_item.id})

    return render_template('create_child_items.html', created_items=created_items)

# Main route to serve the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Run Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

