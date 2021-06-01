from django.urls import path
from . import views

urlpatterns = [
    path("api/parent/<int:id>/", views.api_parent_view, name="parentdetail"),
    path("api/specialist/<int:id>/", views.api_specialist_view, name="specialistdetail"),
    path("api/inquiry/<int:id>/", views.api_inquiry_view, name="inquirydetail"),
    path("api/videosession/<int:id>/", views.api_video_view, name="videodetail"),
    path("api/question/<int:id>/", views.api_question_view, name="questiondetail"),
    path("api/answer/<int:id>/", views.api_answer_view, name="answerdetail"),
    path("api/schedule/<int:id>/", views.api_schedule_view, name="scheduledetail"),

]