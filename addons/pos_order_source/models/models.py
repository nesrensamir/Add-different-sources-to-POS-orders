# -*- coding: utf-8 -*-

import string
from odoo import models ,fields ,api

class Source (models.Model):
    _name= "source" 
    sources= fields.Char('Sources', default="phone"); 


class OrderSource (models.Model): 
  
    _inherit = "pos.order" 
    source_id = fields.Many2one("source",string="Source") 
     