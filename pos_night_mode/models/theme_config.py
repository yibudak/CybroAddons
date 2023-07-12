# -*- coding: utf-8 -*-
################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Ramees Jaman KT (odoo@cybrosys.com)
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


class Users(models.Model):
    _inherit = 'res.users'

    """ Theme Config for night mode """
    mode_check = fields.Boolean(string="Active", help="Enable / Disable checkbox")

    @api.model
    def get_active(self):
        return self.env['res.users'].search([('id', '=', self.env.user.id)]).mode_check

    @api.model
    def set_active(self):
        self.env['res.users'].search([('id', '=', self.env.user.id)]).write({'mode_check': True})
        return self.env['res.users'].search([('id', '=', self.env.user.id)]).mode_check

    @api.model
    def set_deactivate(self):
        self.env['res.users'].search([('id', '=', self.env.user.id)]).write({'mode_check': False})
        return self.env['res.users'].search([('id', '=', self.env.user.id)]).mode_check
