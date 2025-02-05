from django.urls import path
from main.views import forgotpassword

urlpatterns = [
    path('login/confirmationemail/',
         forgotpassword.ForgotPassword.as_view(), name='confirmation-email'),
    path('login/confirmationemail/confirmationcode/',
         forgotpassword.ConfirmationCode.as_view(), name='confirmation-code'),
    path('login/confirmationemail/confirmationcode/changepassword/',
         forgotpassword.ChangePassword.as_view(), name='change-password'),
]
