from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

def enviar_email_teste(nome_usuario, email_destinatario):
    subject = 'E-mail de Teste do Django'
    context = {'nome_usuario': nome_usuario}

    text_content = render_to_string('emails/bem_vindo.txt', context)
    html_content = render_to_string('emails/bem_vindo.html', context)

    try:
        email = EmailMultiAlternatives(
            subject,
            text_content,
            settings.DEFAULT_FROM_EMAIL,
            [email_destinatario]
        )
        email.attach_alternative(html_content, "text/html")
        email.send()
        print(f"\n✅ E-mail enviado com sucesso para {email_destinatario}!")
    except Exception as e:
        print(f"\n❌ Falha ao enviar E-mail: {e}")