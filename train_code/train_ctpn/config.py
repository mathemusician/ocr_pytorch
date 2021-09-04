import os
from getpaths import Path

# ocr_pytorch = 'path to ocr_pytorch'
ocr_pytorch = Path() / ".." / ".."


icdar17_mlt_img_dir = '/Users/mosaicchurchhtx/Desktop/ScriptReader/data/ctpn_data/train'#ocr_pytorch / "ctpn_data" / "train"
icdar17_mlt_gt_dir = '/Users/mosaicchurchhtx/Desktop/ScriptReader/data/ctpn_data/train_gt'#ocr_pytorch / "ctpn_data" / "train_gt"
num_workers = 0  # change to 2 when on GPU
pretrained_weights = ocr_pytorch / "checkpoints" / "CTPN.pth"
batch_size = 1
num_gpus = 0

max_epochs = 30  # change to 30 when on GPU
anchor_scale = 16
IOU_NEGATIVE = 0.3
IOU_POSITIVE = 0.7
IOU_SELECT = 0.7

RPN_POSITIVE_NUM = 150
RPN_TOTAL_NUM = 300

# bgr can find from  here: https://github.com/fchollet/deep-learning-models/blob/master/imagenet_utils.py
IMAGE_MEAN = [123.68, 116.779, 103.939]
OHEM = True

prob_thresh = 0.5
height = 720

checkpoints_dir = ocr_pytorch / "checkpoints"