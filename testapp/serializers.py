from rest_framework.serializers import ModelSerializer
from .models import Band


class BandSerializer(ModelSerializer):
    class Meta:
        """
        Creating a ModelSerializer without either the 'fields'
        attribute or the 'exclude' attribute has been deprecated since
        3.3.0, and is now disallowed.
        Add an explicit fields = '__all__' to the BandSerializer serializer.
        """
        model = Band
        fields = '__all__'
