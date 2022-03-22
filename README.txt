To use PT-Net, select the model and its respective scaler that you would like to use and download them to your prefered directory.

Once done, you can then pip install the python module that will allow you to generate data of prefered length.

The python module can be installed as follows: "pip install TremorGan".
https://pypi.org/project/TremorGan/

or you can use the code provided in file "TremorGan"

If you choose to install and use the python package, you have to load the model using load_model from tensorflow, and you have to load the pickled scaler.
The function takes in the trained model, the length of the sequences of the time series data you want to generate,
the scaler that was used to scale the data to train the mode, and the number of sequences you want to generate.

If you choose to use the code provided in this repositor, navigate to TremorGan file:
1. Load the model and scaler by using the "load_model_scaler" function.
	a. The "load_model_scaler" function takes in the paths of the .h5 model and the .pickle scaler, respectively.
	example: load_model_scaler("C:/Users/.../Desktop/PT_Net_10.h5", "C:/Users/.../Desktop/PT_Net_10_scaler.pickle")
	Replace "..." with username.
		
	b. model, scaler = load_model_scaler("C:/Users/.../Desktop/PT_Net_10.h5", "C:/Users/.../Desktop/PT_Net_10_scaler.pickle")
	
2. Use the "generate_signal" function to generate n*m array of signals 


The function returns a numpy array of size n*m.
Where n is the number of sequences you want to generate.
And m is the length of the sequence.

You can specify three sequence lengths: either 2, for 2 seconds
					    or 5, for 5 seconds
					    or 10, for 10 seconds

example on how to use the function.


generated_sequences = generate_signal(model, 10, scaler, 1000)

# model: is the model you want to use, either PT_Net_2, PT_Net_5 or PT_Net_10.
# 10 refers to the length of the senquence(s) you want to generate. 
# e.g. use 10 for 10 seconds long sequences if using PT-Net 10. or 5 for 5 seconds long sequence(s) if using PT-Net 5, etc.

# scaler is the respective scaler of the model selected.
# 1000 is for 1000 samples or generate 1000 sequences of length 10 seconds, 5 seconds, or 2 seconds.
