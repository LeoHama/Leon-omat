{
    "name": "Compact Inventory Overview",
    "summary": "Smaller inventory overview cards without dashboard charts",
    "version": "19.0.1.0.1",
    "category": "Inventory/Inventory",
    "license": "LGPL-3",
    "depends": ["stock"],
    "data": ["views/stock_picking_type_views.xml"],
    "assets": {
        "web.assets_backend": [
            "stock_overview_compact/static/src/css/stock_overview_compact.css",
        ],
    },
    "installable": True,
    "application": False,
    "auto_install": False,
}
