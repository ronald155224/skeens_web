from django import template
register = template.Library()

from core.models import Setting, SlideImage

@register.simple_tag
def get_setting(language_code=None):
    if not language_code:
        setting = Setting.objects.get(id='zh-hant')
        setting_img = SlideImage.objects.filter(setting=setting)
    else:
        setting = Setting.objects.get(id=language_code)
        setting_img = SlideImage.objects.filter(setting=setting)
    setting_dict = setting.__dict__
    setting_dict['slide_images'] = [img.image for img in setting_img]
    if setting.home_type1:
        setting_dict['home_type1'] = {
            'name': setting.home_type1.name_locale,
            'image': setting.home_type1.image,
            'description': setting.home_type1.description_locale
        }
    if setting.home_type2:
        setting_dict['home_type2'] = {
            'name': setting.home_type2.name_locale,
            'image': setting.home_type2.image,
            'description': setting.home_type2.description_locale
        }
    if setting.home_type3:
        setting_dict['home_type3'] = {
            'name': setting.home_type3.name_locale,
            'image': setting.home_type3.image,
            'description': setting.home_type3.description_locale
        }
    return setting_dict

@register.simple_tag
def get_setting_list():
    settings = Setting.objects.all()
    return [{"code": setting.id, "name_local": setting.language} for setting in settings]