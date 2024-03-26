menu = [{'title': "About page", 'url_name': 'about'},
        {'title': "Add Post", 'url_name': 'add_page'},
        {'title': "Feedback", 'url_name': 'contact'},
        {'title': "Login", 'url_name': 'login'},
        ]

class DataMixin:
    paginate_by = 3
    title_page = None
    cat_selected = None
    extra_context = {}

    def __init__(self):
        if self.extra_context:
            self.extra_context['title'] = self.title_page

        if self.cat_selected is not None:
            self.extra_context['cat_selected'] = self.cat_selected
        
        if 'menu' not in self.extra_context:
            self.extra_context['menu'] = menu

    def get_mixin_content(self, context, **kwargs):
        context['menu'] = menu
        context['cat_selected'] = None
        context.update(kwargs)
        return context