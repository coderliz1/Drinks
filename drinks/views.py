#from django.http import JsonResponse
#from .models import Drink
#from .serializers import DrinkSerializer

#def drink_list(request):

    #get all the drinks
    #serialize them
    #return json
    #drinks = Drink.objects.all()
    #code below difference is the false
    #serializer = DrinkSerializer(drinks, many=False)
    #return JsonResponse({'drinks': serializer.data}, safe=False)


from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def drink_list(request, format=None):

    if request.method == 'GET':

    # Get all the drinks
        drinks = Drink.objects.all()
    
    # Serialize them (use `many=True` for a QuerySet)
        serializer = DrinkSerializer(drinks, many=True)
    
    # Return JSON response
        #return JsonResponse({'drinks': serializer.data}, safe=False)
        return Response(serializer.data)




    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])

def drink_detail(request, id, format=None):


    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

