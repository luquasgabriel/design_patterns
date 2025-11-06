import json
from django.views.decorators.http import require_POST
from django.http import JsonResponse, HttpResponseBadRequest
from .services import FabricaServicoNotificacao

@require_POST
def enviar_notificacao(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return HttpResponseBadRequest("JSON inválido")

    tipo = data.get("tipo")
    destinatario = data.get("destinatario")
    assunto = data.get("assunto")
    conteudo = data.get("conteudo")

    if not all([tipo, destinatario, conteudo]):
        return HttpResponseBadRequest("Campos obrigatórios: tipo, destinatario, conteudo")

    try:
        servico = FabricaServicoNotificacao.criar_servico(tipo)
    except ValueError as e:
        return JsonResponse({"erro": str(e)}, status=400)

    resultado = servico.enviar(destinatario, assunto or "", conteudo)

    return JsonResponse({"resultado": resultado})

'''
Essa view pode ser usada como nos exemplos abaixo:

Para email:
POST http://127.0.0.1:8000/notificacao/enviar/
Content-Type: application/json

{
  "tipo": "email",
  "destinatario": "usuario@email.com",
  "assunto": "bem-vindo!!",
  "conteudo": "obrigado por se registrar!"
}

Ou pra SMS:
{
  "tipo": "sms",
  "destinatario": "+5511999999999",
  "conteudo": "Seu código de verificação é 123456"
}
'''
