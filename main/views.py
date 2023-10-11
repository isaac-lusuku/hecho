from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .model_forms import *
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from datetime import datetime
from .serializer import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import Token
from rest_framework_simplejwt.utils import jwt_decode_handler




@api_view(["POST"])
@permission_classes([IsAuthenticated,])
def register(request):

    if request.method == "POST":
        c_data = UserSerializer(data=request.data)

        if c_data.is_valid():
            c_data.save()
            return Response(status.HTTP_201_CREATED)



@permission_classes([IsAdminUser])
@api_view(["GET", "POST", "PUT", "DELETE"])
def reviews(request):
    # requsting for reviews
    if request.method == "GET":
        reviews = Reviews.objects.all()
        serializer = ReviewsSerializer(reviews, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    
    # this creats a new review
    elif request.method == "POST":
        serializer = ReviewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return(status.HTTP_200_OK)
        
@permission_classes([IsAuthenticated])
@api_view(["GET", "PUT", "DELETE"])
def review(request, pk):

    # fetching the requested review from the database
    try:
         review = Reviews.objects.get(id=pk)
    except:
        return Response(status.HTTP_404_NOT_FOUND)
    
    # sending the review 
    if request.method == "GET":
        serializer = ReviewsSerializer(review, many=False)
        return Response(serializer.data, status.HTTP_200_OK)
    
    # for updating the review
    elif request.method == "PUT":
        serializer = ReviewsSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status.HTTP_200_OK)
        
    # deleting a review from the database
    elif request.method == "DELETE":
        review.delete()
        return Response(status.HTTP_200_OK)
    
    else:
        return Response(status.HTTP_400_BAD_REQUEST)

# read about user authentication and how to know the logged in user
    


def login_page(request):
    if request.method == "POST":
        user_name = request.POST["username"]
        password = request.POST["password"]

        user = User.objects.get(username= user_name)
        if user is not None:
            authenticate(request, username=user_name, password=password)
            login(request, user)
            return redirect("home")
        else:
            # messages.error(request, "user doesnot not exist")
            return redirect('login_page')
    
    context = {}
    return render(request, "main/login_page.html", context)

#

def logout(request):
    logout(request)
    return redirect("welcome")


@login_required(login_url='login_page')
def home(request):
    tasks = Task.objects.filter(Q(user=request.user)&Q(completed=False))
    tasks_c = Task.objects.filter(Q(user=request.user)&Q(completed=True)).order_by("-date_of_completion")

    subtasks = []
    for task in tasks:
        for subtask in task.subtask_set.filter(completed=False):
            subtasks.append(subtask)
    s_subtasks = (sorted(subtasks, key=lambda x: x.deadline))[0:9]

    # TOMORROW
    # start by running and testing 
    # then go on to creat public tasks that fall under the shared topics
    public = list(Task.objects.filter(Q(public=True)&Q(completed=False)))
    for task in tasks:
        public.remove(task)
    # then show the most popular topics
    popular_topics= list(Topic.objects.all())
    popular_topics.sort(key=lambda x: len(list(x.task_set.all())))


    context = {"tasks": tasks, "subtasks":s_subtasks, "completed_tasks":tasks_c, "public":public, "popular_topics":popular_topics}
    return render(request, "main/home.html", context)


def user_profile(request):
    pass


def task_page(request, id):
    task = Task.object.get(id=id)
    name = task.name
    

class MyAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # auth_header = (request.META.get('HTTP_AUTHORIZATION').split(" "))[1]
        # json_obj = jwt.decode(auth_header,"secret", algorithms=["HS256"])
        # return Response(json_obj)
        authorization_header = request.META.get('HTTP_AUTHORIZATION')
        if authorization_header and authorization_header.startswith('Bearer '):
            token = authorization_header.split(' ')[1]
            try:
                payload = jwt_decode_handler(Token(token))
                return Response(payload)
            except Exception as e:
                return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Authorization header missing'}, status=status.HTTP_401_UNAUTHORIZED)





    


# if you can also add in some sort of diaries into the app
# try to include an error handler page with the messages for the errors tha have occured
#make sure you dd the possibilities for the user to add the remaining information
# add fuctionality where a user can request to follow another user's task
# and more than one user can work on a similar task
# include a countdown
