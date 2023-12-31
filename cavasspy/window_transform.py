import numpy as np


def transform_window(input_data, center, window_width):
    min_ = (2 * center - window_width) / 2 + 0.5
    max_ = (2 * center + window_width) / 2 + 0.5
    factor = 255 / (max_ - min_)

    data = (input_data - min_) * factor

    data = np.where(data < 0, 0, data)
    data = np.where(data > 255, 255, data)

    return data.astype(np.uint8)


def cavass_soft_tissue_window(input_data):
    return transform_window(input_data, 1000, 500)


def cavass_bone_window(input_data):
    return transform_window(input_data, 2000, 4000)
