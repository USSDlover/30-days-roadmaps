from datetime import date, datetime, timedelta, time, timezone, tzinfo, UTC, MAXYEAR, MINYEAR


def show_case_module():
    print(f"Date: {date.today()}")
    print(f"DateTime: {datetime.now()}")
    print(f"TimeDelta: {timedelta.max}")
    print(f"Time: {time.hour}")
    print(f"TimeZone: {timezone}")
    print(f"TZ Info: {tzinfo}")
    print(f"UTC: {UTC}")
    print(f"Max Y: {MAXYEAR}")
    print(f"Min Y: {MINYEAR}")


show_case_module()
