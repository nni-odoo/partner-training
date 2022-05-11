from odoo import api, fields, models


class Book(models.Model):
    _name = "library.book"

    name = fields.Char("Title")
    isbn = fields.Char("ISBN")
    copies = fields.Integer("Number of Copies")


class Customer(models.Model):
    _name = "library.customer"

    name = fields.Char("Name")
    mobile = fields.Char("Mobile Phone Number")
    address = fields.Text("Address")
