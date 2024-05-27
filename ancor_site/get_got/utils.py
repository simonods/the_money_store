menu = [
    {'title': 'Main Page', 'url_name': 'main_page'},
    {'title': 'News', 'url_name': 'news'},
    {'title': 'Currence', 'url_name': 'currency'},
    {'title': 'About Us', 'url_name': 'about_us'},
    {'title': 'Contact', 'url_name': 'contact'},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context
