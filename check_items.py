#!/usr/bin/env python3
import json

def check_items_needing_obtainment_methods():
    with open('minecraft-items.json', 'r', encoding='utf-8') as f:
        items = json.load(f)
    
    items_needing_methods = []
    
    for item in items:
        # Skip items that are Creative Only, Commands Only, or OP Only
        if (item.get('Creative Only') == 'TRUE' or 
            item.get('Commands Only') == 'TRUE' or 
            item.get('OP Only') == 'TRUE'):
            continue
            
        # Must have a name and ID
        if not item.get('Item Name') or not item.get('Item ID'):
            continue
            
        # Check if item has obtainment methods
        if 'Obtainment Methods' not in item or not item['Obtainment Methods']:
            items_needing_methods.append(item)
            if len(items_needing_methods) >= 100:
                break
    
    print(f"Found {len(items_needing_methods)} items that need obtainment methods:")
    for i, item in enumerate(items_needing_methods, 1):
        print(f"{i}. {item['Item Name']} ({item['Item ID']})")
    
    return items_needing_methods

if __name__ == "__main__":
    items_needing_methods = check_items_needing_obtainment_methods()
