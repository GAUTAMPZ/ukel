from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add custom fields if needed
    pass

# Add related_name to prevent clashes
CustomUser._meta.get_field('groups').remote_field.related_name = 'custom_user_set'
CustomUser._meta.get_field('user_permissions').remote_field.related_name = 'custom_user_set'
