from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import School, Degree, DegreeView, UserProfile
from .serializers import SchoolSerializer, DegreeSerializer, DegreeViewSerializer, UserProfileSerializer, UserSerializer
from .producer import publish

class SchoolViewSet(viewsets.ViewSet):

    def list(self, request):
        schools = School.objects.all()
        schools_serializer = SchoolSerializer(schools, many=True)
        return Response(schools_serializer.data)

    def create(self, request):
        school_serializer = SchoolSerializer(data=request.data)
        school_serializer.is_valid(raise_exception=True)
        school_serializer.save()
        publish('school_created', school_serializer.data)
        return Response(school_serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        school = School.objects.get(id=pk)
        school_serializer = SchoolSerializer(school)
        return Response(school_serializer.data)

    def update(self, request, pk=None):
        school = School.objects.get(id=pk)
        school_serializer = SchoolSerializer(instance=school, data=request.data)
        school_serializer.is_valid(raise_exception=True)
        school_serializer.save()
        publish('school_updated', school_serializer.data)
        return Response(school_serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        school = School.objects.get(id=pk)
        school.delete()
        publish('school_deleted', {'id': pk})
        return Response(status=status.HTTP_204_NO_CONTENT)


class DegreeViewSet(viewsets.ViewSet):

    def list(self, request):
        degrees = Degree.objects.all()
        degrees_serializer = DegreeSerializer(degrees, many=True)
        return Response(degrees_serializer.data)

    def create(self, request):
        degree_serializer = DegreeSerializer(data=request.data)
        degree_serializer.is_valid(raise_exception=True)
        degree_serializer.save()

        publish('degree_created', degree_serializer.data)
        
        return Response(degree_serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        degree = Degree.objects.get(id=pk)
        degree_serializer = DegreeSerializer(degree)
        return Response(degree_serializer.data)

    def update(self, request, pk=None):
        degree = Degree.objects.get(id=pk)
        degree_serializer = DegreeSerializer(instance=degree, data=request.data)
        degree_serializer.is_valid(raise_exception=True)
        degree_serializer.save()

        publish('degree_updated', degree_serializer.data)

        return Response(degree_serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        degree = Degree.objects.get(id=pk)
        degree.delete()

        publish('degree_deleted', {'id': pk})

        return Response(status=status.HTTP_204_NO_CONTENT)


class DegreeViewViewSet(viewsets.ViewSet):

    def list(self, request):
        degree_views = DegreeView.objects.all()
        degree_views_serializer = DegreeViewSerializer(degree_views, many=True)
        return Response(degree_views_serializer.data)

    def create(self, request):
        degree_view_serializer = DegreeViewSerializer(data=request.data)
        degree_view_serializer.is_valid(raise_exception=True)
        degree_view_serializer.save()

        publish('degree_veiw_created', degree_view_serializer.data) 

        return Response(degree_view_serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        degree_view = DegreeView.objects.get(id=pk)
        degree_view_serializer = DegreeViewSerializer(degree_view)
        return Response(degree_view_serializer.data)

    def update(self, request, pk=None):
        degree_view = DegreeView.objects.get(id=pk)
        degree_view_serializer = DegreeViewSerializer(instance=degree_view, data=request.data)
        degree_view_serializer.is_valid(raise_exception=True)
        degree_view_serializer.save()
        publish('degree_veiw_updated', degree_view_serializer.data) 
        return Response(degree_view_serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        degree_view = DegreeView.objects.get(id=pk)
        degree_view.delete()
        publish('degree_veiw_deleted', {'id':pk}) 
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserProfileViewSet(viewsets.ViewSet):

    def list(self, request):
        user_profiles = UserProfile.objects.all()
        user_profiles_serializer = UserProfileSerializer(user_profiles, many=True)
        return Response(user_profiles_serializer.data)

    def create(self, request):
        user_profile_serializer = UserProfileSerializer(data=request.data)
        user_profile_serializer.is_valid(raise_exception=True)
        user_profile_serializer.save()
        publish('user_profile_created', user_profile_serializer.data) 
        return Response(user_profile_serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        user_profile = UserProfile.objects.get(id=pk)
        user_profile_serializer = UserProfileSerializer(user_profile)
        return Response(user_profile_serializer.data)

    def update(self, request, pk=None):
        user_profile = UserProfile.objects.get(id=pk)
        user_profile_serializer = UserProfileSerializer(instance=user_profile, data=request.data)
        user_profile_serializer.is_valid(raise_exception=True)
        user_profile_serializer.save()
        publish('user_profile_updated', user_profile_serializer.data) 
        return Response(user_profile_serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        user_profile = UserProfile.objects.get(id=pk)
        user_profile.delete()
        publish('user_profile_deleted', {'id':pk}) 
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserViewSet(viewsets.ViewSet):

    def list(self, request):
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return Response(users_serializer.data)

    def create(self, request):
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        publish('user_created', user_serializer.data) 
        return Response(user_serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        user = User.objects.get(id=pk)
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)

    def update(self, request, pk=None):
        user = User.objects.get(id=pk)
        user_serializer = UserSerializer(instance=user, data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        publish('user_updated', user_serializer.data) 
        return Response(user_serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        user = User.objects.get(id=pk)
        user.delete()
        publish('user_deleted', {'id':pk}) 
        return Response(status=status.HTTP_204_NO_CONTENT)
