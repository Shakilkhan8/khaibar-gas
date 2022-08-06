# See LICENSE file for full copyright and licensing details.
"""Transient Model for Set Received date on once click."""

from odoo import _, fields, models
from odoo.exceptions import UserError


class WizSetShippingDate(models.TransientModel):
    """Wizard Transient model."""

    _name = "wiz.set.shipping.date"
    _description = "Wizard set Received Date"

    date = fields.Date(string="Date")
    ship_type = fields.Selection(
        [("recived", "Received"), ("delivered", "Delivered")],
        string="Shipping Type",
        default="recived",
    )
    operation_ids = fields.Many2many(
        "freight.operation",
        "freight_wizrec_rel",
        "operation_id",
        "wiz_id",
        string="Shipping Operations",
    )

    def action_set_date(self):
        """Set Date on shipping Operation."""
        self.ensure_one()
        for operation in self.operation_ids:
            if self.ship_type == "recived":
                if operation.direction == "import":
                    operation.write(
                        {"act_rec_date": self.date or False, "state": "recived"}
                    )
                else:
                    raise UserError(
                        _("Shipping Order %s is export you can't " "set received date.")
                        % operation.name
                    )
            elif self.ship_type == "delivered":
                if operation.direction == "export":
                    operation.write(
                        {"act_send_date": self.date or False, "state": "delivered"}
                    )
                else:
                    raise UserError(
                        _(
                            "Shipping Order %s is import you can't "
                            "set delivered date."
                        )
                        % operation.name
                    )
            containers = operation.operation_line_ids.mapped("container_id")
            if containers:
                containers.write({"state": "available"})
