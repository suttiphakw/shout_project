import statistics

def cut(raw_list, id_list):
  if len(raw_list) == 0:
    return False
  if len(raw_list) == 1:
    context = {
      'final_dict': {id_list[0]: raw_list[0]},
      'ig_average_total_like': raw_list[0],
    }
  else:
    sd = statistics.stdev(raw_list)
    ig_average_total_like = statistics.mean(raw_list)
    final_dict = {id_list[idx]: value for idx, value in enumerate(raw_list) if not value < ig_average_total_like - sd and not value > ig_average_total_like + sd}
    if final_dict:
      ig_average_total_like = statistics.mean([final_dict[key] for key in final_dict])
    context = {
      'final_dict': final_dict,
      'ig_average_total_like': ig_average_total_like,
    }
  return context