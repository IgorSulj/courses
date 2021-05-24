from rest_framework.serializers import ModelSerializer
from .models import PersonModel, CourseModel, ProfileModel


class PersonSerializer(ModelSerializer):

    class Meta:
        model = PersonModel
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    persons = PersonSerializer(many=True)

    class Meta:
        model = CourseModel
        fields = '__all__'

    def create(self, validated_data):
        persons_data = validated_data.pop('persons')
        course = CourseModel.objects.create(**validated_data)
        persons_pks = []
        for person in persons_data:
            person_db, _ = PersonModel.objects.get_or_create(**person)
            persons_pks.append(person_db)
        course.persons.set(persons_pks)
        return course

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        if 'persons' in validated_data:
            persons_pks = []
            for person in validated_data.get('persons'):
                person_db, _ = PersonModel.objects.get_or_create(**person)
                persons_pks.append(person_db)
            instance.persons.set(persons_pks)
        instance.save()
        return instance


class ProfileSerializer(ModelSerializer):

    class Meta:
        model = ProfileModel
        fields = '__all__'
        depth = 1

