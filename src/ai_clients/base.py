from abc import ABC, abstractmethod


class BaseAIClient(ABC):

    @abstractmethod
    async def chat_completion(self, message: str, **filters) -> dict:
        raise NotImplementedError

    @abstractmethod
    async def list_model(self) -> list:
        raise NotImplementedError
