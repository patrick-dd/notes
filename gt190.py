# getting share of top three hundred UCI WT riders with height greater than
# 190 cm

import pandas as pd
from itertools import chain

# I copied the UCI doc and did some vim magic to get this csv
# https://twitter.com/laflammerouge16/status/1457627229375143936
uci_heights = pd.read_csv('uci_heights.csv')
uci_heights.head()
gt190_riders = [ str(f).lower()[1:] + ' ' + str(s).lower() for f, s in zip(uci_heights.firstName.values, uci_heights.surname.values)]

# get top three hundred riders. Thanks First Cycling!
first = pd.read_html('https://firstcycling.com/ranking.php?h=1&rank=1&y=2021-43')[0]['Rider']
second = pd.read_html('https://firstcycling.com/ranking.php?h=1&rank=1&y=2021-43&page=2')[0]['Rider']
third = pd.read_html('https://firstcycling.com/ranking.php?h=1&rank=1&y=2021-43&page=3')[0]['Rider']
riders = [[f for f in first.values] + [s for s in second.values] + [t for t in third.values]]
riders = list(chain.from_iterable(riders))
riders = [r.lower() for r in riders]
num_riders = len(riders)
assert num_riders == 300, "should have 300 riders"

# results
num_top_300_gt190 = len(set(riders).intersection(set(gt190_riders)))
share_top_300_gt190 = num_top_300_gt_190 / num_riders

print("Share of riders in top 300 that are at least 190cm tall",
      share_top_300_gt190)
# 0.07

# For NL males, it's 0.0975

