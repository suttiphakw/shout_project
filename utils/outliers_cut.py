import statistics

from utils.predicted_value import PredictedIG


def outlier_cut(before_list):
    sd = statistics.stdev(before_list)
    mean = statistics.mean(before_list)
    final_list = []
    used_idx = []
    for idx, value in enumerate(before_list):
        if not value < mean - sd and not value > mean + sd:
            final_list.append(value)
            used_idx.append(idx)

    return {
        'mean': statistics.mean(final_list),
        'used_idx': used_idx
    }

