from django.contrib.auth.base_user import BaseUserManager


class MainUserManager(BaseUserManager):

    def create_user(self, identifier, password=None):
        if not identifier:
            raise ValueError('Users must have a identifier')
        user = self.model(identifier=identifier)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, identifier, password):
        user = self.create_user(identifier=identifier, password=password)
        user.is_admin = True
        user.is_superuser = True
        user.is_moderator = True
        user.is_staff = True
        user.save(using=self._db)
        return user
