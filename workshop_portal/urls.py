"""workshop_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from workshop_app import views
import oauth2_provider.views as oauth2_views
from django.conf import settings
# from workshop_app.views import ApiEndpoint
# from django.contrib.auth.models import User, Group
# from django.contrib import admin
# admin.autodiscover()

# from rest_framework import generics, serializers

# from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

#from chatterbot.ext.django_chatterbot import urls as chatterbot_urls
import django

js_info_dict = {
    'packages': ('recurrence', ),
}

# OAuth2 provider endpoints
oauth2_endpoint_views = [
    url(r'^authorize/$', oauth2_views.AuthorizationView.as_view(), name="authorize"),
    url(r'^token/$', oauth2_views.TokenView.as_view(), name="token"),
    url(r'^revoke-token/$', oauth2_views.RevokeTokenView.as_view(), name="revoke-token"),
]

if settings.DEBUG:
    # OAuth2 Application Management endpoints
    oauth2_endpoint_views += [
        url(r'^applications/$', oauth2_views.ApplicationList.as_view(), name="list"),
        url(r'^applications/register/$', oauth2_views.ApplicationRegistration.as_view(), name="register"),
        url(r'^applications/(?P<pk>\d+)/$', oauth2_views.ApplicationDetail.as_view(), name="detail"),
        url(r'^applications/(?P<pk>\d+)/delete/$', oauth2_views.ApplicationDelete.as_view(), name="delete"),
        url(r'^applications/(?P<pk>\d+)/update/$', oauth2_views.ApplicationUpdate.as_view(), name="update"),
    ]

    # OAuth2 Token Management endpoints
    oauth2_endpoint_views += [
        url(r'^authorized-tokens/$', oauth2_views.AuthorizedTokensListView.as_view(), name="authorized-token-list"),
        url(r'^authorized-tokens/(?P<pk>\d+)/delete/$', oauth2_views.AuthorizedTokenDeleteView.as_view(),
            name="authorized-token-delete"),
    ]

# first we define the serializers
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'email', "first_name", "last_name")

# class GroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Group
#         fields = ("name", )

# # Create the API views
# class UserList(generics.ListCreateAPIView):
#     permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserDetails(generics.RetrieveAPIView):
#     permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class GroupList(generics.ListAPIView):
#     permission_classes = [permissions.IsAuthenticated, TokenHasScope]
#     required_scopes = ['groups']
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('workshop_app.urls')),
    url(r'^', include('workshop_app.urls_password_reset')),
    url(r'^o/', include(oauth2_endpoint_views, namespace="oauth2_provider")),
    # url(r'^api/hello', ApiEndpoint.as_view()),  # an example resource endpoint
    url(r'^', include('statistics_app.urls')),
    # url(r'^secret$', 'my.views.secret_page', name='secret'),
    # url(r'^users/', UserList.as_view()),
    # url(r'^users/<pk>/', UserDetails.as_view()),
    # url(r'^groups/', GroupList.as_view()),

]