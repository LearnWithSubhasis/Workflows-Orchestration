import argparse
import joblib
import numpy as np
from sklearn.linear_model import SGDRegressor


def train_model(x_train, y_train):
    print(f'training model ...')

    model_pkl_file = 'model.pkl'

    x_train_data = np.load(x_train)
    y_train_data = np.load(y_train)

    model = SGDRegressor(verbose=1)
    model.fit(x_train_data, y_train_data)

    joblib.dump(model, model_pkl_file)
    print(f'generated model {model_pkl_file}...')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x_train')
    parser.add_argument('--y_train')
    args = parser.parse_args()
    train_model(args.x_train, args.y_train)