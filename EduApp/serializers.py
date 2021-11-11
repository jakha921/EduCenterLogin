from rest_framework import serializers
from EduApp.models import *

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



class regionsSerializersCreate(serializers.ModelSerializer):

    class Meta:
        model = regions
        fields = "__all__"

class schoolsSerializersCreate(serializers.ModelSerializer):

    class Meta:
        model = schools
        fields = "__all__"

class coursesSerializersCreate(serializers.ModelSerializer):

    class Meta:
        model = courses
        fields = "__all__"

class groupsSerializersCreate(serializers.ModelSerializer):

    class Meta:
        model = groups
        fields = "__all__"

class teachersSerializersCreate(serializers.ModelSerializer):

    class Meta:
        model = teachers
        fields = "__all__"

class clientsSerializersCreate(serializers.ModelSerializer):

    class Meta:
        model = clients
        fields = "__all__"

class parentsSerializersCreate(serializers.ModelSerializer):

    class Meta:
        model = parents
        fields = "__all__"

class lessonsSerializersCreate(serializers.ModelSerializer):

    class Meta:
        model = lessons
        fields = "__all__"

class attentionsSerializersCreate(serializers.ModelSerializer):

    class Meta:
        model = attentions
        fields = "__all__"

