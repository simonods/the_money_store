from .owner_info import *

menu = [
    {'title': 'Main Page', 'url_name': 'main_page'},
    {'title': 'News', 'url_name': 'news'},
    {'title': 'Marketplace', 'url_name': 'market'},
    {'title': 'Currency', 'url_name': 'currency'},
    {'title': 'About Us', 'url_name': 'about_us'},
    {'title': 'Contact', 'url_name': 'contact'},
    {'title': 'NFT Uranus', 'url_name': 'nft_uranus'},

]


def get_data_context(**kwargs):
    context = kwargs
    context['menu'] = menu
    context['company_name'] = company_name
    return context


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        context['company_name'] = company_name
        return context

    # def get_data_context(self, **kwargs):
    #     context = kwargs
    #     context['menu'] = menu
    #     context['company_name'] = company_name
    #     return context
