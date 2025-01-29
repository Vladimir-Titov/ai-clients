from src.ai_clients.base import BaseAIClient


class DeepSeekClient(BaseAIClient):
    async def chat_completion(self, message: str, **filters) -> dict:
        pass

    async def list_model(self) -> list:
        pass