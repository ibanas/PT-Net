
# Project Title

To use PT-Net, select the model and its respective scaler that you would like to use and download them to your prefered directory.

Once done, you can then pip install the python module that will allow you to generate data of prefered length.

The python module can be installed as follows: "pip install TremorGan".
https://pypi.org/project/TremorGan/

The function takes in the trained model, the length of the sequences of the time series data you want to generate,
the scaler that was used to scale the data to train the mode, and the number of sequences you want to generate.

The function returns a numpy array of size n*m.
Where n is the number of sequences you want to generate.
And m is the length of the sequence.

You can specify three sequence lengths: either 10, for 10 seconds
						    	            or 5, for 5 seconds
						    	            or 2, for 2 seconds

# Example on how to use the function.

from TremorGan import *

generated_sequences = generate_tremor(model, 10, scaler, 1000)

### model
is the model you want to use, either PT-Net 2, PT-Net 5 or PT-Net 10.
### 10
refers to the length of the senquence(s) you want to generate.

Use 10 for 10 seconds long sequences if using PT-Net 10. or 5 for 5 seconds long sequence(s) if using PT-Net 5, etc.
### scaler
 is the respective scaler of the model selected.
### 1000
 is for 1000 samples or generate 1000 sequences of length 10 seconds, 5 seconds, or 2 seconds.

