from .models import Category, Subcat

def seeder_func():
    categories = [  'Clothes','Shoes','Accessories',
                    'Intimates','Coats','Sportswear','Swimwear']

    subcats = [     'Activewear', 'Cardigans', 'Dresses','Pants'
                    'Shirts','Shorts','Skirts','Suits & Blazers',
                    'Sweaters','T-Shirts','Tops','Boots','Flats',
                    'Heels',  'Loafers', 'Sandals',  'Sneakers',
                    'Bags','Belts','Hats','Jewelry','Scarves',
                    'Sunglasses', 'Ties','Bras', 'Lingerie Sets',
                    'Panties','Shapewear', 'Sleepwear', 'Socks',
                    'Jackets', 'Vests',  'Winter Coat',  'Athletic Tops',
                    'Caps',  'Gym Shorts', 'Joggers', 'Sports Bras',
                    'Sports Jerseys', 'Tracksuit', 'Yoga Pants','Bikinis'
                    'Cover - Up', ' One - Piece',  'Swim Shorts', 'Trunks'
    ]
    for category in categories:
        if not Category.objects.filter(name = category):
            new_category = Category(name=category)
            new_category.save()
    for subcat in subcats:
        if not Subcat.objects.filter(name=subcat):
            new_subcat = Subcat(name=subcat)
            new_subcat.save()