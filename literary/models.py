from django.db import models

# Create your models here.
class Literarysource(models.Model):
    title = models.TextField(("title"), max_length=100)
    author = models.TextField(("author"), max_length=100)
    url_q = models.URLField(("url"), max_length=100)
    pdf_file = models.FileField("file")


def __str__(self):
    return str(self.id) + " // " + str(self.paper)


class Textesource(models.Model):
    essay = models.FileField("file")
    essay_post = models.TextField("text_note", max_length=500)
    project = models.TextField(("project"), max_length=100)

def __str__(self):
    return str(self.id + " // " + str(self.essay))