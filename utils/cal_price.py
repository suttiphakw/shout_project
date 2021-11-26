class IGStoryFc:

    tier_1 = 500
    tier_2 = 1000
    tier_3 = 3000
    tier_4 = 5000
    tier_5 = 8000

    # Price per view
    tier_1_price = 0.5
    tier_2_price = 0.4
    tier_3_price = 0.32
    tier_4_price = 0.256
    tier_5_price = 0.2048
    tier_6_price = 0.1638

    def cal_price(self, story_view):
        if story_view <= 500:
            return story_view * self.tier_1_price

        if story_view <= 1000:
            return (self.tier_1 * self.tier_1_price) + \
                   ((story_view - self.tier_1) * self.tier_2_price)

        if story_view <= 3000:
            return (self.tier_1 * self.tier_1_price) + \
                   ((self.tier_2 - self.tier_1) * self.tier_2_price) + \
                   ((story_view - self.tier_2) * self.tier_3_price)

        if story_view <= 5000:
            return (self.tier_1 * self.tier_1_price) + \
                   ((self.tier_2 - self.tier_1) * self.tier_2_price) + \
                   ((self.tier_3 - self.tier_2) * self.tier_3_price) + \
                   ((story_view - self.tier_3) * self.tier_4_price)

        if story_view <= 8000:
            return (self.tier_1 * self.tier_1_price) + \
                   ((self.tier_2 - self.tier_1) * self.tier_2_price) + \
                   ((self.tier_3 - self.tier_2) * self.tier_3_price) + \
                   ((self.tier_4 - self.tier_3) * self.tier_4_price) + \
                   ((story_view - self.tier_4) * self.tier_5_price)

        return (self.tier_1 * self.tier_1_price) + \
               ((self.tier_2 - self.tier_1) * self.tier_2_price) + \
               ((self.tier_3 - self.tier_2) * self.tier_3_price) + \
               ((self.tier_4 - self.tier_3) * self.tier_4_price) + \
               ((self.tier_5 - self.tier_4) * self.tier_5_price) + \
               ((story_view - self.tier_5) * self.tier_6_price)


class IGStoryUgc:

    tier_1 = 500
    tier_2 = 1000
    tier_3 = 3000
    tier_4 = 5000
    tier_5 = 8000

    # Price per view
    tier_1_price = 0.8
    tier_2_price = 0.64
    tier_3_price = 0.512
    tier_4_price = 0.4096
    tier_5_price = 0.3277
    tier_6_price = 0.2621

    def cal_price(self, story_view):
        if story_view <= 500:
            return story_view * self.tier_1_price

        if story_view <= 1000:
            return (self.tier_1 * self.tier_1_price) + \
                   ((story_view - self.tier_1) * self.tier_2_price)

        if story_view <= 3000:
            return (self.tier_1 * self.tier_1_price) + \
                   ((self.tier_2 - self.tier_1) * self.tier_2_price) + \
                   ((story_view - self.tier_2) * self.tier_3_price)

        if story_view <= 5000:
            return (self.tier_1 * self.tier_1_price) + \
                   ((self.tier_2 - self.tier_1) * self.tier_2_price) + \
                   ((self.tier_3 - self.tier_2) * self.tier_3_price) + \
                   ((story_view - self.tier_3) * self.tier_4_price)

        if story_view <= 8000:
            return (self.tier_1 * self.tier_1_price) + \
                   ((self.tier_2 - self.tier_1) * self.tier_2_price) + \
                   ((self.tier_3 - self.tier_2) * self.tier_3_price) + \
                   ((self.tier_4 - self.tier_3) * self.tier_4_price) + \
                   ((story_view - self.tier_4) * self.tier_5_price)

        return (self.tier_1 * self.tier_1_price) + \
               ((self.tier_2 - self.tier_1) * self.tier_2_price) + \
               ((self.tier_3 - self.tier_2) * self.tier_3_price) + \
               ((self.tier_4 - self.tier_3) * self.tier_4_price) + \
               ((self.tier_5 - self.tier_4) * self.tier_5_price) + \
               ((story_view - self.tier_5) * self.tier_6_price)

