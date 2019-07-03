from app.controller.ExecutionControllerBase import ExecutionControllerBase


class MultithreadExecutionController(ExecutionControllerBase):
    # TODO: Support multi-threading execution, due to time constraint I've decided to submit without this feature
    def execute(self, location_app_params):
        raise NotImplemented
