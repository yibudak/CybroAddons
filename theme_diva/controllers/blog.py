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
from odoo import fields, http
from odoo.http import request


class WebsiteBlog(http.Controller):

    @http.route('/get_blog_post', auth="public", type='json',
                website=True)
    def get_blog_post(self):
        """This function is used to get blog post information"""
        posts = request.env['blog.post'].sudo().search(
            [('website_published', '=', True),
             ('post_date', '<=', fields.Datetime.now())],
            order='published_date desc', limit=3)
        values = {
            'posts_recent': posts.read(['name', 'published_date', 'blog_id', 'cover_properties']),
        }
        return values

    @http.route('/get_blog_posts', auth="public", type='json',
                website=True)
    def get_blog_posts(self):
        """This function is used to get blog post information"""
        posts = request.env['blog.post'].sudo().search(
            [('website_published', '=', True),
             ('post_date', '<=', fields.Datetime.now())],
            order='published_date desc', limit=4)
        values = {
            'posts_recent': posts.read(
                ['name', 'published_date', 'blog_id', 'cover_properties']),
        }
        return values
