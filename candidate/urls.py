from django.urls import path
from candidate import views

urlpatterns=[
    path('home',views.CandidateHomeView.as_view(),name='cand-home'),
    path('profile/add',views.CandidateProfileCreate.as_view(),name='addprofile'),
    path('profile/details',views.CandidateProfileDetailsView.as_view(),name='cand-profileview'),
    path('profile/edit/<int:id>',views.CandidateProfileEdit.as_view(),name='updateprofile'),
    path('jobs/all-list',views.CandidateJoblistView.as_view(),name='cand-joblist'),
    path('jobs/details/<int:id>',views.CandidateJobDetailsView.as_view(),name='cand_job-details'),
    path('user/account/signin', views.logoutview, name='signout'),
    path('user/account/password-reset', views.PasswordChangeView.as_view(), name='passwordreset'),
    path('jobs/myjobs', views.AppliedApplicationListView.as_view(), name='myjobs'),
    path('jobs/applynow/<int:id>',views.apply_now,name='applynow')

]