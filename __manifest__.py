# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'IdeaCode Theme',
    'description': 'IdeaCode website theme',
    'category': 'Theme',
    'sequence': 1000,
    'version': '1.0',
    'depends': ['website'],
    'images': [],
    'snippet_lists': {},
    'license': 'LGPL-3',
    'data': [
        'views/header.xml',
        'views/footer.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            'theme_ideacode/static/src/scss/*.scss',
        ],
        'web.assets_frontend': [
            'theme_ideacode/static/src/scss/styles.scss',
        ],
    }

}
