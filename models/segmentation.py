from typing import Any


class SegmentationModel:
    def predict(self, inputs: Any) -> Any:
        raise NotImplementedError

    def load_checkpoint(self, location: str) -> None:
        raise NotImplementedError


def create_model() -> SegmentationModel:
    raise NotImplementedError
