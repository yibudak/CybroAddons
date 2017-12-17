{
    'name': "Pharmacy Management",
    'summary': """ Some Basics For Field of Medicine """,
    'description': """    """,
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'license': 'AGPL-3',
    'category': 'Medicine',
    'version': '8.0.1.0',
    'depends': ["base",
                "sale",
                "purchase",
                "stock",
                "mrp",
                "mrp_operations",
                "product_expiry",
                "account_accountant"],
    'data': ['views/pharmacy_mgt_view.xml',
             'views/medicines_view.xml',
             'route_manage/route_manage_view.xml',
             'route_manage/report.xml', 'new_names.xml',
             'expiry_manage/expiry_manage_view.xml',
             ],
    'demo': ['demo/demo.xml'],
    'images': ['static/description/banner.jpg'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
