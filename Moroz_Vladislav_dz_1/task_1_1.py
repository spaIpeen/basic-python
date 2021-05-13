duration = int(input("duration = "))
time_in_seconds = [60, 3600, 86400, 2678400, 32140800]

# Промежуток до 59 секунд
if duration < time_in_seconds[0]:
    print(f"{duration} сек")

# Промежуток до 59 минут 59 секунд
elif time_in_seconds[0] <= duration < time_in_seconds[1]:
    minutes = duration // 60
    seconds = duration % 60
    print(f"{minutes} мин {seconds} сек")

# Промежуток до 23 часов 59 минут 59 секунд
elif time_in_seconds[1] <= duration < time_in_seconds[2]:
    hours = duration // 3600
    dur = duration - hours * 3600
    minutes = dur // 60
    seconds = duration % 60
    print(f"{hours} час {minutes} мин {seconds} сек")

# Промежуток до 30 дней 23 часов 59 минут 59 секунд
elif time_in_seconds[2] <= duration < time_in_seconds[3]:
    days = duration // 86400
    days_to_hours = duration - days * 86400
    hours = days_to_hours // 3600
    hours_to_minutes = days_to_hours - hours * 3600
    minutes = hours_to_minutes // 60
    seconds = duration % 60
    print(f"{days} дн {hours} час {minutes} мин {seconds} сек")

# Промежуток до 12 месяцев 30 дней 23 часов 59 минут 59 секунд
elif time_in_seconds[3] <= duration < time_in_seconds[4]:
    months = duration // 2678400
    months_to_days = duration - months * 2678400
    days = months_to_days // 86400
    days_to_hours = months_to_days - days * 86400
    hours = days_to_hours // 3600
    hours_to_minutes = days_to_hours - hours * 3600
    minutes = hours_to_minutes // 60
    seconds = duration % 60
    print(f"{months} мес {days} дн {hours} час {minutes} мин {seconds} сек")

# Промежуток от года и выше
else:
    years = duration // 32140800
    years_to_months = duration - years * 32140800
    months = years_to_months // 2678400
    months_to_days = years_to_months - months * 2678400
    days = months_to_days // 86400
    days_to_hours = months_to_days - days * 86400
    hours = days_to_hours // 3600
    hours_to_minutes = days_to_hours - hours * 3600
    minutes = hours_to_minutes // 60
    seconds = duration % 60
    print(f"{years} лет {months} мес {days} дн {hours} час {minutes} мин {seconds} сек")
