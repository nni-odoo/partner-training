from odoo import api, fields, models
from odoo.exceptions import UserError


class Book(models.Model):
    _name = "library.book"

    name = fields.Char("Title")
    isbn = fields.Char("ISBN")
    copies = fields.Integer("Number of Copies")
    remaining = fields.Integer("Remaining Copies", compute="_compute_remaining", store=True)

    @api.depends('copies')
    def _compute_remaining(self):
        # copies - rentals that refer to this book
        for record in self:
            total_rentals = self.env['library.rental'].search_count([('book', '=', record.id)])
            record.remaining = record.copies - total_rentals


class Customer(models.Model):
    _name = "library.customer"

    name = fields.Char("Name")
    mobile = fields.Char("Mobile Phone Number")
    address = fields.Text("Address")

class Rental(models.Model):
    _name = "library.rental"

    book = fields.Many2one("library.book", "Book")
    customer = fields.Many2one("library.customer", "Customer")
    rent_date = fields.Date("Rental Date")
    end_date = fields.Date("Return Date")

    @api.onchange('end_date')
    def _onchange_end_date(self):
        # can't allow end date set before rent_date
        if self.rent_date and self.end_date < self.rent_date:
            raise UserError("WARNING: You shouldn't set the Return Date to be Earlier than Rent Date")
