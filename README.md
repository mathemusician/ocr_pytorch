## lightning_text_detection

### Demo

CTPN detects text regions (green boxes) and CRNN recognizes the text within each region:

![OCR Demo Result](docs/images/test_result.jpg)

> A full PyTorch Lightning rewrite of [courao/ocr.pytorch](https://github.com/courao/ocr.pytorch)

Text detection (CTPN) and text recognition (CRNN) — converted end-to-end from vanilla PyTorch to **PyTorch Lightning**.

### What's different from the original?

The [original repo](https://github.com/courao/ocr.pytorch) uses hand-rolled training loops with raw PyTorch. This fork **rewrites both models and data pipelines as PyTorch Lightning modules**:

| Component | Original (courao) | This fork |
|---|---|---|
| **CTPN model** | `ctpn_model.py` | `ctpn_model_PL.py` — `pl.LightningModule` |
| **CTPN data** | inline in train script | `ctpn_data_PL.py` — `pl.LightningDataModule` |
| **CTPN training** | `ctpn_train.py` (manual loop) | `ctpn_train_PL.py` — `pl.Trainer` |
| **CRNN model** | `crnn.py` | `crnn_model_PL.py` — `pl.LightningModule` |
| **CRNN data** | `mydataset.py` | `crnn_data_PL.py` — `pl.LightningDataModule` |
| **CRNN training** | `train_pytorch_ctc.py` (manual loop) | `crnn_train_PL.py` — `pl.Trainer` |

This gives you automatic logging (TensorBoard), checkpointing, multi-GPU support, and cleaner separation of model/data/training logic — all out of the box.

Working on implementing [CRAFT](https://github.com/clovaai/CRAFT-pytorch)
and [Transformer_STR](https://github.com/opconty/Transformer_STR).

Pull requests welcome!

## Prerequisite

- python-3.6+
- pytorch-lightning-1.4.1
- opencv-4.5.2.52
- numpy-1.21.1
- Pillow-8.2.0
- pathed-1.1.00


### Detection
Detection is based on [CTPN](https://arxiv.org/abs/1609.03605), some codes are borrowed from 
[pytorch_ctpn](https://github.com/opconty/pytorch_ctpn)

### Recognition
Recognition is based on [CRNN](http://arxiv.org/abs/1507.05717), some codes are borrowed from
[crnn.pytorch](https://github.com/meijieru/crnn.pytorch)

### Test
Download pretrained models from [Baidu Netdisk](https://pan.baidu.com/s/1yllO9hBF8TgChHJ7i3WobA) (extract code: u2ff) or [Google Driver](https://drive.google.com/open?id=1hRr9v9ky4VGygToFjLD9Cd-9xan43qID)
and put these files into checkpoints.
Then run
>python3 demo.py

The image files in ./test_images will be tested for text detection and recognition, the results will be stored in ./test_result.

If you want to test a single image, run
>python3 test_one.py [filename]

### Train
Training codes are placed into train_code directory.  
Train [CTPN](./train_code/train_ctpn/readme.md)  
Train [CRNN](./train_code/train_crnn/readme.md)  

### Licence
[MIT License](https://opensource.org/licenses/MIT)
