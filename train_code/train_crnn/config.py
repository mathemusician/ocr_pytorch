from pathed import filedir
import pickle as pkl

project_directory = filedir / ".." / ".."

# change paths for custom training
image_dir = ""
train_infofile = [project_directory / "train_code" / "train_crnn" / "text_file.txt"]
pretrained_model = project_directory / "checkpoints" / "CRNN-1010.pth"
alphabet_list = pkl.load(open(filedir / '..' / 'train_crnn' / "alphabet.pkl", "rb"))
alphabet = [ord(ch) for ch in alphabet_list]

max_epochs = 10
batchSize = 20  # make 80 if gpu
workers = 4  # make 10 if gpu
gpus = 1

self.config.color_model = "L" # grayscale

imgH = 32
imgW = 800
nclass = len(alphabet) + 1
nh = 256
niter = 100
lr = 0.0003
beta1 = 0.5
remove_blank = True # add spaces like this: " word " or no spaces like: "word"

keep_ratio = True
use_log = True
adam = True

experiment = None
displayInterval = 500
n_test_disp = 9
valInterval = 500
saveInterval = 500
adadelta = False
random_sample = True
