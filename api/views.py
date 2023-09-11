from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime

#Current date and time

currentDate = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
currentDay = datetime.now().strftime('%A')


@api_view(['GET'])
def getData(request):
    person = {'slack_name': 'akaninyene_edwin',
 'current_date': currentDate,
 'current_day': currentDay,
 'track': 'backend',
 'github_file_url': 'https://github.com/AkanEdwin/stage-one/blob/main/endpoint',
 'github_repo_url': 'https://github.com/AkanEdwin/stage-one'
 'status_code': '200',
 }
    return Response(person)