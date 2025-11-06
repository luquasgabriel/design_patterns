from abc import ABC, abstractmethod

# "Interface" legada
class ProcessadorPagamentoLegado(ABC):
    @abstractmethod
    def processar_pagamento(self, pedido_id: str, valor: float) -> dict:
        """
        Processa pagamento do pedido 'pedido_id' no valor 'valor'.
        Retorna um dict com informações de status.
        """
        pass

# nova interface do sistema de pagamento
class SolicitacaoPagamento:
    def __init__(self, pedido_id: str, valor: float):
        self.pedido_id = pedido_id
        self.valor = valor

class NovoSistemaPagamento:
    def executar_pagamento(self, solicitacao: SolicitacaoPagamento) -> dict:

        # aqui estaria a lógica de comunicacao com o sistema de pagamento real
        print(f"Executando pagamento para pedido {solicitacao.pedido_id}, valor {solicitacao.valor}")

        return {
            "pedido_id": solicitacao.pedido_id,
            "valor": solicitacao.valor,
            "status": "sucesso",
            "canal": "novo_sistema"
        }

class AdaptadorPagamento(ProcessadorPagamentoLegado):
    def __init__(self, novo_sistema: NovoSistemaPagamento):
        self._novo_sistema = novo_sistema

    def processar_pagamento(self, pedido_id: str, valor: float) -> dict:
        # aqui sao convertidos os parâmetros pra a interface do novo sistema
        solicitacao = SolicitacaoPagamento(pedido_id, valor)
        resultado = self._novo_sistema.executar_pagamento(solicitacao)
        return resultado