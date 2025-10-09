from typing import List, Union
NumberLike = Union[float, int, str]

def predict(features: List[NumberLike]) -> List[float]:
    return [float(x) * 2 for x in features]