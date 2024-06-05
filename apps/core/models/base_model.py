from django.db import models

from django.db.models import PROTECT

# from apps.user_auth.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # created_by = models.ForeignKey(User,
    #                                on_delete=PROTECT,
    #                                related_name='%(class)s_createdby',
    #                                null=True,
    #                                blank=True)
    # modified_by = models.ForeignKey(User,
    #                                 on_delete=PROTECT,
    #                                 related_name='%(class)s_modifiedby',
    #                                 null=True,
    #                                 blank=True)

    class Meta:
        abstract = True

    # def save(self, *args, **kwargs):
    #     if 'request' in kwargs and not self.pk:
    #         request = kwargs.pop('request')
    #         self.created_by = request.user
    #     self.modified_by = request.user if 'request' in kwargs else self.modified_by
    #     super().save(*args, **kwargs)
