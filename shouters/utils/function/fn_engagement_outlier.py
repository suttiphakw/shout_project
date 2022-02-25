import statistics

def cut(raw_list, id_list):
  sd = statistics.stdev(raw_list)
  ig_average_total_like = statistics.mean(raw_list)
  final_dict = {id_list[idx]: value for idx, value in enumerate(raw_list) if not value < ig_average_total_like - sd and not value > ig_average_total_like + sd}
  context = {
    'final_dict': final_dict,
    'ig_average_total_like': ig_average_total_like,
  }
  return context