# -*- coding: utf-8 -*-
################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies (<https://www.cybrosys.com>)
#    Author: Jumana Jabin MP (odoo@cybrosys.com)
#
#    This program is free software: you can modify
#    it under the terms of the GNU Affero General Public License (AGPL) as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
################################################################################
from odoo import api, fields, models


class SalePack(models.Model):
    """Model for extending the sale order to include a selection of packs."""
    _inherit = 'sale.order'

    product_pack_id = fields.Many2one('product.product', string='Select Pack',
                                      domain=[('is_pack', '=', True)],
                                      required=True,
                                      help='The selected pack product for'
                                           ' the sale order.')

    @api.onchange('product_pack_id')
    def onchange_product_pack_id(self):
        """Perform actions when the selected pack product changes."""
        if self.product_pack_id:
            self.order_line = [(0, 0, {
                'product_id': self.product_pack_id.id,
                'name': self.product_pack_id.name,
                'product_uom_qty': 1,
                'price_unit': self.product_pack_id.list_price,
            })]
        elif not self.product_pack_id:
            self.order_line = [(5, 0, 0)]

    def action_confirm(self):
        """Override the action_confirm method to create stock moves
        for pack products."""
        super(SalePack, self).action_confirm()
        for line in self.order_line:
            if line.product_id.is_pack:
                for record in line.product_id.pack_products_ids:
                    for rec in self.picking_ids:
                        move = rec.move_ids.create({
                            'name': record.product_id.name,
                            'product_id': record.product_id.id,
                            'product_uom_qty': record.quantity * line.product_uom_qty,
                            'product_uom': record.product_id.uom_id.id,
                            'picking_id': rec.id,
                            'location_id': rec.location_id.id,
                            'location_dest_id': rec.location_dest_id.id,
                        })
                        move._action_confirm()
