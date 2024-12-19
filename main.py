import time, random #import

def race(horses, track_length=50):
    progress = [0] * len(horses)

    while True:
        time.sleep(1)

        print("\n" * 50)
        print("START" + "-" * track_length + "FINISH\n")

        for i in range(len(horses)):
            progress[i] += random.randint(1, 3)
            if progress[i] > track_length:
                progress[i] = track_length

        for i in range(len(horses)):
            track = "-" * progress[i]
            spaces = " " * (track_length - progress[i])
            print(f"Horse {i+1}: |{track}>{spaces}|")

        print("\n" + "-" * (track_length+11))

        for i in range(len(horses)):
            if progress[i] >= track_length:
                return i

print("\nWelcome to the Horse Race!")
print("The race is starting\n")

horses = ["Thunderbolt", "Midnight", "Stormchaser", "Blaze", "Shadowfax"]
winner = race(horses)

print("\nThe race has ended")
print(f"The winning horse is Horse {winner+1}: {horses[winner]}")
