import json
from crawler.jobs.scrapper import Scrapper
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['POST'])
def app(request):
    body = json.loads(request.body)
    scrapper = Scrapper(city=body['city'])
    response = scrapper.run()
    return Response(
        response
    )