""" Calculate the total time and awards for a triathalon event """
tri_swim = int(input("Swimming event time (in minutes): \n"))

tri_cyc = int(input
              ("Cycling event time (in minutes): \n"))

tri_run = int(input
              ("Running event time (in minutes): \n"))

# Total time for all events
tri_total_time = tri_swim + tri_cyc + tri_run
print(f"\nThis participant completed the triathalon in "
      f"{tri_total_time}\033[0m mins\n")

# Award based on total time
if tri_total_time <= 100:
    print("\033[32mAward: Provincial colours\033[0m")
elif tri_total_time <= 105:
    print("\033[33mAward: Provincial half colours\033[0m")
elif tri_total_time <= 110:
    print("Award: Provincial scroll")
else:
    print("\033[31mNo award\033[0m")
