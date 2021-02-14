def prefilter_items(data_train, filter=None, department=None):
    # Оставим только 5000 самых популярных товаров
    popularity = data_train.groupby('item_id')['quantity'].sum().reset_index()
    popularity.rename(columns={'quantity': 'n_sold'}, inplace=True)
    
    # Уберем самые непопулряные 
    if filter == 'no_nopop':
        top_5000 = popularity.sort_values('n_sold', ascending=False).head(5000).item_id.tolist()
        #добавим, чтобы не потерять юзеров
        data_train.loc[~data_train['item_id'].isin(top_5000), 'item_id'] = 999999 
    
    # Уберем самые популярные 
    if filter == 'nopop':
        top_5000 = popularity.sort_values('n_sold', ascending=True).head(5000).item_id.tolist()
        # добавим, чтобы не потерять юзеров
        data_train.loc[~data_train['item_id'].isin(top_5000), 'item_id'] = 999999
         
    # Уберем товары, которые не продавались за последние 12 месяцев
    if filter == 'year':
        date_filter = [i for i in range(53)]
        data_train.loc[~data_train['week_no'].isin(date_filter), 'item_id'] = 999999

    # Уберем не интересные для рекоммендаций категории (department)
    if filter == 'department':
        pass
    # в трейне нет колонки отвечающей за департамент
    
    # Уберем слишком дешевые товары (на них не заработаем). 1 покупка из рассылок стоит 60 руб. 
    if filter == 'value_cheap':
        data_train.loc[~data_train['sales_value'] > 60, 'item_id'] = 999999    
    # Уберем слишком дорогие товарыs
    if filter == 'valie_exp':
        data_train.loc[~data_train['sales_value'] < 500, 'item_id'] = 999999
        
    return data_train

def postfilter_items():
    pass


def get_similar_items_recommendation(user, model, N=5):
    """Рекомендуем товары, похожие на топ-N купленных юзером товаров"""

    # your_code
    

    return res


def get_similar_users_recommendation(user, model, N=5):
    """Рекомендуем топ-N товаров, среди купленных похожими юзерами"""

    # your_code

    return res