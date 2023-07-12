# -*- coding: utf-8 -*-
################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Cybrosys Technologies(<https://www.cybrosys.com>)
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
################################################################################
from odoo import api, fields, models


class StockPicking(models.Model):
    """
    This class is created for inherited model Stock Picking.

    Methods:
        action_force_availability(self):
            Function for make quantity done.It also changes state in to assigned.

        _compute_show_qty_button(self):
            This function will super the compute function of a boolean field
             that related to set quantity button.It will avoid showing force
            availability button and set quantity button at the same time.

    """
    _inherit = 'stock.picking'

    is_available = fields.Boolean('Make Available', default=False,
                                  help='The Force Availability button will show based on this field.')

    def action_force_availability(self):
        """Function for make quantity done."""

        for lines in self.move_ids:
            lines.quantity_done = lines.product_uom_qty
        self.is_available = True
        self.state = 'assigned'

    @api.depends('show_validate', 'immediate_transfer',
                 'move_ids.reserved_availability',
                 'move_ids.quantity_done')
    def _compute_show_qty_button(self):
        """This function will super the compute function of a boolean field
        that related to set quantity button.It will avoid showing force
        availability button and set quantity button at the same time."""

        res = super(StockPicking, self)._compute_show_qty_button()
        if self.products_availability_state == 'late':
            self.show_set_qty_button = False
        return res
