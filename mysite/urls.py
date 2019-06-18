"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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

from mathema import views
from rest_framework_jwt.views import refresh_jwt_token, verify_jwt_token
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/tag', views.Tag)
router.register(r'api/curriculum', views.Curriculum)
router.register(r'api/group', views.Group)
router.register(r'api/studentGroup', views.StudentGroup)  # Relacao many-to-many (User(Student) - Group)
router.register(r'api/question', views.Question)
router.register(r'api/topic', views.Topic)
router.register(r'api/modelSolution', views.ModelSolution)
router.register(r'api/proposedSolution', views.ProposedSolution)
router.register(r'api/feedback', views.Feedback)
router.register(r'api/StudentGroup', views.Feedback)

# router.register(r'api/objective', views.Objective)  # Nao esta sendo implementada ainda
# router.register(r'api/activity', views.Activity, base_name='activity')
# router.register(r'api/support', views.Support, base_name='support')
# router.register(r'api/answer', views.Answer, base_name='answer')
# router.register(r'api/evaluation', views.Evaluation, base_name='evaluation')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'api/user/(?P<pk>[0-9]+)/$', views.UserNamePerPK.as_view({'get': 'retrieve'})),
    url(r'api/topic/list/(?P<pk_curriculum>[0-9]+)/$', views.Topic.as_view({'get': 'list'})),
    url(r'api/question/list/(?P<pk_tag>[0-9]+)/$', views.Question.as_view({'get': 'list'})),
    url(r'api/studentGroup/(?P<pk_student>[0-9]+)/(?P<pk_group>[a-zA-Z0-9]+)/$', views.StudentGroup.as_view({'get': 'retrieve'})),
    # url(r'api/activity/list/(?P<pk_topic>[0-9]+)/$', views.Activity.as_view({'get': 'list'})),
    # url(r'api/support/list/(?P<pk_topic>[0-9]+)/$', views.Support.as_view({'get': 'list'})),
    # url(r'api/answer/list/(?P<pk_activity>[0-9]+)/$', views.Answer.as_view({'get': 'list'})),
    url(r'^', include(router.urls)),
    # Session Authentication
    url(r'^api/rest-auth/', include('rest_auth.urls')),
    url(r'^api/rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^api/refresh-token/', refresh_jwt_token),
    url(r'^api/verify-token/', verify_jwt_token),
]
'''rest-auth urls:'''
'''Method: POST'''
'''Reference: http://django-rest-auth.readthedocs.io/en/latest/api_endpoints.html'''
'''Reference: http://getblimp.github.io/django-rest-framework-jwt/'''

# Endpoint: /rest-auth/registration/
# Payload:
# {
#     "username": "USERNAME",
#     "password1": "PASSWORD",
#     "password2": "PASSWORD",
#     "email": "OPTIONAL_EMAIL"
# }

# Endpoint: /rest-auth/login/
# Payload:
# {
#     "username": "USERNAME",
#     "password": "PASSWORD"
# }

# Endpoint: /rest-auth/logout/
# Headers: Authorization: JWT YOUR_TOKEN_HERE

# Endpoint: /refresh-token/
# Payload:
# {
#     "token": "YOUR_OLD_TOKEN"
# }