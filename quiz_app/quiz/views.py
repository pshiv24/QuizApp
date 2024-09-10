from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Quiz, Question, Answer, Result
from .serializers import QuizSerializer, AnswerSerializer, ResultSerializer
from rest_framework.permissions import IsAuthenticated

class CreateQuizView(APIView):
    def post(self, request):
        title = request.data.get('title')
        questions_data = request.data.get('questions')

        quiz = Quiz.objects.create(title=title)

        for question_data in questions_data:
            Question.objects.create(
                quiz=quiz,
                text=question_data['text'],
                options=question_data['options'],
                correct_option=question_data['correct_option']
            )

        return Response({'quiz_id': quiz.id}, status=status.HTTP_201_CREATED)


class GetQuizView(APIView):
    def get(self, request, quiz_id):
        quiz = Quiz.objects.get(id=quiz_id)
        serializer = QuizSerializer(quiz)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SubmitAnswerView(APIView):
    def post(self, request, question_id):
        question = Question.objects.get(id=question_id)
        selected_option = request.data.get('selected_option')
        is_correct = selected_option == question.correct_option

        answer = Answer.objects.create(
            question=question,
            selected_option=selected_option,
            is_correct=is_correct
        )

        return Response({
            'is_correct': is_correct,
            'correct_option': question.correct_option if not is_correct else None
        }, status=status.HTTP_200_OK)



class GetResultsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, quiz_id):
        # Get the logged-in user's ID
        print(request)
        user_id = request.user.id
        print("userrrrr",user_id)
        
        # Fetch the result for the quiz and the logged-in user
        result = Result.objects.filter(quiz_id=quiz_id, user_id=user_id).first()
        
        if result:
            serializer = ResultSerializer(result)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Result not found'}, status=status.HTTP_404_NOT_FOUND)
