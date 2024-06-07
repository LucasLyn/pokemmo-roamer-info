from datetime import datetime # Used for dates
import pytz # Used for timezone
import calendar # Used to get proper date strings (month, day, etc)

# Save month names list in variable for easier reference
month_names = calendar.month_name

# PokeMMO is based on UTC
timezone = pytz.UTC

# Get the current month
current_time = datetime.now(timezone)
current_month = current_time.month
next_month = current_month+1
current_month_name = month_names[current_month]
next_month_name = month_names[next_month]
