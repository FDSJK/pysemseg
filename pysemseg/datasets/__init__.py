from .base import SegmentationDataset
from .pascal_voc.pascal import PascalVOCSegmentation, PascalVOCTransform
from .camvid import CamVid, CamVidTransform
from .transformer import DatasetTransformer


def create_dataset(data_dir, dataset_cls, dataset_args,
                   transformer_cls, transformer_args, mode):
    dataset = dataset_cls(data_dir, mode, **dataset_args)
    transformer = transformer_cls(mode=mode, **transformer_args)
    return DatasetTransformer(dataset, transformer, mode)
