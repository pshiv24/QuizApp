from django.urls import path
from .views import CreateQuizView, GetQuizView, SubmitAnswerView, GetResultsView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('quiz/create/', CreateQuizView.as_view(), name='create_quiz'),
    path('quiz/<int:quiz_id>/', GetQuizView.as_view(), name='get_quiz'),
    path('question/<int:question_id>/submit/', SubmitAnswerView.as_view(), name='submit_answer'),
    path('quiz/<int:quiz_id>/results/', GetResultsView.as_view(), name='get_results'),
]
