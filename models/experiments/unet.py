import torch
import torch.nn as nn
from models.unet import Unet

experiment_name = 'Unet'
log_dir_name = 'lidc'

# number of filter for the latent levels, they will be applied in the order as loaded into the list
filter_channels = [32, 64, 128, 192]
latent_levels = len(filter_channels) - 1
n_classes = 1

no_convs_fcomb = 4 # not used
beta = 10.0 # not used

use_reversible = False

# use 1 for grayscale, 3 for RGB images
input_channels = 1

epochs_to_train = 50

model = Unet