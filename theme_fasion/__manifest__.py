# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
{
    'name': 'Theme Fashion',
    'description': 'Design Web Pages with theme Fashion',
    'summary': 'Theme Fashion',
    'category': 'Theme/eCommerce',
    'version': '16.0.1.0.0',
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com",
    'depends': ['website_sale_wishlist'],
    'data': [
        'views/website_snipppet.xml',
        'views/layout.xml',
        'views/product/product.xml',
        'views/product/blog.xml',
        'views/preview/preview.xml',
        'views/banner/banner.xml',
        'views/slider/slider.xml',
        'views/slider/sliders.xml',
        'views/cart/cart.xml',
        'views/contact/contact.xml',
        'views/about/about.xml',
        'views/template.xml',
        'views/product_views.xml',
    ],
    'images': [
        'static/description/banner.png',
        'static/description/theme_screenshot.jpg',
    ],
    'assets': {
        'web.assets_frontend': [
            'theme_fasion/static/src/css/style.css',
            'theme_fasion/static/src/js/custom.js',
            'theme_fasion/static/src/js/jquery.flexisel.js',
            'theme_fasion/static/src/js/owl.carousel.js',
            'theme_fasion/static/src/css/stylenav.css',
        ],
    },
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
