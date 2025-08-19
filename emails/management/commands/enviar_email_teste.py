# core/management/commands/enviar_email_teste.py

from django.core.management.base import BaseCommand
from django.conf import settings  # Importe o 'settings' do Django
from emails.utils import enviar_email_teste

class Command(BaseCommand):
    help = 'Envia um e-mail de teste para o destinatário definido em settings.py.'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('--- Script para Envio de E-mail de Teste ---'))

        # Verifica se as variáveis de destino foram definidas no settings.py
        if not hasattr(settings, 'EMAIL_DESTINO_ENDERECO') or not settings.EMAIL_DESTINO_ENDERECO:
            self.stdout.write(self.style.ERROR(
                'ERRO: A variável EMAIL_DESTINO_ENDERECO não foi definida em settings.py.'
            ))
            return

        # Pega as informações diretamente do settings.py
        nome_destinatario = getattr(settings, 'EMAIL_DESTINO_NOME', 'Destinatário')
        email_destinatario = settings.EMAIL_DESTINO_ENDERECO

        self.stdout.write(
            f"Lendo destinatário de settings.py: '{nome_destinatario} <{email_destinatario}>'"
        )
        self.stdout.write("Preparando para enviar e-mail...")

        # Chama a função que faz o trabalho pesado
        enviar_email_teste(
            nome_usuario=nome_destinatario,
            email_destinatario=email_destinatario
        )