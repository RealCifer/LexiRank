from celery import shared_task
from .models import Paragraph, WordFrequency


@shared_task
def process_paragraphs(user_id, text):
    paragraphs = text.split("\n\n")

    for para in paragraphs:
        para_obj = Paragraph.objects.create(
            user_id=user_id,
            text=para
        )

        words = para.split()

        for word in words:
            word = word.lower()

            obj, created = WordFrequency.objects.get_or_create(
                user_id=user_id,
                word=word
            )

            obj.count += 1
            obj.save()