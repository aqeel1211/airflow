"""For airflow demonstrations, sends a message to slack channel"""

from datetime import datetime
from slack import WebClient

### VARIABLES ###
slack_token = 'xoxb-515149146933-7273865651924-ojS8natB503pCOPqMsCDVheK'
channel_id = 'C077WHPBXFX'

# Initialize Slack client
client = WebClient(token=slack_token)

UTCtime = datetime.utcnow().strftime('%d-%m-%y %H:%M:%S')
message = f"Airflow demo message ({UTCtime} UTC)"

response = client.chat_postMessage(
    channel=channel_id,
    text=message
)
