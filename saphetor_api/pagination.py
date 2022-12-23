from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def paginate(object_list, page=1, limit=2, **kwargs):
    min_limit = 1
    max_limit = 50000
    
    try:
        page = int(page)
        if page < 1:
            page = 1
    except (TypeError, ValueError):
        page = 1
    try:
        limit = int(limit)
        if limit < min_limit:
            limit = min_limit
        if limit > max_limit:
            limit = max_limit
    except (ValueError, TypeError):
        limit = max_limit
    paginator = Paginator(object_list, limit)
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)
    data = {
        'previous_page': objects.has_previous() and objects.previous_page_number() or None,
        'next_page': objects.has_next() and objects.next_page_number() or None,
        'data': list(objects)
    }
    return data