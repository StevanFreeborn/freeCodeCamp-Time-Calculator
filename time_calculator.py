def add_time(start, duration, day_of_week=None):
  days = {
    "monday": 1,
    "tuesday": 2,
    "wednesday": 3,
    "thursday": 4,
    "friday": 5,
    "saturday": 6,
    "sunday": 7
  }

  start_parts = start.lower().split()
  
  start_time = start_parts[0]

  start_time_parts = start_time.split(":")
  
  start_hour = int(start_time_parts[0])
  start_minutes = int(start_time_parts[1])
  start_period = start_parts[1]

  if day_of_week != None:
    start_day = days[day_of_week.lower()]
  else:
    start_day = 0

  duration_parts = duration.split(":")

  duration_hours = int(duration_parts[0])
  duration_minutes = int(duration_parts[1])

  num_of_days = int(duration_hours / 24)

  if start_period == "pm":
    start_hour = start_hour + 12
  else:
    start_hour = start_hour

  end_minutes = start_minutes + duration_minutes
  end_hour = start_hour + duration_hours
  end_day = start_day + num_of_days
  
  if end_minutes >= 60:
    end_hour += 1
    end_minutes = end_minutes % 60
  
  if end_hour > 24:
    if end_minutes != 59:
      num_of_days += 1
      end_day += 1
    end_hour = end_hour % 24

  if end_day > 7:
    end_day = end_day % 7
  
  if end_hour < 12:
    end_period = 'AM'
  else:
    end_hour = end_hour - 12
    end_period = 'PM'

  if end_minutes <= 9:
    end_minutes_as_str = "0" + str(end_minutes)
  else:
    end_minutes_as_str = str(end_minutes)

  if end_hour == 0:
    end_hour_as_str = "12"
  else:
    end_hour_as_str = str(end_hour)

  new_time = end_hour_as_str + ":" + end_minutes_as_str + " " + end_period

  if day_of_week != None:
    end_day_as_str = list(days.keys())[list(days.values()).index(end_day)]
    new_time += f', {end_day_as_str.capitalize()}'
    
  if num_of_days == 1:
    new_time += " (next day)"
  elif num_of_days > 1:
    new_time += f" ({num_of_days} days later)"
  
  return new_time