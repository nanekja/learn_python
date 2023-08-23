#
from collections import OrderedDict

def main():
    sportTeams = [("Royals", (18,12)), ("Rockets", (24,6)), ("Cardinals", (20,10)), ("Dragons", (22,8)),
    ("Kings", (15,15)), ("Chargers", (20,10)), ("Jets", (16,14)), ("Warriors", (25,5))]

    sortedTeams=sorted(sportTeams, key=lambda t: t[1][0], reverse=True)

    teams=OrderedDict(sortedTeams)
    print(teams)

    tm, wl = teams.popitem(teams)
    print(tm, wl)
    

if __name__=="__main__":
    main()