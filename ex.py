import random

# Define subjects and available time slots (e.g., 5 days, 5 periods per day)
subjects = ['Maths', 'Physics', 'Chemistry', 'Computer Science', 'English', 'Biology', 'History', 'PE']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
periods_per_day = 5  # Number of periods per day

# Function to generate a timetable
def generate_timetable(subjects, days, periods_per_day):
    timetable = {}
    for day in days:
        timetable[day] = random.sample(subjects, periods_per_day)
    return timetable

# Function to display the timetable
def display_timetable(timetable):
    for day, periods in timetable.items():
        print(f"\n{day} Timetable:")
        for i, subject in enumerate(periods, 1):
            print(f"  Period {i}: {subject}")

# Generate and display the timetable
timetable = generate_timetable(subjects, days, periods_per_day)
display_timetable(timetable)
