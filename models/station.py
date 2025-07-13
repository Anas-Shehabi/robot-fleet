from odoo import models, fields

class Station(models.Model):
    _name = 'station'
    _description = 'Robot Station'
    active = fields.Boolean(default=True)


    name = fields.Char(string='Station Name', required=True)

    station_type = fields.Selection([
        ('laboratory', 'Laboratory'),
        ('storage', 'Storage'),
        ('charging', 'Charging Station'),
        ('assembly', 'Assembly Station'),
        ('maintenance', 'Maintenance Bay'),
        ('shipping', 'Shipping Dock')
    ], string='Station Type')