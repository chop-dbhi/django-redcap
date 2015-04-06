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


class BaselineDatum(models.Model):
    study_id_display = models.FloatField(help_text=u'', null=True, verbose_name=u'study_id', blank=True)
    date_visit_b = models.DateField(help_text=u'', null=True, verbose_name=u'Date of baseline visit', blank=True)
    date_blood_b = models.DateField(help_text=u'', null=True, verbose_name=u'Date blood was drawn', blank=True)
    alb_b = models.IntegerField(help_text=u'', null=True, verbose_name=u'Serum Albumin (g/dL)', blank=True)
    prealb_b = models.FloatField(help_text=u'', null=True, verbose_name=u'Serum Prealbumin (mg/dL)', blank=True)
    creat_b = models.FloatField(help_text=u'', null=True, verbose_name=u'Creatinine (mg/dL)', blank=True)
    npcr_b = models.FloatField(help_text=u'', null=True, verbose_name=u'Normalized Protein Catabolic Rate (g/kg/d)', blank=True)
    chol_b = models.FloatField(help_text=u'', null=True, verbose_name=u'Cholesterol (mg/dL)', blank=True)
    transferrin_b = models.FloatField(help_text=u'', null=True, verbose_name=u'Transferrin (mg/dL)', blank=True)
    kt_v_b = models.FloatField(help_text=u'', null=True, verbose_name=u'Kt/V', blank=True)
    drywt_b = models.FloatField(help_text=u'', null=True, verbose_name=u'Dry weight (kilograms)', blank=True)
    plasma1_b = models.IntegerField(help_text=u'', null=True, verbose_name=u'Collected Plasma 1?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    plasma2_b = models.IntegerField(help_text=u'', null=True, verbose_name=u'Collected Plasma 2?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    plasma3_b = models.IntegerField(help_text=u'', null=True, verbose_name=u'Collected Plasma 3?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    serum1_b = models.IntegerField(help_text=u'', null=True, verbose_name=u'Collected Serum 1?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    serum2_b = models.IntegerField(help_text=u'', null=True, verbose_name=u'Collected Serum 2?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    serum3_b = models.IntegerField(help_text=u'', null=True, verbose_name=u'Collected Serum 3?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    sga_b = models.FloatField(help_text=u'', null=True, verbose_name=u'Subject Global Assessment (score = 1-7)', blank=True)
    date_supplement_dispensed = models.DateField(help_text=u'', null=True, verbose_name=u'Date patient begins supplement', blank=True)
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'baselinedatum'


class Month1Datum(models.Model):
    date_visit_1 = models.DateField(help_text=u'', null=True, verbose_name=u'Date of Month 1 visit', blank=True)
    alb_1 = models.FloatField(help_text=u'', null=True, verbose_name=u'Serum Albumin (g/dL)', blank=True)
    prealb_1 = models.FloatField(help_text=u'', null=True, verbose_name=u'Serum Prealbumin (mg/dL)', blank=True)
    creat_1 = models.FloatField(help_text=u'', null=True, verbose_name=u'Creatinine (mg/dL)', blank=True)
    npcr_1 = models.FloatField(help_text=u'', null=True, verbose_name=u'Normalized Protein Catabolic Rate (g/kg/d)', blank=True)
    chol_1 = models.FloatField(help_text=u'', null=True, verbose_name=u'Cholesterol (mg/dL)', blank=True)
    transferrin_1 = models.FloatField(help_text=u'', null=True, verbose_name=u'Transferrin (mg/dL)', blank=True)
    kt_v_1 = models.FloatField(help_text=u'', null=True, verbose_name=u'Kt/V', blank=True)
    drywt_1 = models.FloatField(help_text=u'', null=True, verbose_name=u'Dry weight (kilograms)', blank=True)
    no_show_1 = models.FloatField(help_text=u'', null=True, verbose_name=u'Number of treatments missed', blank=True)
    compliance_1 = models.IntegerField(help_text=u'', null=True, verbose_name=u'How compliant was the patient in drinking the supplement?', blank=True, choices=[(0, u'100 percent'), (1, u'99-75 percent'), (2, u'74-50 percent'), (3, u'49-25 percent'), (4, u'0-24 percent')]) # This field type is a guess
    hospit_1 = models.IntegerField(help_text=u'', null=True, verbose_name=u'Was patient hospitalized since last visit?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    cause_hosp_1 = models.IntegerField(help_text=u'', null=True, verbose_name=u'What was the cause of hospitalization?', blank=True, choices=[(1, u'Vascular access related events'), (2, u'CVD events'), (3, u'Other')]) # This field type is a guess
    admission_date_1 = models.DateField(help_text=u'', null=True, verbose_name=u'Date of hospital admission', blank=True)
    discharge_date_1 = models.DateField(help_text=u'', null=True, verbose_name=u'Date of hospital discharge', blank=True)
    discharge_summary_1 = models.IntegerField(help_text=u'', null=True, verbose_name=u'Discharge summary in patients binder?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    death_1 = models.IntegerField(help_text=u'', null=True, verbose_name=u'Has patient died since last visit?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    date_death_1 = models.DateField(help_text=u'', null=True, verbose_name=u'Date of death', blank=True)
    cause_death_1 = models.IntegerField(help_text=u'', null=True, verbose_name=u'What was the cause of death?', blank=True, choices=[(1, u'All-cause'), (2, u'Cardiovascular')]) # This field type is a guess
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'month1datum'


class Month2Datum(models.Model):
    date_visit_2 = models.DateField(help_text=u'', null=True, verbose_name=u'Date of Month 2 visit', blank=True)
    alb_2 = models.FloatField(help_text=u'', null=True, verbose_name=u'Serum Albumin (g/dL)', blank=True)
    prealb_2 = models.FloatField(help_text=u'', null=True, verbose_name=u'Serum Prealbumin (mg/dL)', blank=True)
    creat_2 = models.FloatField(help_text=u'', null=True, verbose_name=u'Creatinine (mg/dL)', blank=True)
    npcr_2 = models.FloatField(help_text=u'', null=True, verbose_name=u'Normalized Protein Catabolic Rate (g/kg/d)', blank=True)
    chol_2 = models.FloatField(help_text=u'', null=True, verbose_name=u'Cholesterol (mg/dL)', blank=True)
    transferrin_2 = models.FloatField(help_text=u'', null=True, verbose_name=u'Transferrin (mg/dL)', blank=True)
    kt_v_2 = models.FloatField(help_text=u'', null=True, verbose_name=u'Kt/V', blank=True)
    drywt_2 = models.FloatField(help_text=u'', null=True, verbose_name=u'Dry weight (kilograms)', blank=True)
    no_show_2 = models.FloatField(help_text=u'', null=True, verbose_name=u'Number of treatments missed', blank=True)
    compliance_2 = models.IntegerField(help_text=u'', null=True, verbose_name=u'How compliant was the patient in drinking the supplement?', blank=True, choices=[(0, u'100 percent'), (1, u'99-75 percent'), (2, u'74-50 percent'), (3, u'49-25 percent'), (4, u'0-24 percent')]) # This field type is a guess
    hospit_2 = models.IntegerField(help_text=u'', null=True, verbose_name=u'Was patient hospitalized since last visit?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    cause_hosp_2 = models.IntegerField(help_text=u'', null=True, verbose_name=u'What was the cause of hospitalization?', blank=True, choices=[(1, u'Vascular access related events'), (2, u'CVD events'), (3, u'Other')]) # This field type is a guess
    admission_date_2 = models.DateField(help_text=u'', null=True, verbose_name=u'Date of hospital admission', blank=True)
    discharge_date_2 = models.DateField(help_text=u'', null=True, verbose_name=u'Date of hospital discharge', blank=True)
    discharge_summary_2 = models.IntegerField(help_text=u'', null=True, verbose_name=u'Discharge summary in patients binder?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    death_2 = models.IntegerField(help_text=u'', null=True, verbose_name=u'Has patient died since last visit?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    date_death_2 = models.DateField(help_text=u'', null=True, verbose_name=u'Date of death', blank=True)
    cause_death_2 = models.IntegerField(help_text=u'', null=True, verbose_name=u'What was the cause of death?', blank=True, choices=[(1, u'All-cause'), (2, u'Cardiovascular')]) # This field type is a guess
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'month2datum'


class Month3Datum(models.Model):
    date_visit_3 = models.DateField(help_text=u'', null=True, verbose_name=u'Date of Month 3 visit', blank=True)
    date_blood_3 = models.DateField(help_text=u'', null=True, verbose_name=u'Date blood was drawn', blank=True)
    alb_3 = models.FloatField(help_text=u'', null=True, verbose_name=u'Serum Albumin (g/dL)', blank=True)
    prealb_3 = models.FloatField(help_text=u'', null=True, verbose_name=u'Serum Prealbumin (mg/dL)', blank=True)
    creat_3 = models.FloatField(help_text=u'', null=True, verbose_name=u'Creatinine (mg/dL)', blank=True)
    npcr_3 = models.FloatField(help_text=u'', null=True, verbose_name=u'Normalized Protein Catabolic Rate (g/kg/d)', blank=True)
    chol_3 = models.FloatField(help_text=u'', null=True, verbose_name=u'Cholesterol (mg/dL)', blank=True)
    transferrin_3 = models.FloatField(help_text=u'', null=True, verbose_name=u'Transferrin (mg/dL)', blank=True)
    kt_v_3 = models.FloatField(help_text=u'', null=True, verbose_name=u'Kt/V', blank=True)
    drywt_3 = models.FloatField(help_text=u'', null=True, verbose_name=u'Dry weight (kilograms)', blank=True)
    plasma1_3 = models.IntegerField(help_text=u'', null=True, verbose_name=u'Collected Plasma 1?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    plasma2_3 = models.IntegerField(help_text=u'', null=True, verbose_name=u'Collected Plasma 2?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    plasma3_3 = models.IntegerField(help_text=u'', null=True, verbose_name=u'Collected Plasma 3?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    serum1_3 = models.IntegerField(help_text=u'', null=True, verbose_name=u'Collected Serum 1?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    serum2_3 = models.IntegerField(help_text=u'', null=True, verbose_name=u'Collected Serum 2?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    serum3_3 = models.IntegerField(help_text=u'', null=True, verbose_name=u'Collected Serum 3?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    sga_3 = models.FloatField(help_text=u'', null=True, verbose_name=u'Subject Global Assessment (score = 1-7)', blank=True)
    no_show_3 = models.FloatField(help_text=u'', null=True, verbose_name=u'Number of treatments missed', blank=True)
    compliance_3 = models.IntegerField(help_text=u'', null=True, verbose_name=u'How compliant was the patient in drinking the supplement?', blank=True, choices=[(0, u'100 percent'), (1, u'99-75 percent'), (2, u'74-50 percent'), (3, u'49-25 percent'), (4, u'0-24 percent')]) # This field type is a guess
    hospit_3 = models.IntegerField(help_text=u'', null=True, verbose_name=u'Was patient hospitalized since last visit?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    cause_hosp_3 = models.IntegerField(help_text=u'', null=True, verbose_name=u'What was the cause of hospitalization?', blank=True, choices=[(1, u'Vascular access related events'), (2, u'CVD events'), (3, u'Other')]) # This field type is a guess
    admission_date_3 = models.DateField(help_text=u'', null=True, verbose_name=u'Date of hospital admission', blank=True)
    discharge_date_3 = models.DateField(help_text=u'', null=True, verbose_name=u'Date of hospital discharge', blank=True)
    discharge_summary_3 = models.IntegerField(help_text=u'', null=True, verbose_name=u'Discharge summary in patients binder?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    death_3 = models.IntegerField(help_text=u'', null=True, verbose_name=u'Has patient died since last visit?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    date_death_3 = models.DateField(help_text=u'', null=True, verbose_name=u'Date of death', blank=True)
    cause_death_3 = models.IntegerField(help_text=u'', null=True, verbose_name=u'What was the cause of death?', blank=True, choices=[(1, u'All-cause'), (2, u'Cardiovascular')]) # This field type is a guess
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'month3datum'


class Month4Datum(models.Model):
    date_visit_4 = models.DateField(help_text=u'', null=True, verbose_name=u'Date of Month 4 visit', blank=True)
    alb_4 = models.FloatField(help_text=u'', null=True, verbose_name=u'Serum Albumin (g/dL)', blank=True)
    prealb_4 = models.FloatField(help_text=u'', null=True, verbose_name=u'Serum Prealbumin (mg/dL)', blank=True)
    creat_4 = models.FloatField(help_text=u'', null=True, verbose_name=u'Creatinine (mg/dL)', blank=True)
    npcr_4 = models.FloatField(help_text=u'', null=True, verbose_name=u'Normalized Protein Catabolic Rate (g/kg/d)', blank=True)
    chol_4 = models.FloatField(help_text=u'', null=True, verbose_name=u'Cholesterol (mg/dL)', blank=True)
    transferrin_4 = models.FloatField(help_text=u'', null=True, verbose_name=u'Transferrin (mg/dL)', blank=True)
    kt_v_4 = models.FloatField(help_text=u'', null=True, verbose_name=u'Kt/V', blank=True)
    drywt_4 = models.FloatField(help_text=u'', null=True, verbose_name=u'Dry weight (kilograms)', blank=True)
    no_show_4 = models.FloatField(help_text=u'', null=True, verbose_name=u'Number of treatments missed', blank=True)
    compliance_4 = models.IntegerField(help_text=u'', null=True, verbose_name=u'How compliant was the patient in drinking the supplement?', blank=True, choices=[(0, u'100 percent'), (1, u'99-75 percent'), (2, u'74-50 percent'), (3, u'49-25 percent'), (4, u'0-24 percent')]) # This field type is a guess
    hospit_4 = models.IntegerField(help_text=u'', null=True, verbose_name=u'Was patient hospitalized since last visit?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    cause_hosp_4 = models.IntegerField(help_text=u'', null=True, verbose_name=u'What was the cause of hospitalization?', blank=True, choices=[(1, u'Vascular access related events'), (2, u'CVD events'), (3, u'Other')]) # This field type is a guess
    admission_date_4 = models.DateField(help_text=u'', null=True, verbose_name=u'Date of hospital admission', blank=True)
    discharge_date_4 = models.DateField(help_text=u'', null=True, verbose_name=u'Date of hospital discharge', blank=True)
    discharge_summary_4 = models.IntegerField(help_text=u'', null=True, verbose_name=u'Discharge summary in patients binder?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    death_4 = models.IntegerField(help_text=u'', null=True, verbose_name=u'Has patient died since last visit?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    date_death_4 = models.DateField(help_text=u'', null=True, verbose_name=u'Date of death', blank=True)
    cause_death_4 = models.IntegerField(help_text=u'', null=True, verbose_name=u'What was the cause of death?', blank=True, choices=[(1, u'All-cause'), (2, u'Cardiovascular')]) # This field type is a guess
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'month4datum'


class Month5Datum(models.Model):
    date_visit_5 = models.DateField(help_text=u'', null=True, verbose_name=u'Date of Month 5 visit', blank=True)
    alb_5 = models.FloatField(help_text=u'', null=True, verbose_name=u'Serum Albumin (g/dL)', blank=True)
    prealb_5 = models.FloatField(help_text=u'', null=True, verbose_name=u'Serum Prealbumin (mg/dL)', blank=True)
    creat_5 = models.FloatField(help_text=u'', null=True, verbose_name=u'Creatinine (mg/dL)', blank=True)
    npcr_5 = models.FloatField(help_text=u'', null=True, verbose_name=u'Normalized Protein Catabolic Rate (g/kg/d)', blank=True)
    chol_5 = models.FloatField(help_text=u'', null=True, verbose_name=u'Cholesterol (mg/dL)', blank=True)
    transferrin_5 = models.FloatField(help_text=u'', null=True, verbose_name=u'Transferrin (mg/dL)', blank=True)
    kt_v_5 = models.FloatField(help_text=u'', null=True, verbose_name=u'Kt/V', blank=True)
    drywt_5 = models.FloatField(help_text=u'', null=True, verbose_name=u'Dry weight (kilograms)', blank=True)
    no_show_5 = models.FloatField(help_text=u'', null=True, verbose_name=u'Number of treatments missed', blank=True)
    compliance_5 = models.IntegerField(help_text=u'', null=True, verbose_name=u'How compliant was the patient in drinking the supplement?', blank=True, choices=[(0, u'100 percent'), (1, u'99-75 percent'), (2, u'74-50 percent'), (3, u'49-25 percent'), (4, u'0-24 percent')]) # This field type is a guess
    hospit_5 = models.IntegerField(help_text=u'', null=True, verbose_name=u'Was patient hospitalized since last visit?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    cause_hosp_5 = models.IntegerField(help_text=u'', null=True, verbose_name=u'What was the cause of hospitalization?', blank=True, choices=[(1, u'Vascular access related events'), (2, u'CVD events'), (3, u'Other')]) # This field type is a guess
    admission_date_5 = models.DateField(help_text=u'', null=True, verbose_name=u'Date of hospital admission', blank=True)
    discharge_date_5 = models.DateField(help_text=u'', null=True, verbose_name=u'Date of hospital discharge', blank=True)
    discharge_summary_5 = models.IntegerField(help_text=u'', null=True, verbose_name=u'Discharge summary in patients binder?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    death_5 = models.IntegerField(help_text=u'', null=True, verbose_name=u'Has patient died since last visit?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    date_death_5 = models.DateField(help_text=u'', null=True, verbose_name=u'Date of death', blank=True)
    cause_death_5 = models.IntegerField(help_text=u'', null=True, verbose_name=u'What was the cause of death?', blank=True, choices=[(1, u'All-cause'), (2, u'Cardiovascular')]) # This field type is a guess
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'month5datum'


class Month6Datum(models.Model):
    date_visit_6 = models.DateField(help_text=u'', null=True, verbose_name=u'Date of Month 6 visit', blank=True)
    date_blood_6 = models.DateField(help_text=u'', null=True, verbose_name=u'Date blood was drawn', blank=True)
    alb_6 = models.FloatField(help_text=u'', null=True, verbose_name=u'Serum Albumin (g/dL)', blank=True)
    prealb_6 = models.FloatField(help_text=u'', null=True, verbose_name=u'Serum Prealbumin (mg/dL)', blank=True)
    creat_6 = models.FloatField(help_text=u'', null=True, verbose_name=u'Creatinine (mg/dL)', blank=True)
    npcr_6 = models.FloatField(help_text=u'', null=True, verbose_name=u'Normalized Protein Catabolic Rate (g/kg/d)', blank=True)
    chol_6 = models.FloatField(help_text=u'', null=True, verbose_name=u'Cholesterol (mg/dL)', blank=True)
    transferrin_6 = models.FloatField(help_text=u'', null=True, verbose_name=u'Transferrin (mg/dL)', blank=True)
    kt_v_6 = models.FloatField(help_text=u'', null=True, verbose_name=u'Kt/V', blank=True)
    drywt_6 = models.FloatField(help_text=u'', null=True, verbose_name=u'Dry weight (kilograms)', blank=True)
    plasma1_6 = models.IntegerField(help_text=u'', null=True, verbose_name=u'Collected Plasma 1?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    plasma2_6 = models.IntegerField(help_text=u'', null=True, verbose_name=u'Collected Plasma 2?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    plasma3_6 = models.IntegerField(help_text=u'', null=True, verbose_name=u'Collected Plasma 3?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    serum1_6 = models.IntegerField(help_text=u'', null=True, verbose_name=u'Collected Serum 1?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    serum2_6 = models.IntegerField(help_text=u'', null=True, verbose_name=u'Collected Serum 2?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    serum3_6 = models.IntegerField(help_text=u'', null=True, verbose_name=u'Collected Serum 3?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    sga_6 = models.FloatField(help_text=u'', null=True, verbose_name=u'Subject Global Assessment (score = 1-7)', blank=True)
    no_show_6 = models.FloatField(help_text=u'', null=True, verbose_name=u'Number of treatments missed', blank=True)
    compliance_6 = models.IntegerField(help_text=u'', null=True, verbose_name=u'How compliant was the patient in drinking the supplement?', blank=True, choices=[(0, u'100 percent'), (1, u'99-75 percent'), (2, u'74-50 percent'), (3, u'49-25 percent'), (4, u'0-24 percent')]) # This field type is a guess
    hospit_6 = models.IntegerField(help_text=u'', null=True, verbose_name=u'Was patient hospitalized since last visit?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    cause_hosp_6 = models.IntegerField(help_text=u'', null=True, verbose_name=u'What was the cause of hospitalization?', blank=True, choices=[(1, u'Vascular access related events'), (2, u'CVD events'), (3, u'Other')]) # This field type is a guess
    admission_date_6 = models.DateField(help_text=u'', null=True, verbose_name=u'Date of hospital admission', blank=True)
    discharge_date_6 = models.DateField(help_text=u'', null=True, verbose_name=u'Date of hospital discharge', blank=True)
    discharge_summary_6 = models.IntegerField(help_text=u'', null=True, verbose_name=u'Discharge summary in patients binder?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    death_6 = models.IntegerField(help_text=u'', null=True, verbose_name=u'Has patient died since last visit?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    date_death_6 = models.DateField(help_text=u'', null=True, verbose_name=u'Date of death', blank=True)
    cause_death_6 = models.IntegerField(help_text=u'', null=True, verbose_name=u'What was the cause of death?', blank=True, choices=[(1, u'All-cause'), (2, u'Cardiovascular')]) # This field type is a guess
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'month6datum'


class CompletionDatum(models.Model):
    complete_study = models.IntegerField(help_text=u'', null=True, verbose_name=u'Has patient completed study?', blank=True, choices=[(0, u'No'), (1, u'Yes')]) # This field type is a guess
    withdraw_date = models.DateField(help_text=u'', null=True, verbose_name=u'Put a date if patient withdrew study', blank=True)
    withdraw_reason = models.IntegerField(help_text=u'', null=True, verbose_name=u'Reason patient withdrew from study', blank=True, choices=[(0, u'Non-compliance'), (1, u'Did not wish to continue in study'), (2, u'Could not tolerate the supplement'), (3, u'Hospitalization'), (4, u'Other')]) # This field type is a guess
    complete_study_date = models.DateField(help_text=u'', null=True, verbose_name=u'Date of study completion', blank=True)
    study_comments = models.TextField(help_text=u'', null=True, verbose_name=u'Comments', blank=True) # This field type is a guess
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'completiondatum'


class Brfss2009Section21EmotionalSupportAndLifeSatisfaction(models.Model):
    brfss_2009_s21_1_a7efff = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'21.1 How often do you get the social and emotional support you need?<br><br>INTERVIEWER NOTE: If asked, say "please include support from any source.""<br><br><br><br><div>INTERVIEWER NOTE - Please read:</div><div style=\'margin-left:40px;\'> Always<br>Usually<br>Sometimes<br>Rarely<br>Never </div><br><br><div><span style=\'color:red;\'>Do not read:<div style=\'margin-left:40px;\'> Don\'t know/ Not sure<br>Refused</div>"', choices=[(1, u'Always'), (2, u'Usually'), (3, u'Sometimes'), (4, u'Rarely'), (5, u'Never'), (7, u"Don't know / Not sure"), (9, u'Refused')])
    brfss_2009_s21_2_02a4d6 = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'21.2 In general, how satisfied are you with your life?<br><br>INTERVIEWER NOTE: If asked, say "please include support from any source.""<br><br><br><br><div>INTERVIEWER NOTE - Please read:</div><div style=\'margin-left:40px;\'> Very satisfied<br>Satisfied<br>Dissatisfied<br>Very dissatisfied</div><br><br><div><span style=\'color:red;\'>Do not read:<div style=\'margin-left:40px;\'> Don\'t know/ Not sure<br>Refused</div>"', choices=[(1, u'Very satisfied'), (2, u'Satisfied'), (3, u'Dissatisfied'), (4, u'Very dissatisfied'), (7, u"Don't know / Not sure"), (9, u'Refused')])
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'brfss2009section21emotionalsupportandlifesatisfaction'


class Brfss2009Module1Prediabete(models.Model):
    brfss_2009_m1_1_3c9744 = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'1. Have you had a test for high blood sugar or diabetes within the past three years?', choices=[(1, u'Yes'), (2, u'No'), (7, u"Don't know / Not sure"), (9, u'Refused')])
    brfss_2009_m1_2_2481a8 = models.CharField(help_text=u"1, Yes | 2, Yes, during pregnancy | 3, No | 7, Don't know / Not sure | 9, Refused", null=True, max_length=2000, verbose_name=u'2. Have you ever been told by a doctor or other health professional that you have pre-diabetes or borderline diabetes?<br><br>If "Yes"" and respondent is female', blank=True)
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'brfss2009module1prediabete'


