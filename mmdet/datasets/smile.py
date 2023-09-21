from .coco import CocoDataset
from .registry import DATASETS
@DATASETS.register_module
class SmileDataset(CocoDataset):
    CLASSES = ["null","11","12","13","14","21","22","23","24","25","26"]
