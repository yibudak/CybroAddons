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


class PurchaseOrder(models.Model):
    """
       Model representing a purchase order.
       This class extends the 'purchase.order' model and adds additional
        functionality specific to purchase orders.
       """
    _inherit = 'purchase.order'

    @api.model
    def get_pending_tasks(self, order_id):
        """
        Retrieve purchase order based on a specific order ID.
        :param order_id: The ID of the purchase order to retrieve.
        :return: A dictionary representing an action to open the purchase order.
        """
        return {
            'name': "Purchase Order",
            'type': "ir.actions.act_window",
            'res_model': 'purchase.order',
            'domain': [('id', '=', order_id)],
            'view_mode': "tree,form",
            'views': [[False, "tree"], [False, "form"]],
            'target': 'main',
        }
