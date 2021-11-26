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

