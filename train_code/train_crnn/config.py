from pathed import filedir
import pickle as pkl

project_directory = filedir / ".." / ".."

# change paths for custom training
image_dir = "/content/crnn_data"
pretrained_model = project_directory / "checkpoints" / "CRNN-1010.pth"
font_path = "/content/rgreekl21.ttf" # None or path to font file


train_infofile = project_directory / "train_code" / "train_crnn" / "text_file.txt"
alphabet_list = pkl.load(
    open(project_directory / "train_code" / "train_crnn" / "custom_alphabet.pkl", "rb")
)
alphabet = [ord(ch) for ch in alphabet_list]

max_epochs = 10
batchSize = 10  # make 80 if gpu
workers = 0  # make 10 if gpu
gpus = 0

color_model = "L"  # grayscale

imgH = 32
imgW = 800
nclass = len(alphabet) + 1
nh = 256
niter = 100
lr = 0.0003
beta1 = 0.5
remove_blank = True  # add spaces like this: " word " or no spaces like: "word"

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
leakyRelu = False