class IGPostFc:

    tier_1 = 500
    tier_2 = 1000
    tier_3 = 3000
    tier_4 = 5000
    tier_5 = 8000

    # Price per view
    tier_1_price = 1
    tier_2_price = 0.65
    tier_3_price = 0.4225
    tier_4_price = 0.2746
    tier_5_price = 0.1785
    tier_6_price = 0.1160

    def cal_price(self, post_reach):
        if post_reach <= 500:
            return post_reach * self.tier_1_price

        if post_reach <= 1000:
            return (self.tier_1 * self.tier_1_price) + \
                   ((post_reach - self.tier_1) * self.tier_2_price)

        if post_reach <= 3000:
            return (self.tier_1 * self.tier_1_price) + \
                   ((self.tier_2 - self.tier_1) * self.tier_2_price) + \
                   ((post_reach - self.tier_2) * self.tier_3_price)

        if post_reach <= 5000:
            return (self.tier_1 * self.tier_1_price) + \
                   ((self.tier_2 - self.tier_1) * self.tier_2_price) + \
                   ((self.tier_3 - self.tier_2) * self.tier_3_price) + \
                   ((post_reach - self.tier_3) * self.tier_4_price)

        if post_reach <= 8000:
            return (self.tier_1 * self.tier_1_price) + \
                   ((self.tier_2 - self.tier_1) * self.tier_2_price) + \
                   ((self.tier_3 - self.tier_2) * self.tier_3_price) + \
                   ((self.tier_4 - self.tier_3) * self.tier_4_price) + \
                   ((post_reach - self.tier_4) * self.tier_5_price)

        return (self.tier_1 * self.tier_1_price) + \
               ((self.tier_2 - self.tier_1) * self.tier_2_price) + \
               ((self.tier_3 - self.tier_2) * self.tier_3_price) + \
               ((self.tier_4 - self.tier_3) * self.tier_4_price) + \
               ((self.tier_5 - self.tier_4) * self.tier_5_price) + \
               ((post_reach - self.tier_5) * self.tier_6_price)

class IGPostUgc:

    tier_1 = 500
    tier_2 = 1000
    tier_3 = 3000
    tier_4 = 5000
    tier_5 = 8000

    # Price per view
    tier_1_price = 1.2
    tier_2_price = 0.78
    tier_3_price = 0.507
    tier_4_price = 0.3296
    tier_5_price = 0.2142
    tier_6_price = 0.1392

    def cal_price(self, post_reach):
        if post_reach <= 500:
            return post_reach * self.tier_1_price

        if post_reach <= 1000:
            return (self.tier_1 * self.tier_1_price) + \
                   ((post_reach - self.tier_1) * self.tier_2_price)

        if post_reach <= 3000:
            return (self.tier_1 * self.tier_1_price) + \
                   ((self.tier_2 - self.tier_1) * self.tier_2_price) + \
                   ((post_reach - self.tier_2) * self.tier_3_price)

        if post_reach <= 5000:
            return (self.tier_1 * self.tier_1_price) + \
                   ((self.tier_2 - self.tier_1) * self.tier_2_price) + \
                   ((self.tier_3 - self.tier_2) * self.tier_3_price) + \
                   ((post_reach - self.tier_3) * self.tier_4_price)

        if post_reach <= 8000:
            return (self.tier_1 * self.tier_1_price) + \
                   ((self.tier_2 - self.tier_1) * self.tier_2_price) + \
                   ((self.tier_3 - self.tier_2) * self.tier_3_price) + \
                   ((self.tier_4 - self.tier_3) * self.tier_4_price) + \
                   ((post_reach - self.tier_4) * self.tier_5_price)

        return (self.tier_1 * self.tier_1_price) + \
               ((self.tier_2 - self.tier_1) * self.tier_2_price) + \
               ((self.tier_3 - self.tier_2) * self.tier_3_price) + \
               ((self.tier_4 - self.tier_3) * self.tier_4_price) + \
               ((self.tier_5 - self.tier_4) * self.tier_5_price) + \
               ((post_reach - self.tier_5) * self.tier_6_price)
