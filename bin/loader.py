# -*- coding: utf-8 -*-

import yaml

Mob_Regex=r'(?:(?:\+?([1-9]|[0-9][0-9]|[0-9][0-9][0-9])\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([0-9][1-9]|[0-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?'
Mob_Regex2=r'\(?(\d{3})?\)?[\s\.-]{0,2}?(\d{3})[\s\.-]{0,2}(\d{4})'

Email_Regex=r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'
Email_Regex2=r'([^@|\s]+@[^@]+\.com)'
Email_Regex3=r'\S+@\S+'

linurl_Regex=r'linkedin\.com\/in\/[a-z]+\-[a-z0-9]+'


def load_conf(conf_path='./config/config.yaml'):
    config=yaml.load(open(conf_path))
    return config


    
    
