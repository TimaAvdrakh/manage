import inspect

from apps.system import (
    models,
    utils,
)


class MainMixin(object):
    pass


class AuditMixin(MainMixin):

    def description(self) -> str:
        pass

    def before(self) -> str:
        pass

    def after(self) -> str:
        pass

    def user_request(self) -> models.UserRequest:
        pass

    def _save(self, request, user_request, desc):
        models.AuditLog.objects.create(
            user=request.user,
            user_request=user_request,
            description=desc,
            before=self.before(),
            after=self.after(),
            ip_address=utils.get_client_ip(request)
        )

    def dispatch(self, request, *args, **kwargs):
        try:

            user_request = self.user_request()
            desc = self.description()

            if self.user_request() is None:
                user_request = kwargs.get('user_request')

            if self.description() is None:
                desc = kwargs.get('description')

            self._save(request, user_request, desc)
            return super().dispatch(request, *args, **kwargs)
        except Exception as e:
            raise e


class UserRequestMixin(AuditMixin):
    user_request_number = None
    class_name = None
    kind = None

    def check_params(self):
        if self.user_request_number is None:
            raise Exception('Не указан номер запроса')

        if self.class_name is None:
            raise Exception('Не указано имя класса')

        if inspect.isclass(self.class_name) is False:
            raise Exception('Не верно указан class-handler')

        if self.kind is None:
            raise Exception('Не указа вид запроса')

    def dispatch(self, request, *args, **kwargs):
        try:
            self.check_params()

            user_request_obj = models.UserRequest.objects.create(
                user=request.user,
                kind=self.kind,
                class_name=self.class_name.__name__,
                number=self.user_request_number
            )

            obj = self.class_name()
            obj.exec()

            return super().dispatch(
                request, *args, **kwargs, user_request=user_request_obj,
            )
        except Exception as e:
            raise e
