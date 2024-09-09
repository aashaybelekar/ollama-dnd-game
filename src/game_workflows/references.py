weapon_dict = {
        "Simple Melee Weapons": {
            "Club": {"Cost": "1 sp", "Damage": "1d4 bludgeoning", "Weight": "2 lb.", "Properties": "Light"},
            "Dagger": {"Cost": "2 gp", "Damage": "1d4 piercing", "Weight": "1 lb.", "Properties": "Finesse, light, thrown (20/60)"},
            "Greatclub": {"Cost": "2 sp", "Damage": "1d8 bludgeoning", "Weight": "10 lb.", "Properties": "Two-handed"},
            "Handaxe": {"Cost": "5 gp", "Damage": "1d6 slashing", "Weight": "2 lb.", "Properties": "Light, thrown (20/60)"},
            "Javelin": {"Cost": "5 sp", "Damage": "1d6 piercing", "Weight": "2 lb.", "Properties": "Thrown (30/120)"},
            "Light hammer": {"Cost": "2 gp", "Damage": "1d4 bludgeoning", "Weight": "2 lb.", "Properties": "Light, thrown (20/60)"},
            "Mace": {"Cost": "5 gp", "Damage": "1d6 bludgeoning", "Weight": "4 lb.", "Properties": "—"},
            "Quarterstaff": {"Cost": "2 sp", "Damage": "1d6 bludgeoning", "Weight": "4 lb.", "Properties": "Versatile (1d8)"},
            "Sickle": {"Cost": "1 gp", "Damage": "1d4 slashing", "Weight": "2 lb.", "Properties": "Light"},
            "Spear": {"Cost": "1 gp", "Damage": "1d6 piercing", "Weight": "3 lb.", "Properties": "Thrown (20/60), versatile (1d8)"}
        },
        "Simple Ranged Weapons": {
            "Crossbow, light": {"Cost": "25 gp", "Damage": "1d8 piercing", "Weight": "5 lb.", "Properties": "Ammunition, range (80/320), loading, two-handed"},
            "Dart": {"Cost": "5 cp", "Damage": "1d4 piercing", "Weight": "1/4 lb.", "Properties": "Finesse, thrown (20/60)"},
            "Shortbow": {"Cost": "25 gp", "Damage": "1d6 piercing", "Weight": "2 lb.", "Properties": "Ammunition, range (80/320), two-handed"},
            "Sling": {"Cost": "1 sp", "Damage": "1d4 bludgeoning", "Weight": "—", "Properties": "Ammunition, range (30/120)"}
        },
        "Martial Melee Weapons": {
            "Battleaxe": {"Cost": "10 gp", "Damage": "1d8 slashing", "Weight": "4 lb.", "Properties": "Versatile (1d10)"},
            "Flail": {"Cost": "10 gp", "Damage": "1d8 bludgeoning", "Weight": "2 lb.", "Properties": "—"},
            "Glaive": {"Cost": "20 gp", "Damage": "1d10 slashing", "Weight": "6 lb.", "Properties": "Heavy, reach, two-handed"},
            "Greataxe": {"Cost": "30 gp", "Damage": "1d12 slashing", "Weight": "7 lb.", "Properties": "Heavy, two-handed"},
            "Greatsword": {"Cost": "50 gp", "Damage": "2d6 slashing", "Weight": "6 lb.", "Properties": "Heavy, two-handed"},
            "Halberd": {"Cost": "20 gp", "Damage": "1d10 slashing", "Weight": "6 lb.", "Properties": "Heavy, reach, two-handed"},
            "Lance": {"Cost": "10 gp", "Damage": "1d12 piercing", "Weight": "6 lb.", "Properties": "Reach, special"},
            "Longsword": {"Cost": "15 gp", "Damage": "1d8 slashing", "Weight": "3 lb.", "Properties": "Versatile (1d10)"},
            "Maul": {"Cost": "10 gp", "Damage": "2d6 bludgeoning", "Weight": "10 lb.", "Properties": "Heavy, two-handed"},
            "Morningstar": {"Cost": "15 gp", "Damage": "1d8 piercing", "Weight": "4 lb.", "Properties": "—"},
            "Pike": {"Cost": "5 gp", "Damage": "1d10 piercing", "Weight": "18 lb.", "Properties": "Heavy, reach, two-handed"},
            "Rapier": {"Cost": "25 gp", "Damage": "1d8 piercing", "Weight": "2 lb.", "Properties": "Finesse"},
            "Scimitar": {"Cost": "25 gp", "Damage": "1d6 slashing", "Weight": "3 lb.", "Properties": "Finesse, light"},
            "Shortsword": {"Cost": "10 gp", "Damage": "1d6 piercing", "Weight": "2 lb.", "Properties": "Finesse, light"},
            "Trident": {"Cost": "5 gp", "Damage": "1d6 piercing", "Weight": "4 lb.", "Properties": "Thrown (20/60), versatile (1d8)"},
            "War pick": {"Cost": "5 gp", "Damage": "1d8 piercing", "Weight": "2 lb.", "Properties": "—"},
            "Warhammer": {"Cost": "15 gp", "Damage": "1d8 bludgeoning", "Weight": "2 lb.", "Properties": "Versatile (1d10)"},
            "Whip": {"Cost": "2 gp", "Damage": "1d4 slashing", "Weight": "3 lb.", "Properties": "Finesse, reach"}
        },
        "Martial Ranged Weapons": {
            "Blowgun": {"Cost": "10 gp", "Damage": "1 piercing", "Weight": "1 lb.", "Properties": "Ammunition, range (25/100), loading"},
            "Crossbow, hand": {"Cost": "75 gp", "Damage": "1d6 piercing", "Weight": "3 lb.", "Properties": "Ammunition, range (30/120), light, loading"},
            "Crossbow, heavy": {"Cost": "50 gp", "Damage": "1d10 piercing", "Weight": "18 lb.", "Properties": "Ammunition, range (100/400), heavy, loading, two-handed"},
            "Longbow": {"Cost": "50 gp", "Damage": "1d8 piercing", "Weight": "2 lb.", "Properties": "Ammunition, range (150/600), heavy, two-handed"},
            "Net": {"Cost": "1 gp", "Damage": "—", "Weight": "3 lb.", "Properties": "Special, thrown (5/15)"}
        }
    }

