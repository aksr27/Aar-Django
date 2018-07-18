# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from login.models import AarDropdown

class Books(models.Model):
    emp_id=models.CharField(db_column='emp_id_books', max_length=150)    
    role = models.ForeignKey(AarDropdown, models.DO_NOTHING, db_column='Role',related_name='role',default=None)  # Field name made lowercase.
    role_for = models.ForeignKey(AarDropdown, models.DO_NOTHING, db_column='Role_For',default=None)  # Field name made lowercase.
    publisher_type = models.ForeignKey(AarDropdown, models.DO_NOTHING, db_column='Publisher_Type',related_name='publisher_type',default=None)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100)  # Field name made lowercase.
    edition = models.CharField(db_column='Edition',max_length=500)  # Field name made lowercase.
    published_date = models.DateField(db_column='Published_Date')  # Field name made lowercase.
    chapter = models.CharField(db_column='Chapter', max_length=500)  # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=500)  # Field name made lowercase.
    # copyright_status = models.ForeignKey(AarDropdown, models.DO_NOTHING, db_column='Copyright_Status',related_name='copyright_status',default=None)  # Field name made lowercase.
    copyright_status = models.CharField(db_column='Copyright_Status', max_length=100)  # Field name made lowercase.
    copyright_no = models.CharField(db_column='Copyright_No', max_length=100)  # Field name made lowercase.
    author = models.ForeignKey(AarDropdown, models.DO_NOTHING, db_column='Author',related_name='author',default=None)  # Field name made lowercase.
    publisher_name = models.CharField(db_column='Publisher_Name', max_length=100)  # Field name made lowercase.
    publisher_address = models.CharField(db_column='Publisher_Address', max_length=500)  # Field name made lowercase.
    publisher_zip_code = models.IntegerField(db_column='Publisher_Zip_Code')  # Field name made lowercase.
    publisher_contact = models.CharField(db_column='Publisher_Contact',max_length=50)  # Field name made lowercase.
    publisher_email = models.CharField(db_column='Publisher_Email', max_length=50)  # Field name made lowercase.
    publisher_website = models.CharField(db_column='Publisher_Website', max_length=100)  # Field name made lowercase.
    approve_status=models.CharField(db_column='book_status', max_length=100)
    class Meta:
        managed = True
        db_table = 'books'

class Researchconference(models.Model):
    emp_id=models.CharField(db_column='emp_id_conference', max_length=150)
    category = models.ForeignKey(AarDropdown,related_name='Category_Research',limit_choices_to={'field':'CATEGORY'}, on_delete=models.CASCADE, db_column='Category')  # Field name made lowercase.
    type_of_conference = models.ForeignKey(AarDropdown,related_name='Conference_Type',limit_choices_to={'field':'TYPE_OF_CONFERENCE'}, on_delete=models.CASCADE, db_column='Type_Of_Conference')  # Field name made lowercase.
    sub_category = models.ForeignKey(AarDropdown,related_name='Sub_Category_Conference', on_delete=models.CASCADE,limit_choices_to={'field':'SUB_CATEGORY'}, db_column='Sub_Category')  # Field name made lowercase.
    sponsered = models.CharField(db_column='Sponsored', max_length=1000)  # Field name made lowercase.
    conference_title = models.CharField(db_column='Conference_Title', max_length=500)  # Field name made lowercase.
    paper_title = models.CharField(db_column='Paper_Title', max_length=100)  # Field name made lowercase.
    published_date = models.DateField(db_column='Published_Date')  # Field name made lowercase.
    organized_by = models.CharField(db_column='Organized_By', max_length=500)  # Field name made lowercase.
    journal_name = models.CharField(db_column='Journal_Name', max_length=500)  # Field name made lowercase.
    volume_no = models.TextField(db_column='Volume_No')  # Field name made lowercase.
    issue_no = models.CharField(db_column='Issue_No', max_length=500)  # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=500)  # Field name made lowercase.
    page_no = models.CharField(db_column='Page_No', max_length=100)  # Field name made lowercase.
    author = models.ForeignKey(AarDropdown,related_name='Author_Conference',limit_choices_to={'field':'AUTHOR'}, on_delete=models.CASCADE, db_column='Author')  # Field name made lowercase.
    conference_from = models.DateField(db_column='Conference_From')
    conference_to = models.DateField(db_column='Conference_To')  # Field name made lowercase.
    other_description = models.CharField(db_column='Other_Description', max_length=500)  # Field name made lowercase.
    publisher_name = models.CharField(db_column='Publisher_Name', max_length=100)  # Field name made lowercase.
    publisher_address = models.CharField(db_column='Publisher_Address', max_length=500)  # Field name made lowercase.
    publisher_zip_code = models.IntegerField(db_column='Publisher_Zip_Code')  # Field name made lowercase.
    publisher_contact = models.CharField(db_column='Publisher_Contact',max_length=50)  # Field name made lowercase.
    publisher_email = models.CharField(db_column='Publisher_Email', max_length=50)  # Field name made lowercase.
    publisher_website = models.CharField(db_column='Publisher_Website', max_length=100)  # Field name made lowercase.
    others=models.CharField(db_column='other_conference',max_length=100,blank=True,null=True)
    approve_status=models.CharField(db_column='conf_status', max_length=100)
    class Meta:
        managed = True
        db_table = 'researchconference'


