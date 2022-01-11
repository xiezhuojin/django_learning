## UnorderedObjectListWarning(RuntimeWarning)

## InvalidPage(Exception)

## PageNotAnInteger(InvalidPage)

## EmptyPage(InvalidPage)

## Paginator
> [ELLIPSIS] ``` = django.utils.translation.gettext_lazy("…")
* string used to replace omitted page numbers in elided page.

> [\__init__] setup [object_list], [per_page], [orphans], [allow_empty_first_page], and check [object_list] is ordered, 

> [\__iter__]
* yield ```page```.

> [validate_number] raise error based on given ```number```
* validate the given 1-based page number.

> [get_page] basically return [page(```number```)]
* return a valid, even if the page argument isn't a number or isn't in range.

> [page]
* return a page object for the given 1-based page number.

> [\_get_page] basically return ```Page(*args, **kwargs)```
* return an instance of a single page.

> [count]
* return the total number of objects, accross all pages.

> [num_pages]
* return the total number of pages.

> [page_range] (property)
* return a 1-based of pages for iterating through within a template for loop.

> [\_check_object_list_ordered]
* warn if [object_list] is unordered (typically a QuerySet)

> [get_elided_page_range]
* return a 1-based range of pages with some values elided.
* if the page range is larger than a given size, the whole range is provided an compact form is returned instead, e.g. for a paginator with 50 pages. If page 43 were the current page, the output, with default arguments, would be:
    1, 2, …, 40, 41, 42, 43, 44, 45, 46, …, 49, 50

## Page(collections.abc.Sequence)
> [\__init__] setup [object_list], [number], [paginator]

> [\__repr__] ```"<Page %s of %s>"```

> [\__len__]
* length of [object_list]

> [\__getitem__]
* convert [object_list] as needed, and get the ```index``` of it.

> [has_next]
* return [number] < [paginator.num_pages]

> [has_previous]
* return [number] > 1

> [has_other_pages]
* return [has_previous()] or [has_next()]

> [next_page_number]
* return [paginator.validate_number([number] + 1)]

> [previous_page_number]
* return [paginator.validate_number([number] - 1)]

> [start_index]
* return the 1-based index of the first object on this page, relative to total objects in the paginator.

> [end_index]
* return the 1-based index of the last object on thie page, relative to total objects found (hits).
