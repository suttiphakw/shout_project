import statistics

from utils.predicted_value import PredictedIG


def outlier_cut(before_list):
    sd = statistics.stdev(before_list)
    mean = statistics.mean(before_list)
    final_list = []
    used_idx = []
    for idx, value in enumerate(before_list):
        if not value < mean - sd:
            final_list.append(value)
            used_idx.append(idx)

    return {
        'mean': statistics.mean(final_list),
        'used_idx': used_idx
    }

# sample = [1270, 302, 313, 1100, 323, 1000, 1500, 358, 857, 1500, 230, 1058, 400, 1013, 1100]
# sample = [612, 2400, 550, 2300, 240, 1750, 600, 1980, 760, 3800, 3600, 2600, 1000, 2000, 1000, 1900]
