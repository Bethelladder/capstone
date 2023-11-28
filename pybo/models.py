from django.db import models

# Create your models here.

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

class MyModel(models.Model):
    # MEDIA_ROOT/uploads/ 경로로 파일 업로드
    upload = models.FileField(upload_to = 'uploads/')
    # or
    # MEDIA_ROOT/uploads/2021/01/01 경로로 파일 업로드
    upload = models.FileField(upload_to = 'uploads/%Y/%m/%d/')