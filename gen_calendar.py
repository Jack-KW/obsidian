import calendar
from datetime import datetime, timedelta

def generate_markdown_calendar(years=3):
    today = datetime.today()
    current_year = today.year

    for year in range(current_year, current_year + years):
        for month in range(1, 13):
            month_calendar = calendar.monthcalendar(year, month)
            month_name = calendar.month_name[month]
            
            # Markdown header for the month
            print(f"### {month_name} {year}")
            print("| MON | TUE | WED | THU | FRI | SAT | SUN |")
            print("| :-: | :-: | :-: | :-: | :-: | :-: | :-: |")
            
            for week in month_calendar:
                week_str = "|"
                for day in week:
                    if day == 0:
                        week_str += " |"
                    else:
                        date_str = f"{year}{month:02d}{day:02d}"
                        week_str += f" [[{date_str}\|{day}]] |"
                print(week_str)
            print()

generate_markdown_calendar()
