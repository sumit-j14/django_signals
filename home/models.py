from django.db import models

# importing django signals
from django.db.models.signals import pre_save,post_save

# this method makes use of signal-decorator
from django.dispatch import receiver
# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

def task_handler(sender, instance, **kwargs):
    print(instance)
    print("presave signal printed")

# METHOD-1  (using pre_save.connect)
# this line connects signal to task handler
# basically task handler fucntion gets called just before saving any TASK MODEL ENRTY
# pre_save.connect(task_handler, sender=Task)


# METHOD-2  (using decorator)
@receiver(pre_save, sender=Task)
def task_handler(sender, instance, **kwargs):

    # here instance is the database entry
    print(instance)
    print("PRE_SAVE SIGNAL PRINTED")
    print("USED DECORATOR METHOD")


@receiver(post_save, sender=Task)
def task_handler_postsave(sender, instance, **kwargs):

    # here instance is the database entry
    print(instance)
    print("POST_SAVE SIGNAL PRINTED")