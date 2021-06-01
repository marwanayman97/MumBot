from django.db import models

# Create your models here.


class User(models.Model):
    user_password = models.CharField(max_length=32)
    user_name = models.CharField(max_length=25)
    user_phone = models.CharField(max_length=15)
    user_email = models.EmailField(max_length=254)
    user_role = models.IntegerField()


class Parent(User):
    def __str__(self):
        return f"{self.id}"


class Admin(User):
    def __str__(self):
        return f"{self.id}"



class Specialist(User):

    specialist_brief = models.CharField(max_length=500)
    specialist_active_status = models.BooleanField()

    def __str__(self):
        return f"{self.id}"


class SingleInquiry(models.Model):

    parent_id = models.ForeignKey(
        Parent, on_delete=models.CASCADE, related_name="Chats")
    specialist_id = models.ForeignKey(
        Specialist, on_delete=models.CASCADE, related_name="Chats")
    inquiry_price = models.FloatField()
    inquire_duration_in_minutes = models.IntegerField()
    inquiry_start_time = models.TimeField(auto_now=False, auto_now_add=False)
    inquiry_end_time = models.TimeField(auto_now=False, auto_now_add=False)


class VideoSession(models.Model):

    parent_id = models.ForeignKey(
        Parent, on_delete=models.CASCADE, related_name="VideoSessions")
    specialist_id = models.ForeignKey(
        Specialist, on_delete=models.CASCADE, related_name="VideoSessions")
    video_price = models.FloatField()
    video_duration_in_minutes = models.IntegerField()
    video_date = models.DateField(auto_now=False, auto_now_add=False)
    video_start_time = models.TimeField(auto_now=False, auto_now_add=False)
    video_end_time = models.TimeField(auto_now=False, auto_now_add=False)


class Question(models.Model):

    question_body = models.CharField(max_length=1000)
    question_tags = models.CharField(max_length=200,default="")
    question_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    question_admin = models.ForeignKey(Admin, on_delete=models.CASCADE)


class Answer(models.Model):

    answer_body = models.CharField(max_length=1000)
    answer_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    answer_specialist = models.ForeignKey(
        Specialist, on_delete=models.CASCADE, related_name="AnsweredQuestions")
    answer_question = models.ForeignKey(Question, on_delete=models.CASCADE)

class Schedules(models.Model):

    schedule_specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)
    free_day = models.CharField(max_length=20)
    free_day_start_time = models.TimeField(auto_now=False, auto_now_add=False)
    free_day_end_time = models.TimeField(auto_now=False, auto_now_add=False)