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


class BaselineData(models.Model):
    study_id_display = models.FloatField(help_text='', null=True, verbose_name='study_id', blank=True)
    date_visit_b = models.DateField(help_text='', null=True, verbose_name='Date of baseline visit', blank=True)
    date_blood_b = models.DateField(help_text='', null=True, verbose_name='Date blood was drawn', blank=True)
    alb_b = models.IntegerField(help_text='', null=True, verbose_name='Serum Albumin (g/dL)', blank=True)
    prealb_b = models.FloatField(help_text='', null=True, verbose_name='Serum Prealbumin (mg/dL)', blank=True)
    creat_b = models.FloatField(help_text='', null=True, verbose_name='Creatinine (mg/dL)', blank=True)
    npcr_b = models.FloatField(help_text='', null=True, verbose_name='Normalized Protein Catabolic Rate (g/kg/d)', blank=True)
    chol_b = models.FloatField(help_text='', null=True, verbose_name='Cholesterol (mg/dL)', blank=True)
    transferrin_b = models.FloatField(help_text='', null=True, verbose_name='Transferrin (mg/dL)', blank=True)
    kt_v_b = models.FloatField(help_text='', null=True, verbose_name='Kt/V', blank=True)
    drywt_b = models.FloatField(help_text='', null=True, verbose_name='Dry weight (kilograms)', blank=True)
    plasma1_b = models.IntegerField(help_text='', null=True, verbose_name='Collected Plasma 1?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    plasma2_b = models.IntegerField(help_text='', null=True, verbose_name='Collected Plasma 2?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    plasma3_b = models.IntegerField(help_text='', null=True, verbose_name='Collected Plasma 3?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    serum1_b = models.IntegerField(help_text='', null=True, verbose_name='Collected Serum 1?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    serum2_b = models.IntegerField(help_text='', null=True, verbose_name='Collected Serum 2?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    serum3_b = models.IntegerField(help_text='', null=True, verbose_name='Collected Serum 3?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    sga_b = models.FloatField(help_text='', null=True, verbose_name='Subject Global Assessment (score = 1-7)', blank=True)
    date_supplement_dispensed = models.DateField(help_text='', null=True, verbose_name='Date patient begins supplement', blank=True)

    class Meta:
	 db_table = 'BaselineData'


class Month1Data(models.Model):
    date_visit_1 = models.DateField(help_text='', null=True, verbose_name='Date of Month 1 visit', blank=True)
    alb_1 = models.FloatField(help_text='', null=True, verbose_name='Serum Albumin (g/dL)', blank=True)
    prealb_1 = models.FloatField(help_text='', null=True, verbose_name='Serum Prealbumin (mg/dL)', blank=True)
    creat_1 = models.FloatField(help_text='', null=True, verbose_name='Creatinine (mg/dL)', blank=True)
    npcr_1 = models.FloatField(help_text='', null=True, verbose_name='Normalized Protein Catabolic Rate (g/kg/d)', blank=True)
    chol_1 = models.FloatField(help_text='', null=True, verbose_name='Cholesterol (mg/dL)', blank=True)
    transferrin_1 = models.FloatField(help_text='', null=True, verbose_name='Transferrin (mg/dL)', blank=True)
    kt_v_1 = models.FloatField(help_text='', null=True, verbose_name='Kt/V', blank=True)
    drywt_1 = models.FloatField(help_text='', null=True, verbose_name='Dry weight (kilograms)', blank=True)
    no_show_1 = models.FloatField(help_text='', null=True, verbose_name='Number of treatments missed', blank=True)
    compliance_1 = models.IntegerField(help_text='', null=True, verbose_name='How compliant was the patient in drinking the supplement?', blank=True, choices=[(0, '100 percent'), (1, '99-75 percent'), (2, '74-50 percent'), (3, '49-25 percent'), (4, '0-24 percent')]) # This field type is a guess
    hospit_1 = models.IntegerField(help_text='', null=True, verbose_name='Was patient hospitalized since last visit?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    cause_hosp_1 = models.IntegerField(help_text='', null=True, verbose_name='What was the cause of hospitalization?', blank=True, choices=[(1, 'Vascular access related events'), (2, 'CVD events'), (3, 'Other')]) # This field type is a guess
    admission_date_1 = models.DateField(help_text='', null=True, verbose_name='Date of hospital admission', blank=True)
    discharge_date_1 = models.DateField(help_text='', null=True, verbose_name='Date of hospital discharge', blank=True)
    discharge_summary_1 = models.IntegerField(help_text='', null=True, verbose_name='Discharge summary in patients binder?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    death_1 = models.IntegerField(help_text='', null=True, verbose_name='Has patient died since last visit?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    date_death_1 = models.DateField(help_text='', null=True, verbose_name='Date of death', blank=True)
    cause_death_1 = models.IntegerField(help_text='', null=True, verbose_name='What was the cause of death?', blank=True, choices=[(1, 'All-cause'), (2, 'Cardiovascular')]) # This field type is a guess

    class Meta:
	 db_table = 'Month1Data'


class Month2Data(models.Model):
    date_visit_2 = models.DateField(help_text='', null=True, verbose_name='Date of Month 2 visit', blank=True)
    alb_2 = models.FloatField(help_text='', null=True, verbose_name='Serum Albumin (g/dL)', blank=True)
    prealb_2 = models.FloatField(help_text='', null=True, verbose_name='Serum Prealbumin (mg/dL)', blank=True)
    creat_2 = models.FloatField(help_text='', null=True, verbose_name='Creatinine (mg/dL)', blank=True)
    npcr_2 = models.FloatField(help_text='', null=True, verbose_name='Normalized Protein Catabolic Rate (g/kg/d)', blank=True)
    chol_2 = models.FloatField(help_text='', null=True, verbose_name='Cholesterol (mg/dL)', blank=True)
    transferrin_2 = models.FloatField(help_text='', null=True, verbose_name='Transferrin (mg/dL)', blank=True)
    kt_v_2 = models.FloatField(help_text='', null=True, verbose_name='Kt/V', blank=True)
    drywt_2 = models.FloatField(help_text='', null=True, verbose_name='Dry weight (kilograms)', blank=True)
    no_show_2 = models.FloatField(help_text='', null=True, verbose_name='Number of treatments missed', blank=True)
    compliance_2 = models.IntegerField(help_text='', null=True, verbose_name='How compliant was the patient in drinking the supplement?', blank=True, choices=[(0, '100 percent'), (1, '99-75 percent'), (2, '74-50 percent'), (3, '49-25 percent'), (4, '0-24 percent')]) # This field type is a guess
    hospit_2 = models.IntegerField(help_text='', null=True, verbose_name='Was patient hospitalized since last visit?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    cause_hosp_2 = models.IntegerField(help_text='', null=True, verbose_name='What was the cause of hospitalization?', blank=True, choices=[(1, 'Vascular access related events'), (2, 'CVD events'), (3, 'Other')]) # This field type is a guess
    admission_date_2 = models.DateField(help_text='', null=True, verbose_name='Date of hospital admission', blank=True)
    discharge_date_2 = models.DateField(help_text='', null=True, verbose_name='Date of hospital discharge', blank=True)
    discharge_summary_2 = models.IntegerField(help_text='', null=True, verbose_name='Discharge summary in patients binder?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    death_2 = models.IntegerField(help_text='', null=True, verbose_name='Has patient died since last visit?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    date_death_2 = models.DateField(help_text='', null=True, verbose_name='Date of death', blank=True)
    cause_death_2 = models.IntegerField(help_text='', null=True, verbose_name='What was the cause of death?', blank=True, choices=[(1, 'All-cause'), (2, 'Cardiovascular')]) # This field type is a guess

    class Meta:
	 db_table = 'Month2Data'


class Month3Data(models.Model):
    date_visit_3 = models.DateField(help_text='', null=True, verbose_name='Date of Month 3 visit', blank=True)
    date_blood_3 = models.DateField(help_text='', null=True, verbose_name='Date blood was drawn', blank=True)
    alb_3 = models.FloatField(help_text='', null=True, verbose_name='Serum Albumin (g/dL)', blank=True)
    prealb_3 = models.FloatField(help_text='', null=True, verbose_name='Serum Prealbumin (mg/dL)', blank=True)
    creat_3 = models.FloatField(help_text='', null=True, verbose_name='Creatinine (mg/dL)', blank=True)
    npcr_3 = models.FloatField(help_text='', null=True, verbose_name='Normalized Protein Catabolic Rate (g/kg/d)', blank=True)
    chol_3 = models.FloatField(help_text='', null=True, verbose_name='Cholesterol (mg/dL)', blank=True)
    transferrin_3 = models.FloatField(help_text='', null=True, verbose_name='Transferrin (mg/dL)', blank=True)
    kt_v_3 = models.FloatField(help_text='', null=True, verbose_name='Kt/V', blank=True)
    drywt_3 = models.FloatField(help_text='', null=True, verbose_name='Dry weight (kilograms)', blank=True)
    plasma1_3 = models.IntegerField(help_text='', null=True, verbose_name='Collected Plasma 1?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    plasma2_3 = models.IntegerField(help_text='', null=True, verbose_name='Collected Plasma 2?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    plasma3_3 = models.IntegerField(help_text='', null=True, verbose_name='Collected Plasma 3?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    serum1_3 = models.IntegerField(help_text='', null=True, verbose_name='Collected Serum 1?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    serum2_3 = models.IntegerField(help_text='', null=True, verbose_name='Collected Serum 2?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    serum3_3 = models.IntegerField(help_text='', null=True, verbose_name='Collected Serum 3?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    sga_3 = models.FloatField(help_text='', null=True, verbose_name='Subject Global Assessment (score = 1-7)', blank=True)
    no_show_3 = models.FloatField(help_text='', null=True, verbose_name='Number of treatments missed', blank=True)
    compliance_3 = models.IntegerField(help_text='', null=True, verbose_name='How compliant was the patient in drinking the supplement?', blank=True, choices=[(0, '100 percent'), (1, '99-75 percent'), (2, '74-50 percent'), (3, '49-25 percent'), (4, '0-24 percent')]) # This field type is a guess
    hospit_3 = models.IntegerField(help_text='', null=True, verbose_name='Was patient hospitalized since last visit?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    cause_hosp_3 = models.IntegerField(help_text='', null=True, verbose_name='What was the cause of hospitalization?', blank=True, choices=[(1, 'Vascular access related events'), (2, 'CVD events'), (3, 'Other')]) # This field type is a guess
    admission_date_3 = models.DateField(help_text='', null=True, verbose_name='Date of hospital admission', blank=True)
    discharge_date_3 = models.DateField(help_text='', null=True, verbose_name='Date of hospital discharge', blank=True)
    discharge_summary_3 = models.IntegerField(help_text='', null=True, verbose_name='Discharge summary in patients binder?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    death_3 = models.IntegerField(help_text='', null=True, verbose_name='Has patient died since last visit?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    date_death_3 = models.DateField(help_text='', null=True, verbose_name='Date of death', blank=True)
    cause_death_3 = models.IntegerField(help_text='', null=True, verbose_name='What was the cause of death?', blank=True, choices=[(1, 'All-cause'), (2, 'Cardiovascular')]) # This field type is a guess

    class Meta:
	 db_table = 'Month3Data'


class Month4Data(models.Model):
    date_visit_4 = models.DateField(help_text='', null=True, verbose_name='Date of Month 4 visit', blank=True)
    alb_4 = models.FloatField(help_text='', null=True, verbose_name='Serum Albumin (g/dL)', blank=True)
    prealb_4 = models.FloatField(help_text='', null=True, verbose_name='Serum Prealbumin (mg/dL)', blank=True)
    creat_4 = models.FloatField(help_text='', null=True, verbose_name='Creatinine (mg/dL)', blank=True)
    npcr_4 = models.FloatField(help_text='', null=True, verbose_name='Normalized Protein Catabolic Rate (g/kg/d)', blank=True)
    chol_4 = models.FloatField(help_text='', null=True, verbose_name='Cholesterol (mg/dL)', blank=True)
    transferrin_4 = models.FloatField(help_text='', null=True, verbose_name='Transferrin (mg/dL)', blank=True)
    kt_v_4 = models.FloatField(help_text='', null=True, verbose_name='Kt/V', blank=True)
    drywt_4 = models.FloatField(help_text='', null=True, verbose_name='Dry weight (kilograms)', blank=True)
    no_show_4 = models.FloatField(help_text='', null=True, verbose_name='Number of treatments missed', blank=True)
    compliance_4 = models.IntegerField(help_text='', null=True, verbose_name='How compliant was the patient in drinking the supplement?', blank=True, choices=[(0, '100 percent'), (1, '99-75 percent'), (2, '74-50 percent'), (3, '49-25 percent'), (4, '0-24 percent')]) # This field type is a guess
    hospit_4 = models.IntegerField(help_text='', null=True, verbose_name='Was patient hospitalized since last visit?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    cause_hosp_4 = models.IntegerField(help_text='', null=True, verbose_name='What was the cause of hospitalization?', blank=True, choices=[(1, 'Vascular access related events'), (2, 'CVD events'), (3, 'Other')]) # This field type is a guess
    admission_date_4 = models.DateField(help_text='', null=True, verbose_name='Date of hospital admission', blank=True)
    discharge_date_4 = models.DateField(help_text='', null=True, verbose_name='Date of hospital discharge', blank=True)
    discharge_summary_4 = models.IntegerField(help_text='', null=True, verbose_name='Discharge summary in patients binder?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    death_4 = models.IntegerField(help_text='', null=True, verbose_name='Has patient died since last visit?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    date_death_4 = models.DateField(help_text='', null=True, verbose_name='Date of death', blank=True)
    cause_death_4 = models.IntegerField(help_text='', null=True, verbose_name='What was the cause of death?', blank=True, choices=[(1, 'All-cause'), (2, 'Cardiovascular')]) # This field type is a guess

    class Meta:
	 db_table = 'Month4Data'


class Month5Data(models.Model):
    date_visit_5 = models.DateField(help_text='', null=True, verbose_name='Date of Month 5 visit', blank=True)
    alb_5 = models.FloatField(help_text='', null=True, verbose_name='Serum Albumin (g/dL)', blank=True)
    prealb_5 = models.FloatField(help_text='', null=True, verbose_name='Serum Prealbumin (mg/dL)', blank=True)
    creat_5 = models.FloatField(help_text='', null=True, verbose_name='Creatinine (mg/dL)', blank=True)
    npcr_5 = models.FloatField(help_text='', null=True, verbose_name='Normalized Protein Catabolic Rate (g/kg/d)', blank=True)
    chol_5 = models.FloatField(help_text='', null=True, verbose_name='Cholesterol (mg/dL)', blank=True)
    transferrin_5 = models.FloatField(help_text='', null=True, verbose_name='Transferrin (mg/dL)', blank=True)
    kt_v_5 = models.FloatField(help_text='', null=True, verbose_name='Kt/V', blank=True)
    drywt_5 = models.FloatField(help_text='', null=True, verbose_name='Dry weight (kilograms)', blank=True)
    no_show_5 = models.FloatField(help_text='', null=True, verbose_name='Number of treatments missed', blank=True)
    compliance_5 = models.IntegerField(help_text='', null=True, verbose_name='How compliant was the patient in drinking the supplement?', blank=True, choices=[(0, '100 percent'), (1, '99-75 percent'), (2, '74-50 percent'), (3, '49-25 percent'), (4, '0-24 percent')]) # This field type is a guess
    hospit_5 = models.IntegerField(help_text='', null=True, verbose_name='Was patient hospitalized since last visit?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    cause_hosp_5 = models.IntegerField(help_text='', null=True, verbose_name='What was the cause of hospitalization?', blank=True, choices=[(1, 'Vascular access related events'), (2, 'CVD events'), (3, 'Other')]) # This field type is a guess
    admission_date_5 = models.DateField(help_text='', null=True, verbose_name='Date of hospital admission', blank=True)
    discharge_date_5 = models.DateField(help_text='', null=True, verbose_name='Date of hospital discharge', blank=True)
    discharge_summary_5 = models.IntegerField(help_text='', null=True, verbose_name='Discharge summary in patients binder?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    death_5 = models.IntegerField(help_text='', null=True, verbose_name='Has patient died since last visit?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    date_death_5 = models.DateField(help_text='', null=True, verbose_name='Date of death', blank=True)
    cause_death_5 = models.IntegerField(help_text='', null=True, verbose_name='What was the cause of death?', blank=True, choices=[(1, 'All-cause'), (2, 'Cardiovascular')]) # This field type is a guess

    class Meta:
	 db_table = 'Month5Data'


class Month6Data(models.Model):
    date_visit_6 = models.DateField(help_text='', null=True, verbose_name='Date of Month 6 visit', blank=True)
    date_blood_6 = models.DateField(help_text='', null=True, verbose_name='Date blood was drawn', blank=True)
    alb_6 = models.FloatField(help_text='', null=True, verbose_name='Serum Albumin (g/dL)', blank=True)
    prealb_6 = models.FloatField(help_text='', null=True, verbose_name='Serum Prealbumin (mg/dL)', blank=True)
    creat_6 = models.FloatField(help_text='', null=True, verbose_name='Creatinine (mg/dL)', blank=True)
    npcr_6 = models.FloatField(help_text='', null=True, verbose_name='Normalized Protein Catabolic Rate (g/kg/d)', blank=True)
    chol_6 = models.FloatField(help_text='', null=True, verbose_name='Cholesterol (mg/dL)', blank=True)
    transferrin_6 = models.FloatField(help_text='', null=True, verbose_name='Transferrin (mg/dL)', blank=True)
    kt_v_6 = models.FloatField(help_text='', null=True, verbose_name='Kt/V', blank=True)
    drywt_6 = models.FloatField(help_text='', null=True, verbose_name='Dry weight (kilograms)', blank=True)
    plasma1_6 = models.IntegerField(help_text='', null=True, verbose_name='Collected Plasma 1?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    plasma2_6 = models.IntegerField(help_text='', null=True, verbose_name='Collected Plasma 2?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    plasma3_6 = models.IntegerField(help_text='', null=True, verbose_name='Collected Plasma 3?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    serum1_6 = models.IntegerField(help_text='', null=True, verbose_name='Collected Serum 1?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    serum2_6 = models.IntegerField(help_text='', null=True, verbose_name='Collected Serum 2?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    serum3_6 = models.IntegerField(help_text='', null=True, verbose_name='Collected Serum 3?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    sga_6 = models.FloatField(help_text='', null=True, verbose_name='Subject Global Assessment (score = 1-7)', blank=True)
    no_show_6 = models.FloatField(help_text='', null=True, verbose_name='Number of treatments missed', blank=True)
    compliance_6 = models.IntegerField(help_text='', null=True, verbose_name='How compliant was the patient in drinking the supplement?', blank=True, choices=[(0, '100 percent'), (1, '99-75 percent'), (2, '74-50 percent'), (3, '49-25 percent'), (4, '0-24 percent')]) # This field type is a guess
    hospit_6 = models.IntegerField(help_text='', null=True, verbose_name='Was patient hospitalized since last visit?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    cause_hosp_6 = models.IntegerField(help_text='', null=True, verbose_name='What was the cause of hospitalization?', blank=True, choices=[(1, 'Vascular access related events'), (2, 'CVD events'), (3, 'Other')]) # This field type is a guess
    admission_date_6 = models.DateField(help_text='', null=True, verbose_name='Date of hospital admission', blank=True)
    discharge_date_6 = models.DateField(help_text='', null=True, verbose_name='Date of hospital discharge', blank=True)
    discharge_summary_6 = models.IntegerField(help_text='', null=True, verbose_name='Discharge summary in patients binder?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    death_6 = models.IntegerField(help_text='', null=True, verbose_name='Has patient died since last visit?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    date_death_6 = models.DateField(help_text='', null=True, verbose_name='Date of death', blank=True)
    cause_death_6 = models.IntegerField(help_text='', null=True, verbose_name='What was the cause of death?', blank=True, choices=[(1, 'All-cause'), (2, 'Cardiovascular')]) # This field type is a guess

    class Meta:
	 db_table = 'Month6Data'


class CompletionData(models.Model):
    complete_study = models.IntegerField(help_text='', null=True, verbose_name='Has patient completed study?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    withdraw_date = models.DateField(help_text='', null=True, verbose_name='Put a date if patient withdrew study', blank=True)
    withdraw_reason = models.IntegerField(help_text='', null=True, verbose_name='Reason patient withdrew from study', blank=True, choices=[(0, 'Non-compliance'), (1, 'Did not wish to continue in study'), (2, 'Could not tolerate the supplement'), (3, 'Hospitalization'), (4, 'Other')]) # This field type is a guess
    complete_study_date = models.DateField(help_text='', null=True, verbose_name='Date of study completion', blank=True)
    study_comments = models.TextField(help_text='', null=True, verbose_name='Comments', blank=True) # This field type is a guess

    class Meta:
	 db_table = 'CompletionData'


class Brfss2009Section21EmotionalSupportAndLifeSatisfaction(models.Model):
    brfss_2009_s21_1_a7efff = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='21.1 How often do you get the social and emotional support you need?<br><br>INTERVIEWER NOTE: If asked, say \\', choices=[(1, 'Always'), (2, 'Usually'), (3, 'Sometimes'), (4, 'Rarely'), (5, 'Never'), (7, "Don't know / Not sure"), (9, 'Refused')])
    brfss_2009_s21_2_02a4d6 = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='21.2 In general, how satisfied are you with your life?<br><br>INTERVIEWER NOTE: If asked, say \\', choices=[(1, 'Very satisfied'), (2, 'Satisfied'), (3, 'Dissatisfied'), (4, 'Very dissatisfied'), (7, "Don't know / Not sure"), (9, 'Refused')])

    class Meta:
	 db_table = 'Brfss2009Section21EmotionalSupportAndLifeSatisfaction'


class Brfss2009Module1Prediabetes(models.Model):
    brfss_2009_m1_1_3c9744 = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='1. Have you had a test for high blood sugar or diabetes within the past three years?', choices=[(1, 'Yes'), (2, 'No'), (7, "Don't know / Not sure"), (9, 'Refused')])
    brfss_2009_m1_2_2481a8 = models.CharField(help_text="1, Yes | 2, Yes, during pregnancy | 3, No | 7, Don't know / Not sure | 9, Refused", null=True, max_length=2000, verbose_name='2. Have you ever been told by a doctor or other health professional that you have pre-diabetes or borderline diabetes?<br><br>If \\', blank=True)

    class Meta:
	 db_table = 'Brfss2009Module1Prediabetes'


