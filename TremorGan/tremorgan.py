import numpy as np
from Tensorflow.keras.models import load_model
import pickle

def load_model_scaler(h5_model_path, pickled_scaler_path):
	model = load_model(h5_model_path)
	with open(pickled_scaler_path, 'rb') as sc:
		scaler = pickle.load(sc)
	return model, scaler

def generate_signal(model, length, scaler, n_sequences):
	if length == 10:
		window = 1000
		latent_dim = 2000
	elif length == 5:
		window = 500
		latent_dim = 1000
	elif length == 2:
		window = 200
		latent_dim = 150
	generated_sequences = np.zeros((n_sequences, window))
	generated_sequences[:] = np.nan
	for _i_ in range(n_sequences):
		vector = np.random.randn(latent_dim)
		vector = vector.reshape(1, latetnt_dim)
		seq = model.predict(vector)
		seq = seq.reshape(1, window)
		seq = scaler.inverse_transform(seq)
		generated_sequences[_i_] = seq[0]
	return generated sequences
