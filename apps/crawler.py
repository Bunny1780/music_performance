import os
import django
from datetime import datetime
import pytz

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

import requests
from apps.models import Location, Unit, WebSales, MusicEvent

URL = "https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=1"

def parse_date(date_str):
    if date_str:
        for fmt in ("%Y/%m/%d %H:%M:%S", "%Y/%m/%d"):
            try:
                return pytz.timezone("Asia/Taipei").localize(datetime.strptime(date_str, fmt))
            except ValueError:
                continue
        return None

def data():
    resp = requests.get(URL)
    data = resp.json()
    
    for item in data:
        try:
            location = None
            show_info_list = item.get("showInfo", [])
            
            for show_info in show_info_list:
                location_name = show_info.get("locationName")
                latitude = show_info.get("latitude")
                longitude = show_info.get("longitude")
                
                if location_name and latitude and longitude:
                    location, _ = Location.objects.get_or_create(
                        name=location_name,
                        latitude=latitude,
                        longitude=longitude,
                    )
                
                show_unit, _ = Unit.objects.get_or_create(name=item.get("showUnit", ""))
                master_unit, _ = Unit.objects.get_or_create(name=item.get("masterUnit", ""))
                sub_unit, _ = Unit.objects.get_or_create(name=item.get("subUnit", "")) if item.get("subUnit") else (None, False)
                support_unit, _ = Unit.objects.get_or_create(name=item.get("supportUnit", "")) if item.get("supportUnit") else (None, False)
                other_unit, _ = Unit.objects.get_or_create(name=item.get("otherUnit", "")) if item.get("otherUnit") else (None, False)
                web_sales, _ = WebSales.objects.get_or_create(url=item.get("webSales", ""))

                if not MusicEvent.objects.filter(uid=item.get("UID")).exists():
                    event = MusicEvent(
                        version=item.get("version", ""),
                        uid=item.get("UID", ""),
                        title=item.get("title", ""),
                        category=item.get("category", ""),
                        show_unit=show_unit,
                        description_filter_html=item.get("descriptionFilterHtml", ""),
                        discount_info=item.get("discountInfo", ""),
                        image_url=item.get("imageURL", ""),
                        master_unit=master_unit,
                        sub_unit=sub_unit,
                        support_unit=support_unit,
                        other_unit=other_unit,
                        web_sales=web_sales,
                        source_web_promote=item.get("sourceWebPromote"),
                        comment=item.get("comment"),
                        edit_modify_date=parse_date(item.get("editModifyDate")) or datetime.now(pytz.timezone("Asia/Taipei")),
                        source_web_name=item.get("sourceWebName", ""),
                        start_date=parse_date(item.get("startDate")),
                        end_date=parse_date(item.get("endDate")),
                        hit_rate=int(item.get("hitRate", 0)),
                        show_info=show_info,
                        time=parse_date(show_info.get("time")),
                        location=location,
                        on_sales=show_info.get("onSales") == "Y",
                        price=show_info.get("price", ""),
                        end_time=parse_date(show_info.get("endTime")),
                    )
                    event.save()
        except Exception as e:
            print(f"Error {item.get('UID')}: {e}")

if __name__ == "__main__":
    data()