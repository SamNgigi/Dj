from rest_framework import serializers
from .models import ApiTest, LANGUAGE_CHOICES, STYLE_CHOICES


class ApiTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiTest
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new ApiTest instance, given the validated_data
        """
        return ApiTest.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing ApiTest instance given the validated data
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

        """
        Serializing the hard way.

        class ApiTestSerializer(serializers.Serializer):
            id = serializers.IntegerField(read_only=True)
            title = serializers.CharField(
                required=False, allow_blank=True, max_length=100)
            code = serializers.CharField(
            style={'base_template': 'textarea.html'}
            )
            linenos = serializers.BooleanField(required=False)
            language = serializers.ChoiceField(
                choices=LANGUAGE_CHOICES, default='python')
            style = serializers.ChoiceField(
                choices=STYLE_CHOICES, default='friendly')

            def create(self, validated_data):

                Create and return a new ApiTest instance, given the
                validated_data

                return ApiTest.objects.create(**validated_data)

            def update(self, instance, validated_data):

                Update and return an existing ApiTest instance given the validated data

                instance.title = validated_data.get('title', instance.title)
                instance.code = validated_data.get('code', instance.code)
                instance.linenos = validated_data.get('linenos', instance.linenos)
                instance.language = validated_data.get('language', instance.language)
                instance.style = validated_data.get('style', instance.style)
                instance.save()
                return instance


        Playing around with the serializers with the interactive shell.

        python manage.py shell

        >>> Serializing our data.

        from snippets.models import Snippet
        from snippets.serializers import SnippetSerializer
        from rest_framework.renderers import JSONRenderer
        from rest_framework.parsers import JSONParser

        snippet = Snippet(code='foo = "bar"\n')
        snippet.save()

        snippet = Snippet(code='print "hello, world"\n')
        snippet.save()

        serializer = SnippetSerializer(snippet)
        serializer.data

        >>returns {
        'id': 2, 'title': u'', 'code': u'print "hello, world"\n',
        'linenos': False, 'language': u'python', 'style': u'friendly'
        }

        >>>Jsonify
        content = JSONRenderer().render(serializer.data)
        content

        returns {
        "id": 2, "title": "", "code": "print \\"hello, world\\"\\n",
        "linenos": false, "language": "python", "style": "friendly"
        }


        >>>>Doing the reverse and getting python objects/queryset from json

        from django.utils.six import BytesIO

        stream = BytesIO(content)
        data = JSONParser().parse(stream)

        serializer = SnippetSerializer(data=data)
        serializer.is_valid()
        >>returns True

        serializer.validated_data
        >>returns OrderedDict(
        [('title', ''), ('code', 'print "hello, world"\n'),
        ('linenos', False), ('language', 'python'), ('style', 'friendly')]
        )

        serializer.save()
        returns <Snippet: Snippet object>
        """
