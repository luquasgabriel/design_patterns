# Create your views here.
import json
from django.views.decorators.http import require_POST
from django.http import JsonResponse, HttpResponseBadRequest
from .services import NovoSistemaPagamento, AdaptadorPagamento

@require_POST
def processar_pagamento(request):
    try:
        dados = json.loads(request.body)
    except json.JSONDecodeError:
        return HttpResponseBadRequest("JSON inválido")

    pedido_id = dados.get("pedido_id")
    valor = dados.get("valor")

    if not pedido_id or valor is None:
        return HttpResponseBadRequest("Campos obrigatórios: pedido_id, valor")

    try:
        valor = float(valor)
    except (ValueError, TypeError):
        return HttpResponseBadRequest("Campo 'valor' deve ser numérico")

    # aqui se cria o novo sistema e o adapter
    novo_sistema = NovoSistemaPagamento()
    adaptador = AdaptadorPagamento(novo_sistema)

    # usa a interface legada (via adapter) para processar
    resultado = adaptador.processar_pagamento(pedido_id, valor)

    return JsonResponse({"resultado": resultado})


'''
a view pode ser chamada dessa forma:

POST http://127.0.0.1:8000/pagamentos/processar/
Content-Type: application/json

{
  "pedido_id": "ABDC123",
  "valor": 150.75
}
'''