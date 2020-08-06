import os

import h5py as h5py
import numpy as np


def open_h5_file(file_path):
    return h5py.File(file_path,'r')


class H5DatasetFile:
    def __init__(self, dataset_path):
        if os.path.isfile(dataset_path):
            dataset_files_paths = [dataset_path]
        elif os.path.isdir(dataset_path):
            h5_dataset_files = [file_name for file_name in os.listdir(dataset_path) if '.h5' in file_name]
            dataset_files_paths = [os.path.join(dataset_path, file_name) for file_name in h5_dataset_files]
        else:
            raise ValueError(f"Invalid dataset path: {dataset_path}")

        self.ds_dict = {}
        for ds_path in dataset_files_paths:
            with h5py.File(ds_path, 'r') as ds:
                ds_names = tuple(ds.keys())

            for name in ds_names:
                self.ds_dict[name] = H5Dataset(ds_path, name)

    def get_dataset_names(self):
        return tuple(self.ds_dict.keys())

    def get_dataset_by_name(self, dataset_name: str) -> 'H5Dataset':
        assert dataset_name in self.get_dataset_names()
        return self.ds_dict[dataset_name]

    def get_dataset_by_index(self, ds_index: int) -> 'H5Dataset':
        ds_name = self.get_dataset_names()[ds_index]
        return self.get_dataset_by_name(ds_name)

class H5Dataset:
    def __init__(self, dataset_path, dataset_name):
        self.ds_path = dataset_path
        self.ds_name = dataset_name

        with open_h5_file(self.ds_path) as ds_file:
            assert dataset_name in ds_file

        self.ds_name = dataset_name

        # todo: implement fields as class and assign them to ds with setattr()


    def __len__(self):
        with h5py.File(self.ds_path, 'r') as ds:
            ds_len = len(ds[self.ds_name])
        return ds_len

    @property
    def shape(self):
        with h5py.File(self.ds_path, 'r') as ds:
            ds_shape = ds[self.ds_name].shape
        return ds_shape

    def __getitem__(self, item):
        with h5py.File(self.ds_path, 'r') as ds:
            data = np.array(ds[self.ds_name][item])
        return data

    def __iter__(self):
        indexes = range(self.__len__())
        for index in indexes:
            yield self.__getitem__(index)