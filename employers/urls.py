from django.urls import path
from employers import views


urlpatterns = [
    path('home', views.EmployerHome.as_view(),name='emp_home'),
    path('job/add-job',views.EmpAddJob.as_view(),name='addjob'),
    path('job/emp_joblist',views.JobLisView.as_view(),name='joblist'),
    path('job/emp_job-details/<int:id>',views.JobDetailView.as_view(),name='emp-detail'),
    path('job/change_job/<int:id>',views.EditView.as_view(),name='edit-emp_job'),
    path('job/remove/<int:id>',views.DeleteJob.as_view(),name='delete-job'),
    path('user/account/signup',views.Signup.as_view(),name='signup'),
    path('user/account/signin',views.Signin.as_view(),name='signin'),
    path('user/account/signin',views.logout_view,name='signout'),
    path('user/account/verify_password',views.ChangePassword.as_view(),name='verifypwd'),
    path('user/account/reset_password',views.PasswordReset.as_view(),name='resetpwd'),
    path('profile/add',views.CompanyProfileView.as_view(),name='emp_profileadd'),
    path('profile/profile_details',views.EmpProfileView.as_view(),name='emp_profileview'),
    path('profile/edit_profile/<int:id>',views.EmpEditCompanyProfile.as_view(),name='emp-edit_profile')

]
