from django.urls import path
from . import views

urlpatterns = [
    path("api/parent/<int:id>/", views.api_parent_view, name="parentdetail"),
    path("api/parent/create/", views.api_create_parent_view, name="parentcreate"),
    path("api/parent/update/<int:id>/", views.api_update_parent_view, name="parentupdate"),
    path("api/parent/delete/<int:id>/", views.api_delete_parent_view, name="parentdelete"),
    path("api/specialist/<int:id>/", views.api_specialist_view, name="specialistdetail"),
    path("api/inquiry/<int:id>/", views.api_inquiry_view, name="inquirydetail"),
    path("api/videosession/<int:id>/", views.api_video_view, name="videodetail"),
    path("api/question/<int:id>/", views.api_question_view, name="questiondetail"),
    path("api/answer/<int:id>/", views.api_answer_view, name="answerdetail"),
    path("api/schedule/<int:id>/", views.api_schedule_view, name="scheduledetail"),

]