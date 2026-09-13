from dataclasses import dataclass
from typing import Any, Iterator


@dataclass(frozen=True)
class DatasetHandle:
    source: str
    split: str

    def batches(self) -> Iterator[Any]:
        raise NotImplementedError


def prepare_dataset(source: str, split: str) -> DatasetHandle:
    raise NotImplementedError
