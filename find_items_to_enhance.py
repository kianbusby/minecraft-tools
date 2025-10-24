#!/usr/bin/env python3
import json

def find_obtainable_items():
    with open('minecraft-items.json', 'r', encoding='utf-8') as f:
        items = json.load(f)
    
    obtainable_items = []
    items_with_methods = 0
    items_without_methods = 0
    items_with_minimal_methods = 0
    
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
        if 'Obtainment Methods' in item and item['Obtainment Methods']:
            # Check if the methods are minimal (just "Unobtainable" or similar)
            methods = item['Obtainment Methods']
            if len(methods) == 1 and any('Unobtainable' in str(method) for method in methods):
                items_with_minimal_methods += 1
                if len(obtainable_items) < 100:
                    obtainable_items.append(item)
            else:
                items_with_methods += 1
        else:
            items_without_methods += 1
            if len(obtainable_items) < 100:
                obtainable_items.append(item)
    
    print(f"Items with good obtainment methods: {items_with_methods}")
    print(f"Items with minimal/unobtainable methods: {items_with_minimal_methods}")
    print(f"Items without obtainment methods: {items_without_methods}")
    print(f"Found {len(obtainable_items)} obtainable items that need better obtainment methods:")
    
    for i, item in enumerate(obtainable_items, 1):
        print(f"{i}. {item['Item Name']} ({item['Item ID']}) - {item.get('Version Added', 'Unknown version')}")
        if 'Obtainment Methods' in item:
            print(f"   Current methods: {item['Obtainment Methods']}")
    
    return obtainable_items

if __name__ == "__main__":
    obtainable_items = find_obtainable_items()