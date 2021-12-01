import statistics

class PredictedIG:
    peers_story_view_per_like = 1.53
    nano_story_view_per_like = 1.78
    micro_story_view_per_like = 1.55

    @staticmethod
    def like(followers):
        return 0.08 * followers

    @staticmethod
    def post_reach(likes, story_view):
        return statistics.mean([likes*5, story_view*3])

    def story_view(self, likes, followers):
        if followers <= 5000:
            return likes * self.peers_story_view_per_like
        if followers <= 10000:
            return likes * self.nano_story_view_per_like
        return likes * self.micro_story_view_per_like

def check_is_predicted(list_reach):
    final_list = []
    for value in list_reach:
        if value is not 0:
            final_list.append(value)
        else:
            continue

    if len(final_list) > 3:
        return False
    else:
        return True
