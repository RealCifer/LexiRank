from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Paragraph, WordFrequency


# 🔹 Upload API
class ParagraphUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        text = request.data.get('text')

        if not text:
            return Response({"error": "Text is required"}, status=400)

        paragraphs = text.split("\n\n")

        for para in paragraphs:
            para_obj = Paragraph.objects.create(
                user=request.user,
                text=para
            )

            words = para.split()

            for word in words:
                word = word.lower()

                obj, created = WordFrequency.objects.get_or_create(
                    user=request.user,
                    word=word
                )

                obj.count += 1
                obj.save()

        return Response({"message": "Paragraphs processed successfully"})


# 🔥 STEP 5 → ADD THIS BELOW
class SearchWordView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        word = request.GET.get('word')

        if not word:
            return Response({"error": "Word is required"}, status=400)

        word = word.lower()

        paragraphs = Paragraph.objects.filter(
            user=request.user,
            text__icontains=word
        )

        ranked = sorted(
            paragraphs,
            key=lambda p: p.text.lower().count(word),
            reverse=True
        )

        top_10 = ranked[:10]

        result = [
            {"id": p.id, "text": p.text}
            for p in top_10
        ]

        return Response(result)