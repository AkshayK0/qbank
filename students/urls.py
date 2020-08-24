from django.urls import path, include

from students import views

urlpatterns = [
    path('syllabus/', views.SyllList.as_view()),
    path('syllabus/<int:pk>/', views.SyllDetail.as_view()),
    path('', views.StudentList.as_view()),
    path('profile/', views.ProfileList.as_view()),
    path('subject/<syll_id>/', views.SubjectList.as_view()),
    path('detail/<pk>', views.StudentDetailView.as_view()),
    path('science/subject/', views.SubjectSience.as_view()),  
    path('<subject>/science/', views.ScienceView.as_view()), 
    path('science/year/', views.ScienceYear.as_view()),
    # path('science/<subject>/', views.TopicScience.as_view()),
    path('commerce/subject/', views.SubjectCommerce.as_view()),  
    path('<subject>/commerce/', views.CommerceView.as_view()), 
    path('commerce/year/', views.CommerceYear.as_view()),
    # path('commerce/<subject>/', views.TopicCommerce.as_view()),
    path('class10/subject/', views.SubjectClass10.as_view()),  
    path('<subject>/class10/', views.Class10View.as_view()), 
    path('class10/year/', views.Class10Year.as_view()),
    # path('<subject>/class10/', views.TopicClass10.as_view()),
    path('profile/<pk>', views.ProfileView.as_view()),
    path('bookmark/',  views.CreateBookmark.as_view()),
    path('bookmark/<user>/',  views.BookmarkList.as_view()),
    path('bookmark/<user>/<qid>/', views.BookmarkDelete.as_view()),
    path('solved/<user>/',  views.SolvedList.as_view()),
    path('solved/',  views.CreateSolved.as_view()),
]