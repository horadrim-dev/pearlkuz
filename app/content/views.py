from django.shortcuts import render
from django.http import FileResponse, Http404
from django.conf import settings
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from toml import TomlDecodeError
from .models import ContentBase, Post, Feed, Attachment
from grid.models import Module
from menus.models import Menu
import os
# from menus.models import Menu
# Create your views here.

def get_content_if_exists(slug=None):
    '''возвращает объект контента по slug'''
    if slug:
        for content_type in ContentBase.__subclasses__():
            # try:
                # return content_type.objects.get(alias=slug)
            obj = content_type.objects.published().filter(alias=slug)
            if len(obj) > 1:
                raise Http404('Получено несколько объектов с одинаковым alias')
            elif len(obj) == 1:
                return obj[0]
            # except:
            #     continue

        return False

def get_extracontent(menu:Menu=None, module:Module=None):
    ''' Возвращает экстраконтент, привязанный к меню или модулям'''
    # todo: Переделать в get_extracontent 
    if module:
        return module.modulecontent_set.all()

    if menu:
        contents = {}
        # contents['content'] = [menu]

        for content in menu.extracontent_set.all():
            if content.position not in contents:
                contents[content.position] = [content]
            else:
                contents[content.position].append(content)

    # has_content = False
    # contents = {}
    # contents['posts'] = []
    # contents['postfeeds'] = []
    # contents['menus'] = []
    # if from_menu_id:
    #     posts = Post.objects.published().filter(menu_id=from_menu_id) # собираем посты
    #     feeds = Feed.objects.published().filter(menu__id=from_menu_id) # собираем ленты
    #     menus = None
    # elif from_slug: # контент на абстрактных страницах
    #     posts =  Post.objects.published().filter(alias=from_slug)
    #     feeds = None
    #     menus = None
    # elif module:
        # posts = Post.objects.published().filter(id=module.post_content_id)
        # feeds = Feed.objects.published().filter(id=module.feed_content_id)
        # # menus = Menu.objects.published().filter(id=module.menu_content_id)
        # posts = []
        # feeds = None
        # menus = []
        # assert False, (module, Menu.objects.published)
        # assert False, (module, module.modulecontent_set.all())
    # post_ids = posts.values_list('id', flat=True)
    # attachments = Attachment.objects.filter(post__in=post_ids)#[x.attachment_set.all() for x in contents['posts']]
    # for post in posts:
    #     contents['posts'].append({
    #         'post' : post,
    #         'attachments': post.get_attachments()
    #     })

    # if menus:
    #     for menu in menus:
    #         contents['menus'].append({
    #             'parent': menu,
    #             'subitems': menu.get_subitems()
    #         })

    # if feeds:
    #     for feed in feeds:
    #         contents['postfeeds'].append({
    #             'feed': feed,
    #             'posts': feed.get_page(page=1),
    #         })

    # собираем информацию
    # num_total = 0
    # info = {'count':{}}
    # for key, content  in contents.items():
    #     if len(content) > 0:
    #         has_content = True
    #         num_total += len(content)
    #         info['count'].update({key: len(content)})

    # info['count']['total'] = num_total

    # contents['info'] = info

    return contents
    # if has_content:
    #     return contents
    # else:
    #     return False

def render_content(request, context, unknown_slugs=None):
    if unknown_slugs:
        # Если есть slug-и "не меню" то проверяем их и передаем на обработку
        # разным функциям (зависит от контент-типа текущего меню)
        unknown_objects = []
        for slug in unknown_slugs:
            obj = get_content_if_exists(slug)
            ### Здесь должна быть проверка на родство [slugs между собой]
            ### и [первого slug с последним меню]
            if obj:
                unknown_objects.append(obj)
                context['bc_items'].append((obj.title, slug))
            else:
                raise Http404('Контент не найден')
                
        # context['page'] = content
        # context['contents'] = get_content(slug=slug)
        if context['page'].content_type == 'feed':
            # ПРОДУМАТЬ НАСЛЕДОВАНИИЕ ЛЕНТ
            if len(unknown_objects) == 1 :
                if (unknown_objects[0].__class__.__name__ == 'Post'):

                    post = unknown_objects[0]

                    if post.feed != context['page'].content_feed:
                        raise Http404('Проверка на родство ленты и поста не пройдена')

                    CONTENT_HTML = render_to_string(
                        'content/layout_post.html', 
                        {
                            'uid': 'CONTENT_123', # ПРОДУМАТЬ UID
                            'post' : post, 
                            'attachments': post.get_attachments()
                        }
                    )
                else:
                    raise Http404('Для меню-ленты unknown_slug!=Post не предусмотрен.')
            else:
                raise Http404('Получено '+len(unknown_objects)+' unknown_slugs, не предусмотрено')
        elif context['page'].content_type == 'post':
            raise Http404('Не продумано.(unknown_slug после меню-поста)')
        elif context['page'].content_type == 'menu':
            raise Http404('Не продумано.(unknown_slug после меню-"меню")')
    else:
        CONTENT_HTML = render_to_string(
            'content/content_layout.html', 
            {'content' : context['page']}
        )


    context['CONTENT_HTML'] = CONTENT_HTML
    context['contents'] = get_extracontent(menu=context['page'])

    for section in context['sections']:
        for column in section['columns']:
            for module in column['modules']:
                module['contents'] = get_extracontent(module=module['obj'])


    return render(request, 'content/content.html', context)

# def render_module

def download_attachment(request, uuid, *args, **kwargs):
    # media_root = settings.MEDIA_ROOT
    try:
        attachment = Attachment.objects.get(uuid=uuid)
    except:
        raise Http404('Файл не найден.')

    if os.path.isfile(attachment.attached_file.path):
        attachment.hits += 1
        attachment.save()
        return FileResponse(
            open(attachment.attached_file.path, 'rb'),
            as_attachment=True,
            filename='{}.{}'.format(attachment.name[:100], attachment.extension)
        )
    else:
        raise Http404(
            'Файл "{}" в хранилище не найден.'.format(attachment.attached_file.path)
        )

def ajax_feed_page(request, slug, *args, **kwargs):
    # if not request.headers.get('x-requested-with') == 'XMLHttpRequest':
    #     raise Http404()

    context = {}
    try:
        feed = Feed.objects.published().get(alias=slug)
    except Exception:
        raise Http404('Лента не найдена')
    
    context['feed'] = feed

    if request.GET.get('items_per_page'):
        context['count_items'] = int(request.GET.get('items_per_page'))

    if request.GET.get('page'):
        if request.GET.get('items_per_page') :
            context['posts'] = feed.get_page(
                page=request.GET.get('page'), posts_per_page=context['count_items']
            )
        else:
            context['posts'] = feed.get_page(page=request.GET.get('page'))
    else:
        context['posts'] = feed.get_page()

    context['uid'] = request.GET.get('uid') # для использования в качестве уникального id в шаблоне
    context['layout'] = request.GET.get('layout')

    return render(request, 'content/layout_feed_list.html', context)

def ajax_post(request, *args, **kwargs):
    # if not request.headers.get('x-requested-with') == 'XMLHttpRequest':
    #     raise Http404()
    if not request.GET.get('post'):
        return Http404()

    context = {}
    try:
        post = Post.objects.published().get(alias=request.GET.get('post'))
    except Exception:
        raise Http404('Пост не найден')
    
    context['post'] = post
    context['attachments'] = post.get_attachments()

    return render(request, 'content/layout_post.html', context)