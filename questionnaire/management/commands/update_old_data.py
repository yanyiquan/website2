from django.core.management.base import BaseCommand

from questionnaire.models import Answer, QuestionSLR, QuestionTolerance, QuestionESG, QuestionTrends, QuestionInvtype


class Command(BaseCommand):
    help = 'Update old data'

    def handle(self, *args, **kwargs):
        answers = Answer.objects.all()
        for a in answers:
            if a.pid == "SLR" and a.question_slr is None:
                q = QuestionSLR.objects.filter(id=a.qid).first()
                a.question_slr = q
                a.textbox = a.answer
                a.textbox2 = a.answer
                a.save()
            if a.pid in ["tolerance", "ESG", "Trends", "invtype"]:
                if a.id == "tolerance":
                    q = QuestionTolerance.objects.filter(id=a.qid).first()
                    a.question_tolerance = q
                elif a.pid == "ESG":
                    q = QuestionESG.objects.filter(id=a.qid).first()
                    a.question_esg = q
                elif a.pid == "Trends":
                    q = QuestionTrends.objects.filter(id=a.qid).first()
                    a.question_trend = q
                else:
                    q = QuestionInvtype.objects.filter(id=a.qid).first()
                    a.question_inv_type = q
                a.save()
