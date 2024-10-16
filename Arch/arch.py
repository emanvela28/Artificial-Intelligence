#
# arch.py
#
# This script implements three Python classes for three different artificial
# neural network architectures: no hidden layer, one hidden layer, and two
# hidden layers. Note that this script requires the installation of the
# PyTorch (torch) Python package.
#
# This content is protected and may not be shared, uploaded, or distributed.
#
# PLACE ANY COMMENTS, INCLUDING ACKNOWLEDGMENTS, HERE.
# I referenced David Noelle's lecture slides from 11/14/23.
# I watched this YouTube video: https://www.youtube.com/watch?v=yN7ypxC7838
# I skimmed about half of this article to draw necessary information https://www.geeksforgeeks.org/artificial-neural-networks-and-its-applications/
#
#
# Which network architecture achieves the lowest training set error?
# The training model with two hidden layers.

# Which network architecture tends to exhibit the best testing set accuracy?
# The training model with one hidden layer.
#
# Emmanuel Velazquez 12/12/23
#

# PyTorch - Deep Learning Models
import torch.nn as nn
import torch.nn.functional as F

input_size = 4
output_size = 3

class AnnLinear(nn.Module):
    """Class describing a linear artificial neural network, with no hidden
    layers, with inputs directly projecting to outputs."""

    def __init__(self):
        super().__init__()
        # Define a linear layer: input_size features to output_size classes
        self.my_layer = nn.Linear(input_size, output_size)

    def forward(self, x):
        # Forward pass: input features directly project to output classes
        output = self.my_layer(x)
        return output


class AnnOneHid(nn.Module):
    """Class describing an artificial neural network with one hidden layer,
    using the rectified linear (ReLU) activation function."""

    def __init__(self):
        super().__init__()
        # Define a hidden layer and an output layer
        # Input size: input_size features, output size: 20 neurons
        self.hidden_layer = nn.Linear(input_size, 20)
        # Output layer: 20 neurons to output_size classes
        self.output_layer = nn.Linear(20, output_size)

    def forward(self, x):
        # Forward pass with ReLU activation for hidden layer
        hidden_layer = F.relu(self.hidden_layer(x))
        # Output layer projects hidden layer activations to output classes
        output = self.output_layer(hidden_layer)
        return output


class AnnTwoHid(nn.Module):
    """Class describing an artificial neural network with two hidden layers,
    using the rectified linear (ReLU) activation function."""

    def __init__(self):
        super().__init__()
        # Define two hidden layers and output layer
        # Input size: input_size features, output size: 16 neurons
        self.hidden_layer1 = nn.Linear(input_size, 16)
        # Hidden layer 2: 16 neurons to 12 neurons
        self.hidden_layer2 = nn.Linear(16, 12)
        # Output layer: 12 neurons to output_size classes
        self.output_layer = nn.Linear(12, output_size)

    def forward(self, x):
        # Forward pass with ReLU activation for both hidden layers
        hidden1 = F.relu(self.hidden_layer1(x))
        hidden2 = F.relu(self.hidden_layer2(hidden1))
        # Output layer projects hidden layer activations to output classes
        output = self.output_layer(hidden2)
        return output
