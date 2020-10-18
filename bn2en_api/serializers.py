from rest_framework import serializers


class Bn2EnSerializer(serializers.Serializer):
    """Your data serializer, define your fields here."""
    text = serializers.CharField(max_length=250)

