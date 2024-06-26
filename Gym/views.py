from rest_framework.decorators import api_view
from django.http import JsonResponse

from Gym.models import Location, Equipment
from Gym.serializers import LocationSerializer, EquipmentSerializer

# Create your views here.
@api_view(['GET'])
def get_locations(request):
    try:
        locations = Location.objects.all()
        data = LocationSerializer(locations, many=True).data
        return JsonResponse({'success': True, 'data': data, 'error': ''})
    except Exception as e:
        return JsonResponse({'success': False, 'data': {}, 'error': str(e)})
    

@api_view(['GET'])
def get_equipments(request):
    try:
        equipments = Equipment.objects.all()
        data = EquipmentSerializer(equipments, many=True).data
        return JsonResponse({'success': True, 'data': data, 'error': ''})
    except Exception as e:
        return JsonResponse({'success': False, 'data': {}, 'error': str(e)})