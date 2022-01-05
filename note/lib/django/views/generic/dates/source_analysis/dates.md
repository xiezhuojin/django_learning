## YearMixin
* mixin for views manipulating year-base data.
> [year_format] ``` = %Y```
> [year] ``` = None```

> [get_year_format]
* get a year format string in strptime syntax to be used to parse the year from url variables.

> [get_year]
* return the year for which this view should display data.

> [get_next_year]
* get the next valid year.

> [get_previous_year]
* get the previous valid year.

> [\_get_next_year]
* return the start date of the next interval.

> [\_get_current_year]
* return the start date of the current interval.

## MonthMixin
* mixin for views manipulating month-based data.
> [month_format] ``` = "%b"```
> [month] = ```None```

> [get_month_format]
* get a month format string in strptime syntax to be used to parse the month from url variables.

> [get_month]
* return the month for which this view should display data.

> [get_next_month]
* get the next valid month.

> [get_previous_month]
* get the previous valid month.

> [\_get_next_month]
* return the start date of the next interval.

> [\_get_current_month]
* return the start date of the previous interval.

## DayMixin
* mixin for views manipulating day-based data.
> [day_format] ``` = "%d"```
> [day] ``` = None```

> [get_day_format]
* get a day format string in strptime syntax to be used to parse day from url variables.

> [get_day]
* return the day for which this view should be display data.

> [get_next_day]
* get the next valid day.

> [get_previous_day]
* get the previous valid day.

> [\_get_next_day]
* return the start date of the next interval.

> [\_get_current_day]
* return the start date of the current interval.

## WeekMixin
* mixin for views manipulating week-based data.
> [week_format] ``` = "%U"```
> [week] ``` = None```

> [get_week_format]
* get a week format string in strptime syntax to be used to parse the week from url variables.

> [get_week]
* return the week for which this view should display data.

> [get_next_week]
* get the next valid week.

> [get_previous_week]
* get the previous valid week.

> [\_get_next_week]
* return the start date of the next interval.

> [\_get_current_week]
* return the start date of the current interval.

> [\_get_weekday]
* return the weekday for a given date.

## DateMixin
* mixin class for views manipulating date-based data.
> [date_field] ``` = None```
> [allow_future] ``` = False```

> [get_date_field]
* get the name of the date field to be used to filter by.

> [get_allow_future]
* return ```True``` if the view should be allowed to display object from the future.

> [uses_datetime_field]
* return ```True``` if the date field is a ```DateTimeField``` and ```False``` if it's a ```DateField```

> [\_make_date_lookup_arg]
* convert a date into a datetime when the date field is a DateTimeField.

> [\_make_single_date_lookup]
* get the lookup kwargs for filtering on a single date.

## BaseDateListView(django.views.generic.list.MultipleObjectMixin, DateMixin, django.views.generic.base.View)
* abstract base class for date-based views displaying a list of object.
> [allow_empty] ``` = False```
> [data_list_period] ``` = "year"```

> [get] get [date_list], [object_list], [extra_context] from [get_dated_items], then put them into context, render.

> [get_dated_items]
* obtain the list of dates and items.
* Not implemented!!

> [get_ordering]
* return the field or fields to use for ordering the queryset; use the date field by default.

> [get_dated_queryset]
* get a queryset properly filtered according to ```allow_future``` and any extra lookup kwargs.

> [get_date_list_period]
* get the aggregation period for the list of dates: "year", "month", or "day".

> [get_date_list]
* get a date list by calling ```queryset.dates/datetimes()```, checking along the way for empty lists that aren't allowed.

## BaseArchiveIndexView(BaseDateListView)
> [context_object_name] ``` = "latest"```

> [get_dated_items]
* return the ```(date_list, items, extra_context)``` for this requests.

## ArchiveIndexView(django.views.generic.list.MultipleObjectTemplateResponseMixin, BaseArchiveIndexView)
* top-level archive of date-based items.
> [template_name_suffix] ``` = "_archive"```

## BaseYearArchiveView(YearMixin, BaseDateListView)
* list of objects published in a given year.
> [date_list_period] ``` = "month"```
> [make_object_list] ``` = False```

> [get_dated_items]
* return ```(date_list, items, extra_context)``` for this request.

> [get_make_object_list]
* return ```True``` if this view should contain the full list of objects in the given year.

## YearArchiveView(django.views.generic.list.MultipleObjectTemplateResponseMixin, BaseYearArchiveView)
* list of objects published in a given year.
> [template_name_suffix] ``` = "_archive_year"```

## BaseMonthArchiveView(YearMixin, MonthMixin, BaseDateListView)
* list of objects published in a given month.
> [date_list_period] ``` = "day"```

> [get_dated_items]
* return ```(date_list, items, extra_context)``` for this request.

## MonthArchiveView(django.views.generic.list.MultipleObjectTemplateResponseMixin, BaseMonthArchiveView)
* list of objects published in a given month.
> [template_name_suffix] ``` = "_archive_month"```

## BaseWeekArchiveView(YearMixin, WeekMixin, BaseDateListView)
* list of objects published in a given week.
> [get_dated_items]
* return ```(date_list, items, extra_context)``` for this request.

## WeekArchiveView(django.views.generic.list.MultipleObjectTemplateResponseMixin， BaseWeekArchiveView)
* list of objects published in a given week.
> [template_name_suffix] ``` = "_archive_week"```

## BaseDayArchiveView(YearMixin, MonthMixin, DayMixin, BaseDateListView)
* list of objects published on a given day.
> [get_dated_items] basically call [\_get_dated_items]
* return ```(date_list, items, extra_context)```

> [\_get_dated_items]
* do the actual heavy lifting

## DayArchiveView(django.views.generic.list.MultipleObjectTemplateResponseMixin, BaseDayArchiveView)
* list of objects published on a given day.
> [template_name_suffix] ``` = "_archive_day"```

## BaseTodayArchiveView(BaseDayArchiveView)
* list of objects published today.
> [get_dated_items]
* return ```(date_list, items, extra_context)``` for this request.

## TodayArchiveView(django.views.generic.list.MultipleObjectTemplateResponseMixin, BaseTodayArchiveView)
* list of objects published today
> [template_name_suffix] ``` = "_archive_day"```

## BaseDateDetailView(YearMixin, MonthMixin, DayMixin, DateMixin, BaseDetailView)
* detail view of a single object on a single date: this differs from the standard DetailView by accepting a year/month/day in the URL.
> [get_object]
* get the object this request displays.

## DateDetailView(django.views.generic.detail.SingleObjectTemplateResponseMixin, BaseDateDetailView)
* detail view of a single object on a single date; this differs from the standard ```DetailView``` by accepting a year/month/day in the URL.
> [template_name_suffix] ``` = "_detail"```

## _date_from_string
* get a datetime.date object given a format string and a year, month, and day (only year is mandatory). Raise a 404 for an invalid date.
## _get_next_prev
* get the next or the previous valid date. The idea is to allow links on month/day views to never by 404s by never providing a date that'll be invalid for the given view.

## timezone_today
* return the current day in the current time zone.