armor_dict = {
        "Light Armor": {
            "Padded": {"AC": "11 + Dex modifier", "Strength": "-", "Stealth": "Disadvantage", "Weight": "8 lb.", "Cost": "5 gp"},
            "Leather": {"AC": "11 + Dex modifier", "Strength": "-", "Stealth": "-", "Weight": "10 lb.", "Cost": "10 gp"},
            "Studded Leather": {"AC": "12 + Dex modifier", "Strength": "-", "Stealth": "-", "Weight": "13 lb.", "Cost": "45 gp"}
        },
        "Medium Armor": {
            "Hide": {"AC": "12 + Dex modifier (max 2)", "Strength": "-", "Stealth": "-", "Weight": "12 lb.", "Cost": "10 gp"},
            "Chain Shirt": {"AC": "13 + Dex modifier (max 2)", "Strength": "-", "Stealth": "-", "Weight": "20 lb.", "Cost": "50 gp"},
            "Scale Mail": {"AC": "14 + Dex modifier (max 2)", "Strength": "-", "Stealth": "Disadvantage", "Weight": "45 lb.", "Cost": "50 gp"},
            "Spiked Armor": {"AC": "14 + Dex modifier (max 2)", "Strength": "-", "Stealth": "Disadvantage", "Weight": "45 lb.", "Cost": "75 gp"},
            "Breastplate": {"AC": "14 + Dex modifier (max 2)", "Strength": "-", "Stealth": "-", "Weight": "20 lb.", "Cost": "400 gp"},
            "Halfplate": {"AC": "15 + Dex modifier (max 2)", "Strength": "-", "Stealth": "Disadvantage", "Weight": "40 lb.", "Cost": "750 gp"}
        },
        "Heavy Armor": {
            "Ring Mail": {"AC": "14", "Strength": "-", "Stealth": "Disadvantage", "Weight": "40 lb.", "Cost": "30 gp"},
            "Chain Mail": {"AC": "16", "Strength": "Str 13", "Stealth": "Disadvantage", "Weight": "55 lb.", "Cost": "75 gp"},
            "Splint": {"AC": "17", "Strength": "Str 15", "Stealth": "Disadvantage", "Weight": "60 lb.", "Cost": "200 gp"},
            "Plate": {"AC": "18", "Strength": "Str 15", "Stealth": "Disadvantage", "Weight": "65 lb.", "Cost": "1,500 gp"}
        }
    }
