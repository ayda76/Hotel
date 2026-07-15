from rest_framework.routers import DefaultRouter
from django.urls import path , include ,re_path
from account.api.views import (AccountViewSet,
                                   AccountMeViewSet,
                                   EmployeeViewSet,
                                   GuestViewSet,
                                   PasswordChangeView,
                                   RegisterView,
                                   LoginView)


router = DefaultRouter()
router.register("Account", AccountViewSet)
router.register("Employee",EmployeeViewSet)
router.register("Guest",GuestViewSet)

urlpatterns = [

    path("", include(router.urls)),
    path('change/password/', PasswordChangeView.as_view()),
    path('SignUp/', RegisterView.as_view(), name='signup'),
    path('Login/', LoginView.as_view(), name='login'),
    path('ME/', AccountMeViewSet.as_view(), name='me'),

]
