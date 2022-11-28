import datetime

from odoo import models, fields,_
import openpyxl
import base64
from io import BytesIO
from odoo.exceptions import UserError
class ImportCustomerWizard(models.TransientModel):
   _name = "price.import"
   file = fields.Binary(string="File", required=True)

   def import_sale(self):
      try:      
         wb = openpyxl.load_workbook(filename=BytesIO(base64.b64decode(self.file)), read_only=True)
         ws = wb.active

         for record in ws.iter_rows(min_row=2, max_row=None, min_col=None, max_col=None, values_only=True):
               old_price={
                  'product_id':self.env['product.product'].search([('name','=',record[4])]).id,
                  'new_price':record[6],
                  'old_price':record[5],
               }
               od=self.env['product.price.change.line'].sudo().create(old_price)
               price_data={
            'name':record[0],
            'date':record[1],
            'warehouse_id':self.env['stock.warehouse'].search([
                	('name', '=', record[2])]).id,
            'location_id':self.env['stock.location'].search([
                	('name', '=', record[3])]).id,
            'line_ids':od,
                  }
               self.env['product.price.change'].sudo().create(price_data)
      except:
         raise UserError(_('Please insert a valid file'))