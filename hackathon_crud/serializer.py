from models import Cars, Comment


class BaseSerializer:
    class Meta:
        fields = []
        queryset = []
    
    def serialize_obj(self, obj):
        fields = self.Meta.fields
        dict_ = {}
        for field in fields:
            dict_[field] = getattr(obj, field)
        return dict_
    
    def serialize_queryset(self, queryset=None):
        if queryset is None:
            queryset = self.Meta.queryset

        list1 = []
        for obj in queryset:
            dict_ = self.serialize_obj(obj)
            list1.append(dict_)
        return list1

class CarsSerializer(BaseSerializer):
    class Meta:
        fields = [
            "id", "brand", "model", 
            "year", "volume", "color", 
            "body", "mileage", "price", "comment"
            ]
        queryset = Cars.objects
    
    def serialize_obj(self, obj):
        dict1 = super().serialize_obj(obj)
        dict1["comment"] = CommentSerializer().serialize_queryset(obj.comment)
        return dict1

class CommentSerializer(BaseSerializer):
    class Meta:
        fields = ["text", "created_at"]
        queryset = Comment.objects
    
    def serialize_obj(self, obj):
        dict_ = super().serialize_obj(obj)
        dict_['created_at'] = obj.created_at.strftime("%d.%m.%Y %H:%M:%S")
        return dict_
