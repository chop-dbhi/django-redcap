class Demographics(models.Model):
    study_id = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Study ID', blank=True)
    checkbox_test = models.IntegerField(max_length=2000, blank=True, help_text='Helps the data entry person', null=True, verbose_name='Checkbox', choices=[(0, 'option 1'), (1, 'option 2'), (2, 'option 3'), (3, 'option 4')])
    date_enrolled = models.DateField(help_text='YYYY-MM-DD', null=True, verbose_name='Date subject signed consent', blank=True)
    file_upload = models.TextField(help_text='', null=True, verbose_name='file upload', blank=True) # This field type is a guess
    first_name = models.CharField(help_text='', null=True, max_length=2000, verbose_name='First Name', blank=True)
    last_name = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Last Name', blank=True)
    address = models.TextField(help_text='', null=True, verbose_name='Street, City, State, ZIP', blank=True) # This field type is a guess
    telephone_1 = models.CharField(help_text='Include Area Code', null=True, max_length=2000, verbose_name='Phone number', blank=True)
    telephone_2 = models.CharField(help_text='Include Area Code', null=True, max_length=2000, verbose_name='Second phone number', blank=True)
    sex = models.IntegerField(help_text='', null=True, verbose_name='Gender', blank=True, choices=[(0, 'Female'), (1, 'Male')]) # This field type is a guess
    email = models.EmailField(help_text='', null=True, verbose_name='E-mail', blank=True)
    num_children = models.IntegerField(help_text='', null=True, verbose_name='How many times has the subject given birth?', blank=True)
    given_birth = models.TextField(help_text='', null=True, verbose_name='Has the subject given birth before?', blank=True) # This field type is a guess
    ethnicity = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Ethnicity', choices=[(0, 'Hispanic or Latino'), (1, 'NOT Hispanic or Latino'), (2, 'Unknown / Not Reported')])
    race = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Race', choices=[(0, 'American Indian/Alaska Native'), (1, 'Asian'), (2, 'Native Hawaiian or Other Pacific Islander'), (3, 'Black or African American'), (4, 'White'), (5, 'More Than One Race'), (6, 'Unknown / Not Reported')])
    age = models.FloatField(help_text='', null=True, verbose_name='Age (years)', blank=True)
    dob = models.DateField(help_text='', null=True, verbose_name='Date of birth', blank=True)
    height = models.FloatField(help_text='', null=True, verbose_name='Height (cm)', blank=True)
    bmi = models.FloatField(help_text='', null=True, verbose_name='BMI', blank=True)
    weight = models.IntegerField(help_text='', null=True, verbose_name='Weight (kilograms)', blank=True)
    patient_document = models.TextField(help_text='', null=True, verbose_name='Patient document', blank=True) # This field type is a guess
    diabetes = models.IntegerField(help_text='', null=True, verbose_name='Patient has a diagnosis of diabetes mellitus?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    comorbidities = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Any comorbid condition', blank=True)
    diabetes_type = models.IntegerField(help_text='', null=True, verbose_name='Type of Diabetes Mellitus', blank=True, choices=[(0, 'Type 1 insulin-dependent'), (1, 'Type 2 insulin-dependent'), (2, 'Type 2 non insulin-dependent')]) # This field type is a guess
    dialysis_initiation = models.DateField(help_text='', null=True, verbose_name='Date of first outpatient dialysis treatment', blank=True)
    access_type = models.IntegerField(help_text='', null=True, verbose_name='Type of vascular access', blank=True, choices=[(0, 'Graft'), (1, 'Fistula'), (2, 'Catheter with maturing graft'), (3, 'Catheter with maturing fistula')]) # This field type is a guess
    access_location = models.IntegerField(help_text='', null=True, verbose_name='Location of currently used vascular access', blank=True, choices=[(0, 'Forearm'), (1, 'Upper arm'), (2, 'Internal jugular vein'), (3, 'Subclavian vein'), (4, 'Other')]) # This field type is a guess
    dialysis_unit_name = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Name of dialysis unit', blank=True)
    dialysis_unit_phone = models.CharField(help_text='Include Area Code', null=True, max_length=2000, verbose_name='Phone number', blank=True)
    dialysis_schedule_days = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Days of the week patient is dialyzed', choices=[(0, 'Monday-Wednesday-Friday'), (1, 'Tuesday-Thursday-Saturday'), (2, 'Other')])
    dialysis_schedule_time = models.IntegerField(help_text='', null=True, verbose_name='Shift patient is dialyzed', blank=True, choices=[(0, 'First shift'), (1, 'Second shift'), (2, 'Third shift'), (3, 'Fourth shift')]) # This field type is a guess
    subject_comments = models.TextField(help_text='', null=True, verbose_name='Comments', blank=True) # This field type is a guess
    etiology_esrd = models.IntegerField(help_text='', null=True, verbose_name='Etiology of ESRD', blank=True, choices=[(0, 'Diabetes'), (1, 'Hypertension'), (2, 'Glomerulonephritis'), (3, 'Polycystic Kidney Disease'), (4, 'Interstitial Nephritis'), (5, 'Hereditary Nephritis'), (6, 'Other')]) # This field type is a guess
    survey_1 = models.IntegerField(max_length=2000, blank=True, help_text='This describes the field', null=True, verbose_name='Test', choices=[(1, 'choice 1'), (2, 'choice 2')])

    class Meta:
	 db_table = 'Demographics'


