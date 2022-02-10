from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

#"""Web API'mize başlamak için ihtiyacımız olan ilk şey, snippet örneklerini json gibi temsillere serileştirmenin ve seri durumdan çıkarmanın bir yolunu sağlamaktır."""

# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=128)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
    
    
#     def create(self, validated_data):
#         """Doğrulanmiş verilere göre yeni bir "Snippet" örneği oluşturun ve döndürün."""
        
#         return Snippet.objects.create(**validated_data)


#     def update(self, instance, validated_data):
#         """Doğrulanmiş verilere göre mevcut bir "Snippet" örneğini güncelleyin ve döndürün."""
        
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance


#"""Django'nun hem Form sınıflarını hem de ModelForm sınıflarını sağladığı gibi, REST çerçevesi hem Serializer sınıflarını hem de ModelSerializer sınıflarını içerir."""

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
        
        
        
        
        
#"""ModelSerializer sınıflarının özellikle sihirli bir şey yapmadığını hatırlamak önemlidir, bunlar sadece seri hale getirici sınıfları oluşturmak için bir kısayoldur:"""