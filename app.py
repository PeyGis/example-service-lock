# Dependencies to install:
# $ python -m pip install requests
import requests

CLIENT_ID = ''
CLIENT_SECRET = ''

API_URL = 'https://api.getport.io/v1'

credentials = {'clientId': CLIENT_ID, 'clientSecret': CLIENT_SECRET}

token_response = requests.post(f'{API_URL}/auth/access_token', json=credentials)

access_token = token_response.json()['accessToken']

# You can now use the value in access_token when making further requests

headers = {
	'Authorization': f'Bearer {access_token}'
}

blueprint_id = 'service'

entity = {
  "identifier": "dashboard-service",
  "title": "Dashboard Service",
  "properties": {
    "readme": "string",
    "url": "https://example.com",
    "language": "GO",
    "slack": "https://example.com",
    "tier": "Mission Critical",
    "code_owners": "string",
    "resource_definitions": "https://example.com",
    "type": "Backend",
    "lifecycle": "Production",
    "require_approval_count": 0,
    "is_protected": False,
    "require_code_owner_review": False,
    "locked_in_prod": False,
    "last_push": "2024-02-23T16:14:21.746Z",
    "required_approvals": 0,
    "last_contributer": "string",
    "locked_reason_prod": "string",
    "locked_reason_test": "string",
    "locked_in_test": False
  },
  "relations": {
  }
}

response = requests.post(f'{API_URL}/blueprints/{blueprint_id}/entities?upsert=true', json=entity, headers=headers)

# response.json() contains the content of the resulting entity