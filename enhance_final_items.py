#!/usr/bin/env python3
import json

def enhance_final_items():
    # Load the JSON file
    with open('minecraft-items.json', 'r', encoding='utf-8') as f:
        items = json.load(f)
    
    # Define enhanced obtainment methods for final items
    enhanced_methods = {
        # Birch variants
        "birch_trapdoor": [
            {
                "method": "🔨 Crafting",
                "description": "Craft 6 birch planks in trapdoor pattern",
                "recipe": "6x Birch Planks (trapdoor pattern)",
                "location": "Crafting table"
            },
            {
                "method": "⛏️ Mining",
                "description": "Mine existing birch trapdoors",
                "tools": "Any axe",
                "location": "Generated structures"
            },
            {
                "method": "🏗️ Generated Structures",
                "description": "Find in villages and woodland mansions",
                "tools": "Any axe",
                "location": "Villages, Woodland Mansions"
            }
        ],
        
        "birch_hanging_sign": [
            {
                "method": "🔨 Crafting",
                "description": "Craft 6 stripped birch logs and 2 chains in hanging sign pattern",
                "recipe": "6x Stripped Birch Log + 2x Chain (hanging sign pattern)",
                "location": "Crafting table"
            },
            {
                "method": "⛏️ Mining",
                "description": "Mine existing birch hanging signs",
                "tools": "Any axe",
                "location": "Generated structures"
            },
            {
                "method": "🏗️ Generated Structures",
                "description": "Find in villages and woodland mansions",
                "tools": "Any axe",
                "location": "Villages, Woodland Mansions"
            }
        ],
        
        # Spruce variants
        "spruce_trapdoor": [
            {
                "method": "🔨 Crafting",
                "description": "Craft 6 spruce planks in trapdoor pattern",
                "recipe": "6x Spruce Planks (trapdoor pattern)",
                "location": "Crafting table"
            },
            {
                "method": "⛏️ Mining",
                "description": "Mine existing spruce trapdoors",
                "tools": "Any axe",
                "location": "Generated structures"
            },
            {
                "method": "🏗️ Generated Structures",
                "description": "Find in villages and woodland mansions",
                "tools": "Any axe",
                "location": "Villages, Woodland Mansions"
            }
        ],
        
        "spruce_sign": [
            {
                "method": "🔨 Crafting",
                "description": "Craft 6 spruce planks and 1 stick in sign pattern",
                "recipe": "6x Spruce Planks + 1x Stick (sign pattern)",
                "location": "Crafting table"
            },
            {
                "method": "⛏️ Mining",
                "description": "Mine existing spruce signs",
                "tools": "Any axe",
                "location": "Generated structures"
            },
            {
                "method": "🏗️ Generated Structures",
                "description": "Find in villages and woodland mansions",
                "tools": "Any axe",
                "location": "Villages, Woodland Mansions"
            }
        ],
        
        "spruce_hanging_sign": [
            {
                "method": "🔨 Crafting",
                "description": "Craft 6 stripped spruce logs and 2 chains in hanging sign pattern",
                "recipe": "6x Stripped Spruce Log + 2x Chain (hanging sign pattern)",
                "location": "Crafting table"
            },
            {
                "method": "⛏️ Mining",
                "description": "Mine existing spruce hanging signs",
                "tools": "Any axe",
                "location": "Generated structures"
            },
            {
                "method": "🏗️ Generated Structures",
                "description": "Find in villages and woodland mansions",
                "tools": "Any axe",
                "location": "Villages, Woodland Mansions"
            }
        ],
        
        "spruce_pressure_plate": [
            {
                "method": "🔨 Crafting",
                "description": "Craft 2 spruce planks in pressure plate pattern",
                "recipe": "2x Spruce Planks (pressure plate pattern)",
                "location": "Crafting table"
            },
            {
                "method": "⛏️ Mining",
                "description": "Mine existing spruce pressure plates",
                "tools": "Any axe",
                "location": "Generated structures"
            },
            {
                "method": "🏗️ Generated Structures",
                "description": "Find in villages and woodland mansions",
                "tools": "Any axe",
                "location": "Villages, Woodland Mansions"
            }
        ],
        
        "spruce_button": [
            {
                "method": "🔨 Crafting",
                "description": "Craft 1 spruce plank into 1 spruce button",
                "recipe": "1x Spruce Plank = 1x Spruce Button",
                "location": "Crafting table"
            },
            {
                "method": "⛏️ Mining",
                "description": "Mine existing spruce buttons",
                "tools": "Any axe",
                "location": "Generated structures"
            },
            {
                "method": "🏗️ Generated Structures",
                "description": "Find in villages and woodland mansions",
                "tools": "Any axe",
                "location": "Villages, Woodland Mansions"
            }
        ],
        
        "spruce_boat": [
            {
                "method": "🔨 Crafting",
                "description": "Craft 5 spruce planks in boat pattern",
                "recipe": "5x Spruce Planks (boat pattern)",
                "location": "Crafting table"
            },
            {
                "method": "⛏️ Mining",
                "description": "Mine existing spruce boats",
                "tools": "Any axe",
                "location": "Generated structures"
            },
            {
                "method": "🏗️ Generated Structures",
                "description": "Find in villages and woodland mansions",
                "tools": "Any axe",
                "location": "Villages, Woodland Mansions"
            }
        ],
        
        "spruce_chest_boat": [
            {
                "method": "🔨 Crafting",
                "description": "Craft 1 spruce boat and 1 chest in chest boat pattern",
                "recipe": "1x Spruce Boat + 1x Chest (chest boat pattern)",
                "location": "Crafting table"
            },
            {
                "method": "⛏️ Mining",
                "description": "Mine existing spruce chest boats",
                "tools": "Any axe",
                "location": "Generated structures"
            },
            {
                "method": "🏗️ Generated Structures",
                "description": "Find in villages and woodland mansions",
                "tools": "Any axe",
                "location": "Villages, Woodland Mansions"
            }
        ],
        
        # Dark Oak variants
        "dark_oak_slab": [
            {
                "method": "🔨 Crafting",
                "description": "Craft 3 dark oak planks in a row",
                "recipe": "3x Dark Oak Planks (horizontal line)",
                "location": "Crafting table"
            },
            {
                "method": "🏗️ Stonecutter",
                "description": "Use stonecutter to create dark oak slabs",
                "recipe": "1x Dark Oak Planks",
                "location": "Stonecutter"
            },
            {
                "method": "⛏️ Mining",
                "description": "Mine existing dark oak slabs",
                "tools": "Any axe",
                "location": "Generated structures"
            }
        ],
        
        "dark_oak_stairs": [
            {
                "method": "🔨 Crafting",
                "description": "Craft 6 dark oak planks in stairs pattern",
                "recipe": "6x Dark Oak Planks (stairs shape)",
                "location": "Crafting table"
            },
            {
                "method": "🏗️ Stonecutter",
                "description": "Use stonecutter to create dark oak stairs",
                "recipe": "1x Dark Oak Planks",
                "location": "Stonecutter"
            },
            {
                "method": "⛏️ Mining",
                "description": "Mine existing dark oak stairs",
                "tools": "Any axe",
                "location": "Generated structures"
            }
        ],
        
        "dark_oak_fence": [
            {
                "method": "🔨 Crafting",
                "description": "Craft 4 dark oak planks and 2 sticks in fence pattern",
                "recipe": "4x Dark Oak Planks + 2x Sticks (fence pattern)",
                "location": "Crafting table"
            },
            {
                "method": "⛏️ Mining",
                "description": "Mine existing dark oak fences",
                "tools": "Any axe",
                "location": "Generated structures"
            },
            {
                "method": "🏗️ Generated Structures",
                "description": "Find in woodland mansions and villages",
                "tools": "Any axe",
                "location": "Woodland Mansions, Villages"
            }
        ],
        
        "dark_oak_fence_gate": [
            {
                "method": "🔨 Crafting",
                "description": "Craft 4 sticks and 2 dark oak planks in gate pattern",
                "recipe": "4x Sticks + 2x Dark Oak Planks (gate pattern)",
                "location": "Crafting table"
            },
            {
                "method": "⛏️ Mining",
                "description": "Mine existing dark oak fence gates",
                "tools": "Any axe",
                "location": "Generated structures"
            },
            {
                "method": "🏗️ Generated Structures",
                "description": "Find in woodland mansions and villages",
                "tools": "Any axe",
                "location": "Woodland Mansions, Villages"
            }
        ],
        
        "dark_oak_door": [
            {
                "method": "🔨 Crafting",
                "description": "Craft 6 dark oak planks in door pattern",
                "recipe": "6x Dark Oak Planks (door pattern)",
                "location": "Crafting table"
            },
            {
                "method": "⛏️ Mining",
                "description": "Mine existing dark oak doors",
                "tools": "Any axe",
                "location": "Generated structures"
            },
            {
                "method": "🏗️ Generated Structures",
                "description": "Find in woodland mansions and villages",
                "tools": "Any axe",
                "location": "Woodland Mansions, Villages"
            }
        ],
        
        "dark_oak_trapdoor": [
            {
                "method": "🔨 Crafting",
                "description": "Craft 6 dark oak planks in trapdoor pattern",
                "recipe": "6x Dark Oak Planks (trapdoor pattern)",
                "location": "Crafting table"
            },
            {
                "method": "⛏️ Mining",
                "description": "Mine existing dark oak trapdoors",
                "tools": "Any axe",
                "location": "Generated structures"
            },
            {
                "method": "🏗️ Generated Structures",
                "description": "Find in woodland mansions and villages",
                "tools": "Any axe",
                "location": "Woodland Mansions, Villages"
            }
        ],
        
        "dark_oak_shelf": [
            {
                "method": "🔨 Crafting",
                "description": "Craft 6 dark oak planks and 3 books in shelf pattern",
                "recipe": "6x Dark Oak Planks + 3x Book (shelf pattern)",
                "location": "Crafting table"
            },
            {
                "method": "⛏️ Mining",
                "description": "Mine existing dark oak shelves",
                "tools": "Any axe",
                "location": "Generated structures"
            },
            {
                "method": "🏗️ Generated Structures",
                "description": "Find in woodland mansions and villages",
                "tools": "Any axe",
                "location": "Woodland Mansions, Villages"
            }
        ],
        
        "dark_oak_sign": [
            {
                "method": "🔨 Crafting",
                "description": "Craft 6 dark oak planks and 1 stick in sign pattern",
                "recipe": "6x Dark Oak Planks + 1x Stick (sign pattern)",
                "location": "Crafting table"
            },
            {
                "method": "⛏️ Mining",
                "description": "Mine existing dark oak signs",
                "tools": "Any axe",
                "location": "Generated structures"
            },
            {
                "method": "🏗️ Generated Structures",
                "description": "Find in woodland mansions and villages",
                "tools": "Any axe",
                "location": "Woodland Mansions, Villages"
            }
        ],
        
        "dark_oak_hanging_sign": [
            {
                "method": "🔨 Crafting",
                "description": "Craft 6 stripped dark oak logs and 2 chains in hanging sign pattern",
                "recipe": "6x Stripped Dark Oak Log + 2x Chain (hanging sign pattern)",
                "location": "Crafting table"
            },
            {
                "method": "⛏️ Mining",
                "description": "Mine existing dark oak hanging signs",
                "tools": "Any axe",
                "location": "Generated structures"
            },
            {
                "method": "🏗️ Generated Structures",
                "description": "Find in woodland mansions and villages",
                "tools": "Any axe",
                "location": "Woodland Mansions, Villages"
            }
        ],
        
        "dark_oak_pressure_plate": [
            {
                "method": "🔨 Crafting",
                "description": "Craft 2 dark oak planks in pressure plate pattern",
                "recipe": "2x Dark Oak Planks (pressure plate pattern)",
                "location": "Crafting table"
            },
            {
                "method": "⛏️ Mining",
                "description": "Mine existing dark oak pressure plates",
                "tools": "Any axe",
                "location": "Generated structures"
            },
            {
                "method": "🏗️ Generated Structures",
                "description": "Find in woodland mansions and villages",
                "tools": "Any axe",
                "location": "Woodland Mansions, Villages"
            }
        ],
        
        "dark_oak_button": [
            {
                "method": "🔨 Crafting",
                "description": "Craft 1 dark oak plank into 1 dark oak button",
                "recipe": "1x Dark Oak Plank = 1x Dark Oak Button",
                "location": "Crafting table"
            },
            {
                "method": "⛏️ Mining",
                "description": "Mine existing dark oak buttons",
                "tools": "Any axe",
                "location": "Generated structures"
            },
            {
                "method": "🏗️ Generated Structures",
                "description": "Find in woodland mansions and villages",
                "tools": "Any axe",
                "location": "Woodland Mansions, Villages"
            }
        ],
        
        "dark_oak_boat": [
            {
                "method": "🔨 Crafting",
                "description": "Craft 5 dark oak planks in boat pattern",
                "recipe": "5x Dark Oak Planks (boat pattern)",
                "location": "Crafting table"
            },
            {
                "method": "⛏️ Mining",
                "description": "Mine existing dark oak boats",
                "tools": "Any axe",
                "location": "Generated structures"
            },
            {
                "method": "🏗️ Generated Structures",
                "description": "Find in woodland mansions and villages",
                "tools": "Any axe",
                "location": "Woodland Mansions, Villages"
            }
        ],
        
        "dark_oak_chest_boat": [
            {
                "method": "🔨 Crafting",
                "description": "Craft 1 dark oak boat and 1 chest in chest boat pattern",
                "recipe": "1x Dark Oak Boat + 1x Chest (chest boat pattern)",
                "location": "Crafting table"
            },
            {
                "method": "⛏️ Mining",
                "description": "Mine existing dark oak chest boats",
                "tools": "Any axe",
                "location": "Generated structures"
            },
            {
                "method": "🏗️ Generated Structures",
                "description": "Find in woodland mansions and villages",
                "tools": "Any axe",
                "location": "Woodland Mansions, Villages"
            }
        ],
        
        # Acacia variants
        "acacia_slab": [
            {
                "method": "🔨 Crafting",
                "description": "Craft 3 acacia planks in a row",
                "recipe": "3x Acacia Planks (horizontal line)",
                "location": "Crafting table"
            },
            {
                "method": "🏗️ Stonecutter",
                "description": "Use stonecutter to create acacia slabs",
                "recipe": "1x Acacia Planks",
                "location": "Stonecutter"
            },
            {
                "method": "⛏️ Mining",
                "description": "Mine existing acacia slabs",
                "tools": "Any axe",
                "location": "Generated structures"
            }
        ],
        
        "acacia_stairs": [
            {
                "method": "🔨 Crafting",
                "description": "Craft 6 acacia planks in stairs pattern",
                "recipe": "6x Acacia Planks (stairs shape)",
                "location": "Crafting table"
            },
            {
                "method": "🏗️ Stonecutter",
                "description": "Use stonecutter to create acacia stairs",
                "recipe": "1x Acacia Planks",
                "location": "Stonecutter"
            },
            {
                "method": "⛏️ Mining",
                "description": "Mine existing acacia stairs",
                "tools": "Any axe",
                "location": "Generated structures"
            }
        ],
        
        "acacia_fence": [
            {
                "method": "🔨 Crafting",
                "description": "Craft 4 acacia planks and 2 sticks in fence pattern",
                "recipe": "4x Acacia Planks + 2x Sticks (fence pattern)",
                "location": "Crafting table"
            },
            {
                "method": "⛏️ Mining",
                "description": "Mine existing acacia fences",
                "tools": "Any axe",
                "location": "Generated structures"
            },
            {
                "method": "🏗️ Generated Structures",
                "description": "Find in villages and desert temples",
                "tools": "Any axe",
                "location": "Villages, Desert Temples"
            }
        ],
        
        "acacia_fence_gate": [
            {
                "method": "🔨 Crafting",
                "description": "Craft 4 sticks and 2 acacia planks in gate pattern",
                "recipe": "4x Sticks + 2x Acacia Planks (gate pattern)",
                "location": "Crafting table"
            },
            {
                "method": "⛏️ Mining",
                "description": "Mine existing acacia fence gates",
                "tools": "Any axe",
                "location": "Generated structures"
            },
            {
                "method": "🏗️ Generated Structures",
                "description": "Find in villages and desert temples",
                "tools": "Any axe",
                "location": "Villages, Desert Temples"
            }
        ],
        
        "acacia_door": [
            {
                "method": "🔨 Crafting",
                "description": "Craft 6 acacia planks in door pattern",
                "recipe": "6x Acacia Planks (door pattern)",
                "location": "Crafting table"
            },
            {
                "method": "⛏️ Mining",
                "description": "Mine existing acacia doors",
                "tools": "Any axe",
                "location": "Generated structures"
            },
            {
                "method": "🏗️ Generated Structures",
                "description": "Find in villages and desert temples",
                "tools": "Any axe",
                "location": "Villages, Desert Temples"
            }
        ],
        
        "acacia_trapdoor": [
            {
                "method": "🔨 Crafting",
                "description": "Craft 6 acacia planks in trapdoor pattern",
                "recipe": "6x Acacia Planks (trapdoor pattern)",
                "location": "Crafting table"
            },
            {
                "method": "⛏️ Mining",
                "description": "Mine existing acacia trapdoors",
                "tools": "Any axe",
                "location": "Generated structures"
            },
            {
                "method": "🏗️ Generated Structures",
                "description": "Find in villages and desert temples",
                "tools": "Any axe",
                "location": "Villages, Desert Temples"
            }
        ],
        
        "acacia_shelf": [
            {
                "method": "🔨 Crafting",
                "description": "Craft 6 acacia planks and 3 books in shelf pattern",
                "recipe": "6x Acacia Planks + 3x Book (shelf pattern)",
                "location": "Crafting table"
            },
            {
                "method": "⛏️ Mining",
                "description": "Mine existing acacia shelves",
                "tools": "Any axe",
                "location": "Generated structures"
            },
            {
                "method": "🏗️ Generated Structures",
                "description": "Find in villages and desert temples",
                "tools": "Any axe",
                "location": "Villages, Desert Temples"
            }
        ],
        
        "acacia_sign": [
            {
                "method": "🔨 Crafting",
                "description": "Craft 6 acacia planks and 1 stick in sign pattern",
                "recipe": "6x Acacia Planks + 1x Stick (sign pattern)",
                "location": "Crafting table"
            },
            {
                "method": "⛏️ Mining",
                "description": "Mine existing acacia signs",
                "tools": "Any axe",
                "location": "Generated structures"
            },
            {
                "method": "🏗️ Generated Structures",
                "description": "Find in villages and desert temples",
                "tools": "Any axe",
                "location": "Villages, Desert Temples"
            }
        ],
        
        "acacia_hanging_sign": [
            {
                "method": "🔨 Crafting",
                "description": "Craft 6 stripped acacia logs and 2 chains in hanging sign pattern",
                "recipe": "6x Stripped Acacia Log + 2x Chain (hanging sign pattern)",
                "location": "Crafting table"
            },
            {
                "method": "⛏️ Mining",
                "description": "Mine existing acacia hanging signs",
                "tools": "Any axe",
                "location": "Generated structures"
            },
            {
                "method": "🏗️ Generated Structures",
                "description": "Find in villages and desert temples",
                "tools": "Any axe",
                "location": "Villages, Desert Temples"
            }
        ],
        
        "acacia_pressure_plate": [
            {
                "method": "🔨 Crafting",
                "description": "Craft 2 acacia planks in pressure plate pattern",
                "recipe": "2x Acacia Planks (pressure plate pattern)",
                "location": "Crafting table"
            },
            {
                "method": "⛏️ Mining",
                "description": "Mine existing acacia pressure plates",
                "tools": "Any axe",
                "location": "Generated structures"
            },
            {
                "method": "🏗️ Generated Structures",
                "description": "Find in villages and desert temples",
                "tools": "Any axe",
                "location": "Villages, Desert Temples"
            }
        ],
        
        "acacia_button": [
            {
                "method": "🔨 Crafting",
                "description": "Craft 1 acacia plank into 1 acacia button",
                "recipe": "1x Acacia Plank = 1x Acacia Button",
                "location": "Crafting table"
            },
            {
                "method": "⛏️ Mining",
                "description": "Mine existing acacia buttons",
                "tools": "Any axe",
                "location": "Generated structures"
            },
            {
                "method": "🏗️ Generated Structures",
                "description": "Find in villages and desert temples",
                "tools": "Any axe",
                "location": "Villages, Desert Temples"
            }
        ],
        
        "acacia_boat": [
            {
                "method": "🔨 Crafting",
                "description": "Craft 5 acacia planks in boat pattern",
                "recipe": "5x Acacia Planks (boat pattern)",
                "location": "Crafting table"
            },
            {
                "method": "⛏️ Mining",
                "description": "Mine existing acacia boats",
                "tools": "Any axe",
                "location": "Generated structures"
            },
            {
                "method": "🏗️ Generated Structures",
                "description": "Find in villages and desert temples",
                "tools": "Any axe",
                "location": "Villages, Desert Temples"
            }
        ],
        
        "acacia_chest_boat": [
            {
                "method": "🔨 Crafting",
                "description": "Craft 1 acacia boat and 1 chest in chest boat pattern",
                "recipe": "1x Acacia Boat + 1x Chest (chest boat pattern)",
                "location": "Crafting table"
            },
            {
                "method": "⛏️ Mining",
                "description": "Mine existing acacia chest boats",
                "tools": "Any axe",
                "location": "Generated structures"
            },
            {
                "method": "🏗️ Generated Structures",
                "description": "Find in villages and desert temples",
                "tools": "Any axe",
                "location": "Villages, Desert Temples"
            }
        ]
    }
    
    # Update the items with enhanced obtainment methods
    updated_count = 0
    for item in items:
        item_id = item.get('Item ID', '')
        if item_id in enhanced_methods:
            # Only update if the item has 2 or fewer current methods
            current_methods = item.get('Obtainment Methods', [])
            if len(current_methods) <= 2:
                item['Obtainment Methods'] = enhanced_methods[item_id]
                updated_count += 1
                print(f"Enhanced obtainment methods for: {item['Item Name']} ({len(enhanced_methods[item_id])} methods)")
    
    # Save the updated JSON
    with open('minecraft-items.json', 'w', encoding='utf-8') as f:
        json.dump(items, f, indent=2, ensure_ascii=False)
    
    print(f"\nEnhanced obtainment methods for {updated_count} items!")
    return updated_count

if __name__ == "__main__":
    enhance_final_items()
