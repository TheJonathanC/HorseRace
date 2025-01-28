import time
import random

def race(horses, track_length=50):
    progress = [0] * len(horses)
    standings = []

    while True:
        time.sleep(1)

        print("\n" * 50)
        print("START" + "-" * track_length + "FINISH\n")

        for i in range(len(horses)):
            if i not in standings:
                progress[i] += random.randint(1, 3)
                if progress[i] >= track_length:
                    progress[i] = track_length
                    standings.append(i)

        for i in range(len(horses)):
            track = "-" * progress[i]
            spaces = " " * (track_length - progress[i])
            print(f"Horse {i+1}: |{track}>{spaces}|")

        print("\n" + "-" * (track_length + 11))

        if len(standings) == len(horses):
            return standings

print("\nWelcome to the Horse Race!")
print("The race is starting\n")

horses = ["Thunderbolt", "Midnight", "Stormchaser", "Blaze", "Shadowfax"]
standings = race(horses)

print("\nThe race has ended")
print("Final Standings:")
for position, horse_index in enumerate(standings):
    print(f"{position + 1}. Horse {horse_index + 1}: {horses[horse_index]}")
