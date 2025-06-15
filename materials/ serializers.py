from rest_framework import serializers

from .models import Course, Lesson, Subscription, Payment
from .validators import YoutubeLinkValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        validators = [YoutubeLinkValidator(field="video_link")]
        model = Lesson
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    course_lessons = serializers.SerializerMethodField()
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    def get_lessons_count(self, obj):
        """
        Подсчет количества уроков в курсе
        """
        return Lesson.objects.filter(course=obj).count()

    def get_course_lessons(self, obj):
        """
        Список уроков в курсе
        """
        return [lesson.id for lesson in Lesson.objects.filter(course=obj)]

    def get_is_subscribed(self, obj):
        """
        Проверка, подписан ли пользователь на курс
        """
        if Subscription.objects.filter(owner=self.context["request"].user, course=obj).exists():
            return "Вы подписаны"
        else:
            return "Вы еще не подписаны"


class StaffCourseSerializer(CourseSerializer):
    """
    Сериализатор для модели Course, отображающийся модератору и админу
    """
    lessons_count = serializers.SerializerMethodField()
    course_lessons = LessonSerializer(source="lessons", many=True, read_only=True)


class PaymentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для списка объектов модели Payment
    """

    class Meta:
        model = Payment
        fields = "__all__"