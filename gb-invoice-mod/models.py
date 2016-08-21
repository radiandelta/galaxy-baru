# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.tools import amount_to_text_en

class res_company(models.Model):
	_inherit="res.company"
	logo_report=fields.Binary("Header Image", help="This field holds the image used for the logo on the prints, limited to 1024x1024px")
	
class account_invoice_extension(models.Model):
	_inherit = "account.invoice"
	
	

