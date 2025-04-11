# Constants
KM_TO_MILES = 1.61
MINUTES_TO_HOURS = 60

def average_time_per_mile(dist_km, time_min):
    dist_miles = dist_km / KM_TO_MILES
    time_mile = time_min / MINUTES_TO_HOURS
    return time_mile / dist_miles

def main():
    dist_km = int(input("Enter distance in km: "))
    time_min = int(input("Enter time in minutes: "))
    result = average_time_per_mile(dist_km, time_min)
    print("Average time per mile:", result)

if __name__ == "__main__":
    main()
