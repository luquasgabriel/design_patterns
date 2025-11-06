from abc import ABC, abstractmethod

class ServicoNotificacao(ABC):
    @abstractmethod
    def enviar(self, destinatario: str, assunto: str, conteudo: str):
        pass

class ServicoNotificacaoEmail(ServicoNotificacao):
    def enviar(self, destinatario: str, assunto: str, conteudo: str):
        # aqui seria inserida uma lógica para envio de e-mail
        print(f"[EMAIL] Para {destinatario}: {assunto} — {conteudo}")
        return {"canal": "email", "destinatario": destinatario, "status": "enviado"}

class ServicoNotificacaoSMS(ServicoNotificacao):
    def enviar(self, destinatario: str, assunto: str, conteudo: str):
        # aqui, seria inserida uma lógica pra envio de SMS
        print(f"[SMS] Para {destinatario}: {conteudo}")
        return {"canal": "sms", "destinatario": destinatario, "status": "enviado"}

class ServicoNotificacaoPush(ServicoNotificacao):
    def enviar(self, destinatario: str, assunto: str, conteudo: str):
        # aqui seria inserida uma lógica de Push
        print(f"[PUSH] Para {destinatario}: {assunto} — {conteudo}")
        return {"canal": "push", "destinatario": destinatario, "status": "enviado"}

class FabricaServicoNotificacao:
    @staticmethod
    def criar_servico(tipo: str) -> ServicoNotificacao:
        tipo = tipo.lower()
        if tipo == "email":
            return ServicoNotificacaoEmail()
        elif tipo == "sms":
            return ServicoNotificacaoSMS()
        elif tipo == "push":
            return ServicoNotificacaoPush()
        else:
            raise ValueError(f"Tipo de notificação desconhecido: {tipo}")
