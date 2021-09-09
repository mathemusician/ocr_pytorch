from pathed import filedir
import pickle as pkl

project_directory = filedir / ".." / ".."

alphabet_list = pkl.load(open(filedir / '..' / 'train_crnn' / "alphabet.pkl", "rb"))
alphabet = [ord(ch) for ch in alphabet_list]

alphabet = alphabet
imgH = 32
imgW = 800
nc = 1
nclass = len(alphabet) + 1
nh = 256
niter = 100
lr = 0.0003
beta1 = 0.5
cuda = True
gpus = 1
saved_model_dir = "crnn_models"
remove_blank = False

saved_model_prefix = "CRNN-1010"
train_infofile = [project_directory / "train_code" / "train_crnn" / "text_file.txt"]
val_infofile = "path_to_test_infofile.txt"
keep_ratio = True
use_log = True
pretrained_model = project_directory / "checkpoints" / "CRNN-1010.pth"
batchSize = 20  # make 80 if gpu
workers = 4  # make 10 if gpu
adam = True


experiment = None
displayInterval = 500
n_test_disp = 9
valInterval = 500
saveInterval = 500
adadelta = False
random_sample = True


max_epochs = 10
