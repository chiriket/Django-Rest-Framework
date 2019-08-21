from django.shortcuts import render
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  BankMerch
from .serializer import MerchSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
import requests


# Create your views here.
#........
def index(request):
    title = 'Home'
    # bank = Bank.objects.all()
   
    return render(request, 'index.html', {'title':title})


def bank(request):
   url = 'http://127.0.0.1:8000/api/merch/'
   response = requests.get(url)

   transaction = response.json()
    
   return render(request, 'bank.html',{
    #    'search': transaction'searchedByName')
     
   })

def get_transaction():
   '''
   Fetches and returns transcription from api
   '''

   url = 'http://127.0.0.1:8000/api/merch/'
   response = requests.get(url)

   transaction = response.json()

   return transaction

class MerchList(APIView):
    def get(self, request, format=None):
        all_merch = BankMerch.objects.all()
        serializers = MerchSerializer(all_merch, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = MerchSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = MerchSerializer(merch, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, pk, format=None):
        merch = self.get_merch(pk)
        merch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class User(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)

class MerchDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_merch(self, pk):
        try:
            return MoringaMerch.objects.get(pk=pk)
        except MoringaMerch.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = MerchSerializer(merch)
        return Response(serializers.data)

    def delete(self, request, pk, format=None):
        merch = self.get_merch(pk)
        merch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
