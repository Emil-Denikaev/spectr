from utils.db_api.db_commands import add_item


async def add_items():
    await add_item(name="Intel",
                   category_name="🔌 Техника", category_code="Electronics",
                   subcategory_name="🖥 Компьютеры", subcategory_code="PCs",
                   price=100500, photo="-")
    await add_item(name="Acer",
                   category_name="🔌 Техника", category_code="Electronics",
                   subcategory_name="🖥 Компьютеры", subcategory_code="PCs",
                   price=123000, photo="-")
    await add_item(name="Apple",
                   category_name="🔌 Техника", category_code="Electronics",
                   subcategory_name="🖥 Компьютеры", subcategory_code="PCs",
                   price=80000, photo="-")
    await add_item(name="Iphone",
                   category_name="🔌 Техника", category_code="Electronics",
                   subcategory_name="☎️ Телефоны", subcategory_code="Phones",
                   price=57000, photo="-")
    await add_item(name="Samsung",
                   category_name="🔌 Техника", category_code="Electronics",
                   subcategory_name="☎️ Телефоны", subcategory_code="Phones",
                   price=100000, photo="-")
    await add_item(name="Веселая механика",
                   category_name="🛍 Услуги Рекламы", category_code="Ads",
                   subcategory_name="📹 На Youtube", subcategory_code="Youtube",
                   price=300000, photo="-")
    await add_item(name="Детский",
                   category_name="🛍 Услуги Рекламы", category_code="Ads",
                   subcategory_name="📹 На Youtube", subcategory_code="Youtube",
                   price=106000, photo="-")
    await add_item(name="Твой",
                   category_name="🛍 Услуги Рекламы", category_code="Ads",
                   subcategory_name="🗣 На Вконтакте", subcategory_code="VK",
                   price=10000, photo="-")
    await add_item(name="Человечки",
                   category_name="🛍 Услуги Рекламы", category_code="Ads",
                   subcategory_name="🗣 На Вконтакте", subcategory_code="VK",
                   price=10000, photo="-")