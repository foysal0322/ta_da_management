from django.db import models

# Create your models here.


class Employee(models.Model):
    '''this will be the given employee name table'''
    emp_name=models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.emp_name



class TaDa(models.Model):
    '''data for tada history page...will be fetched from these table'''
    status=(('Paid','Paid'),('Unpaid','Unpaid'))
    date=models.CharField(max_length=200,null=True)
    emp_name=models.ForeignKey(Employee,on_delete=models.CASCADE,null=True,blank=True) #taken from the given 'Employee' table
    tr_cost=models.CharField(max_length=200,null=True,blank=True)
    ln_cost=models.CharField(max_length=200,null=True,blank=True)
    ins_cost=models.CharField(max_length=200,null=True,blank=True)
    paid=models.CharField(max_length=200,choices=status,blank=True)

    def __str__(self):
        return str(self.emp_name)
    def reset(self):
        self.id=None

