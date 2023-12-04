from rest_framework import serializers
from .models import ModelA, ModelB
import json


class ModelBSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelB
        fields = '__all__'


class ModelASerializer(serializers.ModelSerializer):
    nested = ModelBSerializer(many=True, required=False)
    file = serializers.FileField(required=False)

    class Meta:
        model = ModelA
        fields = '__all__'

    def create(self, validated_data):
        json_file = validated_data.pop('file', None)
        nested = validated_data.pop('nested', [])

        try:
            if json_file:
                python_data = json.loads(json_file)

                name = python_data.get('name', None)
                roll = python_data.get('roll', None)
                city = python_data.get('roll', None)

                model_a_instance = ModelA.objects.create(name=name,
                                                         roll=roll,
                                                         city=city)

                for data in nested:
                    ModelB.objects.create(
                        name=model_a_instance,
                        percentage=data.get('percentage'),
                        subject=data.get('subject'),
                        sport=data.get('sport')
                    )

                return model_a_instance
            else:
                raise serializers.ValidationError("No file was submitted")

        except json.JSONDecodeError:
            raise serializers.ValidationError("Invalid JSON format in the file field.")


"""
from rest_framework import serializers
from .models import ModelA, ModelB
import json


class ModelBSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelB
        fields = ['percentage', 'subject', 'sport', 'name']


class ModelASerializer(serializers.ModelSerializer):
    nested = ModelBSerializer(many=True, write_only=True)

    class Meta:
        model = ModelA
        fields = ['file', 'name', 'roll', 'city', 'nested']

    def create(self, validated_data):
        nested_data = validated_data.pop('nested', None)
        file_data = validated_data.pop('file').read().decode('utf-8')

        try:
            json_data = json.loads(file_data)

            # Extract data for ModelA
            model_a_data = {
                'name': json_data.get('name', ''),
                'roll': json_data.get('roll', None),
                'city': json_data.get('city', ''),
            }

            # Create ModelA instance
            model_a_instance = ModelA.objects.create(**model_a_data)

            # Create ModelB instance and associate it with ModelA instance
            if nested_data:
                ModelB.objects.create(
                    model_a=model_a_instance,
                    percentage=nested_data.get('percentage', None),
                    subject=nested_data.get('subject', ''),
                    sport=nested_data.get('sport', ''),
                    name=nested_data.get('name', ''),
                )

            return model_a_instance

        except json.JSONDecodeError:
            raise serializers.ValidationError("Invalid JSON format in the file field.")
"""
