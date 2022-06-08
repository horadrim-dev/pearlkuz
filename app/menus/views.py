# from webbrowser import get
# from asyncio.windows_events import NULL
from django.shortcuts import render
from django.http import Http404 # JsonResponse
from . models import Menu
from site_settings.models import Section
from content import views as content_views

def get_menu_if_exists(slug=None):
    if slug:
        try:
            obj = Menu.objects.get(alias=slug)
        except Exception:
            return False

        return obj


def menus(request, *args, **kwargs):

    slugs = list(kwargs.values())
    try:
        current_menu = Menu.objects.filter(alias=slugs.pop(0)).get()
    except Exception:
        raise Http404('Раздел не найден')
    unknown_slugs = []
    bc_items = [(current_menu.title, current_menu.alias)]

    # перебираем кварги пока не наткнемся на несуществующий в меню
    # все кварги-меню заносим в breadcrumbs
    # все неизвестные кварги передаем дальше в контент
    if len(slugs) > 0:
        # urlpath = list(kwargs.values())

        for i, slug in enumerate(slugs):
            obj = get_menu_if_exists(slug)
            if obj:
                current_menu = obj
                bc_items.append((current_menu.title, slug))
            else:
                unknown_slugs += slugs[i:]
                break


    menus = Menu.objects.filter(parent_id=current_menu.id)

    sections = [
        {
            'obj': section, 'columns': [
                {
                    'obj': column, 'modules':[
                        module for module in column.module_set.on_page(current_menu)
                    ]
                } for column in section.column_set.on_page(current_menu)
            ]
        } for section in Section.objects.on_page(current_menu)
    ]

    context = {
        # 'data': 'normal',
        'bc_items': bc_items,
        'page': current_menu,
        'menus': menus,
        'sections': sections
    }
    # if request.GET.get('data') == 'component':
    #     context['data'] = 'component'
    #     return render(request, 'menus/menus.html', context)
    # else:
        # return render(request, 'menus/block_menus.html', context)
    return content_views.render_content(request, context, unknown_slugs)

def sitemap(request, *args, **kwargs):
    context = {}
    context['menu_tree'] = Menu.get_subitems(parent=None, maxlevel=None)
    context['bc_items'] = [('Карта сайта', 'sitemap')]
    return render(request, 'menus/sitemap.html', context)