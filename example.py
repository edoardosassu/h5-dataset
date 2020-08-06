from h5_dataset import H5DatasetFile
from plot_utils import show_frame


def show_datasets_in_h5_file(dataset_path):
    ds_file = H5DatasetFile(dataset_path)
    print(ds_file.get_dataset_names())


def get_dataset_objects_by_name(dataset_path):
    ds_file = H5DatasetFile(dataset_path)

    for ds_name in ds_file.get_dataset_names():
        ds = ds_file.get_dataset_by_name(ds_name)
        print(ds_name, ds.shape)


def get_dataset_objects_by_index(dataset_path, index=0):
    ds_file = H5DatasetFile(dataset_path)

    # this is equal to:
    #  ds = ds_file.get_dataset_by_name(ds_file.get_dataset_names()[index])
    ds = ds_file.get_dataset_by_index(index)
    print(ds.ds_name, ds.shape)


def show_frame_from_dataset(dataset_path, index=0):
    ds = H5DatasetFile(dataset_path).get_dataset_by_index(index)

    show_frame(frame=ds[0], title=f'{ds.ds_name}')

def filter_datasets(dataset_path):
    ds = H5DatasetFile(dataset_path)
    wt_ds_list = [ds_name for ds_name in ds.get_dataset_names() if 'wt' in ds_name]
    print(wt_ds_list)
    ko_ds_list = [ds_name for ds_name in ds.get_dataset_names() if 'ko' in ds_name]
    print(ko_ds_list)

#if __name__ == '__main__':
    #ds_path = path to .h5 file or to folder containing .h5 files

    # ds = H5DatasetFile(ds_path).get_dataset_by_index(0)
    # print(ds.shape)
    # print(f"{'='*10} show_datasets_in_h5_file {'='*10}")
    # show_datasets_in_h5_file(ds_path)

    # print(f"\n{'=' * 10} get_dataset_objects_by_name {'=' * 10}")
    # get_dataset_objects_by_name(ds_path)
    #
    # print(f"\n{'=' * 10} get_dataset_objects_by_index {'=' * 10}")
    # get_dataset_objects_by_index(ds_path)
    #
    # print(f"\n{'=' * 10} show_frame_from_dataset {'=' * 10}")
    # show_frame_from_dataset(ds_path)
    #
    # print(f"\n{'=' * 10} filter_datasets {'=' * 10}")
    # filter_datasets(ds_path)

    # show_frame(H5DatasetFile(ds_path).get_dataset_by_index(2)[3])
