# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
from odoo import fields, models


class BlastConfiguration(models.Model):
    """contains fields to add needed values for snippets"""
    _name = 'blast.configuration'
    _description = 'Blast Configuration'

    name = fields.Char('Name')
    best_deal_id = fields.Many2one('product.product',
                                   help="Choose products to display as "
                                        "Best Deal product")
    date_start = fields.Datetime(string='Start Date',
                                 default=fields.Datetime.now(),
                                 help="Choose date to start the Deal")
    date_end = fields.Datetime(string='End Date',
                               help="Choose date to end the Deal")
    best_products_ids = fields.Many2many('product.product',
                                         help="Choose multiple products "
                                              "to display as Best Products")
    asked_questions_ids = fields.One2many('asked.questions',
                                          'blast_configuration_id',
                                          string="Questions And Answers")
