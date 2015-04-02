from django.db import models

class Record(models.Model):

    class Meta:
	 db_table = 'record'


class Demographic(models.Model):
    study_id = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Study ID', blank=True)
    date_enrolled = models.DateField(help_text=u'YYYY-MM-DD', null=True, verbose_name=u'Date subject signed consent', blank=True)
    file_upload = models.TextField(help_text=u'', null=True, verbose_name=u'file upload', blank=True) # This field type is a guess
    first_name = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'First Name', blank=True)
    last_name = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Last Name', blank=True)
    address = models.TextField(help_text=u'', null=True, verbose_name=u'Street, City, State, ZIP', blank=True) # This field type is a guess
    telephone_1 = models.CharField(help_text=u'Include Area Code', null=True, max_length=2000, verbose_name=u'Phone number', blank=True)
    telephone_2 = models.CharField(help_text=u'Include Area Code', null=True, max_length=2000, verbose_name=u'Second phone number', blank=True)
    sex = models.IntegerField(help_text=u'', null=True, verbose_name=u'Gender', blank=True, choices=[(0, u'Female'), (1, u'Male')]) # This field type is a guess
    email = models.EmailField(help_text=u'', null=True, verbose_name=u'E-mail', blank=True)
    num_children = models.IntegerField(help_text=u'', null=True, verbose_name=u'How many times has the subject given birth?', blank=True)
    given_birth = models.TextField(help_text=u'', null=True, verbose_name=u'Has the subject given birth before?', blank=True) # This field type is a guess
    ethnicity = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Ethnicity', choices=[(0, u'Hispanic or Latino'), (1, u'NOT Hispanic or Latino'), (2, u'Unknown / Not Reported')])
    race = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Race', choices=[(0, u'American Indian/Alaska Native'), (1, u'Asian'), (2, u'Native Hawaiian or Other Pacific Islander'), (3, u'Black or African American'), (4, u'White'), (5, u'More Than One Race'), (6, u'Unknown / Not Reported')])
    age = models.FloatField(help_text=u'', null=True, verbose_name=u'Age (years)', blank=True)
    dob = models.DateField(help_text=u'', null=True, verbose_name=u'Date of birth', blank=True)
    height = models.FloatField(help_text=u'', null=True, verbose_name=u'Height (cm)', blank=True)
    bmi = models.FloatField(help_text=u'', null=True, verbose_name=u'BMI', blank=True)
    weight = models.IntegerField(help_text=u'', null=True, verbose_name=u'Weight (kilograms)', blank=True)
    patient_document = models.TextField(help_text=u'', null=True, verbose_name=u'Patient document', blank=True) # This field type is a guess
    diabetes = models.IntegerField(help_text=u'', null=True, verbose_name=u'Patient has a diagnosis of diabetes mellitus?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    comorbidities = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Any comorbid condition', blank=True)
    diabetes_type = models.IntegerField(help_text=u'', null=True, verbose_name=u'Type of Diabetes Mellitus', blank=True, choices=[(0, u'Type 1 insulin-dependent'), (1, u'Type 2 insulin-dependent'), (2, u'Type 2 non insulin-dependent')]) # This field type is a guess
    dialysis_initiation = models.DateField(help_text=u'', null=True, verbose_name=u'Date of first outpatient dialysis treatment', blank=True)
    access_type = models.IntegerField(help_text=u'', null=True, verbose_name=u'Type of vascular access', blank=True, choices=[(0, u'Graft'), (1, u'Fistula'), (2, u'Catheter with maturing graft'), (3, u'Catheter with maturing fistula')]) # This field type is a guess
    access_location = models.IntegerField(help_text=u'', null=True, verbose_name=u'Location of currently used vascular access', blank=True, choices=[(0, u'Forearm'), (1, u'Upper arm'), (2, u'Internal jugular vein'), (3, u'Subclavian vein'), (4, u'Other')]) # This field type is a guess
    dialysis_unit_name = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Name of dialysis unit', blank=True)
    dialysis_unit_phone = models.CharField(help_text=u'Include Area Code', null=True, max_length=2000, verbose_name=u'Phone number', blank=True)
    dialysis_schedule_days = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Days of the week patient is dialyzed', choices=[(0, u'Monday-Wednesday-Friday'), (1, u'Tuesday-Thursday-Saturday'), (2, u'Other')])
    dialysis_schedule_time = models.IntegerField(help_text=u'', null=True, verbose_name=u'Shift patient is dialyzed', blank=True, choices=[(0, u'First shift'), (1, u'Second shift'), (2, u'Third shift'), (3, u'Fourth shift')]) # This field type is a guess
    subject_comments = models.TextField(help_text=u'', null=True, verbose_name=u'Comments', blank=True) # This field type is a guess
    etiology_esrd = models.IntegerField(help_text=u'', null=True, verbose_name=u'Etiology of ESRD', blank=True, choices=[(0, u'Diabetes'), (1, u'Hypertension'), (2, u'Glomerulonephritis'), (3, u'Polycystic Kidney Disease'), (4, u'Interstitial Nephritis'), (5, u'Hereditary Nephritis'), (6, u'Other')]) # This field type is a guess
    survey_1 = models.IntegerField(max_length=2000, blank=True, help_text=u'This describes the field', null=True, verbose_name=u'Test', choices=[(1, u'choice 1'), (2, u'choice 2')])
    checkbox_test_summary = models.CharField(help_text=u'0, option 1 | 1, option 2 | 2, option 3 | 3, option 4', null=True, max_length=2000, verbose_name=u'Checkbox', blank=True)
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'demographic'


class checkboxtest(models.Model):
    label = models.CharField(help_text=u'Helps the data entry person', null=True, max_length=2000, verbose_name=u'Checkbox', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'Helps the data entry person', null=True, verbose_name=u'Checkbox', choices=[(0, u'option 1'), (1, u'option 2'), (2, u'option 3'), (3, u'option 4')])
    demographic = models.ForeignKey(Demographic)

    class Meta:
	 db_table = 'checkboxtest'


