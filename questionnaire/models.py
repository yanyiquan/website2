import ast

from django.db import models


# Create your models here.


class Client(models.Model):
    id = models.CharField('client_id', max_length=20, primary_key=True)
    password = models.CharField('pwd', max_length=20, default='000000')

    class Meta:
        db_table = 'client'
        verbose_name = 'clientInfo'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id


class QuestionSLR(models.Model):
    id = models.IntegerField('question_id', primary_key=True)
    title = models.TextField('question_title')
    optionA = models.CharField('option_a', blank=True, max_length=500)
    optionB = models.CharField("option_b", blank=True, max_length=500)
    optionC = models.CharField("option_c", blank=True, max_length=500)
    optionD = models.CharField("option_d", blank=True, max_length=500)
    optionE = models.CharField("option_e", blank=True, max_length=500)
    textbox = models.TextField("dialogue_box", blank=True)
    textbox2 = models.TextField("dialogue_box_2", blank=True)

    @property
    def answered(self):
        return self.answer.first()

    class Meta:
        db_table = "questionSLR"
        verbose_name = 'SLR questions'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class QuestionTolerance(models.Model):
    id = models.IntegerField('question_id', primary_key=True)
    title = models.TextField('question_title')
    optionA = models.CharField('option_a', max_length=500)
    optionB = models.CharField("option_b", max_length=500)
    optionC = models.CharField("option_c", max_length=500)
    optionD = models.CharField("option_d", max_length=500)

    @property
    def answered(self):
        return self.answer.first()

    class Meta:
        db_table = "questionTolerance"
        verbose_name = 'Tolerance questions'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class QuestionInvtype(models.Model):
    id = models.IntegerField('question_id', primary_key=True)
    title = models.TextField('question_title')
    optionA = models.CharField('option_a', max_length=500)
    optionB = models.CharField("option_b", max_length=500)
    optionC = models.CharField("option_c", max_length=500)
    optionD = models.CharField("option_d", max_length=500)

    @property
    def answered(self):
        return self.answer.first()

    class Meta:
        db_table = "questionInvtype"
        verbose_name = 'Invtype questions'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class QuestionESG(models.Model):
    id = models.IntegerField('question_id', primary_key=True)
    title = models.TextField('question_title')
    optionA = models.CharField('option_a', max_length=500)
    optionB = models.CharField("option_b", blank=True, max_length=500)
    optionC = models.CharField("option_c", blank=True, max_length=500)
    optionD = models.CharField("option_d", blank=True, max_length=500)
    optiononly = models.CharField("only_option", blank=True, max_length=500)

    @property
    def answered(self):
        return self.answer.first()

    class Meta:
        db_table = "questionESG"
        verbose_name = 'ESG questions'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class QuestionTrends(models.Model):
    id = models.IntegerField('question_id', primary_key=True)
    title = models.TextField('question_title')
    optionA = models.CharField('option_a', blank=True, max_length=500)
    optionB = models.CharField("option_b", blank=True, max_length=500)
    optionC = models.CharField("option_c", blank=True, max_length=500)
    optionD = models.CharField("option_d", blank=True, max_length=500)
    optionE = models.CharField("option_e", blank=True, max_length=500)
    optionF = models.CharField("option_f", blank=True, max_length=500)
    optionG = models.CharField("option_g", blank=True, max_length=500)
    optionH = models.CharField("option_h", blank=True, max_length=500)
    optionI = models.CharField("option_i", blank=True, max_length=500)
    optionJ = models.CharField("option_j", blank=True, max_length=500)
    optionK = models.CharField("option_k", blank=True, max_length=500)
    optionL = models.CharField("option_l", blank=True, max_length=500)
    optionM = models.CharField("option_m", blank=True, max_length=500)
    optionN = models.CharField("option_n", blank=True, max_length=500)
    optionO = models.CharField("option_o", blank=True, max_length=500)
    optionP = models.CharField("option_p", blank=True, max_length=500)
    optionQ = models.CharField("option_q", blank=True, max_length=500)
    optionR = models.CharField("option_r", blank=True, max_length=500)
    optionS = models.CharField("option_s", blank=True, max_length=500)
    optionT = models.CharField("option_t", blank=True, max_length=500)
    optionU = models.CharField("option_u", blank=True, max_length=500)
    optionV = models.CharField("option_v", blank=True, max_length=500)
    optionW = models.CharField("option_w", blank=True, max_length=500)
    optiononly = models.CharField("only_option", blank=True, max_length=500)

    @property
    def answered(self):
        return self.answer.first()

    class Meta:
        db_table = "questionTrends"
        verbose_name = 'Trends questions'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Result(models.Model):
    cid = models.ForeignKey(Client, on_delete=models.CASCADE, default='')
    result = models.CharField('investor_type', max_length=100)

    class Meta:
        db_table = 'result'
        verbose_name = 'Investor type result'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '<%s:%s>' % (self.cid, self.result)


class Answer(models.Model):
    cid = models.ForeignKey(Client, on_delete=models.CASCADE, default='')
    pid = models.CharField('question_page', max_length=20)
    qid = models.CharField('question_id', max_length=10)
    answer = models.CharField('answer', max_length=5000, null=True)
    textbox = models.TextField("dialogue_box", blank=True, null=True)
    textbox2 = models.TextField("dialogue_box_2", blank=True, null=True)

    question_slr = models.ForeignKey(QuestionSLR, related_name="answer", null=True, blank=True,
                                     on_delete=models.CASCADE)
    question_esg = models.ForeignKey(QuestionESG, related_name="answer", null=True, blank=True,
                                     on_delete=models.CASCADE)
    question_trend = models.ForeignKey(QuestionTrends, related_name="answer", null=True, blank=True,
                                       on_delete=models.CASCADE)
    question_inv_type = models.ForeignKey(QuestionInvtype, related_name="answer", null=True, blank=True,
                                          on_delete=models.CASCADE)
    question_tolerance = models.ForeignKey(QuestionTolerance, related_name="answer", null=True, blank=True,
                                           on_delete=models.CASCADE)

    @property
    def answers(self):
        return ast.literal_eval(self.answer)

    class Meta:
        db_table = 'answer'
        verbose_name = 'answer'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '<%s:%s:%s>' % (self.cid, self.pid, self.qid)


class ResultSLR(models.Model):
    cid = models.ForeignKey(Client, on_delete=models.CASCADE, default='')
    slr = models.CharField('slr', max_length=100)

    class Meta:
        db_table = 'result_slr'
        verbose_name = 'SLR result'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '<%s:%s>' % (self.cid, self.slr)


class Discount(models.Model):
    income_growth = models.FloatField('income_growth_rate', blank=False)
    expense_growth = models.FloatField('expense_growth_rate', blank=False)
    discounting_factor = models.FloatField('discounting_factor', blank=False)

    class Meta:
        db_table = 'discount'
        verbose_name = 'discount parameters'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '<%s:%s:%s>' % (self.income_growth, self.expense_growth, self.discounting_factor)
