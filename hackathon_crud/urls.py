from views import *


urlpatterns = [
    ('cars/', car_list),
    ('create/', create),
    ('detail/id', car_detail),
    ('update/id', car_update),
    ('delete/id', car_delete),
    ('comment/id', comment)
    
    # ('category-create/', category_create),
    # ('comment-create/', create_comment),
]