class Researchguidence(models.Model):
    emp_id=models.CharField(db_column='emp_id_guid', max_length=150)    
    guidence = models.ForeignKey(AarDropdown,related_name='Guidence',limit_choices_to={'field':'GUIDENCE'},on_delete= models.CASCADE, db_column='Guidence')  # Field name made lowercase.
    course = models.ForeignKey(AarDropdown,related_name='Course_Guidence',limit_choices_to={'field':'COURSE'}, on_delete=models.CASCADE, db_column='Course', blank=True, null=True)  # Field name made lowercase.
    degree=models.ForeignKey(AarDropdown,related_name='Degree',limit_choices_to={'field':'DEGREE'}, on_delete=models.CASCADE, db_column='Degree', blank=True, null=True)
    no_of_students = models.IntegerField(db_column='No_Of_Students', blank=True, null=True)  # Field name made lowercase.
    degree_awarded = models.CharField(db_column='degree_awarded', max_length=100, blank=True, null=True)  #YES OR NO Field name made lowercase.
    status = models.ForeignKey(AarDropdown,related_name='Status', on_delete=models.CASCADE,limit_choices_to={'field':'STATUS'}, db_column='Status', blank=True, null=True)  # Field name made lowercase.
    project_title = models.CharField(db_column='Project_Title', max_length=500, blank=True, null=True)  # Field name made lowercase.
    area_of_spec = models.CharField(db_column='Area_Of_Spec', max_length=100, blank=True, null=True)  # Field name made lowercase.
    approve_status=models.CharField(db_column='guid_status', max_length=100)
    class Meta:
        managed = True
        db_table = 'researchguidence'


class Researchjournal(models.Model):
    emp_id=models.CharField(db_column='emp_id_journal', max_length=150)
    category = models.ForeignKey(AarDropdown,related_name='Category_Journal',limit_choices_to={'field':'CATEGORY'}, on_delete=models.CASCADE, db_column='Category')  # Field name made lowercase.
    type_of_journal = models.ForeignKey(AarDropdown,related_name='Type_Of_Journal',limit_choices_to={'field':'TYPE_JOURNAL'}, on_delete=models.CASCADE, db_column='Type_Of_Journal')  # Field name made lowercase.
    sub_category = models.ForeignKey(AarDropdown,related_name='Sub_Category_Journal',limit_choices_to={'field':'SUB_CATEGORY'}, on_delete=models.CASCADE, db_column='Sub_Category')  # Field name made lowercase.
    published_date = models.DateField(db_column='Published_Date')  # Field name made lowercase.
    paper_title = models.CharField(db_column='Paper_Title', max_length=100)  # Field name made lowercase.
    impact_factor = models.FloatField(db_column='Impact_Factor',blank=True,null=True)  # Field name made lowercase.
    journal_name = models.CharField(db_column='Journal_Name', max_length=500)  # Field name made lowercase.
    volume_no = models.TextField(db_column='Volume_No')  # Field name made lowercase.
    issue_no = models.CharField(db_column='Issue_No', max_length=500)  # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=500)  # Field name made lowercase.
    page_no = models.CharField(db_column='Page_No', max_length=100)  # Field name made lowercase.
    author = models.ForeignKey(AarDropdown,related_name='Author_Journal',limit_choices_to={'field':'AUTHOR'}, on_delete=models.CASCADE, db_column='Author')  # Field name made lowercase.
    publisher_name = models.CharField(db_column='Publisher_Name', max_length=100)  # Field name made lowercase.
    publisher_address = models.CharField(db_column='Publisher_Address', max_length=500)  # Field name made lowercase.
    publisher_zip_code = models.IntegerField(db_column='Publisher_Zip_Code')  # Field name made lowercase.
    publisher_contact = models.CharField(db_column='Publisher_Contact',max_length=15)  # Field name made lowercase.
    publisher_email = models.CharField(db_column='Publisher_Email', max_length=50)  # Field name made lowercase.
    publisher_website = models.CharField(db_column='Publisher_Website', max_length=100)  # Field name made lowercase.
    others=models.CharField(db_column='other_journal',max_length=100,blank=True,null=True)
    approve_status=models.CharField(db_column='jour_status', max_length=100)
    class Meta:
        managed = True
        db_table = 'researchjournal'
        
class Sponsers(models.Model):
    spons_id=models.IntegerField(db_column='spons_id')
    sponser_name=models.CharField(db_column='sponsor_name',max_length=100)

    class Meta:
        managed = True
        db_table = 'Sponsers'