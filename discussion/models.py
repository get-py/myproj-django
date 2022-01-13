from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class HotPotato(TimestampedModel):
    author = models.CharField(max_length=20, db_index=True)
    title = models.CharField(max_length=100, db_index=True)
    content = models.TextField()
    photo = models.ImageField(upload_to="discussion/post/%Y/%m/%d", blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["-id"]


class Comment(TimestampedModel):
    hot_potato = models.ForeignKey(HotPotato, on_delete=models.CASCADE)
    author = models.CharField(max_length=20, db_index=True)
    review = models.TextField()

    def __str__(self) -> str:
        return self.review

    class Meta:
        ordering = ["-id"]


class Tag(TimestampedModel):
    name = models.CharField(max_length=200, db_index=True, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["name"]
