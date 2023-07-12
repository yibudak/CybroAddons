# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions (<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
from odoo import api, models


class AccountMove(models.Model):
    """
    Inherits from account.move to add functionality for automatically adding
    the terms and conditions of a customer's country to the narration field of
    an invoice.
    """
    _inherit = "account.move"

    @api.depends('move_type', 'partner_id', 'company_id')
    def _compute_narration(self):
        """Compute the narration field for the invoice."""
        terms_condition = self.partner_id.country_id.sale_terms_condition
        if terms_condition:
            self.narration = terms_condition
        else:
            res = super(AccountMove, self)._compute_narration()
            return res
