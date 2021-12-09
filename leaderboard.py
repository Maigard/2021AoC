import json
from datetime import datetime
leaderboard = json.load(open("leaderboard.txt","r"))
print(leaderboard['owner_id'])
for (id, member) in leaderboard['members'].items():
    print(member['name'], end="")
    for completion in range(1,len(member['completion_day_level'])+1):
        completion = member['completion_day_level'][str(completion)]
        print(f"\t {datetime.fromtimestamp(completion['1']['get_star_ts'])}", end="")
        print(f"\t {datetime.fromtimestamp(completion['2']['get_star_ts'])}", end="")
    print()