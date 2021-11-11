from django import forms
from .models import *
from django.shortcuts import redirect, render
from rest_framework import generics
from .serializers import *
from .forms import clients, clientsForm, parentsForm
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

#! TODO:
# ?*  regions
# ?*  schools
# ?*  courses
# ?*  groups
# ?*  teachers
# ?*  clients
# ?*  parents
# ?  tests
# ?*  lessons
# ?*  attentions


# def index(request):
#     return render(request, 'EduApp/index.html')

def sign(request):
    return render(request, 'EduApp/sign.html')


def create_user(request):
    error = ''
    if request.method == "POST":
        form = clientsForm(request.POST)
        if form.is_valid():
            print(form)
            form.validate_unique()
            form.save()
            return redirect('sign')
        else:
            error = 'Form is uncorrect'



    form = clientsForm()

    group = groups.objects.all()
    
    data = {
        'form' : form,
        'error': error,
        'group' : group,
    }

    return render(request, 'EduApp/create_user.html', data)


def create_parent(request):

    error = ''
    if request.method == "POST":
        form = parentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign')
        else:
            error = 'Form is uncorrect'

    client = clients.objects.all()

    form = parentsForm()

    data = {
        'form' : form,
        'client': client,
        'error': error,
    }


    return render(request, 'EduApp/create_parent.html', data)

#! regions


class regionsCreateAPIView(generics.ListCreateAPIView):

    queryset = regions.objects.all()
    serializer_class = regionsSerializersCreate
    permission_classes = (IsAdminUser,)


class regionsUpdAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = regions.objects.all()
    serializer_class = regionsSerializersCreate
    permission_classes = (AllowAny,)

#! schools


class schoolsCreateAPIView(generics.ListCreateAPIView):

    queryset = schools.objects.all()
    serializer_class = schoolsSerializersCreate
    permission_classes = (IsAuthenticated,)


class schoolsUpdAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = schools.objects.all()
    serializer_class = schoolsSerializersCreate
    permission_classes = (AllowAny,)

#! courses


class coursesCreateAPIView(generics.ListCreateAPIView):

    queryset = courses.objects.all()
    serializer_class = coursesSerializersCreate
    permission_classes = (AllowAny,)


class coursesUpdAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = courses.objects.all()
    serializer_class = coursesSerializersCreate
    permission_classes = (AllowAny,)

#! groups


class groupsCreateAPIView(generics.ListCreateAPIView):

    queryset = groups.objects.all()
    serializer_class = groupsSerializersCreate
    permission_classes = (AllowAny,)


class groupsUpdAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = groups.objects.all()
    serializer_class = groupsSerializersCreate
    permission_classes = (AllowAny,)

#! teachers


class teachersCreateAPIView(generics.ListCreateAPIView):

    queryset = teachers.objects.all()
    serializer_class = teachersSerializersCreate
    permission_classes = (AllowAny,)


class teachersUpdAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = teachers.objects.all()
    serializer_class = teachersSerializersCreate
    permission_classes = (AllowAny,)

#! clients


class clientsCreateAPIView(generics.ListCreateAPIView):

    queryset = clients.objects.all()
    serializer_class = clientsSerializersCreate
    permission_classes = (AllowAny,)


class clientsUpdAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = clients.objects.all()
    serializer_class = clientsSerializersCreate
    permission_classes = (AllowAny,)

#! parents


class parentsCreateAPIView(generics.ListCreateAPIView):

    queryset = parents.objects.all()
    serializer_class = parentsSerializersCreate
    permission_classes = (AllowAny,)


class parentsUpdAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = parents.objects.all()
    serializer_class = parentsSerializersCreate
    permission_classes = (AllowAny,)

#! lessons


class lessonsCreateAPIView(generics.ListCreateAPIView):

    queryset = lessons.objects.all()
    serializer_class = lessonsSerializersCreate
    permission_classes = (AllowAny,)


class lessonsUpdAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = lessons.objects.all()
    serializer_class = lessonsSerializersCreate
    permission_classes = (AllowAny,)

#! attentions


class attentionsCreateAPIView(generics.ListCreateAPIView):

    queryset = attentions.objects.all()
    serializer_class = attentionsSerializersCreate
    permission_classes = (AllowAny,)


class attentionsUpdAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = attentions.objects.all()
    serializer_class = attentionsSerializersCreate
    permission_classes = (AllowAny,)
