from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime

today = datetime.now()
# Current day and time
currentDay = datetime.now().strftime("%A")
utcTime = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")


@api_view(['GET'])
def getData(request):
    person = {'slack_name': 'akaninyene_edwin',
              'current_day': currentDay,
              'utc_time': utcTime
              'track': 'backend',
              'github_file_url': 'https://github.com/AkanEdwin/stage-one/api',
              'github_repo_url': 'https://github.com/AkanEdwin/stage-one',
              'status_code': '200',}
    return Response(person)
