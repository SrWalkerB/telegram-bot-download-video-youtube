from database import BaseModelService

class UserCommandRequestModel(BaseModelService):
    collection_name = "user_command_request"

    def __init__(self):
        super().__init__(self.collection_name)

    