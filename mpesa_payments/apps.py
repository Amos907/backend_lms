from django.apps import AppConfig


class MpesaPaymentsConfig(AppConfig):
    name = 'mpesa_payments'

    def ready(self):
        from .jobs import updater
        updater.start()
