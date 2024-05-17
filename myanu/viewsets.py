# viewsets.py
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
import re
from django.shortcuts import render
from django.http import JsonResponse

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['get','post'])
    def search(self, request):
        # Check if the request method is POST
        if request.method == 'POST':
            # Get the search word from the request data
            word = request.POST.get('searchWord', None)
            # Check if the search word is provided
            if not word:
                return JsonResponse({"error": "No word provided for search."}, status=400)

            results = []
            # Filter users based on the search word present in their content
            users = User.objects.filter(content__icontains=word)
            
            # Iterate through each user and extract sentences containing the search word
            for user in users:
                content =   user.content
                # Use regular expression to find sentences containing the search word
                sentences = re.findall(r'[^.!?]*\b{}\b[^.!?]*'.format(re.escape(word)), content, re.IGNORECASE)
                for sentence in sentences:
                    results.append({
                        'username': user.username,
                        'sentence': sentence.strip()
                    })
            # Return the search results in JSON format with proper indentation
            return JsonResponse(results, safe=False, json_dumps_params={'indent': 2})
        
        # If the request method is not POST, render the search form template
        return render(request, 'search_form.html')