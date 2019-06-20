from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

User = get_user_model()

class LtCommonField(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class LtLotteryCategory(LtCommonField):
    amount = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=255)
    max_winning_amount = models.PositiveIntegerField()

    class Meta:
        db_table = "lt_lottery_category"
        verbose_name = "Lottery Category"


class LtLottery(LtCommonField):
    # STATUS = (("yt", "Yet to start"), ("ip", "In Progress"), ("fn", "Finished"))
    category = models.ForeignKey(LtLotteryCategory, related_name="category_lottery", null=True,
                                 on_delete=models.SET_NULL)
    time_to_end = models.DateTimeField()
    time_started = models.DateTimeField()
    # status = models.CharField(max_length=2, choices=STATUS, default="yt")
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Lottery"
        verbose_name_plural = "Lotteries"


class LtLotteryPlayers(LtCommonField):
    lottery = models.ForeignKey(LtLottery, related_name="lottery_players", on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, related_name="played_lotteries", on_delete=models.SET_NULL, null=True)
    joined_at = models.DateTimeField(auto_now=True)
    # number = models.PositiveIntegerField()
    is_winner = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Lottery Players"


class LtCredit(LtCommonField):
    user = models.ForeignKey(User, related_name="my_credit", on_delete=models.SET_NULL, null=True)
    credit = models.PositiveIntegerField()
    updated_by = models.ForeignKey(User, related_name="updated_credits", on_delete=models.SET_NULL, null=True)


class LtCreditHistory(LtCommonField):
    user = models.ForeignKey(User, related_name="my_credit_history", on_delete=models.SET_NULL, null=True)
    mode_of_payment = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()



