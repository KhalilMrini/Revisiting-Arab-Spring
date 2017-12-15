from os import listdir
import sparkpickle
import pandas as pd
import time
import joblib
import pickle
import numpy as np
from joblib import Parallel, delayed

def load_files(files):
	print(time.ctime(), '    Start...')
	data = []
	for file in files:
		for obj in sparkpickle.load_gen(open('data.pkl/{}'.format(file), 'rb')):
				data.append(obj)
	print(time.ctime(), '    Loading DF...')
	df = pd.DataFrame(data)
	print(time.ctime(), '    Loaded DF. Saving...')
	del data
	df.to_pickle('dataframes/df.{}.pkl'.format(time.time()))
	print(time.ctime(), '    Saved.')
	del df

def main():
	files = [file for file in listdir('data.pkl') if file.startswith('part')]
	data_rows = []
	print(time.ctime(), 'Starting...')

	range_ = np.arange(len(files))

	njobs = 20
	files_range = np.array_split(files, njobs)

	Parallel(n_jobs=njobs, verbose=11)(delayed(load_files)(f) for f in files_range)

	print(time.ctime(), 'Done ...')

if __name__ == '__main__':
	main()
