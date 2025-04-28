import random

# Constants
HOURS = list(range(6, 21))  # 6 AM to 8 PM
MINUTES = [0, 15, 20, 30, 40, 45]
DRIVE_LENGTHS = [20, 30, 40, 45, 60, 75]
LENGTH_WEIGHTS = [20, 25, 30, 15, 5, 5]
DRIVERS = ["mom", "dad"]
DRIVER_WEIGHTS = [80, 20]

# Target Goals (in minutes)
DAY_TARGET = 3000
NIGHT_TARGET = 600

# Tracking progress
day_minutes = 0
night_minutes = 0

# History log of all drives
driving_log = []

# Helper functions
def select_random_time():
    hour = random.choice(HOURS)
    minute = random.choice(MINUTES)
    return hour, minute

def select_drive_length():
    return random.choices(DRIVE_LENGTHS, weights=LENGTH_WEIGHTS, k=1)[0]

def select_driver():
    return random.choices(DRIVERS, weights=DRIVER_WEIGHTS, k=1)[0]

def is_night(hour):
    return hour >= 18  # 6 PM and later is night

# Simulation loop
while day_minutes < DAY_TARGET or night_minutes < NIGHT_TARGET:
    hour, minute = select_random_time()
    drive_length = select_drive_length()
    driver = select_driver()

    # Save drive info into the log
    drive_record = {
        "hour": hour,
        "minute": minute,
        "length": drive_length,
        "driver": driver,
        "is_night": is_night(hour)
    }
    driving_log.append(drive_record)

    # Update totals
    if drive_record["is_night"]:
        night_minutes += drive_length
    else:
        day_minutes += drive_length

    # Optional: Print each drive immediately
    if minute == 0:
        print(f"{hour} O'clock for {drive_length} minutes. Driving with {driver}.")
    else:
        print(f"{hour}:{minute:02d} for {drive_length} minutes. Driving with {driver}.")

    # Print progress
    print(f"Day Hours: {day_minutes/60:.2f}")
    print(f"Night Hours: {night_minutes/60:.2f}\n")

# --- After simulation ends ---

# Final Summary
print("\n✅ All Drives Summary:\n")

for i, drive in enumerate(driving_log, start=1):
    time_str = f"{drive['hour']}:{drive['minute']:02d}" if drive['minute'] != 0 else f"{drive['hour']} o'clock"
    day_night = "Night" if drive["is_night"] else "Day"
    print(f"Drive {i}: {time_str}, {drive['length']} minutes, with {drive['driver']} ({day_night})")

# Final totals
print(f"\n🏁 Final Total Day Hours: {day_minutes/60:.2f}")
print(f"🏁 Final Total Night Hours: {night_minutes/60:.2f}")
