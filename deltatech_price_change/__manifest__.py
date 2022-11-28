# ©  2021 Deltatech
#              Dorin Hongu <dhongu(@)gmail(.)com
# See README.rst file on addons root folder for license details


{
    "name": "Price Change",
    "summary": "Price Change",
    "version": "15.0.1.0.0",
    "author": "Terrabit, Dorin Hongu",
    "website": "https://www.terrabit.ro",
    "category": "Generic Modules",
    "depends": ["base", "stock", "product", "sale"],
    "license": "LGPL-3",
    "data": [
        "views/product_view.xml",
        "wizard/import_code.xml",
        "views/product_price_change_view.xml",
        # "views/purchase_report.xml",
        "views/price_change_report.xml",
        "views/report_pricechange.xml",
        "views/upl.xml",
        "security/ir.model.access.csv",
    ],
    "images": ["images/main_screenshot.png"],
    "installable": True,
    "development_status": "Production/Stable",
    "maintainers": ["dhongu"],
    'assets': {
   'web.assets_backend': [
       'deltatech_price_change/static/src/js/tree_button.js',
   ],
   'web.assets_qweb': [
       'deltatech_price_change/static/src/xml/upload.xml',
       
   ],
},
}
