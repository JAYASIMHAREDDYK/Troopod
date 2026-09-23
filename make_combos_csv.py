import csv
import json
import os

output_dir = r"u:\Internship\Troopod"

# Real store GIDs provided by user's admin list:
gids = {
    'kitchen': 'gid://shopify/Product/8483480961109',
    'tap': 'gid://shopify/Product/8483480862805',
    'copper': 'gid://shopify/Product/8483480993877',
    'wm_descaler': 'gid://shopify/Product/8483481026645',
    'dishwash': 'gid://shopify/Product/8483481059413',
    'floor': 'gid://shopify/Product/8483481092181',
    'toilet': 'gid://shopify/Product/8483481124949',
    'handwash': 'gid://shopify/Product/8483481157717',
    'laundry_det': 'gid://shopify/Product/8483481190485',
    'fabric_cond': 'gid://shopify/Product/8483481223253',
    'machine_powder': 'gid://shopify/Product/8483481256021',
    'eraser': 'gid://shopify/Product/8483481288789',
}

combos_data = [
    {
        'Handle': 'purelane-combo-kitchen-essentials',
        'Title': 'Kitchen essentials',
        'Body (HTML)': '<p>Includes: Foaming Kitchen Cleaner, Dishwash Gel &amp; Tap Cleaner. Everything for a sparkling kitchen, no need to pick separately.</p>',
        'Vendor': 'Purelane',
        'Product Category': '',
        'Type': 'Combo',
        'Tags': 'combo,kitchen,most-popular',
        'Published': 'TRUE',
        'Option1 Name': 'Size',
        'Option1 Value': 'Default',
        'Variant SKU': 'PUR-CMB-KIT',
        'Variant Grams': '1250',
        'Variant Inventory Tracker': 'shopify',
        'Variant Inventory Qty': '60',
        'Variant Inventory Policy': 'deny',
        'Variant Fulfillment Service': 'manual',
        'Variant Price': '499.00',
        'Variant Compare At Price': '897.00',
        'Variant Requires Shipping': 'TRUE',
        'Variant Taxable': 'TRUE',
        'Image Src': '',
        'Image Position': '',
        'Image Alt Text': '',
        'Gift Card': 'FALSE',
        'SEO Title': 'Kitchen essentials combo',
        'SEO Description': 'Kitchen cleaner, dishwash gel and tap cleaner combo.',
        'Status': 'active',
        'product.metafields.purelane.badge': 'Most popular',
        'product.metafields.purelane.rating': '4.7',
        'product.metafields.purelane.review_count': '64',
        'product.metafields.purelane.bundle_size': '3',
        'product.metafields.purelane.component_labels': json.dumps(['Foaming Kitchen Cleaner', 'Dishwash Gel', 'Tap Cleaner']),
        'product.metafields.purelane.components': f"{gids['kitchen']};{gids['dishwash']};{gids['tap']}"
    },
    {
        'Handle': 'purelane-combo-laundry-care-bundle',
        'Title': 'Laundry care bundle',
        'Body (HTML)': '<p>Includes: Laundry Detergent, Fabric Conditioner &amp; Machine Cleaner Powder. Softer, fresher wash, all in one box.</p>',
        'Vendor': 'Purelane',
        'Product Category': '',
        'Type': 'Combo',
        'Tags': 'combo,laundry',
        'Published': 'TRUE',
        'Option1 Name': 'Size',
        'Option1 Value': 'Default',
        'Variant SKU': 'PUR-CMB-LDY',
        'Variant Grams': '1350',
        'Variant Inventory Tracker': 'shopify',
        'Variant Inventory Qty': '50',
        'Variant Inventory Policy': 'deny',
        'Variant Fulfillment Service': 'manual',
        'Variant Price': '499.00',
        'Variant Compare At Price': '947.00',
        'Variant Requires Shipping': 'TRUE',
        'Variant Taxable': 'TRUE',
        'Image Src': '',
        'Image Position': '',
        'Image Alt Text': '',
        'Gift Card': 'FALSE',
        'SEO Title': 'Laundry care bundle',
        'SEO Description': 'Laundry detergent, fabric conditioner and machine cleaner powder combo.',
        'Status': 'active',
        'product.metafields.purelane.badge': '',
        'product.metafields.purelane.rating': '4.5',
        'product.metafields.purelane.review_count': '37',
        'product.metafields.purelane.bundle_size': '3',
        'product.metafields.purelane.component_labels': json.dumps(['Laundry Detergent', 'Fabric Conditioner', 'Machine Cleaner Powder']),
        'product.metafields.purelane.components': f"{gids['laundry_det']};{gids['fabric_cond']};{gids['machine_powder']}"
    },
    {
        'Handle': 'purelane-combo-complete-home-bundle',
        'Title': 'Complete home bundle',
        'Body (HTML)': '<p>Includes: Kitchen Cleaner, Laundry Detergent, Floor Cleaner, Toilet Cleaner &amp; Handwash. Our biggest saving box.</p>',
        'Vendor': 'Purelane',
        'Product Category': '',
        'Type': 'Combo',
        'Tags': 'combo,whole-home,best-value',
        'Published': 'TRUE',
        'Option1 Name': 'Size',
        'Option1 Value': 'Default',
        'Variant SKU': 'PUR-CMB-CPL',
        'Variant Grams': '2200',
        'Variant Inventory Tracker': 'shopify',
        'Variant Inventory Qty': '35',
        'Variant Inventory Policy': 'deny',
        'Variant Fulfillment Service': 'manual',
        'Variant Price': '799.00',
        'Variant Compare At Price': '1495.00',
        'Variant Requires Shipping': 'TRUE',
        'Variant Taxable': 'TRUE',
        'Image Src': '',
        'Image Position': '',
        'Image Alt Text': '',
        'Gift Card': 'FALSE',
        'SEO Title': 'Complete home bundle',
        'SEO Description': 'Kitchen, laundry, floor, toilet and handwash combo.',
        'Status': 'active',
        'product.metafields.purelane.badge': 'Best value',
        'product.metafields.purelane.rating': '4.6',
        'product.metafields.purelane.review_count': '52',
        'product.metafields.purelane.bundle_size': '5',
        'product.metafields.purelane.component_labels': json.dumps(['Kitchen Cleaner', 'Laundry Detergent', 'Floor Cleaner', 'Toilet Cleaner', 'Handwash']),
        'product.metafields.purelane.components': f"{gids['kitchen']};{gids['laundry_det']};{gids['floor']};{gids['toilet']};{gids['handwash']}"
    },
    {
        'Handle': 'purelane-combo-bathroom-deep-clean',
        'Title': 'Bathroom deep clean',
        'Body (HTML)': '<p>Includes: Toilet Cleaner, Tap Cleaner &amp; Magic Eraser. A complete bathroom refresh in one box.</p>',
        'Vendor': 'Purelane',
        'Product Category': '',
        'Type': 'Combo',
        'Tags': 'combo,bathroom',
        'Published': 'TRUE',
        'Option1 Name': 'Size',
        'Option1 Value': 'Default',
        'Variant SKU': 'PUR-CMB-BTH',
        'Variant Grams': '1200',
        'Variant Inventory Tracker': 'shopify',
        'Variant Inventory Qty': '55',
        'Variant Inventory Policy': 'deny',
        'Variant Fulfillment Service': 'manual',
        'Variant Price': '499.00',
        'Variant Compare At Price': '897.00',
        'Variant Requires Shipping': 'TRUE',
        'Variant Taxable': 'TRUE',
        'Image Src': '',
        'Image Position': '',
        'Image Alt Text': '',
        'Gift Card': 'FALSE',
        'SEO Title': 'Bathroom deep clean',
        'SEO Description': 'Toilet cleaner, tap cleaner and magic eraser combo.',
        'Status': 'active',
        'product.metafields.purelane.badge': '',
        'product.metafields.purelane.rating': '4.4',
        'product.metafields.purelane.review_count': '33',
        'product.metafields.purelane.bundle_size': '3',
        'product.metafields.purelane.component_labels': json.dumps(['Toilet Cleaner', 'Tap Cleaner', 'Magic Eraser']),
        'product.metafields.purelane.components': f"{gids['toilet']};{gids['tap']};{gids['eraser']}"
    },
    {
        'Handle': 'purelane-combo-hard-water-solution-kit',
        'Title': 'Hard water solution kit',
        'Body (HTML)': '<p>Includes: Tap Cleaner &amp; Toilet Cleaner. A quick, focused fix for hard water stains across the home.</p>',
        'Vendor': 'Purelane',
        'Product Category': '',
        'Type': 'Combo',
        'Tags': 'combo,hard-water',
        'Published': 'TRUE',
        'Option1 Name': 'Size',
        'Option1 Value': 'Default',
        'Variant SKU': 'PUR-CMB-HWS',
        'Variant Grams': '900',
        'Variant Inventory Tracker': 'shopify',
        'Variant Inventory Qty': '65',
        'Variant Inventory Policy': 'deny',
        'Variant Fulfillment Service': 'manual',
        'Variant Price': '349.00',
        'Variant Compare At Price': '598.00',
        'Variant Requires Shipping': 'TRUE',
        'Variant Taxable': 'TRUE',
        'Image Src': '',
        'Image Position': '',
        'Image Alt Text': '',
        'Gift Card': 'FALSE',
        'SEO Title': 'Hard water solution kit',
        'SEO Description': 'Tap cleaner and toilet cleaner combo for hard water.',
        'Status': 'active',
        'product.metafields.purelane.badge': '',
        'product.metafields.purelane.rating': '4.3',
        'product.metafields.purelane.review_count': '21',
        'product.metafields.purelane.bundle_size': '2',
        'product.metafields.purelane.component_labels': json.dumps(['Tap Cleaner', 'Toilet Cleaner']),
        'product.metafields.purelane.components': f"{gids['tap']};{gids['toilet']}"
    }
]

# File 1: Safe 5 Combos creation WITHOUT the product reference column
# This guarantees 100% clean creation into your Shopify store
safe_fields = [k for k in combos_data[0].keys() if k != 'product.metafields.purelane.components']
safe_path = os.path.join(output_dir, 'purelane-combos-create.csv')
with open(safe_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=safe_fields)
    writer.writeheader()
    for row in combos_data:
        r = {k: v for k, v in row.items() if k != 'product.metafields.purelane.components'}
        writer.writerow(r)
print('Generated safe combos create:', safe_path)

# File 2: Full 5 Combos with GIDs
gid_fields = list(combos_data[0].keys())
gid_path = os.path.join(output_dir, 'purelane-combos-with-gids.csv')
with open(gid_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=gid_fields)
    writer.writeheader()
    for row in combos_data:
        writer.writerow(row)
print('Generated combos with GIDs:', gid_path)
