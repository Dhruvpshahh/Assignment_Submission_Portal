from django.urls import path
from . import views


app_name='assignments'

urlpatterns=[
    path('', views.AssigmentList,name='list'),
    path('grading_page/<int:pk>', views.GradingPage,name='grading_page'),
    # path('after_grading/<int:pk>', views.AfterGrading,name='after_grading'),
    path('submit/<int:pk>/', views.SubmissionFormView,name='submit'),
    path('register_course/<int:pk>/', views.RegisterFormView,name='register_course'),
    path('create_assignment/', views.CourseView, name='create'),
    path('create_course/', views.CreateCourseView, name='create_course'),
    path('submissions/',views.SubmissionListView,name='submission'),
    path('assignment/<int:pk>/',views.Assignments_list,name='assignment_list'),
    path('assignment/<int:pk>/delete/',views.deletingAssign,name='deleteassign'),
    path('available_courses/',views.AvailableListView,name='available'),
    path('deregister/<int:pk>/',views.DeregisterCourse,name='deregister_course'),

]


