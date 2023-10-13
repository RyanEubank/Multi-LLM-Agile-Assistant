from langchain.chat_models import ChatVertexAI
from server.multillm.llm_communication import Abstract_LLM_Model

class ChatBison(Abstract_LLM_Model.Endpoint):

        def __init__(self) -> None:
            super().__init__(ChatVertexAI(model_name="chat-bison"))

