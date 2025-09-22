
products=[
    ('Palak Paneer',('spinach','paneer','onions','tomatoes','ginger','garlic','cream')),
    ('Dal Makhani',('black lentis','kidney beans','butter','cream','onion','tomatoes','ghee')),
    ('Roti',('flour','water','salt')),
    ('Chicken Korma',('chicken','yogurt','onions','cashews','ginger','garlic','spices')),
    ('Aloo Gobi',('potatoes','cauliflower','onions','turmeric','vegetable oil')),
    ('Gajar Ka Halwa',('carrots','milk','sugar','ghee','almonds','cardamom'))
]

user_allergy={'suger','ghee'}

def find_allergy(product_ingredients,allergy):
    ingredients=set(product_ingredients)
    wrong=ingredients.intersection(allergy)
    return wrong

for name,ingredients in products:
    found=find_allergy(ingredients,user_allergy)

    if found:
        print(f"❌ WARNING: '{name}' contains: {','.join(found)}")
    else:
        print(f"☑️ OK: '{name}' is safe for you to eat.")