from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime

today = datetime.now()
currentDate = datetime.utcnow().isoformat(sep='T', timespec='milliseconds') + 'Z'
currentDay = today.strftime('%A')


@api_view(['GET'])
def getData(request):
    person = {'slack_name': 'akaninyene_edwin',
 'current_date': currentDate,
 'current_day': currentDay,
 'track': 'backend',
 'status_code': '200',
 }
    return Response(person)