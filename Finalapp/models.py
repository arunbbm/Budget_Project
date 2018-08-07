from django.db import models

# Create your models here.
class Budget(models.Model):
    client_name=models.CharField(max_length=264)
    client_id=models.AutoField(primary_key=True)
    client_phone=models.CharField(max_length=264)
    client_email=models.EmailField(max_length=264)
    client_purpose=models.CharField(max_length=264)
    client_chequeno=models.CharField(max_length=264)
    client_chequeamount=models.CharField(max_length=264)
    client_issuedate=models.DateField(max_length=264)
    client_chequedate=models.DateField(max_length=264)
    client_preparedby=models.CharField(max_length=264)
    client_signedby=models.CharField(max_length=264)
    client_bankname=models.CharField(max_length=264)
    client_branchname=models.CharField(max_length=264)
    client_chequestatus=models.CharField(max_length=264)
    client_cleareddata=models.CharField(max_length=264)
    client_remarks=models.CharField(max_length=264)

    def __str__(self):
        return self.client_name

class Expense(models.Model):
    E_recivername=models.CharField(max_length=264)
    E_month=models.CharField(max_length=264)
    E_email=models.EmailField(max_length=264)
    E_purpose=models.CharField(max_length=264)
    E_expenseamount=models.CharField(max_length=264)
    E_previous_due_date=models.CharField(max_length=264)
    E_total_expense_amount=models.CharField(max_length=264)
    E_planned_period_of_payment=models.CharField(max_length=264)
    E_actual_period_of_payment=models.CharField(max_length=264)
    E_amount_paid=models.CharField(max_length=264)
    E_date_of_payment=models.CharField(max_length=264)
    E_mode_of_payment=models.CharField(max_length=264)
    E_dd_no=models.CharField(max_length=264)
    E_cheque_no=models.CharField(max_length=264)
    E_transaction_no=models.CharField(max_length=264)
    E_cheque_date=models.CharField(max_length=264)
    E_dd_date=models.CharField(max_length=264)
    E_transaction_date=models.CharField(max_length=264)
    E_total_due_amount=models.CharField(max_length=264)
    E_payment_status=models.CharField(max_length=264)

    def __str__(self):
        return self.E_recivername

class Collection(models.Model):
    C_date=models.CharField(max_length=264)
    C_mode_of_payment=models.CharField(max_length=264)
    C_amount_paid=models.CharField(max_length=264)
    def __str__(self):
        return self.C_date
