from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Paragraph, WordFrequency

class ParagraphUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        text = request.data.get('text')

        if not text:
            return Response({"error": "Text is required"}, status=400)

        paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]

        for para in paragraphs:
            Paragraph.objects.create(
                user=request.user,
                text=para
            )

            words = para.lower().split()

            for word in words:
                obj, created = WordFrequency.objects.get_or_create(
                    user=request.user,
                    word=word
                )
                obj.count += 1
                obj.save()

        return Response({"message": "Paragraphs processed successfully"}, status=201)


class SearchWordView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        word = request.GET.get('word')

        if not word:
            return Response({"error": "Word is required"}, status=400)

        word = word.lower().strip()

        paragraphs = Paragraph.objects.filter(
            user=request.user,
            text__icontains=word
        )

        ranked = sorted(
            paragraphs,
            key=lambda p: p.text.lower().split().count(word),
            reverse=True
        )

        top_10 = ranked[:10]

        result = [
            {
                "id": p.id,
                "text": p.text
            }
            for p in top_10
        ]

        return Response(result, status=200)