from django.db import models

class Record(models.Model):

    class Meta:
	 db_table = 'record'


class Demographic(models.Model):
    study_id = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Study ID', blank=True)
    gender = models.IntegerField(help_text=u'', null=True, verbose_name=u'Gender', blank=True, choices=[(0, u'Female'), (1, u'Male'), (2, u'Other')]) # This field type is a guess
    other_gender = models.IntegerField(help_text=u'Newborn Screening LTFU', null=True, verbose_name=u'Other gender | Please specify  gender', blank=True, choices=[(1, u'Not tested'), (2, u'XX genotype/Female'), (3, u'XY genotype/Male'), (4, u"XXY Klinefelter's Syndrome"), (5, u"XO Turner's Syndrome"), (6, u'XXXY syndrome'), (7, u'XXYY syndrome'), (8, u'Mosaic including XXXXY'), (9, u'Penta X syndrome'), (10, u'XYY'), (11, u'Unknown'), (12, u'Other')]) # This field type is a guess
    year_of_birth = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Year of birth (XXXX)', blank=True)
    ethnicity = models.IntegerField(help_text=u'', null=True, verbose_name=u'Ethnicity', blank=True, choices=[(1, u'Non-Hispanic'), (2, u'Hispanic or Latino'), (3, u'Unknown')]) # This field type is a guess
    ethnicity_followup = models.IntegerField(help_text=u'', null=True, verbose_name=u'Ethnicity follow-up', blank=True, choices=[(1, u'Ashkenazi Jewish'), (2, u'Amish'), (3, u'French Canadian'), (4, u'None of the above'), (5, u'Unknown')]) # This field type is a guess
    demographics_feedback = models.TextField(help_text=u'', null=True, verbose_name=u'Please provide any feedback for this form (for example: missing questions, questions not relevant for a disease area, ambiguities, places where a textbox could be replaced with discrete choices, missing discrete choices)', blank=True) # This field type is a guess
    race_summary = models.CharField(help_text=u'1, White | 2, Black or African American | 3, American Indian or Alaska Native | 4, Native Hawaiian or Other Pacific Islander | 5, Asian | 6, More than one race | 7, Unknown or Not reported', null=True, max_length=2000, verbose_name=u'Race', blank=True)
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'demographic'


class race(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Race', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Race', choices=[(1, u'White'), (2, u'Black or African American'), (3, u'American Indian or Alaska Native'), (4, u'Native Hawaiian or Other Pacific Islander'), (5, u'Asian'), (6, u'More than one race'), (7, u'Unknown or Not reported')])
    demographic = models.ForeignKey(Demographic)

    class Meta:
	 db_table = 'race'


class PediseqStudyId(models.Model):
    family_code = models.FloatField(help_text=u'', null=True, verbose_name=u'Family Code', blank=True)
    family_member_code = models.CharField(help_text=u'P - Proband, S - Sibling, M - Mother, F - Father', null=True, max_length=2000, verbose_name=u'Family Member', blank=True)
    other_family_member = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Other family member', blank=True)
    affected_status = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Affected Status', blank=True)
    validation_or_prospective = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Validation or Prospective', blank=True)
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'pediseqstudyid'


class StudyId(models.Model):
    original_study_id = models.CharField(help_text=u"Enter the subject's ID from the original consenting study (HLS, Mito, etc.)", null=True, max_length=2000, verbose_name=u'Original Study ID', blank=True)
    discarded_clinical = models.NullBooleanField(help_text=u'', verbose_name=u'Discarded Clinical Specimen?', blank=True)
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'studyid'


class BirthHistory(models.Model):
    birthweight = models.TextField(help_text=u'Please indicate out to one decimal place unless units are lbs. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name=u'Birthweight', blank=True) # This field type is a guess
    birth_length = models.TextField(help_text=u'Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name=u'Birth length', blank=True) # This field type is a guess
    birth_head_circumference = models.FloatField(help_text=u'Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name=u'Birth head circumference (cm)', blank=True)
    gestational_age_wks = models.IntegerField(help_text=u'Specify partial week in days below. If full term but exact month and days are unknown, specify 40 weeks and 0 days.', null=True, verbose_name=u'Gestational age full weeks', blank=True)
    gestational_age_days = models.IntegerField(help_text=u'', null=True, verbose_name=u'Gestation age days', blank=True)
    mother_birth_age = models.CharField(help_text=u'Please round up if the age is 6 months or more into the current year.', null=True, max_length=2000, verbose_name=u"Mother's age when child was born (years)", blank=True)
    gravida = models.IntegerField(help_text=u'', null=True, verbose_name=u'Gravida\n(Number of prior gestations including proband)', blank=True)
    para = models.IntegerField(help_text=u'', null=True, verbose_name=u'Para\n(Number of live births including the proband)', blank=True)
    assisted_reproduction_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Was any type of assisted reproduction (for example sperm donation, in vitro fertilization) used in the pregnancy for this child?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    assisted_reproduction_spec = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Please specify type of assisted reproduction', blank=True)
    miscarriages_no = models.IntegerField(help_text=u'', null=True, verbose_name=u'Number of spontaneous miscarriages', blank=True)
    still_births_no = models.IntegerField(help_text=u'', null=True, verbose_name=u'Number of still births', blank=True)
    terminations_no = models.IntegerField(help_text=u'', null=True, verbose_name=u'Number of terminations', blank=True)
    multiples_no = models.IntegerField(help_text=u'', null=True, verbose_name=u'Number of multiple births', blank=True)
    pn_exposure_med = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Medications during pregnancy', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ultrasound_no = models.IntegerField(help_text=u'', null=True, verbose_name=u'How many ultrasound tests do you want to enter?', blank=True)
    ultrasound_increased_reason = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Reason for increased number of ultrasounds?', blank=True)
    pn_exposure_alc_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Specify prenatal alcohol exposure\n(Alcohol amount, time of exposure, duration of exposure)', blank=True) # This field type is a guess
    pn_exposure_tob_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Specify prenatal tobacco exposures\n(Tobacco amount, time of exposure, duration of exposure)', blank=True) # This field type is a guess
    pn_exposure_inf_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Specify prenatal infection exposures\n(Infection, time of exposure, duration of exposure, treatment)', blank=True) # This field type is a guess
    maternal_screening = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Maternal serum screening', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not performed'), (5, u'Not determined'), (4, u'Unknown/Not documented')])
    maternal_serum_type = models.TextField(help_text=u'', null=True, verbose_name=u'Type of maternal serum screening', blank=True) # This field type is a guess
    maternal_serum_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Maternal serum screening revealed', blank=True) # This field type is a guess
    cvs = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'CVS', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not performed'), (6, u'Not determined'), (5, u'Recommended but declined'), (4, u'Unknown/Not documented')])
    cvs_spec = models.TextField(help_text=u'', null=True, verbose_name=u'CVS revealed', blank=True) # This field type is a guess
    amniocentesis = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Amniocentesis', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not performed'), (6, u'Not determined'), (5, u'Recommended but declined'), (4, u'Unknown/Not documented')])
    amniocentesis_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Amniocentesis revealed', blank=True) # This field type is a guess
    fetal_activity = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Fetal activity was', choices=[(1, u'Normal'), (2, u'Reduced'), (3, u'Unknown/Not documented')])
    apgar_1 = models.IntegerField(help_text=u'', null=True, verbose_name=u'Apgar score at 1 minute of life', blank=True, choices=[(1, u'0'), (2, u'1'), (3, u'2'), (4, u'3'), (5, u'4'), (6, u'5'), (7, u'6'), (8, u'7'), (9, u'8'), (10, u'9'), (11, u'10'), (12, u'Not performed'), (13, u'Unknown/Not documented')]) # This field type is a guess
    apgar_5 = models.IntegerField(help_text=u'', null=True, verbose_name=u'Apgar score at 5 minutes of life', blank=True, choices=[(1, u'0'), (2, u'1'), (3, u'2'), (4, u'3'), (5, u'4'), (6, u'5'), (7, u'6'), (8, u'7'), (9, u'8'), (10, u'9'), (11, u'10'), (12, u'Not performed'), (13, u'Unknown/Not documented')]) # This field type is a guess
    neonatal_complications_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Neonatal complications', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    neonatal_complications_spec = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Neonatal complications included', blank=True)
    newborn_hearing_screen = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Newborn hearing screening', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not performed'), (5, u'Not determined'), (4, u'Unknown/Not document')])
    newborn_hearing_screen_ears_failed = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Failed ear', choices=[(1, u'Left'), (2, u'Right'), (3, u'Both'), (4, u'Unknown/Not documented')])
    newborn_metabolic_screening = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Newborn metabolic screening', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not performed'), (5, u'Not determined'), (4, u'Unknown/Not documented')])
    newborn_metabolic_screening_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe abnormal newborn metabolic screening', blank=True) # This field type is a guess
    dol_went_home = models.FloatField(help_text=u'', null=True, verbose_name=u'Baby went home on day of life ', blank=True)
    birth_history_feedback = models.TextField(help_text=u'', null=True, verbose_name=u'Please provide any feedback for this form (for example: missing questions, questions not relevant for a disease area, ambiguities, places where a textbox could be replaced with discrete choices, missing discrete choices)', blank=True) # This field type is a guess
    prior_pregnancy_history_summary = models.CharField(help_text=u'5, None | 1, spontaneous miscarriages | 2, still births | 3, terminations | 4, multiples (twins, triples) | 6, Unknown/Not documented', null=True, max_length=2000, verbose_name=u'Did the mother have any of the following', blank=True)
    pregnancy_complications_summary = models.CharField(help_text=u'10, None | 1, Bleeding | 2, Eclampsia | 3, Pre-eclampsia | 4, Gestational diabetes | 5, Maternal seizures | 6, Maternal hypertension | 7, Polyhydramnios | 8, Oligohydramnios | 9, Preterm labor  | 11, Unknown/Not documented | 12, Other', null=True, max_length=2000, verbose_name=u'Pregnancy complications', blank=True)
    pn_exposure_summary = models.CharField(help_text=u'6, None | 1, Recreational drugs | 2, Alcohol | 3, Tobacco | 4, Infection | 5, Unknown/Not documented | 7, Other unknown exposures | 8, Other known exposures (specify below)', null=True, max_length=2000, verbose_name=u'Prenatal exposures', blank=True)
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'birthhistory'


class priorpregnancyhistory(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Did the mother have any of the following', blank=True)
    value = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Did the mother have any of the following', blank=True)
    birthhistory = models.ForeignKey(BirthHistory)

    class Meta:
	 db_table = 'priorpregnancyhistory'


class pregnancycomplications(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Pregnancy complications', blank=True)
    value = models.IntegerField(help_text=u'', null=True, verbose_name=u'Pregnancy complications', blank=True, choices=[(10, u'None'), (1, u'Bleeding'), (2, u'Eclampsia'), (3, u'Pre-eclampsia'), (4, u'Gestational diabetes'), (5, u'Maternal seizures'), (6, u'Maternal hypertension'), (7, u'Polyhydramnios'), (8, u'Oligohydramnios'), (9, u'Preterm labor'), (11, u'Unknown/Not documented'), (12, u'Other')]) # This field type is a guess
    birthhistory = models.ForeignKey(BirthHistory)

    class Meta:
	 db_table = 'pregnancycomplications'


class pnexposure(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Prenatal exposures', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Prenatal exposures', choices=[(6, u'None'), (1, u'Recreational drugs'), (2, u'Alcohol'), (3, u'Tobacco'), (4, u'Infection'), (5, u'Unknown/Not documented'), (7, u'Other unknown exposures'), (8, u'Other known exposures (specify below)')])
    birthhistory = models.ForeignKey(BirthHistory)

    class Meta:
	 db_table = 'pnexposure'


class Miscarriage(models.Model):
    miscarriages_gestational_age = models.TextField(help_text=u'', null=True, verbose_name=u'Gestational age of miscarriage', blank=True) # This field type is a guess
    birthhistory = models.ForeignKey(BirthHistory)

    class Meta:
	 db_table = 'miscarriage'


class StillBirth(models.Model):
    still_births_gestational_age = models.TextField(help_text=u'', null=True, verbose_name=u'Gestational age of still birth', blank=True) # This field type is a guess
    birthhistory = models.ForeignKey(BirthHistory)

    class Meta:
	 db_table = 'stillbirth'


class Termination(models.Model):
    terminations_gestational_age = models.TextField(help_text=u'', null=True, verbose_name=u'Gestational age of termination', blank=True) # This field type is a guess
    birthhistory = models.ForeignKey(BirthHistory)

    class Meta:
	 db_table = 'termination'


class MultipleBirth(models.Model):
    multiple_number = models.IntegerField(help_text=u'', null=True, verbose_name=u'Number of children in multiple birth', blank=True)
    multiple_gestational_age = models.TextField(help_text=u'', null=True, verbose_name=u'Gestation age of multiple birth', blank=True) # This field type is a guess
    birthhistory = models.ForeignKey(BirthHistory)

    class Meta:
	 db_table = 'multiplebirth'


class PrenatalMedication(models.Model):
    pn_med = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Specify prenatal medication', blank=True)
    birthhistory = models.ForeignKey(BirthHistory)

    class Meta:
	 db_table = 'prenatalmedication'


class Ultrasound(models.Model):
    ultrasound_weeks_gestation_drop = models.IntegerField(help_text=u'', null=True, verbose_name=u'ultrasound performed at (weeks gestation)', blank=True, choices=[(39, u'Unknown'), (1, u'4 weeks + 1 day to 5 weeks'), (2, u'5 weeks + 1 day to 6 weeks'), (3, u'6 weeks + 1 day to 7 weeks'), (4, u'7 weeks + 1 day to 8 weeks'), (5, u'8 weeks + 1 day to 9 weeks'), (6, u'9 weeks + 1 day to 10 weeks'), (7, u'10 weeks + 1 day to 11 weeks'), (8, u'11 weeks + 1 day to 12 weeks'), (9, u'12 weeks + 1 day to 13 weeks'), (10, u'13 weeks + 1 day to 14 weeks'), (11, u'14 weeks + 1 day to 15 weeks'), (12, u'15 weeks + 1 day to 16 weeks'), (13, u'16 weeks + 1 day to 17 weeks'), (14, u'17 weeks + 1 day to 18 weeks'), (15, u'18 weeks + 1 day to 19 weeks'), (16, u'19 weeks + 1 day to 20 weeks'), (17, u'20 weeks + 1 day to 21 weeks'), (18, u'21 weeks + 1 day to 22 weeks'), (19, u'22 weeks + 1 day to 23 weeks'), (20, u'23 weeks + 1 day to 24 weeks'), (21, u'24 weeks + 1 day to 25 weeks'), (22, u'25 weeks + 1 day to 26 weeks'), (23, u'26 weeks + 1 day to 27 weeks'), (24, u'27 weeks + 1 day to 28 weeks'), (25, u'28 weeks + 1 day to 29 weeks'), (26, u'29 weeks + 1 day to 30 weeks'), (27, u'30 weeks + 1 day to 31 weeks'), (28, u'31 weeks + 1 day to 32 weeks'), (29, u'32 weeks + 1 day to 33 weeks'), (30, u'33 weeks + 1 day to 34 weeks'), (31, u'34 weeks + 1 day to 25 weeks'), (32, u'35 weeks + 1 day to 36 weeks'), (33, u'36 weeks + 1 day to 37 weeks'), (34, u'37 weeks + 1 day to 38 weeks'), (35, u'38 weeks + 1 day to 39 weeks'), (36, u'39 weeks + 1 day to 40 weeks'), (37, u'40 weeks + 1 day to 41 weeks'), (38, u'41 weeks + 1 day to 42 weeks')]) # This field type is a guess
    ultrasound_normal_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'ultrasound within normal limits', choices=[(1, u'Yes'), (2, u'No'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    ultrasound_spec = models.TextField(help_text=u'', null=True, verbose_name=u'ultrasound significant for', blank=True) # This field type is a guess
    birthhistory = models.ForeignKey(BirthHistory)

    class Meta:
	 db_table = 'ultrasound'


class RecreationalDrugExposure(models.Model):
    pn_exposure_drug = models.CharField(help_text=u'(Drug, Drug amount, time of exposure, duration of pregnancy)', null=True, max_length=2000, verbose_name=u'Specify prenatal recreational drug exposure', blank=True)
    birthhistory = models.ForeignKey(BirthHistory)

    class Meta:
	 db_table = 'recreationaldrugexposure'


class PrenatalExposure(models.Model):
    pn_exposure_other_spec = models.CharField(help_text=u'(exposure, exposure amount, time of exposure, duration of pregnancy)', null=True, max_length=2000, verbose_name=u'Specify other prenatal exposure', blank=True)
    birthhistory = models.ForeignKey(BirthHistory)

    class Meta:
	 db_table = 'prenatalexposure'


class PriorGeneticTesting(models.Model):
    karyotype_date = models.FloatField(help_text=u'Please specify four digit year', null=True, verbose_name=u'Year of Karyotype', blank=True)
    karyotype_tissue = models.IntegerField(help_text=u'', null=True, verbose_name=u'Karyotype tissue studied | Specify other tissue studied', blank=True, choices=[(1, u'Amniotic fluid'), (2, u'Blood'), (3, u'Chorionic villi'), (4, u'Fibroblasts'), (5, u'Saliva'), (6, u'Unknown/Not documented'), (7, u'Other')]) # This field type is a guess
    karyotype_result = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Karyotype result', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    karyotype_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Specify other karyotype abnormalities', blank=True) # This field type is a guess
    karyotype_location = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Lab where Karyotype was performed', blank=True)
    mito_analysis_type = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'What type(s) of mitochondrial DNA analysis was performed?', choices=[(1, u'Target point mutation analysis (without deletion analysis)'), (2, u'Whole mitochondrial genome sequencing'), (3, u'Deletion analysis (without targetted point mutation analysis)'), (4, u'Combination deletion and targetted mutation analysis panel'), (5, u'Other')])
    fragx_type = models.IntegerField(max_length=2000, blank=True, help_text=u'Example: GNE1 or 15q11', null=True, verbose_name=u'What were the results of the Fragile X testing?', choices=[(1, u'Full Mutation'), (2, u'Pre-Mutation'), (3, u'Normal'), (6, u'Inconclusive'), (5, u'Result not known'), (4, u'Results pending')])
    cardiac_gene_test_done = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Previous cardiac genetic testing done', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    cardiac_gene_sent_out = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Previous cardiac genetic testing sent to outside lab', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    cardiac_gene_lab = models.IntegerField(help_text=u'', null=True, verbose_name=u'Outside Lab test done at | Outside lab Other - Specify', blank=True, choices=[(1, u'Familion (Transgenomics)'), (2, u'Gene Dx'), (3, u'Harvard Partners'), (4, u'Medical Genetics Laboratories at Baylor College of Medicine'), (5, u"Heart Institute Diagnostic Lab at Cincinnati Children's Hospital"), (7, u'Uknown/Not doucmented'), (6, u'Other')]) # This field type is a guess
    cardiac_gene_summary = models.TextField(help_text=u'', null=True, verbose_name=u'Previous Genetic testing results summary', blank=True) # This field type is a guess
    other_genetic_testing_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe other genetic tests performed', blank=True) # This field type is a guess
    prior_genetic_testing_feedback = models.TextField(help_text=u'', null=True, verbose_name=u'Please provide any feedback for this form (for example: missing questions, questions not relevant for a disease area, ambiguities, places where a textbox could be replaced with discrete choices, missing discrete choices)', blank=True) # This field type is a guess
    genetic_tests_performed_summary = models.CharField(help_text=u' 6, None | 1, Karyotype | 2, Microarray | 3, Sequence analysis of a single nuclear gene or group of nuclear genes | 8, Deletion or duplication analysis of a single nuclear gene or group of nuclear genes | 4, Nuclear exome/Genome sequencing | 5, Mitochondrial DNA analysis | 9, Methylation analysis | 10, Testing for Fragile X Syndrome | 7, Other', null=True, max_length=2000, verbose_name=u'Genetic tests performed', blank=True)
    karyotype_result_details_summary = models.CharField(help_text=u'1, Balanced reciprocal translocation | 2, Balanced Robertsonian translocation | 3, Delete | 4, Duplication | 5, Extra marker chromosome | 6, Trisomy 13 | 7, Trisomy 18 | 8, 22q11 deletion | 9, 45,  X | 10, 47, XXX | 11, 47, XXY | 12, 47, XYY | 13, Paracentric inversion | 14, Pericentric inversion | 15, Structural X chromosome | 16, Structural Y chromosome | 17, Unbalanced reciprocal translocation | 18, Unbalanced Robertsonian translocation | 19, Other', null=True, max_length=2000, verbose_name=u'Specify karyotype abnormalities', blank=True)
    gene_or_panel_summary = models.CharField(help_text=u'1, Single genes | 2, Gene panels', null=True, max_length=2000, verbose_name=u'Was the sequencing testing performed on single genes or gene panels (containing multiple genes)?', blank=True)
    targeted_mito_single_or_panel_summary = models.CharField(help_text=u'1, Single mutations | 2, Mutation Panels', null=True, max_length=2000, verbose_name=u'Was the targeted mutation analysis for single mutations or mutation panels?', blank=True)
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'priorgenetictesting'


class genetictestsperformed(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Genetic tests performed', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Genetic tests performed', choices=[(6, u'None'), (1, u'Karyotype'), (2, u'Microarray'), (3, u'Sequence analysis of a single nuclear gene or group of nuclear genes'), (8, u'Deletion or duplication analysis of a single nuclear gene or group of nuclear genes'), (4, u'Nuclear exome/Genome sequencing'), (5, u'Mitochondrial DNA analysis'), (9, u'Methylation analysis'), (10, u'Testing for Fragile X Syndrome'), (7, u'Other')])
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'genetictestsperformed'


class karyotyperesultdetails(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Specify karyotype abnormalities', blank=True)
    value = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Specify karyotype abnormalities', blank=True)
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'karyotyperesultdetails'


class geneorpanel(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Was the sequencing testing performed on single genes or gene panels (containing multiple genes)?', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Was the sequencing testing performed on single genes or gene panels (containing multiple genes)?', choices=[(1, u'Single genes'), (2, u'Gene panels')])
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'geneorpanel'


class targetedmitosingleorpanel(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Was the targeted mutation analysis for single mutations or mutation panels?', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Was the targeted mutation analysis for single mutations or mutation panels?', choices=[(1, u'Single mutations'), (2, u'Mutation Panels')])
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'targetedmitosingleorpanel'


class Microarray(models.Model):
    microarray_date = models.FloatField(help_text=u'Please specify four digit year', null=True, verbose_name=u'Year of microarray', blank=True)
    microarray_type = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Microarray type', choices=[(1, u'Oligonucleotide by aCGH'), (2, u'SNP'), (3, u'Targeted BAC'), (4, u'Whole genomic BAC'), (5, u'Unknown'), (6, u'Other')])
    microarray_type_spec = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Specify microarray type', blank=True)
    microarray_platform = models.IntegerField(help_text=u'', null=True, verbose_name=u'microarray platform | Specify microarray platform', blank=True, choices=[(1, u'Affymetrix'), (2, u'Agilent'), (3, u'Illumina'), (4, u'Nimblegen'), (5, u'Unknown/Not documented'), (6, u'Other')]) # This field type is a guess
    microarray_location = models.IntegerField(help_text=u'', null=True, verbose_name=u'Which laboratory performed microarray? | Specify microarray lab', blank=True, choices=[(1, u'Baylor'), (2, u'Provential'), (3, u'GeneDX'), (4, u'Transgenomic Familion'), (7, u'CHOP'), (5, u'Unknown'), (6, u'Other')]) # This field type is a guess
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'microarray'


class Variant(models.Model):
    variant_type = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Type of variant on microarray', choices=[(1, u'Deletion'), (2, u'Duplication'), (3, u'Run of homozygosity'), (4, u'Unknown')])
    variant_chromosome = models.IntegerField(help_text=u'', null=True, verbose_name=u'variant (on microarray) on chromosome', blank=True, choices=[(1, u'1'), (2, u'2'), (3, u'3'), (4, u'4'), (5, u'5'), (6, u'6'), (7, u'7'), (8, u'8'), (9, u'9'), (10, u'10'), (11, u'11'), (12, u'12'), (13, u'13'), (14, u'14'), (15, u'15'), (16, u'16'), (17, u'17'), (18, u'18'), (19, u'19'), (20, u'20'), (21, u'21'), (22, u'22'), (23, u'X'), (24, u'Y')]) # This field type is a guess
    microarray = models.ForeignKey(Microarray)

    class Meta:
	 db_table = 'variant'


class GeneTest(models.Model):
    gene_result = models.CharField(help_text=u'Example: GNE1  Note: Results from gene panels should be entered under gene panel section.', null=True, max_length=2000, verbose_name=u'Gene tested $d', blank=True)
    gene_result_was_summary = models.CharField(help_text=u'1, Positive - disease-causing mutation identified | 2, Negative - no definite/possible disease-causing mutation identified | 3, Variant of uncertain significance | 6, Polymorphism | 4, Results pending | 5, Results not known', null=True, max_length=2000, verbose_name=u'Indicate ALL types of results identified in gene $d', blank=True)
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'genetest'


class generesultwas(models.Model):
    label = models.CharField(help_text=u'For example, if testing showed both a disease-causing mutation and a polymorphism, check positive and polymorphism.', null=True, max_length=2000, verbose_name=u'Indicate ALL types of results identified in gene $d', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'For example, if testing showed both a disease-causing mutation and a polymorphism, check positive and polymorphism.', null=True, verbose_name=u'Indicate ALL types of results identified in gene $d', choices=[(1, u'Positive - disease-causing mutation identified'), (2, u'Negative - no definite/possible disease-causing mutation identified'), (3, u'Variant of uncertain significance'), (6, u'Polymorphism'), (4, u'Results pending'), (5, u'Results not known')])
    genetest = models.ForeignKey(GeneTest)

    class Meta:
	 db_table = 'generesultwas'


class Mutation(models.Model):
    change_dna_level = models.CharField(help_text=u'Example c.33C>G', null=True, max_length=2000, verbose_name=u'Change at cDNA level for disease causing mutation (on gene test)', blank=True)
    change_protein_level = models.CharField(help_text=u'Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name=u'Change  at protein level for disease causing mutation (on gene test)', blank=True)
    genetest = models.ForeignKey(GeneTest)

    class Meta:
	 db_table = 'mutation'


class VariantOfUnknownSignificance(models.Model):
    vus_dna_level = models.CharField(help_text=u'Example c.33C>G', null=True, max_length=2000, verbose_name=u'variant of unknown significance at cDNA level (on gene test)', blank=True)
    vus_protein_level = models.CharField(help_text=u'Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name=u'variant of unknown significance at protein level (on gene test)', blank=True)
    genetest = models.ForeignKey(GeneTest)

    class Meta:
	 db_table = 'variantofunknownsignificance'


class GenePanel(models.Model):
    gene_panel = models.CharField(help_text=u'For example, cardiomyopathy panel or hearing loss panel', null=True, max_length=2000, verbose_name=u'Name of gene panel performed', blank=True)
    panel_laboratory = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Which laboratory performed gene panel?', blank=True)
    panel_date_performed = models.FloatField(help_text=u'Please specify four digit year', null=True, verbose_name=u'Year panel was performed', blank=True)
    panel_list_gene = models.IntegerField(max_length=2000, blank=True, help_text=u'Optional', null=True, verbose_name=u'Would you like to list the genes that were on the panel?', choices=[(1, u'Yes'), (2, u'No')])
    panel_list_gene_entry = models.CharField(help_text=u'Example: PTPN11, HRAS, SOS1', null=True, max_length=2000, verbose_name=u'List genes on this panel (Separate with commas)', blank=True)
    panel_result_type_summary = models.CharField(help_text=u'1, Positive - disease-causing mutation identified | 2, Negative - no definite/possible disease-causing mutation identified | 3, Variant of uncertain significance | 4, Polymorphism | 5, Results pending | 6, Results not known', null=True, max_length=2000, verbose_name=u'Indicate ALL types of results identified on panel. ', blank=True)
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'genepanel'


class panelresulttype(models.Model):
    label = models.CharField(help_text=u'For example, if testing showed both a disease-causing mutation and a polymorphism, check positive and polymorphism.', null=True, max_length=2000, verbose_name=u'Indicate ALL types of results identified on panel. ', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'For example, if testing showed both a disease-causing mutation and a polymorphism, check positive and polymorphism.', null=True, verbose_name=u'Indicate ALL types of results identified on panel. ', choices=[(1, u'Positive - disease-causing mutation identified'), (2, u'Negative - no definite/possible disease-causing mutation identified'), (3, u'Variant of uncertain significance'), (4, u'Polymorphism'), (5, u'Results pending'), (6, u'Results not known')])
    genepanel = models.ForeignKey(GenePanel)

    class Meta:
	 db_table = 'panelresulttype'


class Gene(models.Model):
    gene_result = models.CharField(help_text=u'Example: GNE1', null=True, max_length=2000, verbose_name=u'gene tested on gene panel', blank=True)
    genepanel = models.ForeignKey(GenePanel)

    class Meta:
	 db_table = 'gene'


class Dcm(models.Model):
    change_at_dna_level = models.CharField(help_text=u'Example c.33C>G', null=True, max_length=2000, verbose_name=u'Change at cDNA level for disease-causing mutation on gene on gene panel ', blank=True)
    change_at_protein_level = models.CharField(help_text=u'Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name=u'Change at protein level for disease-causing mutation on gene on gene panel ', blank=True)
    gene = models.ForeignKey(Gene)

    class Meta:
	 db_table = 'dcm'


class VariantOfUnknownSignificance2(models.Model):
    vus_at_dna_level = models.CharField(help_text=u'Example c.33C>G', null=True, max_length=2000, verbose_name=u'variant of unknown significance at cDNA level on gene on gene panel', blank=True)
    vus_at_protein_level = models.CharField(help_text=u'Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name=u'variant of unknown significance at protein level on gene on gene panel', blank=True)
    gene = models.ForeignKey(Gene)

    class Meta:
	 db_table = 'variantofunknownsignificance2'


class SingleGeneDeletionDuplicationTest(models.Model):
    deldup_result = models.CharField(help_text=u'Example: GNE1', null=True, max_length=2000, verbose_name=u'Gene tested $d', blank=True)
    type_deldup_test = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Type of deletion/duplication testing performed', choices=[(1, u'MLPA'), (2, u'FISH'), (3, u'Unknown'), (4, u'Other')])
    deldup_result_was_summary = models.CharField(help_text=u'1, Positive - disease-causing deletion/duplication identified | 2, Negative - no definite/possible disease-causing deletion/duplication identified | 3, Variant of uncertain significance | 6, Polymorphism | 4, Results pending | 5, Results not known', null=True, max_length=2000, verbose_name=u'Indicate ALL types of results identified in gene $d', blank=True)
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'singlegenedeletionduplicationtest'


class deldupresultwas(models.Model):
    label = models.CharField(help_text=u'For example, if testing showed both a disease-causing mutation and a polymorphism, check positive and polymorphism.', null=True, max_length=2000, verbose_name=u'Indicate ALL types of results identified in gene $d', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'For example, if testing showed both a disease-causing mutation and a polymorphism, check positive and polymorphism.', null=True, verbose_name=u'Indicate ALL types of results identified in gene $d', choices=[(1, u'Positive - disease-causing deletion/duplication identified'), (2, u'Negative - no definite/possible disease-causing deletion/duplication identified'), (3, u'Variant of uncertain significance'), (6, u'Polymorphism'), (4, u'Results pending'), (5, u'Results not known')])
    singlegenedeletionduplicationtest = models.ForeignKey(SingleGeneDeletionDuplicationTest)

    class Meta:
	 db_table = 'deldupresultwas'


class DeletionDuplication(models.Model):
    change_dna_level = models.CharField(help_text=u'Example c.33C>G', null=True, max_length=2000, verbose_name=u'Deletion/Duplication at cDNA level for disease causing mutation (on deletion duplication  test)', blank=True)
    change_protein_level = models.CharField(help_text=u'Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name=u'Deletion/Duplication  at protein level for disease causing mutation (on deletion/duplication gene test)', blank=True)
    change_add_info_deldup = models.CharField(help_text=u'Example: Expected to result in exon skipping of exon 3', null=True, max_length=2000, verbose_name=u'Additional Information about deletion/duplication (if available) (on deletion/duplication test)', blank=True)
    singlegenedeletionduplicationtest = models.ForeignKey(SingleGeneDeletionDuplicationTest)

    class Meta:
	 db_table = 'deletionduplication'


class VariantOfUnknownSignificance3(models.Model):
    vus_dna_level = models.CharField(help_text=u'Example c.33C>G', null=True, max_length=2000, verbose_name=u'variant of unknown significance at cDNA level (on deletion/duplication test)', blank=True)
    vus_protein_level = models.CharField(help_text=u'Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name=u'variant of unknown significance at protein level (on deletion/duplication test)', blank=True)
    vus_add_info_deldup = models.CharField(help_text=u'Example: Expected to result in exon skipping of exon 3', null=True, max_length=2000, verbose_name=u'Additional Information about deletion/duplication VUS (on deletion/duplication test) (if available)', blank=True)
    singlegenedeletionduplicationtest = models.ForeignKey(SingleGeneDeletionDuplicationTest)

    class Meta:
	 db_table = 'variantofunknownsignificance3'


class TargetedTest(models.Model):
    targeted_mito_single_test = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'targeted mutation tested ', blank=True)
    targeted_mito_single_test_result = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'What was the result of the single mutation targeted test?', choices=[(1, u'Positive'), (2, u'Negative')])
    targeted_mito_single_test_sample_summary = models.CharField(help_text=u'1, blood | 2, urine | 3, muscle | 4, saliva | 5, other', null=True, max_length=2000, verbose_name=u'Tissue type tested for single mutation targeted test', blank=True)
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'targetedtest'


class targetedmitosingletestsample(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Tissue type tested for single mutation targeted test', blank=True)
    value = models.IntegerField(help_text=u'', null=True, verbose_name=u'Tissue type tested for single mutation targeted test', blank=True, choices=[(1, u'blood'), (2, u'urine'), (3, u'muscle'), (4, u'saliva'), (5, u'other')]) # This field type is a guess
    targetedtest = models.ForeignKey(TargetedTest)

    class Meta:
	 db_table = 'targetedmitosingletestsample'


class MitochondrialPanel(models.Model):
    targeted_mito_panel_loc = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Laboratory that performed targeted mitochondrial panel', blank=True)
    targeted_mito_panel_date = models.FloatField(help_text=u'Please specify four digit year', null=True, verbose_name=u'Year targeted mitochondrial panel was performed', blank=True)
    targeted_mito_panel_type = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'What was the type of the targeted mitochondrial panel?', blank=True)
    targeted_mito_panel_results = models.IntegerField(help_text=u'', null=True, verbose_name=u'Results of targeted mitochondrial panel', blank=True, choices=[(1, u'Normal'), (2, u'Variant Positive')]) # This field type is a guess
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'mitochondrialpanel'


class Gene2(models.Model):
    gene = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'gene on targeted mitochondrial panel that contained mutation', blank=True)
    mitochondrialpanel = models.ForeignKey(MitochondrialPanel)

    class Meta:
	 db_table = 'gene2'


class MdnaChange(models.Model):
    mdna_change = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'change in mDNA on gene on targeted mitochondrial panel', blank=True)
    gene2 = models.ForeignKey(Gene2)

    class Meta:
	 db_table = 'mdnachange'


class MdnaVariantOfUnknownSignificance(models.Model):
    vus_mdna = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'variant of unknown significance on gene on  targeted mitochondrial panel', blank=True)
    mitochondrialpanel = models.ForeignKey(MitochondrialPanel)

    class Meta:
	 db_table = 'mdnavariantofunknownsignificance'


class WholeMitoGeneSeq(models.Model):
    whole_mito_sequencing_date = models.FloatField(help_text=u'Please specify four digit year', null=True, verbose_name=u'Year of whole mitochondrial genome sequencing', blank=True)
    whole_mito_sequencing_loc = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Lab where whole mitochondrial genome sequencing was performed', blank=True)
    whole_mito_sequencing_sample_summary = models.CharField(help_text=u'1, blood | 2, urine | 3, muscle | 4, saliva | 5, other', null=True, max_length=2000, verbose_name=u'Sample type for whole mitochondrial genome sequencing', blank=True)
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'wholemitogeneseq'


class wholemitosequencingsample(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Sample type for whole mitochondrial genome sequencing', blank=True)
    value = models.IntegerField(help_text=u'', null=True, verbose_name=u'Sample type for whole mitochondrial genome sequencing', blank=True, choices=[(1, u'blood'), (2, u'urine'), (3, u'muscle'), (4, u'saliva'), (5, u'other')]) # This field type is a guess
    wholemitogeneseq = models.ForeignKey(WholeMitoGeneSeq)

    class Meta:
	 db_table = 'wholemitosequencingsample'


class Mutation2(models.Model):
    dc_mutation_gene = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Gene in which disease causing mutation was located on whole mitochondrial sequencing', blank=True)
    dc_mutation_mdna_level = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Change at mDNA level for disease causing mutation on whole mitochondrial sequencing', blank=True)
    wholemitogeneseq = models.ForeignKey(WholeMitoGeneSeq)

    class Meta:
	 db_table = 'mutation2'


class VariantOfUnknownSignificance4(models.Model):
    vus_mdna_level = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Change at mDNA level for variant of unknown significance on whole mitochondrial sequencing', blank=True)
    wholemitogeneseq = models.ForeignKey(WholeMitoGeneSeq)

    class Meta:
	 db_table = 'variantofunknownsignificance4'


class WholeMitoDel(models.Model):
    mito_deletion_analsysis_date = models.FloatField(help_text=u'Please specify four digit year', null=True, verbose_name=u'Year of mitochondrial deletion analysis', blank=True)
    mito_deletion_analsysis_loc = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Lab where mitochondrial deletion analysis was performed', blank=True)
    mito_deletion_analsysis_sample_summary = models.CharField(help_text=u'1, blood | 2, urine | 3, muscle | 4, saliva | 5, other', null=True, max_length=2000, verbose_name=u'Sample type for mitochondrial deletion analysis', blank=True)
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'wholemitodel'


class mitodeletionanalsysissample(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Sample type for mitochondrial deletion analysis', blank=True)
    value = models.IntegerField(help_text=u'', null=True, verbose_name=u'Sample type for mitochondrial deletion analysis', blank=True, choices=[(1, u'blood'), (2, u'urine'), (3, u'muscle'), (4, u'saliva'), (5, u'other')]) # This field type is a guess
    wholemitodel = models.ForeignKey(WholeMitoDel)

    class Meta:
	 db_table = 'mitodeletionanalsysissample'


class Deletion(models.Model):
    dc_deletion = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'What was the disease causing deletion identified on mitochondrial deletion analysis?', blank=True)
    dc_deletion_spec = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Other details for disease causing deletion on mitochondrial deletion analysis', blank=True)
    wholemitodel = models.ForeignKey(WholeMitoDel)

    class Meta:
	 db_table = 'deletion'


class VariantOfUnknownSignificance5(models.Model):
    vus = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'variant of unknown significance on mitochondrial deletion analysis', blank=True)
    wholemitodel = models.ForeignKey(WholeMitoDel)

    class Meta:
	 db_table = 'variantofunknownsignificance5'


class MitoCombo(models.Model):
    mito_combo_analysis_date = models.FloatField(help_text=u'Please specify four digit year', null=True, verbose_name=u'Year of combination mitochondrial analysis', blank=True)
    mito_combo_analysis_loc = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Lab where combination mitochondrial analysis was performed', blank=True)
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'mitocombo'


class Deletion2(models.Model):
    mito_combo_analysis_sample_summary = models.CharField(help_text=u'1, blood | 2, urine | 3, muscle | 4, saliva | 5, other', null=True, max_length=2000, verbose_name=u'Sample type for mitochondrial deletion analysis (from combined analysis $d1)', blank=True)
    mitocombo = models.ForeignKey(MitoCombo)

    class Meta:
	 db_table = 'deletion2'


class mitocomboanalysissample(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Sample type for mitochondrial deletion analysis (from combined analysis $d1)', blank=True)
    value = models.IntegerField(help_text=u'', null=True, verbose_name=u'Sample type for mitochondrial deletion analysis (from combined analysis $d1)', blank=True, choices=[(1, u'blood'), (2, u'urine'), (3, u'muscle'), (4, u'saliva'), (5, u'other')]) # This field type is a guess
    deletion2 = models.ForeignKey(Deletion2)

    class Meta:
	 db_table = 'mitocomboanalysissample'


class Deletion3(models.Model):
    dc_deletion = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'What was the disease causing deletion identified on mitochondrial deletion analysis (from combined analysis)?', blank=True)
    dc_deletion_spec = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Other details for disease causing deletion on mitochondrial deletion analysis (from combined analysis)', blank=True)
    deletion2 = models.ForeignKey(Deletion2)

    class Meta:
	 db_table = 'deletion3'


class VariantOfUnknownSignificance6(models.Model):
    vus = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'variant of unknown significance on mitochondrial deletion analysis (from combined analysis)', blank=True)
    deletion2 = models.ForeignKey(Deletion2)

    class Meta:
	 db_table = 'variantofunknownsignificance6'


class Panel(models.Model):
    targeted_mito_combo_panel_type = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'panel performed (on combination analysis)?', blank=True)
    targeted_mito_combo_panel_results = models.TextField(help_text=u'', null=True, verbose_name=u'Describe results of panel (on combined analysis)', blank=True) # This field type is a guess
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'panel'


class Gene3(models.Model):
    gene = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'gene on panel that contained mutation (on combined analysis)', blank=True)
    panel = models.ForeignKey(Panel)

    class Meta:
	 db_table = 'gene3'


class MdnaChange2(models.Model):
    mdna_change = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'change in mDNA on gene on panel (on combined analysis)', blank=True)
    gene3 = models.ForeignKey(Gene3)

    class Meta:
	 db_table = 'mdnachange2'


class MdnaVariantOfUnknownSignificance2(models.Model):
    vus_mdna = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'variant of unknown significance on gene from panel (on combined analysis)', blank=True)
    panel = models.ForeignKey(Panel)

    class Meta:
	 db_table = 'mdnavariantofunknownsignificance2'


class MethylationAnalysisTest(models.Model):
    meth_gene_tested = models.CharField(help_text=u'Example: GNE1 or 15q11', null=True, max_length=2000, verbose_name=u'Gene/Region tested $d', blank=True)
    meth_cond_test = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Condition/s being tested for', blank=True)
    meth_result = models.IntegerField(max_length=2000, blank=True, help_text=u'For example, if testing showed both a disease-causing mutation and a polymorphism, check positive and polymorphism.', null=True, verbose_name=u'Indicate result methylation analysis identified in gene/region $d', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Inconclusive'), (5, u'Result not known'), (4, u'Results pending')])
    meth_add_info = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Additional Information about methylation testing  (if available)', blank=True)
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'methylationanalysistest'


class FragileXFullMutationRepeat(models.Model):
    fragx_full_mut = models.FloatField(help_text=u'', null=True, verbose_name=u'What was the size of the full mutation repeat?', blank=True)
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'fragilexfullmutationrepeat'


class FragileXPreMutationRepeat(models.Model):
    fragx_pre_mut = models.FloatField(help_text=u'', null=True, verbose_name=u'What was the size of the pre mutation repeat?', blank=True)
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'fragilexpremutationrepeat'


class FragileXNormalRepeat(models.Model):
    fragx_norm = models.FloatField(help_text=u'', null=True, verbose_name=u'What was the size of the normal repeat?', blank=True)
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'fragilexnormalrepeat'


class FragileXInconclusiveRepeat(models.Model):
    fragx_incon = models.FloatField(help_text=u'', null=True, verbose_name=u'What was the size of the inconclusive repeat?', blank=True)
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'fragilexinconclusiverepeat'


class PriorTesting(models.Model):
    prior_test_explain = models.TextField(help_text=u'', null=True, verbose_name=u"Many of the sections on this instrument ask if there is a history of abnormal results for a type of test. If you answer yes you can summarize the patient's result history by giving result value ranges. Regardless of whether there is a history of abnormal results you can also add results of individual tests and specify if each one was normal or abnormal. Please answer Yes or No to the history of abnormal results question, and then choose whether to summarize the results (if they were abnormal), enter results of individual tests, or if you have no specific data, skip both.", blank=True) # This field type is a guess
    blood_lactate_sum_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'Answering yes will present a result summary section. This should be skipped if you would rather enter individual test results in the section below.', null=True, verbose_name=u'History of abnormal Blood Lactate results?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    blood_lactate_sum = models.TextField(help_text=u'', null=True, verbose_name=u'Blood Lactate range ', blank=True) # This field type is a guess
    blood_lactate_sum_comments = models.TextField(help_text=u'', null=True, verbose_name=u'Blood Lactate range result comment (quality concerns, normal range)', blank=True) # This field type is a guess
    blood_lactate_datapoints = models.NullBooleanField(help_text=u'', verbose_name=u'Would you like to enter individual Blood Lactate results?', blank=True)
    blood_pyruvate_sum_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'Answering yes will present a result summary section. This should be skipped if you would rather enter individual test results in the section below.', null=True, verbose_name=u'History of abnormal Blood Pyruvate results?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    blood_pyruvate_sum = models.TextField(help_text=u'', null=True, verbose_name=u'Blood Pyruvate range ', blank=True) # This field type is a guess
    blood_pyruvate_sum_comments = models.TextField(help_text=u'', null=True, verbose_name=u'Blood Pyruvate range result comment (quality concerns, normal range)', blank=True) # This field type is a guess
    blood_pyruvate_datapoints = models.NullBooleanField(help_text=u'', verbose_name=u'Would you like to enter individual Blood Pyruvate results?', blank=True)
    csf_lactate_sum_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'Answering yes will present a result summary section. This should be skipped if you would rather enter individual test results in the section below.', null=True, verbose_name=u'History of abnormal CSF Lactate results?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    csf_lactate_sum = models.TextField(help_text=u'', null=True, verbose_name=u'CSF Lactate range ', blank=True) # This field type is a guess
    csf_lactate_comments = models.TextField(help_text=u'', null=True, verbose_name=u'CSF Lactate range result comment (quality concerns, normal range)', blank=True) # This field type is a guess
    csf_lactate_datapoints = models.NullBooleanField(help_text=u'', verbose_name=u'Would you like to enter individual CSF Lactate results?', blank=True)
    csf_pyruvate_sum_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'Answering yes will present a result summary section. This should be skipped if you would rather enter individual test results in the section below.', null=True, verbose_name=u'History of abnormal CSF Pyruvate results?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    csf_pyruvate_sum = models.TextField(help_text=u'', null=True, verbose_name=u'CSF Pyruvate range ', blank=True) # This field type is a guess
    csf_pyruvate_comments = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'CSF Pyruvate range result comment (quality concerns, normal range)', blank=True)
    csf_pyruvate_datapoints = models.NullBooleanField(help_text=u'', verbose_name=u'Would you like to enter individual CSF Pyruvate results?', blank=True)
    paa_sum_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'Answering yes will present a result summary section. This should be skipped if you would rather enter individual test results in the section below.', null=True, verbose_name=u'History of abnormal PAA results?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    paa_sum = models.TextField(help_text=u'', null=True, verbose_name=u'PAA range ', blank=True) # This field type is a guess
    paa_comments = models.TextField(help_text=u'', null=True, verbose_name=u'PAA range result comment (quality concerns, normal range)', blank=True) # This field type is a guess
    paa_datapoints = models.NullBooleanField(help_text=u'', verbose_name=u'Would you like to enter individual PAA results?', blank=True)
    plasma_cn_acp_sum_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'Answering yes will present a result summary section. This should be skipped if you would rather enter individual test results in the section below.', null=True, verbose_name=u'History of abnormal Plasma CN/ACP results?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    plasma_cn_acp_sum = models.TextField(help_text=u'', null=True, verbose_name=u'Plasma CN/ACP range ', blank=True) # This field type is a guess
    plasma_cn_acp_comments = models.TextField(help_text=u'', null=True, verbose_name=u'Plasma CN/ACP  range result comment (quality concerns, normal range)', blank=True) # This field type is a guess
    plasma_cn_acp_datapoints = models.NullBooleanField(help_text=u'', verbose_name=u'Would you like to enter individual Plasma CN/ACP results?', blank=True)
    uoa_sum_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'Answering yes will present a result summary section. This should be skipped if you would rather enter individual test results in the section below.', null=True, verbose_name=u'History of abnormal UOA results?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    uoa_sum = models.TextField(help_text=u'', null=True, verbose_name=u'UOA range ', blank=True) # This field type is a guess
    uoa_comments = models.TextField(help_text=u'', null=True, verbose_name=u'UOA  range result comment (quality concerns, normal range)', blank=True) # This field type is a guess
    uoa_datapoints = models.NullBooleanField(help_text=u'', verbose_name=u'Would you like to enter individual UOA results?', blank=True)
    ck_sum_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'Answering yes will present a result summary section. This should be skipped if you would rather enter individual test results in the section below.', null=True, verbose_name=u'History of abnormal CK results?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    ck_sum = models.TextField(help_text=u'', null=True, verbose_name=u'CK range ', blank=True) # This field type is a guess
    ck_comments = models.TextField(help_text=u'', null=True, verbose_name=u'CK range result comment (quality concerns, normal range)', blank=True) # This field type is a guess
    ck_datapoints = models.NullBooleanField(help_text=u'', verbose_name=u'Would you like to enter individual CK results?', blank=True)
    uric_acid_sum_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'Answering yes will present a result summary section. This should be skipped if you would rather enter individual test results in the section below.', null=True, verbose_name=u'History of abnormal Uric acid results?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    uric_acid_sum = models.TextField(help_text=u'', null=True, verbose_name=u'Uric acid range ', blank=True) # This field type is a guess
    uric_acid_comments = models.TextField(help_text=u'', null=True, verbose_name=u'Uric acid range result comment (quality concerns, normal range)', blank=True) # This field type is a guess
    uric_acid_datapoints = models.NullBooleanField(help_text=u'', verbose_name=u'Would you like to enter individual Uric acid results?', blank=True)
    lfts_sum_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'Answering yes will present a result summary section. This should be skipped if you would rather enter individual test results in the section below.', null=True, verbose_name=u'History of abnormal LFTs results?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    lfts_sum = models.TextField(help_text=u'', null=True, verbose_name=u'LFTs range ', blank=True) # This field type is a guess
    lfts_comments = models.TextField(help_text=u'', null=True, verbose_name=u'LFTs range result comment (quality concerns, normal range)', blank=True) # This field type is a guess
    lfts_datapoints = models.NullBooleanField(help_text=u'', verbose_name=u'Would you like to enter individual LFTs results?', blank=True)
    cbc_sum_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'Answering yes will present a result summary section. This should be skipped if you would rather enter individual test results in the section below.', null=True, verbose_name=u'History of abnormal CBC results?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    cbc_sum = models.TextField(help_text=u'', null=True, verbose_name=u'CBC range ', blank=True) # This field type is a guess
    cbc_comments = models.TextField(help_text=u'', null=True, verbose_name=u'CBC range result comment (quality concerns, normal range)', blank=True) # This field type is a guess
    cbc_datapoints = models.NullBooleanField(help_text=u'', verbose_name=u'Would you like to enter individual CBC results?', blank=True)
    urinalysis_comments = models.TextField(help_text=u'', null=True, verbose_name=u'Urinalysis comment (quality concerns, normal range)', blank=True) # This field type is a guess
    urinalysis_datapoints = models.NullBooleanField(help_text=u'', verbose_name=u'Would you like to enter individual urinalysis results?', blank=True)
    cmp_sum_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'Answering yes will present a result summary section. This should be skipped if you would rather enter individual test results in the section below.', null=True, verbose_name=u'History of abnormal Chemistry Panel results?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    cmp_glucose_sum = models.TextField(help_text=u'', null=True, verbose_name=u'Glucose level ', blank=True) # This field type is a guess
    cmp_calcium_sum = models.TextField(help_text=u'', null=True, verbose_name=u'Calcium level ', blank=True) # This field type is a guess
    cmp_sodium_sum = models.TextField(help_text=u'', null=True, verbose_name=u'Sodium level ', blank=True) # This field type is a guess
    cmp_potassium_sum = models.TextField(help_text=u'', null=True, verbose_name=u'Potassium level ', blank=True) # This field type is a guess
    cmp_bicarb_sum = models.TextField(help_text=u'', null=True, verbose_name=u'Bicarb level ', blank=True) # This field type is a guess
    cmp_chloride_sum = models.TextField(help_text=u'', null=True, verbose_name=u'Chloride level ', blank=True) # This field type is a guess
    cmp_bun_sum = models.TextField(help_text=u'', null=True, verbose_name=u'BUN level ', blank=True) # This field type is a guess
    cmp_creatinine_sum = models.TextField(help_text=u'', null=True, verbose_name=u'Creatinine level ', blank=True) # This field type is a guess
    cmp_albumin_sum = models.TextField(help_text=u'', null=True, verbose_name=u'Albumin level ', blank=True) # This field type is a guess
    cmp_total_protein_sum = models.TextField(help_text=u'', null=True, verbose_name=u'Total protein level ', blank=True) # This field type is a guess
    cmp_alp_sum = models.TextField(help_text=u'', null=True, verbose_name=u'ALP (Alkaline Phospatase) level ', blank=True) # This field type is a guess
    cmp_alt_sum = models.TextField(help_text=u'', null=True, verbose_name=u'ALT (Alanine aminotransferase) level ', blank=True) # This field type is a guess
    cmp_ast_sum = models.TextField(help_text=u'', null=True, verbose_name=u'AST (Aspartate aminotransferase) level ', blank=True) # This field type is a guess
    cmp_bilirubin_sum = models.TextField(help_text=u'', null=True, verbose_name=u'Bilirubin level ', blank=True) # This field type is a guess
    cmp_comments = models.TextField(help_text=u'', null=True, verbose_name=u'Chemistry Panel comments (quality concerns, normal ranges)', blank=True) # This field type is a guess
    cmp_datapoints = models.NullBooleanField(help_text=u'', verbose_name=u'Would you like to enter individual Chemistry panel results', blank=True)
    thyroid_study_comment = models.TextField(help_text=u'', null=True, verbose_name=u'Thyroid study comment (quality concerns)', blank=True) # This field type is a guess
    thyroid_datapoints = models.NullBooleanField(help_text=u'', verbose_name=u'Would you like to enter individual thyroid study results?', blank=True)
    renal_function_sum_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'Answering yes will present a result summary section. This should be skipped if you would rather enter individual test results in the section below.', null=True, verbose_name=u'History of abnormal renal study results?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    renal_function_sum_urea_nitrogen = models.TextField(help_text=u'', null=True, verbose_name=u'Urea nitrogen range ', blank=True) # This field type is a guess
    renal_function_sum_sodium = models.TextField(help_text=u'', null=True, verbose_name=u'Sodium range ', blank=True) # This field type is a guess
    renal_function_sum_potassium = models.TextField(help_text=u'', null=True, verbose_name=u'Potassium range ', blank=True) # This field type is a guess
    renal_function_sum_bicarb = models.TextField(help_text=u'', null=True, verbose_name=u'Bicarb range ', blank=True) # This field type is a guess
    renal_function_sum_chloride = models.TextField(help_text=u'', null=True, verbose_name=u'Chloride range ', blank=True) # This field type is a guess
    renal_function_sum_creatinine = models.TextField(help_text=u'', null=True, verbose_name=u'Creatinine range ', blank=True) # This field type is a guess
    renal_function_sum_comment = models.TextField(help_text=u'', null=True, verbose_name=u'Renal function range result comment (quality concerns, normal range)', blank=True) # This field type is a guess
    renal_function_datapoints = models.NullBooleanField(help_text=u'', verbose_name=u'Would you like to enter individual renal function studies?', blank=True)
    sweat_sum_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'Answering yes will present a result summary section. This should be skipped if you would rather enter individual test results in the section below.', null=True, verbose_name=u'History of abnormal sweat testing?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    sweat_sum = models.TextField(help_text=u'', null=True, verbose_name=u'Sweat test range ', blank=True) # This field type is a guess
    sweat_comments = models.TextField(help_text=u'', null=True, verbose_name=u'Sweat test range result comment (quality concerns, normal range)', blank=True) # This field type is a guess
    sweat_datapoints = models.NullBooleanField(help_text=u'', verbose_name=u'Would you like to enter individual Sweat test results?', blank=True)
    celiac_sum_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'Answering yes will present a result summary section. This should be skipped if you would rather enter individual test results in the section below.', null=True, verbose_name=u'History of abnormal  testing for celiac disease?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    celiac_test_type_sum = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Type of testing for celiac disease', blank=True)
    celiac_sum = models.TextField(help_text=u'', null=True, verbose_name=u'Celiac disease range ', blank=True) # This field type is a guess
    celiac_comments = models.TextField(help_text=u'', null=True, verbose_name=u'Celiac disease test range result comment (quality concerns, normal range)', blank=True) # This field type is a guess
    celiac_datapoints = models.NullBooleanField(help_text=u'', verbose_name=u'Would you like to enter individual Celiac disease test results?', blank=True)
    biopsies_performed = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Biopsies performed', choices=[(6, u'None'), (1, u'Muscle'), (2, u'Skin'), (3, u'Liver'), (4, u'Brain'), (5, u'Bone Marrow'), (7, u'Other'), (8, u'Unknown/Not documented')])
    cardio_tests_performed = models.IntegerField(help_text=u'', null=True, verbose_name=u'Cardiovascular tests performed | Describe  cardiac testing', blank=True, choices=[(1, u'None'), (2, u'Electrocardiogram (ECG)'), (3, u'Echocardiogram (ECHO)'), (4, u'24 Hour Monitoring (Holter Monitor)'), (5, u'Exercise Stress Test (EST)'), (6, u'Cardiac MRI'), (8, u'Unknown/Not documented'), (7, u'Other')]) # This field type is a guess
    musculoskeletal_tests_performed = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Musculoskeletal tests performed', choices=[(3, u'None'), (1, u'Electromyogram (EMG)'), (2, u'Nerve Conduction Velocity (NCV)'), (4, u'Unknown/Not documented')])
    prior_testing_feedback = models.TextField(help_text=u'', null=True, verbose_name=u'Please provide any feedback for this form (for example: missing questions, questions not relevant for a disease area, ambiguities, places where a textbox could be replaced with discrete choices, missing discrete choices)', blank=True) # This field type is a guess
    lab_tests_performed_summary = models.CharField(help_text=u'19, None | 1, Blood Lactate | 2, Blood Pyruvate | 3, CSF Lactate | 4, CSF Pyruvate | 5, PAA | 6, Plasma CN/ACP | 7, UOA | 8, CK | 9, Uric Acid | 10, LFTs | 11, CBC | 12, Urinalysis | 13, Chemistry Panel (CMP) | 14, Thyroid Function | 15, Renal Function | 16, Sweat Test | 17, Celiac Disease | 18, Unknown/Not documented', null=True, max_length=2000, verbose_name=u'Laboratory tests performed', blank=True)
    urinalysis_range_summary = models.CharField(help_text=u'1, Blood | 2, Protein | 3, Infection', null=True, max_length=2000, verbose_name=u'Presence of any of the following over all urinalsyses?', blank=True)
    thyroid_function_sum_summary = models.CharField(help_text=u'1, TSH elevation | 2, TSH decrease | 3, T4 elevation | 4, T4 decrease', null=True, max_length=2000, verbose_name=u'Thyroid function findings over time', blank=True)
    image_studies_performed_summary = models.CharField(help_text=u'6, None | 1, MRI | 2, Spectroscopy (MRS) | 3, CT | 4, Ultrasound | 5, Xray | 7, Endoscopy | 8, Unknown/Not documented', null=True, max_length=2000, verbose_name=u'Imaging studies performed', blank=True)
    vision_tests_performed_summary = models.CharField(help_text=u' 2, None | 1, Electroretinogram (ERG) | 3, Other | 4, Unknown/Not documented', null=True, max_length=2000, verbose_name=u'Vision tests performed', blank=True)
    neurologic_tests_performed_summary = models.CharField(help_text=u'2, None | 1, Electroencephalogram (EEG) | 3, Unknown/Not documented', null=True, max_length=2000, verbose_name=u'Neurologic tests performed', blank=True)
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'priortesting'


class labtestsperformed(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Laboratory tests performed', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Laboratory tests performed', choices=[(19, u'None'), (1, u'Blood Lactate'), (2, u'Blood Pyruvate'), (3, u'CSF Lactate'), (4, u'CSF Pyruvate'), (5, u'PAA'), (6, u'Plasma CN/ACP'), (7, u'UOA'), (8, u'CK'), (9, u'Uric Acid'), (10, u'LFTs'), (11, u'CBC'), (12, u'Urinalysis'), (13, u'Chemistry Panel (CMP)'), (14, u'Thyroid Function'), (15, u'Renal Function'), (16, u'Sweat Test'), (17, u'Celiac Disease'), (18, u'Unknown/Not documented')])
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'labtestsperformed'


class urinalysisrange(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Presence of any of the following over all urinalsyses?', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Presence of any of the following over all urinalsyses?', choices=[(1, u'Blood'), (2, u'Protein'), (3, u'Infection')])
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'urinalysisrange'


class thyroidfunctionsum(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Thyroid function findings over time', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Thyroid function findings over time', choices=[(1, u'TSH elevation'), (2, u'TSH decrease'), (3, u'T4 elevation'), (4, u'T4 decrease')])
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'thyroidfunctionsum'


class imagestudiesperformed(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Imaging studies performed', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Imaging studies performed', choices=[(6, u'None'), (1, u'MRI'), (2, u'Spectroscopy (MRS)'), (3, u'CT'), (4, u'Ultrasound'), (5, u'Xray'), (7, u'Endoscopy'), (8, u'Unknown/Not documented')])
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'imagestudiesperformed'


class visiontestsperformed(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Vision tests performed', blank=True)
    value = models.IntegerField(help_text=u'', null=True, verbose_name=u'Vision tests performed', blank=True, choices=[(2, u'None'), (1, u'Electroretinogram (ERG)'), (3, u'Other'), (4, u'Unknown/Not documented')]) # This field type is a guess
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'visiontestsperformed'


class neurologictestsperformed(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Neurologic tests performed', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Neurologic tests performed', choices=[(2, u'None'), (1, u'Electroencephalogram (EEG)'), (3, u'Unknown/Not documented')])
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'neurologictestsperformed'


class BloodLactate(models.Model):
    blood_lactate_date = models.FloatField(help_text=u'Please specify four digit year', null=True, verbose_name=u'Year of Blood Lactate', blank=True)
    blood_lactate = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Blood Lactate result', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    blood_lactate_result = models.TextField(help_text=u'', null=True, verbose_name=u'Blood Lactate result ', blank=True) # This field type is a guess
    blood_lactate_location = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Lab where Blood Lactate was performed', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'bloodlactate'


class BloodPyruvate(models.Model):
    blood_pyruvate_date = models.FloatField(help_text=u'Please specify four digit year', null=True, verbose_name=u'Year of Blood Pyruvate', blank=True)
    blood_pyruvate = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'$ Blood Pyruvate result', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    blood_pyruvate_result = models.TextField(help_text=u'', null=True, verbose_name=u'Blood Pyruvate result ', blank=True) # This field type is a guess
    blood_pyruvate_location = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Lab where Blood Pyruvate was performed?', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'bloodpyruvate'


class CsfLactate(models.Model):
    csf_lactate_date = models.FloatField(help_text=u'Please specify four digit year', null=True, verbose_name=u'Year of CSF Lactate', blank=True)
    csf_lactate = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'CSF Lactate result', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    csf_lactate_result = models.TextField(help_text=u'', null=True, verbose_name=u'CSF Lactate result ', blank=True) # This field type is a guess
    csf_lactate_location = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Lab where CSF Lactate was performed?', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'csflactate'


class CsfPyruvate(models.Model):
    csf_pyruvate_date = models.FloatField(help_text=u'Please specify four digit year', null=True, verbose_name=u'Year of CSF Pyruvate', blank=True)
    csf_pyruvate = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'CSF Pyruvate result', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    csf_pyruvate_result = models.TextField(help_text=u'', null=True, verbose_name=u'CSF Pyruvate result ', blank=True) # This field type is a guess
    csf_pyruvate_location = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Lab where $ CSF Pyruvate was performed?', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'csfpyruvate'


class Paa(models.Model):
    paa_date = models.FloatField(help_text=u'Please specify four digit year', null=True, verbose_name=u'Year of PAA', blank=True)
    paa = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'PAA Pyruvate result', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    paa_result = models.TextField(help_text=u'', null=True, verbose_name=u'PAA result ', blank=True) # This field type is a guess
    paa_location = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Lab where was PAA performed?', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'paa'


class PlasmaCnacp(models.Model):
    plasma_cn_acp_date = models.FloatField(help_text=u'Please specify four digit year', null=True, verbose_name=u'Year of Plasma CN/ACP', blank=True)
    plasma_cn_acp = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Plasma CN/ACP result', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    plasma_cn_acp_result = models.TextField(help_text=u'', null=True, verbose_name=u'Plasma CN/ACP result ', blank=True) # This field type is a guess
    plasma_cn_acp_location = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Lab where Plasma CN/ACP was performed?', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'plasmacnacp'


class Uoa(models.Model):
    uoa_date = models.FloatField(help_text=u'Please specify four digit year', null=True, verbose_name=u'Year of UOA', blank=True)
    uoa = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'UOA result', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    uoa_result = models.TextField(help_text=u'', null=True, verbose_name=u'UOA result ', blank=True) # This field type is a guess
    uoa_location = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Lab where UOA  was performed?', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'uoa'


class Ck(models.Model):
    ck_date = models.FloatField(help_text=u'Please specify four digit year', null=True, verbose_name=u'Year of CK', blank=True)
    ck = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'CK result', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    ck_result = models.TextField(help_text=u'', null=True, verbose_name=u'CK result ', blank=True) # This field type is a guess
    ck_location = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Lab where CK was performed?', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'ck'


class UricAcid(models.Model):
    uric_acid_date = models.FloatField(help_text=u'Please specify four digit year', null=True, verbose_name=u'Year of Uric acid', blank=True)
    uric_acid = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Uric acid result', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    uric_acid_result = models.TextField(help_text=u'', null=True, verbose_name=u'Uric acid result ', blank=True) # This field type is a guess
    uric_acid_location = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Lab where Uric acid was performed?', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'uricacid'


class Lft(models.Model):
    lfts_date = models.FloatField(help_text=u'Please specify four digit year', null=True, verbose_name=u'Year of LFTs', blank=True)
    lfts = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'LFTs result', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    lfts_result = models.TextField(help_text=u'', null=True, verbose_name=u'LFTs result ', blank=True) # This field type is a guess
    lfts_location = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Lab where LFTs was performed?', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'lft'


class Cbc(models.Model):
    cbc_date = models.FloatField(help_text=u'Please specify four digit year', null=True, verbose_name=u'Year of CBC', blank=True)
    cbc = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'CBC result', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    cbc_result = models.TextField(help_text=u'', null=True, verbose_name=u'CBC result ', blank=True) # This field type is a guess
    cbc_location = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Lab where CBC was performed?', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'cbc'


class Urinalysi(models.Model):
    urinalysis_date = models.FloatField(help_text=u'Please specify four digit year', null=True, verbose_name=u'Year of  Urinalysis', blank=True)
    urinalysis = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Urinalysis result', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    urinalysis_location = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Lab where Urinalysis was performed?', blank=True)
    urinalysis_details_summary = models.CharField(help_text=u'1, Blood | 2, Protein | 3, Infection', null=True, max_length=2000, verbose_name=u'Presence of', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'urinalysi'


class urinalysisdetails(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Presence of', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Presence of', choices=[(1, u'Blood'), (2, u'Protein'), (3, u'Infection')])
    urinalysi = models.ForeignKey(Urinalysi)

    class Meta:
	 db_table = 'urinalysisdetails'


class ChemistryPanel(models.Model):
    cmp_glucose_level = models.TextField(help_text=u'', null=True, verbose_name=u'Glucose level ', blank=True) # This field type is a guess
    cmp_calcium_level = models.TextField(help_text=u'', null=True, verbose_name=u'Calcium level ', blank=True) # This field type is a guess
    cmp_electrolyte_sodium_level = models.TextField(help_text=u'', null=True, verbose_name=u'Sodium level ', blank=True) # This field type is a guess
    cmp_electrolyte_potassium_level = models.TextField(help_text=u'', null=True, verbose_name=u'Potassium level ', blank=True) # This field type is a guess
    cmp_electrolyte_bicarb_level = models.TextField(help_text=u'', null=True, verbose_name=u'Bicarb level ', blank=True) # This field type is a guess
    cmp_electrolyte_chloride_level = models.TextField(help_text=u'', null=True, verbose_name=u'Chloride level ', blank=True) # This field type is a guess
    cmp_bun_level = models.TextField(help_text=u'', null=True, verbose_name=u'BUN level ', blank=True) # This field type is a guess
    cmp_creatinine_level = models.TextField(help_text=u'', null=True, verbose_name=u'Creatinine level ', blank=True) # This field type is a guess
    cmp_albumin_level = models.TextField(help_text=u'', null=True, verbose_name=u'Albumin level ', blank=True) # This field type is a guess
    cmp_total_protein_level = models.TextField(help_text=u'', null=True, verbose_name=u'Total protein level ', blank=True) # This field type is a guess
    cmp_alp_level = models.TextField(help_text=u'', null=True, verbose_name=u'ALP (Alkaline Phospatase) level ', blank=True) # This field type is a guess
    cmp_alt_level = models.TextField(help_text=u'', null=True, verbose_name=u'ALT (Alanine aminotransferase) level ', blank=True) # This field type is a guess
    cmp_ast_level = models.TextField(help_text=u'', null=True, verbose_name=u'AST(Aspartate aminotransferase) level ', blank=True) # This field type is a guess
    cmp_bilirubin_level = models.TextField(help_text=u'', null=True, verbose_name=u'Bilirubin level ', blank=True) # This field type is a guess
    cmp_date = models.FloatField(help_text=u'Please specify four digit year', null=True, verbose_name=u'Year of chemistry panel', blank=True)
    cmp_location = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Lab where chemistry panel was performed', blank=True)
    cmp_misc_summary = models.CharField(help_text=u'1, Glucose | 2, Calcium | 3, All of the above within normal range', null=True, max_length=2000, verbose_name=u'Chemistry Panel Results (Part 1)\n\nAbnormal values', blank=True)
    cmp_electrolyte_summary = models.CharField(help_text=u'1, Sodium | 2, Potassium | 3, Bicarb | 4, Chloride | 5, All of the above within normal range', null=True, max_length=2000, verbose_name=u'Chemistry Panel Results (Part 2)\n\nAbnormal electrolytes', blank=True)
    cmp_kidney_summary = models.CharField(help_text=u'1, Blood Urea Nitrogen (BUN) | 2, Creatinine | 3, All of the above within normal range', null=True, max_length=2000, verbose_name=u'Chemistry Panel Results (Part 3)\n\nAbnormal Kidney values', blank=True)
    cmp_protein_summary = models.CharField(help_text=u'1, Albumin | 2, Total protein | 3, All of the above within normal range', null=True, max_length=2000, verbose_name=u'Chemistry Panel Results (Part 4)\n\nAbnormal protein values', blank=True)
    cmp_liver_summary = models.CharField(help_text=u'1, ALP (Alkaline Phosphatase) | 2, ALT (Alanine aminotransferase) | 3, AST (Aspartate aminotransferase) | 4, Bilirubin | 5, All of the above within normal range', null=True, max_length=2000, verbose_name=u'Chemistry Panel Results (Part 5)\n\nAbnormal liver values', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'chemistrypanel'


class cmpmisc(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Chemistry Panel Results (Part 1)\n\nAbnormal values', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Chemistry Panel Results (Part 1)\n\nAbnormal values', choices=[(1, u'Glucose'), (2, u'Calcium'), (3, u'All of the above within normal range')])
    chemistrypanel = models.ForeignKey(ChemistryPanel)

    class Meta:
	 db_table = 'cmpmisc'


class cmpelectrolyte(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Chemistry Panel Results (Part 2)\n\nAbnormal electrolytes', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Chemistry Panel Results (Part 2)\n\nAbnormal electrolytes', choices=[(1, u'Sodium'), (2, u'Potassium'), (3, u'Bicarb'), (4, u'Chloride'), (5, u'All of the above within normal range')])
    chemistrypanel = models.ForeignKey(ChemistryPanel)

    class Meta:
	 db_table = 'cmpelectrolyte'


class cmpkidney(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Chemistry Panel Results (Part 3)\n\nAbnormal Kidney values', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Chemistry Panel Results (Part 3)\n\nAbnormal Kidney values', choices=[(1, u'Blood Urea Nitrogen (BUN)'), (2, u'Creatinine'), (3, u'All of the above within normal range')])
    chemistrypanel = models.ForeignKey(ChemistryPanel)

    class Meta:
	 db_table = 'cmpkidney'


class cmpprotein(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Chemistry Panel Results (Part 4)\n\nAbnormal protein values', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Chemistry Panel Results (Part 4)\n\nAbnormal protein values', choices=[(1, u'Albumin'), (2, u'Total protein'), (3, u'All of the above within normal range')])
    chemistrypanel = models.ForeignKey(ChemistryPanel)

    class Meta:
	 db_table = 'cmpprotein'


class cmpliver(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Chemistry Panel Results (Part 5)\n\nAbnormal liver values', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Chemistry Panel Results (Part 5)\n\nAbnormal liver values', choices=[(1, u'ALP (Alkaline Phosphatase)'), (2, u'ALT (Alanine aminotransferase)'), (3, u'AST (Aspartate aminotransferase)'), (4, u'Bilirubin'), (5, u'All of the above within normal range')])
    chemistrypanel = models.ForeignKey(ChemistryPanel)

    class Meta:
	 db_table = 'cmpliver'


class ThyroidStudy(models.Model):
    thyroid_study_date = models.FloatField(help_text=u'Please specify four digit year', null=True, verbose_name=u'Year of thyroid study', blank=True)
    thyroid_study = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Thyroid study result', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    thyroid_function_location = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Lab where thyroid testing was performed?', blank=True)
    thyroid_study_function_summary = models.CharField(help_text=u'1, TSH elevation | 2, TSH decrease | 3, T4 elevation | 4, T4 decrease', null=True, max_length=2000, verbose_name=u'Thyroid function findings', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'thyroidstudy'


class thyroidstudyfunction(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Thyroid function findings', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Thyroid function findings', choices=[(1, u'TSH elevation'), (2, u'TSH decrease'), (3, u'T4 elevation'), (4, u'T4 decrease')])
    thyroidstudy = models.ForeignKey(ThyroidStudy)

    class Meta:
	 db_table = 'thyroidstudyfunction'


class RenalFunctionStudy(models.Model):
    renal_function_date = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Year of renal function study', blank=True)
    renal_function_urea_nitrogen = models.TextField(help_text=u'', null=True, verbose_name=u'Urea Nitrogen  on renal function study', blank=True) # This field type is a guess
    renal_function_electrolyte_sodium_level = models.TextField(help_text=u'', null=True, verbose_name=u'Sodium  on renal function study', blank=True) # This field type is a guess
    renal_function_electrolyte_potassium_level = models.TextField(help_text=u'', null=True, verbose_name=u'Potassium  on renal function study', blank=True) # This field type is a guess
    renal_function_electrolyte_bicarb_level = models.TextField(help_text=u'', null=True, verbose_name=u'Bicarb  on renal function study', blank=True) # This field type is a guess
    renal_function_electrolyte_chloride_level = models.TextField(help_text=u'', null=True, verbose_name=u'Chloride  on renal function study', blank=True) # This field type is a guess
    renal_function_creatinine = models.TextField(help_text=u'', null=True, verbose_name=u'Creatinine  on renal function study', blank=True) # This field type is a guess
    renal_function_location = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Lab where renal study was performed', blank=True)
    renal_function_summary = models.CharField(help_text=u'1, Urea Nitrogen | 2, Electrolytes | 3, Creatinine | 4, All of the above within normal range', null=True, max_length=2000, verbose_name=u'Abnormal Renal Function Study Results', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'renalfunctionstudy'


class renalfunction(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Abnormal Renal Function Study Results', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Abnormal Renal Function Study Results', choices=[(1, u'Urea Nitrogen'), (2, u'Electrolytes'), (3, u'Creatinine'), (4, u'All of the above within normal range')])
    renalfunctionstudy = models.ForeignKey(RenalFunctionStudy)

    class Meta:
	 db_table = 'renalfunction'


class SweatTest(models.Model):
    sweat_date = models.FloatField(help_text=u'Please specify four digit year', null=True, verbose_name=u'Year of Sweat test', blank=True)
    sweat = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Sweat test result', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    sweat_result = models.TextField(help_text=u'', null=True, verbose_name=u'Sweat test result ', blank=True) # This field type is a guess
    sweat_location = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Lab where Sweat test was performed?', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'sweattest'


class CeliacDiseaseTest(models.Model):
    celiac_date = models.FloatField(help_text=u'Please specify four digit year', null=True, verbose_name=u'Year of Celiac disease test', blank=True)
    celiac = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Celiac disease test result', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    celiac_test_type = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Celiac disease test type', blank=True)
    celiac_result = models.TextField(help_text=u'', null=True, verbose_name=u'Celiac disease test result ', blank=True) # This field type is a guess
    celiac_location = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Lab where Celiac disease test was performed?', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'celiacdiseasetest'


class Mri(models.Model):
    mri_date = models.FloatField(help_text=u'Please specify four digit year', null=True, verbose_name=u'Year of MRI', blank=True)
    mri = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'MRI result', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    mri_temp_bone_other_features = models.TextField(help_text=u'', null=True, verbose_name=u'Other temporal bone features', blank=True) # This field type is a guess
    mri_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Specify MRI Result', blank=True) # This field type is a guess
    mri_location = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Where was MRI performed?', blank=True)
    mri_body_part_summary = models.CharField(help_text=u'1, Brain | 2, Kidney | 3, Abdomen | 4, Chest | 5, Muscle | 6, Head | 8, Temporal Bones | 7, Other', null=True, max_length=2000, verbose_name=u'Part of body screened on MRI | Specify  part of body screened', blank=True)
    mri_temp_bone_features_summary = models.CharField(help_text=u'1, Cochlear Nerve Hypoplasia | 2, EVA | 3, Other', null=True, max_length=2000, verbose_name=u'Temporal bone features', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'mri'


class mribodypart(models.Model):
    label = models.CharField(help_text=u'Please enter cardiac MRIs in CMRI Results instrument if the cardiac intake forms will be used.', null=True, max_length=2000, verbose_name=u'Part of body screened on MRI | Specify  part of body screened', blank=True)
    value = models.IntegerField(help_text=u'Please enter cardiac MRIs in CMRI Results instrument if the cardiac intake forms will be used.', null=True, verbose_name=u'Part of body screened on MRI | Specify  part of body screened', blank=True, choices=[(1, u'Brain'), (2, u'Kidney'), (3, u'Abdomen'), (4, u'Chest'), (5, u'Muscle'), (6, u'Head'), (8, u'Temporal Bones'), (7, u'Other')]) # This field type is a guess
    mri = models.ForeignKey(Mri)

    class Meta:
	 db_table = 'mribodypart'


class mritempbonefeatures(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Temporal bone features', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Temporal bone features', choices=[(1, u'Cochlear Nerve Hypoplasia'), (2, u'EVA'), (3, u'Other')])
    mri = models.ForeignKey(Mri)

    class Meta:
	 db_table = 'mritempbonefeatures'


class BrainSpectroscopyMr(models.Model):
    mrs_date = models.FloatField(help_text=u'Please specify four digit year', null=True, verbose_name=u'Year of spectroscopy (MRS)', blank=True)
    mrs = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'spectroscopy (MRS) result', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    mrs_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Specify spectroscopy (MRS) result', blank=True) # This field type is a guess
    mrs_location = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Where was spectroscopy (MRS) performed?', blank=True)
    mrs_body_part_summary = models.CharField(help_text=u'1, Brain | 2, Kidney | 3, Abdomen | 4, Chest | 5, Muscle | 6, Head | 7, Other', null=True, max_length=2000, verbose_name=u'Part of body screened on spectroscopy  (MRS) | Specify  part of body screened', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'brainspectroscopymr'


class mrsbodypart(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Part of body screened on spectroscopy  (MRS) | Specify  part of body screened', blank=True)
    value = models.IntegerField(help_text=u'', null=True, verbose_name=u'Part of body screened on spectroscopy  (MRS) | Specify  part of body screened', blank=True, choices=[(1, u'Brain'), (2, u'Kidney'), (3, u'Abdomen'), (4, u'Chest'), (5, u'Muscle'), (6, u'Head'), (7, u'Other')]) # This field type is a guess
    brainspectroscopymr = models.ForeignKey(BrainSpectroscopyMr)

    class Meta:
	 db_table = 'mrsbodypart'


class Ct(models.Model):
    ct_date = models.FloatField(help_text=u'Please specify four digit year', null=True, verbose_name=u'Year of CT', blank=True)
    ct = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'CT result', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    ct_temp_bone_other_features = models.TextField(help_text=u'', null=True, verbose_name=u'Other temporal bone features', blank=True) # This field type is a guess
    ct_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Specify CT result', blank=True) # This field type is a guess
    ct_location = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Where was CT performed?', blank=True)
    ct_body_part_summary = models.CharField(help_text=u'1, Brain | 2, Kidney | 3, Abdomen | 4, Chest | 5, Muscle | 6, Head | 8, Temporal Bones | 7, Other', null=True, max_length=2000, verbose_name=u'Part of body screened on CT | Specify  part of body screened', blank=True)
    ct_temp_bone_features_summary = models.CharField(help_text=u'1, Cochlear Nerve Hypoplasia | 2, EVA | 3, Other', null=True, max_length=2000, verbose_name=u'Temporal bone features', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'ct'


class ctbodypart(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Part of body screened on CT | Specify  part of body screened', blank=True)
    value = models.IntegerField(help_text=u'', null=True, verbose_name=u'Part of body screened on CT | Specify  part of body screened', blank=True, choices=[(1, u'Brain'), (2, u'Kidney'), (3, u'Abdomen'), (4, u'Chest'), (5, u'Muscle'), (6, u'Head'), (8, u'Temporal Bones'), (7, u'Other')]) # This field type is a guess
    ct = models.ForeignKey(Ct)

    class Meta:
	 db_table = 'ctbodypart'


class cttempbonefeatures(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Temporal bone features', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Temporal bone features', choices=[(1, u'Cochlear Nerve Hypoplasia'), (2, u'EVA'), (3, u'Other')])
    ct = models.ForeignKey(Ct)

    class Meta:
	 db_table = 'cttempbonefeatures'


class Ultrasound2(models.Model):
    us_date = models.FloatField(help_text=u'Please specify four digit year', null=True, verbose_name=u'Year of US', blank=True)
    us = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'US result', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    us_renal_laterality = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Laterality of abnormal renal ultrasound findings', choices=[(1, u'Unilateral'), (2, u'Bilateral')])
    us_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Specify US result', blank=True) # This field type is a guess
    us_location = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Where was US performed?', blank=True)
    us_body_part_summary = models.CharField(help_text=u'1, Brain | 2, Kidney | 3, Abdomen | 4, Chest | 5, Muscle | 6, Head | 7, Other', null=True, max_length=2000, verbose_name=u'Part of body screened on US | Specify  part of body screened', blank=True)
    us_renal_finding_summary = models.CharField(help_text=u'1, Cysts | 2, Hypoplasia | 3, Aplasia | 4, Duplicated Ureters | 5, Horseshoe | 6, Other', null=True, max_length=2000, verbose_name=u'Renal ultrasound finding details', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'ultrasound2'


class usbodypart(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Part of body screened on US | Specify  part of body screened', blank=True)
    value = models.IntegerField(help_text=u'', null=True, verbose_name=u'Part of body screened on US | Specify  part of body screened', blank=True, choices=[(1, u'Brain'), (2, u'Kidney'), (3, u'Abdomen'), (4, u'Chest'), (5, u'Muscle'), (6, u'Head'), (7, u'Other')]) # This field type is a guess
    ultrasound2 = models.ForeignKey(Ultrasound2)

    class Meta:
	 db_table = 'usbodypart'


class usrenalfinding(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Renal ultrasound finding details', blank=True)
    value = models.IntegerField(help_text=u'', null=True, verbose_name=u'Renal ultrasound finding details', blank=True, choices=[(1, u'Cysts'), (2, u'Hypoplasia'), (3, u'Aplasia'), (4, u'Duplicated Ureters'), (5, u'Horseshoe'), (6, u'Other')]) # This field type is a guess
    ultrasound2 = models.ForeignKey(Ultrasound2)

    class Meta:
	 db_table = 'usrenalfinding'


class Xray(models.Model):
    xray_date = models.FloatField(help_text=u'Please specify four digit year', null=True, verbose_name=u'Year of Xray', blank=True)
    xray = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Xray result', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    xray_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Specify Xray result', blank=True) # This field type is a guess
    xray_location = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Where was Xray performed?', blank=True)
    xray_body_part_summary = models.CharField(help_text=u'1, Brain | 2, Kidney | 3, Abdomen | 4, Chest | 5, Muscle | 6, Head | 7, Other', null=True, max_length=2000, verbose_name=u'Part of body screened on Xray | Specify  part of body screened', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'xray'


class xraybodypart(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Part of body screened on Xray | Specify  part of body screened', blank=True)
    value = models.IntegerField(help_text=u'', null=True, verbose_name=u'Part of body screened on Xray | Specify  part of body screened', blank=True, choices=[(1, u'Brain'), (2, u'Kidney'), (3, u'Abdomen'), (4, u'Chest'), (5, u'Muscle'), (6, u'Head'), (7, u'Other')]) # This field type is a guess
    xray = models.ForeignKey(Xray)

    class Meta:
	 db_table = 'xraybodypart'


class Endoscopy(models.Model):
    endo_date = models.FloatField(help_text=u'Please specify four digit year', null=True, verbose_name=u'Year of Endoscopy', blank=True)
    endo = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Endoscopy result | Specify  Type of Endoscopy ', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    endo_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Specify Endoscopy Result', blank=True) # This field type is a guess
    endo_location = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Where was Endoscopy performed?', blank=True)
    endo_body_part_summary = models.CharField(help_text=u'1, Gastroscopy or Upper endoscopy (mouth, oesophagus, stomach and duodenum) | 2, Colonoscopy | 3, Flexible sigmoidoscopy | 4, Proctoscopy (anal canal) | 5, Cytoscopy (bladder) | 6, Ureteroscopy | 8, Endoscopic ultrasound | 7, Other', null=True, max_length=2000, verbose_name=u'Type of Endoscopy ', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'endoscopy'


class endobodypart(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Type of Endoscopy ', blank=True)
    value = models.TextField(help_text=u'', null=True, verbose_name=u'Type of Endoscopy ', blank=True) # This field type is a guess
    endoscopy = models.ForeignKey(Endoscopy)

    class Meta:
	 db_table = 'endobodypart'


class MuscleBiopsy(models.Model):
    muscle_biopsy_date = models.FloatField(help_text=u'Please specify four digit year', null=True, verbose_name=u'Year of muscle biopsy', blank=True)
    muscle_biopsy_result = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'General pathological analysis of muscle biopsy', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    muscle_biopsy_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Specify abnormal result for muscle biopsy', db_column=u'muscle_biopsy_spec ', blank=True) # Field renamed to remove spaces. Field renamed to remove ending underscore Field name made lowercase. This field type is a guess
    muscle_biopsy_mito_test_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Mitochondrial testing done on muscle biopsy', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    muscle_biopsy_mito_test_type_summary = models.CharField(help_text=u'1, PDH | 2, OXPHOS | 3, ETC Enzymes | 4, Coenzyme Q10 | 5, Mitochondrial DNA Content', null=True, max_length=2000, verbose_name=u'Type of testing performed on muscle biopsy | Results of ', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'musclebiopsy'


class musclebiopsymitotesttype(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Type of testing performed on muscle biopsy | Results of ', blank=True)
    value = models.IntegerField(help_text=u'', null=True, verbose_name=u'Type of testing performed on muscle biopsy | Results of ', blank=True, choices=[(1, u'PDH'), (2, u'OXPHOS'), (3, u'ETC Enzymes'), (4, u'Coenzyme Q10'), (5, u'Mitochondrial DNA Content')]) # This field type is a guess
    musclebiopsy = models.ForeignKey(MuscleBiopsy)

    class Meta:
	 db_table = 'musclebiopsymitotesttype'


class SkinBiopsy(models.Model):
    skin_biopsy_date = models.FloatField(help_text=u'Please specify four digit year', null=True, verbose_name=u'Year of skin biopsy', blank=True)
    skin_biopsy_result = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'General pathological analysis of skin biopsy', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    skin_biopsy_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Specify abnormal result for skin biopsy', blank=True) # This field type is a guess
    skin_biopsy_mito_test_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Mitochondrial testing done on skin biopsy', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    skin_biopsy_mito_test_type_summary = models.CharField(help_text=u'1, PDH | 2, OXPHOS | 3, ETC Enzymes | 4, Coenzyme Q10 | 5, Mitochondrial DNA Content', null=True, max_length=2000, verbose_name=u'Type of testing performed on skin biopsy | Results of ', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'skinbiopsy'


class skinbiopsymitotesttype(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Type of testing performed on skin biopsy | Results of ', blank=True)
    value = models.IntegerField(help_text=u'', null=True, verbose_name=u'Type of testing performed on skin biopsy | Results of ', blank=True, choices=[(1, u'PDH'), (2, u'OXPHOS'), (3, u'ETC Enzymes'), (4, u'Coenzyme Q10'), (5, u'Mitochondrial DNA Content')]) # This field type is a guess
    skinbiopsy = models.ForeignKey(SkinBiopsy)

    class Meta:
	 db_table = 'skinbiopsymitotesttype'


class LiverBiopsy(models.Model):
    liver_biopsy_date = models.FloatField(help_text=u'Please specify four digit year', null=True, verbose_name=u'Year of liver biopsy', blank=True)
    liver_biopsy_result = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'General pathological analysis of liver biopsy', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    liver_biopsy_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Specify abnormal result for liver biopsy', blank=True) # This field type is a guess
    liver_biopsy_mito_test_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Mitochondrial testing done on liver biopsy', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    liver_biopsy_mito_test_type_summary = models.CharField(help_text=u'1, PDH | 2, OXPHOS | 3, ETC Enzymes | 4, Coenzyme Q10 | 5, Mitochondrial DNA Content', null=True, max_length=2000, verbose_name=u'Type of testing performed on liver biopsy | Results of ', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'liverbiopsy'


class liverbiopsymitotesttype(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Type of testing performed on liver biopsy | Results of ', blank=True)
    value = models.IntegerField(help_text=u'', null=True, verbose_name=u'Type of testing performed on liver biopsy | Results of ', blank=True, choices=[(1, u'PDH'), (2, u'OXPHOS'), (3, u'ETC Enzymes'), (4, u'Coenzyme Q10'), (5, u'Mitochondrial DNA Content')]) # This field type is a guess
    liverbiopsy = models.ForeignKey(LiverBiopsy)

    class Meta:
	 db_table = 'liverbiopsymitotesttype'


class BrainBiopsy(models.Model):
    brain_biopsy_date = models.FloatField(help_text=u'Please specify four digit year', null=True, verbose_name=u'Year of brain biopsy', blank=True)
    brain_biopsy_result = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'General pathological analysis of brain biopsy', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    brain_biopsy_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Specify abnormal result for brain biopsy', blank=True) # This field type is a guess
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'brainbiopsy'


class BoneMarrow(models.Model):
    bone_marrow_biopsy_date = models.FloatField(help_text=u'Please specify four digit year', null=True, verbose_name=u'Year of bone marrow biopsy', blank=True)
    bone_marrow_biopsy_result = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'General pathological analysis of bone marrow biopsy', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    bone_marrow_biopsy_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Specify abnormal result for bone marrow biopsy', blank=True) # This field type is a guess
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'bonemarrow'


class OtherBiopsy(models.Model):
    other_biopsy_type = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Specify other biopsy type', blank=True)
    other_biopsy_date = models.FloatField(help_text=u'Please specify four digit year', null=True, verbose_name=u'Year of other biopsy', blank=True)
    other_biopsy_result = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'General pathological analysis of other biopsy', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    other_biopsy_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Specify abnormal result for other biopsy', blank=True) # This field type is a guess
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'otherbiopsy'


class ElectroretinogramErg(models.Model):
    erg_date = models.FloatField(help_text=u'Please specify four digit year', null=True, verbose_name=u'Year of electroretinogram (ERG)', blank=True)
    erg = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Electroretinogram (ERG) result', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    erg_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Specify Electroretinogram (ERG) result', blank=True) # This field type is a guess
    erg_location = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Where was electroretinogram performed?', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'electroretinogramerg'


class ElectroencephalogramEeg(models.Model):
    eeg = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Electroencephalogram (EEG) result', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    eeg_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Specify Electroencephalogram (EEG) result', blank=True) # This field type is a guess
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'electroencephalogrameeg'


class ElectromyogramEmg(models.Model):
    emg = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Electromyogram (EMG) results', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    emg_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Specify Electromyogram (EMG) results', blank=True) # This field type is a guess
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'electromyogramemg'


class NerveConductionVelocityNcv(models.Model):
    ncv = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Nerve Conduction Velocity (NCV) results', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    ncv_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Specify Nerve Conduction Velocity (NCV) results', blank=True) # This field type is a guess
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'nerveconductionvelocityncv'


class FamilyHistory(models.Model):
    suspected_inheritance = models.IntegerField(help_text=u'', null=True, verbose_name=u'Suspected mode of  inheritance', blank=True, choices=[(1, u'Autosomal dominant'), (2, u'Autosomal recessive'), (3, u'X-linked dominant'), (4, u'X-linked recessive'), (5, u'Multifactorial'), (6, u'Mitochondrial inheritance'), (7, u'Unknown/Not documented')]) # This field type is a guess
    mat_ancestry = models.CharField(help_text=u'Separate with commas.  Example: Irish, English, Scottish', null=True, max_length=2000, verbose_name=u'Maternal ancestry', blank=True)
    pat_ancestry = models.CharField(help_text=u'Separate with commas.  Example: Irish, English, Scottish', null=True, max_length=2000, verbose_name=u'Paternal ancestry', blank=True)
    consanguinity_identified = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Consanguinity identified?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    consanguinity_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Consanguinity details', blank=True) # This field type is a guess
    occupation_mother = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u"Mother's occupation", blank=True)
    occupation_father = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u"Father's occupation", blank=True)
    father_affected = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Father suspected to be affected by same condition as proband?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    father_alive = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Father alive?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    current_age = models.IntegerField(help_text=u'', null=True, verbose_name=u"Father's current age", blank=True)
    father_age_at_death = models.IntegerField(help_text=u'', null=True, verbose_name=u"Father's age at death", blank=True)
    father_cause_of_death = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u"Father's cause of death", blank=True)
    mother_affected = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Mother suspected to be affected by same condition as proband?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    mother_alive = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Mother alive?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    mother_age = models.IntegerField(help_text=u'', null=True, verbose_name=u"Mother's current age", blank=True)
    mother_age_at_death = models.IntegerField(help_text=u'', null=True, verbose_name=u"Mother's age at death", blank=True)
    mother_cause_of_death = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u"Mother's cause of death", blank=True)
    full_brothers = models.IntegerField(help_text=u'', null=True, verbose_name=u'Number of full brothers with same parents', blank=True)
    full_sisters = models.IntegerField(help_text=u'', null=True, verbose_name=u'Number of full sisters with same parents', blank=True)
    sibling_dx = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Are any of the brothers or sisters suspected to have the same medical condition as the proband?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    sibling_dx_spec = models.TextField(help_text=u'(Please specify which sibling, diagnosis, age at diagnosis, and relevant symptoms)', null=True, verbose_name=u'Sibling diagnosis details', blank=True) # This field type is a guess
    children = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Does the proband have any children?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    sons = models.IntegerField(help_text=u'', null=True, verbose_name=u'Number of sons', blank=True)
    daughters = models.IntegerField(help_text=u'', null=True, verbose_name=u'Number of daughters', blank=True)
    other_family = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Any other family members with symptoms similar to proband other than those described above?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    family_history_feedback = models.TextField(help_text=u'', null=True, verbose_name=u'Please provide any feedback for this form (for example: missing questions, questions not relevant for a disease area, ambiguities, places where a textbox could be replaced with discrete choices, missing discrete choices)', blank=True) # This field type is a guess
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'familyhistory'


class OtherFamilyMembersWithSimilarSymptom(models.Model):
    other_family_side = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Which side of the family is the family member on?', choices=[(1, u'Maternal'), (2, u'Paternal'), (3, u'Unknown/Not documented')])
    other_family_rel = models.CharField(max_length=2000, db_column=u'other_family_rel ', blank=True, help_text=u'Ex: First cousin, aunt, etc.', null=True, verbose_name=u'What is the relationship of the family member to the proband?') # Field renamed to remove spaces. Field renamed to remove ending underscore Field name made lowercase.
    other_family_symptoms = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Describe the symptoms of the family member.', blank=True)
    familyhistory = models.ForeignKey(FamilyHistory)

    class Meta:
	 db_table = 'otherfamilymemberswithsimilarsymptom'


class DevelopmentalHistory(models.Model):
    age_rolled_over = models.FloatField(help_text=u'Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name=u'Age first rolled over (months)', blank=True)
    age_sat = models.FloatField(help_text=u'Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name=u'Age when first sat (months)', blank=True)
    age_walk = models.FloatField(help_text=u'Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name=u'Age when first walked (months)', blank=True)
    age_speech = models.FloatField(help_text=u'Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name=u'Age of first word (months)', blank=True)
    speech_delay = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'History of speech delay?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    speech_delay_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Speech delay details', blank=True) # This field type is a guess
    current_speech = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Current speech', choices=[(1, u'Normal'), (2, u'Delayed'), (3, u'Nonverbal'), (4, u'Unknown/Not documented')])
    motor_delay = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'History of motor delay?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    motor_delay_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Motor delay details', blank=True) # This field type is a guess
    current_motor_ability = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Current motor ability', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Unknown/Not documented')])
    articulation_issues = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Articulation issues?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    articulation_issues_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Articulation issues details', blank=True) # This field type is a guess
    balance_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Any balance or coordination problems?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    balance_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe balance or coordination problems', blank=True) # This field type is a guess
    other_milestones_delay_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Specify other developmental delays', blank=True) # This field type is a guess
    developmental_quotient_dq = models.FloatField(help_text=u'', null=True, verbose_name=u'Developmental Quotient (DQ)', blank=True)
    iq = models.FloatField(help_text=u'', null=True, verbose_name=u'Intelligence Quotient (IQ)', blank=True)
    developmental_regression = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Any developmental regression or loss of skills?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    grade_level = models.TextField(help_text=u'', null=True, verbose_name=u'Current school level/grade or most recent school level/grade completed', blank=True) # This field type is a guess
    repeat_grade = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Ever had to repeat a grade?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    grade_repeat_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Grade repeated details', blank=True) # This field type is a guess
    iep_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Receiving Current Early Intervention, IEP, or Special Education regime?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    iep_spec = models.TextField(help_text=u'(Age range when received services, specific developmental areas that were focused on, etc.)', null=True, verbose_name=u'Please specify details about IEP, Current Early Intervention, or Special Education Regime', blank=True) # This field type is a guess
    avg_grade_perfomance = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Current average grade performance', choices=[(1, u'A'), (2, u'B'), (3, u'C'), (4, u'D'), (5, u'E'), (6, u'F'), (7, u'Unknown/Not documented')])
    autism_diagnosis_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Autism Spectrum Diagnosis', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    asd_id_link = models.TextField(help_text=u'', null=True, verbose_name=u'If this subject has an autism spectrum disorder or intellectual disability, please consider completing the full Intellectual Disability questionnaire.', blank=True) # This field type is a guess
    autism_spectrum_features = models.TextField(help_text=u'', null=True, verbose_name=u'Autism spectrum features | Describe other autism spectrum features present', blank=True) # This field type is a guess
    beh_issues_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Please specify any behavioral issues not described above.', blank=True) # This field type is a guess
    developmental_history_feedback = models.TextField(help_text=u'', null=True, verbose_name=u'Please provide any feedback for this form (for example: missing questions, questions not relevant for a disease area, ambiguities, places where a textbox could be replaced with discrete choices, missing discrete choices)', blank=True) # This field type is a guess
    developmental_regression_area_summary = models.CharField(help_text=u'1, Speech | 2, Motor | 3, Cognition | 4, Social skills', null=True, max_length=2000, verbose_name=u'Area of regression/loss of skill | Describe loss of ', blank=True)
    current_therapies_summary = models.CharField(help_text=u'5, None | 1, Physical therapy | 2, Occupational therapy | 3, Speech therapy | 4, Vision therapy | 6, Unknown/Not documented', null=True, max_length=2000, verbose_name=u'Current therapies', blank=True)
    autism_spectum_summary = models.CharField(help_text=u'1, Autism | 2, Asperger Syndrome | 3, PDD-NOS (pervasive developmental disorder, not otherwise specified) | 4, Unclassified | 5, Unknown/Not documented', null=True, max_length=2000, verbose_name=u'Autism spectrum category', blank=True)
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'developmentalhistory'


class developmentalregressionarea(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Area of regression/loss of skill | Describe loss of ', blank=True)
    value = models.IntegerField(help_text=u'', null=True, verbose_name=u'Area of regression/loss of skill | Describe loss of ', blank=True, choices=[(1, u'Speech'), (2, u'Motor'), (3, u'Cognition'), (4, u'Social skills')]) # This field type is a guess
    developmentalhistory = models.ForeignKey(DevelopmentalHistory)

    class Meta:
	 db_table = 'developmentalregressionarea'


class currenttherapies(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Current therapies', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Current therapies', choices=[(5, u'None'), (1, u'Physical therapy'), (2, u'Occupational therapy'), (3, u'Speech therapy'), (4, u'Vision therapy'), (6, u'Unknown/Not documented')])
    developmentalhistory = models.ForeignKey(DevelopmentalHistory)

    class Meta:
	 db_table = 'currenttherapies'


class autismspectum(models.Model):
    label = models.CharField(help_text=u'ID ', null=True, max_length=2000, verbose_name=u'Autism spectrum category', blank=True)
    value = models.CharField(help_text=u'ID ', null=True, max_length=2000, verbose_name=u'Autism spectrum category', blank=True)
    developmentalhistory = models.ForeignKey(DevelopmentalHistory)

    class Meta:
	 db_table = 'autismspectum'


class ReviewOfSystem(models.Model):
    ros_growth_normal_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'History of abnormal growth', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_growth_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe abnormal growth', blank=True) # This field type is a guess
    ros_odors_details = models.IntegerField(help_text=u'', null=True, verbose_name=u'Unusual odors | Describe other unusual odor', blank=True, choices=[(1, u'None'), (2, u'Sweet (maple syrup)'), (3, u'Fishy'), (4, u'Foul'), (5, u'Musty'), (6, u'Unknown/Not documented'), (7, u'Other')]) # This field type is a guess
    ros_decompensation_w_illness_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Decompensation with illness', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_decompensation_w_illness_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe decompensation with illness', blank=True) # This field type is a guess
    ros_anesthetic_problems_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Anesthetic problems (hypersensitivity)', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_anesthetic_problems_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe anesthetic problems', blank=True) # This field type is a guess
    ros_general_other = models.TextField(help_text=u'', null=True, verbose_name=u'Describe any other general issues', blank=True) # This field type is a guess
    ros_psychiatric_problems_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Psychiatric problems', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_psychiatric_problems_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe psychiatric problems', blank=True) # This field type is a guess
    ros_sleep_disturbances_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Sleep disturbances', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_sleep_disturbances_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe sleep disturbances', blank=True) # This field type is a guess
    ros_stereotypies_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Stereotypies', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_stereotypies_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe stereotypies', blank=True) # This field type is a guess
    ros_inattention_o_hyper_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Inattention or hyperactivity', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_inattention_o_hyper_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe inattention or hyperactivity', blank=True) # This field type is a guess
    ros_behavior_other_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe other behavior issues', blank=True) # This field type is a guess
    ros_patient_resembles = models.IntegerField(help_text=u'', null=True, verbose_name=u'Patient resembles', blank=True, choices=[(1, u'Mother'), (2, u'Father'), (3, u'Both'), (4, u'Neither'), (5, u'Unknown/Not documented')]) # This field type is a guess
    ros_headaches_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Chronic headaches or migraines', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_headaches_freq = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Frequency of chronic headaches or migraines', choices=[(1, u'Daily'), (2, u'Weekly'), (3, u'Monthly'), (4, u'Yearly'), (5, u'Less than Yearly'), (6, u'Unknown/Not documented')])
    ros_optho = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Opthalmologic eval', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not performed'), (5, u'Not determined'), (4, u'Unknown/Not documented')])
    ros_vision_concerns_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Vision concerns or known opthalmologic conditions', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_optho_structural_findings = models.IntegerField(help_text=u'', null=True, verbose_name=u'Structural findings detail', blank=True, choices=[(6, u'None'), (1, u'microphalmia'), (2, u'cataract'), (3, u'anterior chamber defect'), (4, u'coloboma'), (5, u'optic nerve hypoplasia'), (7, u'Unknown/Not documented'), (8, u'Other')]) # This field type is a guess
    ros_vision_concerns = models.IntegerField(help_text=u'', null=True, verbose_name=u'Additional vision conditions', blank=True, choices=[(11, u'None'), (1, u'CPEO'), (2, u'Optic atrophy'), (4, u'Nyctalopia'), (5, u'Hyperopia'), (6, u'Nystagmus'), (7, u'Strabismus'), (8, u'Corneal Clouding'), (9, u'Retinoblastoma'), (10, u'Other')]) # This field type is a guess
    ros_hearing_concerns_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Hearing concerns', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_hearing_concerns_description = models.TextField(help_text=u'', null=True, verbose_name=u'Please consider filling out the Hearing Impairment instrument.', blank=True) # This field type is a guess
    ros_hearing_concerns_spec = models.TextField(help_text=u'Please skip if also filling out hearing impairment intake', null=True, verbose_name=u'Describe hearing concerns', blank=True) # This field type is a guess
    ros_audio_eval = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Audiology evaluation', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not performed'), (5, u'Not determined'), (4, u'Unknown/Undocumented')])
    ros_audio_eval_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe abnormal audiology eval', blank=True) # This field type is a guess
    ros_swallowing_difficulties_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Swallowing difficulties', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_swallowing_difficulties_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe swallowing difficulties', blank=True) # This field type is a guess
    ros_cardiac_anomalies_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Congenital heart defects', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_cardiac_anomalies_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe congenital heart defects', blank=True) # This field type is a guess
    ros_arrhythmias = models.IntegerField(help_text=u'', null=True, verbose_name=u'Arrhythmias | Describe other arrhythmias', blank=True, choices=[(18, u'None'), (1, u'Atrial Fibrillation (A-Fib)'), (2, u'Atrial Flutter'), (3, u'Bradycardia'), (4, u'Brugada Syndrome'), (5, u'Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT)'), (6, u'Heart Block'), (7, u'Long QT Syndrome (LQTS)'), (8, u'Premature Atrial Complexes (PAC)'), (9, u'Premature Ventricular Complexes (PVC)'), (10, u'Short QT Syndrome (SQTS)'), (11, u'Supraventricular Tachycardia (SVT)'), (12, u'Tachycardia'), (13, u'Torsades de pointes'), (14, u'Ventricular Fibrillation (V-Fib)'), (15, u'Ventricular Flutter'), (16, u'Wolff-Parkinson-White Syndrome (WPW)'), (17, u'Other')]) # This field type is a guess
    ros_other_cv_issues_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe other cardiovascular issues', blank=True) # This field type is a guess
    ros_wheezing_o_asthma_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Wheezing or asthma', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_wheezing_o_asthma_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe wheezing or asthma', blank=True) # This field type is a guess
    ros_sleep_apnea_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Sleep apnea', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_sleep_apnea_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe sleep apnea', blank=True) # This field type is a guess
    ros_prior_intubation_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Prior intubation', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_age_intubated = models.TextField(help_text=u'', null=True, verbose_name=u'Age at intubation', blank=True) # This field type is a guess
    ros_intubation_removed = models.NullBooleanField(help_text=u'', verbose_name=u'Has intubation been removed?', blank=True)
    ros_age_intubation_removed = models.TextField(help_text=u'', null=True, verbose_name=u'Age at intubation removal', blank=True) # This field type is a guess
    ros_pulmonary_other = models.TextField(help_text=u'', null=True, verbose_name=u'Describe other pulmonary issues', blank=True) # This field type is a guess
    ros_gast_reflux_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Gasteroesophageal reflux', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_gast_reflux_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe gasteroesophageal reflux', blank=True) # This field type is a guess
    ros_current_feeding = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Current feeding', choices=[(1, u'Oral'), (2, u'Tube Fed'), (3, u'Both'), (4, u'Unknown/No documented')])
    ros_frequent_vomiting_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Frequent vomiting', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_frequent_vomiting_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe frequent vomiting', blank=True) # This field type is a guess
    ros_diarrhea = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Diarrhea', choices=[(1, u'History of diarrhea'), (2, u'Resolved by medication'), (3, u'Currently has diarrhea'), (4, u'Currently on medication'), (5, u'No history of diarrhea'), (6, u'Unknown/Not documented')])
    ros_feeding_history = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Feeding history', choices=[(1, u'Always Oral'), (2, u'G-tube'), (3, u'N-tube'), (4, u'J-tube'), (5, u'Unknown/Not documented')])
    ros_gtube_age_placement = models.TextField(help_text=u'', null=True, verbose_name=u'Age at G-tube placement', blank=True) # This field type is a guess
    ros_gtube_removed = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Has G-tube been removed', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_gtube_age_removed = models.TextField(help_text=u'', null=True, verbose_name=u'Age at G-tube removal', blank=True) # This field type is a guess
    ros_ntube_age_placement = models.TextField(help_text=u'', null=True, verbose_name=u'Age at N-tube placement', blank=True) # This field type is a guess
    ros_ntube_removed = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Has N-tube been removed', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_ntube_age_removed = models.TextField(help_text=u'', null=True, verbose_name=u'Age at N-tube removal', blank=True) # This field type is a guess
    ros_jtube_age_placement = models.TextField(help_text=u'', null=True, verbose_name=u'Age at J-tube placement', blank=True) # This field type is a guess
    ros_jtube_removed = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Has J-tube been removed', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_jtube_age_removed = models.TextField(help_text=u'', null=True, verbose_name=u'Age at J-tube removal', blank=True) # This field type is a guess
    ros_fail_thrive_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'History of failure to thrive', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_fail_thrive_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe history of failure to thrive', blank=True) # This field type is a guess
    ros_liver_problems_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Liver problems', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_liver_problems_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe liver problems', blank=True) # This field type is a guess
    ros_gi_other_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe other GI issues', blank=True) # This field type is a guess
    ros_hema_prot_dysuria_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Hematuria, proteinura or dysuria', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_hema_prot_dysuria_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe hematuria, proteinura or dysuria', blank=True) # This field type is a guess
    ros_known_renal_anomalies_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Renal anomalies', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_known_renal_anomalies_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe renal anomalies', blank=True) # This field type is a guess
    ros_renal_tubular_acidosis_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Renal tubular acidosis', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_renal_tubular_acidosis_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe renal tubular acidosis', blank=True) # This field type is a guess
    ros_renal_other_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe other renal issues', blank=True) # This field type is a guess
    ros_tanner_scale = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Tanner Scale', choices=[(1, u'Tanner I'), (2, u'Tanner II'), (3, u'Tanner III'), (4, u'Tanner IV'), (5, u'Tanner V'), (6, u'Unknown/Not documented')])
    ros_puberty_timing = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Puberty timing', choices=[(1, u'Normal'), (2, u'Delayed'), (3, u'Early'), (4, u'Too early to tell'), (5, u'Unknown/Not documented')])
    ros_menarche = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'First menarche occurred', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented'), (4, u'Not applicable')])
    ros_menarche_date = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Date of menarche (month/year)', blank=True)
    ros_diabetes_mellitus_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Diabetes mellitus', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_diabetes_mellitus_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe diabetes mellitus', blank=True) # This field type is a guess
    ros_known_hormone_problem_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Hormonal imbalance/problems', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_known_hormone_adrenal_cortex_medulla = models.IntegerField(help_text=u'', null=True, verbose_name=u'Adrenal Cortex/medulla hormonal imbalance', blank=True, choices=[(1, u'None'), (2, u'Aldosterone'), (3, u'Cortisol'), (4, u'Epinephrine'), (5, u'Norepinephrine'), (6, u'Unknown/Not documented'), (7, u'Other')]) # This field type is a guess
    ros_known_hormone_gonadal = models.IntegerField(help_text=u'', null=True, verbose_name=u'Gonadal hormonal imbalance', blank=True, choices=[(1, u'None'), (2, u'Testosterone'), (3, u'Progesterone'), (4, u'Estrogen'), (5, u'hCG'), (6, u'Unknown/Not documented'), (7, u'Other')]) # This field type is a guess
    ros_known_hormone_problem_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Please any other known hormone problems', blank=True) # This field type is a guess
    ros_hirsutism_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Hirsutism', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_hirsutism_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe hirsutism', blank=True) # This field type is a guess
    ros_endocrine_other_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe other endocrine issues', blank=True) # This field type is a guess
    ros_easy_bruising_bleeding_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Easy bruising or bleeding', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_easy_bruising_bleeding_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe bruising or bleeding', blank=True) # This field type is a guess
    ros_blood_clots_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Blood clots', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_blood_clots_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe blood clots', blank=True) # This field type is a guess
    ros_anemia_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Anemia', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_anemia_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Please describe anemia', blank=True) # This field type is a guess
    ros_hematologic_other = models.TextField(help_text=u'', null=True, verbose_name=u'Describe other hematologic issues', blank=True) # This field type is a guess
    ros_muscle_strength = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Muscle strength history', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Unknown/Not documented')])
    ros_muscle_strength_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe abnormal muscle strength history', blank=True) # This field type is a guess
    ros_muscle_bulk = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Muscle bulk history', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Unknown/Not documented')])
    ros_muscle_bulk_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe abnormal muscle bulk history', blank=True) # This field type is a guess
    ros_hypotonia_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Hypotonia', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_hypotonia_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe hypotonia', blank=True) # This field type is a guess
    ros_fatigue = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Fatigue', choices=[(4, u'None'), (1, u'Chronic Fatigue'), (2, u'Fatigues easily'), (3, u'Low Energy'), (5, u'Unknown/Not documented')])
    ros_fractures_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Fractures', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_fractues_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe fractures', blank=True) # This field type is a guess
    ros_spine_curvature = models.IntegerField(help_text=u'', null=True, verbose_name=u'Spine Curvature', blank=True, choices=[(6, u'Normal'), (1, u'Kyphosis'), (2, u'Lordosis'), (3, u'Scoliosis'), (5, u'Kyphoscoliosis'), (7, u'Unknown/Not documented'), (4, u'Other')]) # This field type is a guess
    ros_joint_laxity_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Joint laxity', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_joint_laxity_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe joint laxity', blank=True) # This field type is a guess
    ros_musculoskeletal_other_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe other musculoskeletal issues', blank=True) # This field type is a guess
    ros_seizures_freq = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Seizures', choices=[(7, u'None'), (1, u'Rare (1-5)'), (2, u'daily'), (3, u'weekly'), (4, u'monthly'), (5, u'yearly'), (6, u'Febrile only'), (8, u'Unknown/Not documented')])
    ros_seizures_spec = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Type of seizure', blank=True)
    ros_seizures_onset_age = models.TextField(help_text=u'', null=True, verbose_name=u'Age of onset of seizures', blank=True) # This field type is a guess
    ros_seizures_require_med_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Seizures require seizure medication', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_seizures_med_controlled_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Seizures controlled by seizure medication', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_peripheral_neuropathy_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Peripheral neuropathy', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_peripheral_neuropathy_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe peripheral neuropathy', blank=True) # This field type is a guess
    ros_movement_disorders_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Movement disorders', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_movement_disorders_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe movement disorders', blank=True) # This field type is a guess
    ros_neurologic_other_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe other neurologic issues', blank=True) # This field type is a guess
    ros_frequent_illness_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Frequent illness', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_frequent_illness_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe frequent illness', blank=True) # This field type is a guess
    ros_immunologic_other_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe other immunologic issues', blank=True) # This field type is a guess
    ros_lipomas_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Lipomas', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ros_lipomas_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe lipomas', blank=True) # This field type is a guess
    ros_dermatologic_other_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe other dermatologic issues', blank=True) # This field type is a guess
    ros_other_notes_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Additional notes', blank=True) # This field type is a guess
    ros_feedback = models.TextField(help_text=u'', null=True, verbose_name=u'Please provide any feedback for this form (for example: missing questions, questions not relevant for a disease area, ambiguities, places where a textbox could be replaced with discrete choices, missing discrete choices)', blank=True) # This field type is a guess
    ros_retinal_findings_summary = models.CharField(help_text=u'4, None | 1, Retinal pigmentary difference | 2, Retinopathy | 3, Retinitis pigmentosa | 5, Unknown/Not documented | 6, Other', null=True, max_length=2000, verbose_name=u'Retinal findings', blank=True)
    ros_optho_acuity_findings_summary = models.CharField(help_text=u'6, None | 1, myopia | 2, farsighted | 3, blind | 4, amblyopia | 5, astigmatism | 7, Unknown/Not documented | 8, Other', null=True, max_length=2000, verbose_name=u'Acuity findings detail', blank=True)
    ros_dental_problems_summary = models.CharField(help_text=u'6, None | 1, Caries | 2, Oligodontia | 3, Rotting | 4, Dental crowding | 8, Unknown/Not documented | 7, Other unknown problem | 5, Other', null=True, max_length=2000, verbose_name=u'Dental problems', blank=True)
    ros_cardiac_muscle_hypertrophy_summary = models.CharField(help_text=u'7, None | 1, Hypertrophic Cardiomyopathy | 2, Dilated Cardiomyopathy | 3, Left Ventricular Noncompaction | 4, Restrictive Cardiomyopathy | 5, Arrhythmogenic Right Ventricular Dysplasia (ARVD) | 6, Other', null=True, max_length=2000, verbose_name=u'Cardiomyopathy', blank=True)
    ros_constipation_summary = models.CharField(help_text=u'1, History of constipation | 2, Resolved by medication | 3, Currently has constipation | 4, Currently on medication | 5, No history of constipation | 6, Unknown/Not documented', null=True, max_length=2000, verbose_name=u'Constipation', blank=True)
    ros_genitalia_summary = models.CharField(help_text=u'6, None | 1, Undescended teste | 2, Hypospadias | 3, Freckling | 4, Labial abnormality | 7, Unknown/Not documented | 8, Other unknown abnormality | 5, Other', null=True, max_length=2000, verbose_name=u'Genitalia abnormality', blank=True)
    ros_known_hormone_hypothalmic_pituitary_summary = models.CharField(help_text=u'1, None | 2, GnRH | 3, TRH | 4, Dopamine | 5, CRH | 6, GHRH/Somatostatin | 7, Vasopressor | 8, Oxytocin | 9, FSH | 10, FSHB | 11, LH | 12, LHB | 13, TSH | 14, TSHB | 15, CGA | 16, Prolactin | 17, POMC | 18, ACTH | 19, GH | 20, Unkonwn/Not documented | 21, Other', null=True, max_length=2000, verbose_name=u'Hypothalamic-pituitary hormonal imbalance', blank=True)
    ros_known_hormone_thyroid_parathyroid_summary = models.CharField(help_text=u'1, None | 2, Thyroid hormone (T3 and/or T4) | 3, Calcitonin | 4, PTH | 5, Unknown/Not documented | 6, Other', null=True, max_length=2000, verbose_name=u'Thyroid/Parathyroid hormonal imbalance', blank=True)
    ros_allergies_summary = models.CharField(help_text=u'6, None | 1, Medication | 2, Food | 3, Seasonal or environmental | 4, Unknown/Not documented | 7, Other unknown allergy | 5, Other ', null=True, max_length=2000, verbose_name=u'Known allergies', blank=True)
    ros_rashes_eczema_birthmarks_summary = models.CharField(help_text=u'1, None | 2, Cafe au lait spots | 3, Capillary hemangioma | 4, Cutis marmorata | 5, Diffuse hypopigmented skin lesions | 6, Unknown/Not documented| 7, Other unknown abnormality | 8, Other', null=True, max_length=2000, verbose_name=u'Birthmarks or rash | Describe other birthmark rash', blank=True)
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'reviewofsystem'


class rosretinalfindings(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Retinal findings', blank=True)
    value = models.IntegerField(help_text=u'', null=True, verbose_name=u'Retinal findings', blank=True, choices=[(4, u'None'), (1, u'Retinal pigmentary difference'), (2, u'Retinopathy'), (3, u'Retinitis pigmentosa'), (5, u'Unknown/Not documented'), (6, u'Other')]) # This field type is a guess
    reviewofsystem = models.ForeignKey(ReviewOfSystem)

    class Meta:
	 db_table = 'rosretinalfindings'


class rosopthoacuityfindings(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Acuity findings detail', blank=True)
    value = models.IntegerField(help_text=u'', null=True, verbose_name=u'Acuity findings detail', blank=True, choices=[(6, u'None'), (1, u'myopia'), (2, u'farsighted'), (3, u'blind'), (4, u'amblyopia'), (5, u'astigmatism'), (7, u'Unknown/Not documented'), (8, u'Other')]) # This field type is a guess
    reviewofsystem = models.ForeignKey(ReviewOfSystem)

    class Meta:
	 db_table = 'rosopthoacuityfindings'


class rosdentalproblems(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Dental problems', blank=True)
    value = models.IntegerField(help_text=u'', null=True, verbose_name=u'Dental problems', blank=True, choices=[(6, u'None'), (1, u'Caries'), (2, u'Oligodontia'), (3, u'Rotting'), (4, u'Dental crowding'), (8, u'Unknown/Not documented'), (7, u'Other unknown problem'), (5, u'Other')]) # This field type is a guess
    reviewofsystem = models.ForeignKey(ReviewOfSystem)

    class Meta:
	 db_table = 'rosdentalproblems'


class roscardiacmusclehypertrophy(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Cardiomyopathy', blank=True)
    value = models.IntegerField(help_text=u'', null=True, verbose_name=u'Cardiomyopathy', blank=True, choices=[(7, u'None'), (1, u'Hypertrophic Cardiomyopathy'), (2, u'Dilated Cardiomyopathy'), (3, u'Left Ventricular Noncompaction'), (4, u'Restrictive Cardiomyopathy'), (5, u'Arrhythmogenic Right Ventricular Dysplasia (ARVD)'), (6, u'Other')]) # This field type is a guess
    reviewofsystem = models.ForeignKey(ReviewOfSystem)

    class Meta:
	 db_table = 'roscardiacmusclehypertrophy'


class rosconstipation(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Constipation', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Constipation', choices=[(1, u'History of constipation'), (2, u'Resolved by medication'), (3, u'Currently has constipation'), (4, u'Currently on medication'), (5, u'No history of constipation'), (6, u'Unknown/Not documented')])
    reviewofsystem = models.ForeignKey(ReviewOfSystem)

    class Meta:
	 db_table = 'rosconstipation'


class rosgenitalia(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Genitalia abnormality', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Genitalia abnormality', choices=[(6, u'None'), (1, u'Undescended teste'), (2, u'Hypospadias'), (3, u'Freckling'), (4, u'Labial abnormality'), (7, u'Unknown/Not documented'), (8, u'Other unknown abnormality'), (5, u'Other')])
    reviewofsystem = models.ForeignKey(ReviewOfSystem)

    class Meta:
	 db_table = 'rosgenitalia'


class rosknownhormonehypothalmicpituitary(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Hypothalamic-pituitary hormonal imbalance', blank=True)
    value = models.IntegerField(help_text=u'', null=True, verbose_name=u'Hypothalamic-pituitary hormonal imbalance', blank=True, choices=[(1, u'None'), (2, u'GnRH'), (3, u'TRH'), (4, u'Dopamine'), (5, u'CRH'), (6, u'GHRH/Somatostatin'), (7, u'Vasopressor'), (8, u'Oxytocin'), (9, u'FSH'), (10, u'FSHB'), (11, u'LH'), (12, u'LHB'), (13, u'TSH'), (14, u'TSHB'), (15, u'CGA'), (16, u'Prolactin'), (17, u'POMC'), (18, u'ACTH'), (19, u'GH'), (20, u'Unkonwn/Not documented'), (21, u'Other')]) # This field type is a guess
    reviewofsystem = models.ForeignKey(ReviewOfSystem)

    class Meta:
	 db_table = 'rosknownhormonehypothalmicpituitary'


class rosknownhormonethyroidparathyroid(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Thyroid/Parathyroid hormonal imbalance', blank=True)
    value = models.IntegerField(help_text=u'', null=True, verbose_name=u'Thyroid/Parathyroid hormonal imbalance', blank=True, choices=[(1, u'None'), (2, u'Thyroid hormone (T3 and/or T4)'), (3, u'Calcitonin'), (4, u'PTH'), (5, u'Unknown/Not documented'), (6, u'Other')]) # This field type is a guess
    reviewofsystem = models.ForeignKey(ReviewOfSystem)

    class Meta:
	 db_table = 'rosknownhormonethyroidparathyroid'


class rosallergies(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Known allergies', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Known allergies', choices=[(6, u'None'), (1, u'Medication'), (2, u'Food'), (3, u'Seasonal or environmental'), (4, u'Unknown/Not documented'), (7, u'Other unknown allergy'), (5, u'Other')])
    reviewofsystem = models.ForeignKey(ReviewOfSystem)

    class Meta:
	 db_table = 'rosallergies'


class rosrasheseczemabirthmarks(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Birthmarks or rash | Describe other birthmark rash', blank=True)
    value = models.IntegerField(help_text=u'', null=True, verbose_name=u'Birthmarks or rash | Describe other birthmark rash', blank=True, choices=[(1, u'None'), (2, u'Cafe au lait spots'), (3, u'Capillary hemangioma'), (4, u'Cutis marmorata'), (5, u'Diffuse hypopigmented skin lesions'), (6, u'Unknown/Not documented'), (7, u'Other unknown abnormality'), (8, u'Other')]) # This field type is a guess
    reviewofsystem = models.ForeignKey(ReviewOfSystem)

    class Meta:
	 db_table = 'rosrasheseczemabirthmarks'


class OtherGenitaliaAbnormality(models.Model):
    ros_other_genitalia_abnormality = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'other genitalia abnormality', blank=True)
    reviewofsystem = models.ForeignKey(ReviewOfSystem)

    class Meta:
	 db_table = 'othergenitaliaabnormality'


class MedicationAllergy(models.Model):
    ros_allergies_medication = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'medication allergy', blank=True)
    reviewofsystem = models.ForeignKey(ReviewOfSystem)

    class Meta:
	 db_table = 'medicationallergy'


class FoodAllergy(models.Model):
    ros_allergies_food = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'food allergy', blank=True)
    reviewofsystem = models.ForeignKey(ReviewOfSystem)

    class Meta:
	 db_table = 'foodallergy'


class OtherAllergy(models.Model):
    ros_allergies_other = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'other allergry', blank=True)
    reviewofsystem = models.ForeignKey(ReviewOfSystem)

    class Meta:
	 db_table = 'otherallergy'


class Surgery(models.Model):
    ros_surgeries = models.TextField(help_text=u'Please specify age, reason, and treatment/type of surgery. If filling out cardiac intake forms, please describe any Cardiac Surgeries in the appropriate question there instead of here.', null=True, verbose_name=u'Significant surgery', blank=True) # This field type is a guess
    reviewofsystem = models.ForeignKey(ReviewOfSystem)

    class Meta:
	 db_table = 'surgery'


class Hospitalization(models.Model):
    ros_hospita = models.TextField(help_text=u'Please specify age, reason for hospitalization', null=True, verbose_name=u'Significant hospitalization', blank=True) # This field type is a guess
    reviewofsystem = models.ForeignKey(ReviewOfSystem)

    class Meta:
	 db_table = 'hospitalization'


class Medication(models.Model):
    ros_medication = models.TextField(help_text=u'', null=True, verbose_name=u'current medication (if known)', blank=True) # This field type is a guess
    reviewofsystem = models.ForeignKey(ReviewOfSystem)

    class Meta:
	 db_table = 'medication'


class PhysicalExam(models.Model):
    age_of_exam = models.TextField(help_text=u'', null=True, verbose_name=u'Age of exam', blank=True) # This field type is a guess
    height = models.TextField(help_text=u'Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name=u'Height', blank=True) # This field type is a guess
    weight = models.TextField(help_text=u'Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name=u'Weight', blank=True) # This field type is a guess
    head_cir = models.FloatField(help_text=u'Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name=u'Head circumference (cm)', blank=True)
    head_shape = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Head shape', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Unknown/Not documented')])
    head_shape_spec = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Specify abnormal head shape', blank=True)
    anterior_fontanel_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Anterior fontanelle open and flat', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    anterior_fontanel_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe fontanelle', blank=True) # This field type is a guess
    forehead = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Forehead', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Unknown/Not documented')])
    forehead_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe abnormal forehead', blank=True) # This field type is a guess
    eyes_measured = models.NullBooleanField(help_text=u'', verbose_name=u'Eyes measured', blank=True)
    icd = models.FloatField(help_text=u'Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name=u'Inner Canthal Distance (mm)', blank=True)
    ocd = models.FloatField(help_text=u'Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name=u'Outer Canthal Distance (mm)', blank=True)
    ipd = models.FloatField(help_text=u'Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name=u'Inter Pupillary Distance (mm)', blank=True)
    ipd_source = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Inter Pupillary Distance (IPD) was', choices=[(1, u'measured'), (2, u'calculated')])
    w_index = models.FloatField(help_text=u'', null=True, verbose_name=u'W Index', blank=True)
    epicanthal_folds_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Epicanthal folds', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    epicanthal_folds_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe epicanthal folds', blank=True) # This field type is a guess
    heterochromia_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Heterochromia', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ears = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Ears', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Unknown/Not documented')])
    ear_lowset = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Lowset ear(s)', choices=[(1, u'Right'), (2, u'Left'), (3, u'Unknown/Not documented')])
    ear_pit_side = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Pit side', choices=[(1, u'Right'), (2, u'Left'), (3, u'Unknown/Not documented')])
    ear_pits_no_r = models.IntegerField(help_text=u'', null=True, verbose_name=u'Number of pits right', blank=True, choices=[(1, u'1'), (2, u'2'), (3, u'3'), (4, u'4'), (5, u'5'), (6, u'6'), (7, u'Unknown/Not documented')]) # This field type is a guess
    ear_pits_no_l = models.IntegerField(help_text=u'', null=True, verbose_name=u'Number of pits left', blank=True, choices=[(1, u'1'), (2, u'2'), (3, u'3'), (4, u'4'), (5, u'5'), (6, u'6'), (7, u'Unknown/Not documented')]) # This field type is a guess
    ear_tags_no_r = models.IntegerField(help_text=u'', null=True, verbose_name=u'Number of tags right', blank=True, choices=[(1, u'1'), (2, u'2'), (3, u'3'), (4, u'4'), (5, u'5'), (6, u'6'), (7, u'Unknown/Not documented')]) # This field type is a guess
    ear_tags_no_l = models.IntegerField(help_text=u'', null=True, verbose_name=u'Number of tags left', blank=True, choices=[(1, u'1'), (2, u'2'), (3, u'3'), (4, u'4'), (5, u'5'), (6, u'6'), (7, u'Unknown/Not documented')]) # This field type is a guess
    ear_abnormality_type_r = models.TextField(help_text=u'', null=True, verbose_name=u'Type of right ear structural abnormality', blank=True) # This field type is a guess
    ear_abnormality_type_l = models.TextField(help_text=u'', null=True, verbose_name=u'Type of left ear structural abnormality', blank=True) # This field type is a guess
    ear_large_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Large ears?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ear_small_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Small ears?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ears_measured = models.NullBooleanField(help_text=u'', verbose_name=u'Ears measured?', blank=True)
    ear_length_r = models.FloatField(help_text=u'Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name=u'Right ear length (cm)', blank=True)
    ear_length_l = models.FloatField(help_text=u'Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name=u'Left ear length (cm)', blank=True)
    midface_abnormality = models.IntegerField(help_text=u'', null=True, verbose_name=u'Midface abnormalities', blank=True, choices=[(4, u'None'), (1, u'Midface Hypoplasia'), (2, u'Unknown/Not documented'), (3, u'Other unknown abnormality'), (5, u'Other')]) # This field type is a guess
    philtrum = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Philtrum', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Unknown/Not documented')])
    philtrum_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe philtrum abnormalities', blank=True) # This field type is a guess
    palate_uvula_abnormality = models.IntegerField(help_text=u'', null=True, verbose_name=u'Palate/uvula abnormalities', blank=True, choices=[(4, u'None'), (1, u'Cleft'), (2, u'Arched'), (3, u'Narrowed'), (5, u'Other unknown abnormality'), (6, u'Other')]) # This field type is a guess
    cleft_spec = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Cleft type', choices=[(1, u'soft'), (2, u'hard'), (3, u'uvula')])
    chin = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Chin', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Unknown/Not documented')])
    chin_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe chin abnormalities', blank=True) # This field type is a guess
    neck_webbing_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Neck webbing', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    neck_webbing_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe neck webbing', blank=True) # This field type is a guess
    neck_jugular_venous_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Jugular venous distention present', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    neck_tracheostomy_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Tracheostomy present', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    neck_hairline = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Hairline', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Unknown/Not documented')])
    neck_hairline_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe abnormal hairline', blank=True) # This field type is a guess
    thyroid_enlargement_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Thyroid enlargement', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    murmurs_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Murmurs', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    murmurs_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe murmurs', blank=True) # This field type is a guess
    asym_chest_wall_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Asymmetrical chest wall', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    asym_chest_wall_spec = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Describe asymmetrical chest wall', blank=True)
    sternotomy_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Sternotomy ', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    thoractomy_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Thoracotomy', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    marfan_stigmata_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Marfan Stigmata/findings present', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    marfan_minor_criteria = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Ghent Criteria for Marfan Syndrome (Minor Criteria/System)', choices=[(16, u'None'), (1, u'Skeletal: Characteristic facies'), (2, u'Skeletal: High palate with dental crowding'), (3, u'Skeletal: Joint hypermobility'), (4, u'Skeletal: Pectus excavatum'), (5, u'CV: Calcified mitral annuls in patient'), (6, u'CV: Mitral valve prolapse'), (7, u'CV: Pulmonary artery dilation'), (8, u'CV: Other aortic dilation/ dissection'), (9, u'Ocular: Abnormal flat cornea'), (10, u'Ocular: Hypoplastic iris or cillary muscle causing decreased miosis'), (11, u'Ocular: Increased axial length of globe causing myopia'), (12, u'Pulmonary: Apical blebs'), (13, u'Pulmonary: Pneumothorax'), (14, u'Skin: Hernias'), (15, u'Skin: Striae atrophicae')])
    nipples = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Nipples (form and position)', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Unknown/Not documented')])
    nipples_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe nipple abnormalities', blank=True) # This field type is a guess
    inter_nipple_dist = models.CharField(help_text=u'Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, max_length=2000, verbose_name=u'Inter nipple distance (cm)', blank=True)
    chest_cir = models.CharField(help_text=u'Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, max_length=2000, verbose_name=u'Chest circumference (cm)', blank=True)
    ipc_cc_ratio = models.FloatField(help_text=u'', null=True, verbose_name=u'Inter nipple distance chest circumference ratio', blank=True)
    nephromegaly_extent = models.FloatField(help_text=u'', null=True, verbose_name=u'Extent of Nephromegaly (cm)', blank=True)
    hepatomegaly_extent = models.FloatField(help_text=u'', null=True, verbose_name=u'Extent of Hepatomegaly (cm)', blank=True)
    splenomegaly_extent = models.FloatField(help_text=u'', null=True, verbose_name=u'Extent of Splenomegaly (cm)', blank=True)
    hepatosplenomegaly_extent = models.FloatField(help_text=u'', null=True, verbose_name=u'Extent of Hepatosplenomegaly (cm)', blank=True)
    other_organomegaly_extent = models.FloatField(help_text=u'', null=True, verbose_name=u'Extent of other Organomegaly (cm)', blank=True)
    hernia_inguinal_lat = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Inguinal hernia laterality', choices=[(1, u'Bilateral'), (2, u'Unilateral')])
    hernia_inguinal_side = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Inguinal hernia side', choices=[(1, u'Right'), (2, u'Left')])
    ascites_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Ascites present', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ascites_fluid_wave_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Ascites fluid wave', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ascites_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe ascites', blank=True) # This field type is a guess
    spine_curvature = models.IntegerField(help_text=u'', null=True, verbose_name=u'Abnormal curvature of the spine | Type of curvature', blank=True, choices=[(1, u'None'), (2, u'Kyphosis'), (3, u'Lordosis'), (5, u'Scoliosis'), (6, u'Kyphoscoliosis'), (7, u'Unknown/Not documented'), (8, u'Other unknown abnormality'), (9, u'Other')]) # This field type is a guess
    sacral_abnormality = models.IntegerField(help_text=u'', null=True, verbose_name=u'Sacral abnormality | Type of sacral abnormality', blank=True, choices=[(10, u'None'), (1, u'abnormal crease'), (4, u'Meningomyelocele'), (5, u'Spina Bifida'), (6, u'Deep sacral simple'), (7, u'Unknown/Not documented'), (8, u'Other unknown abnormality'), (9, u'Other')]) # This field type is a guess
    skin_hyperextensibility_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Skin hyperextensibility', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    skin_hyperextensibility_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe skin hyperextensibility', blank=True) # This field type is a guess
    hair_abnormal_spec = models.IntegerField(help_text=u'', null=True, verbose_name=u'Hair abnormalities', blank=True, choices=[(9, u'None'), (1, u'Alopecia'), (2, u'Hirsutism'), (3, u'Dry'), (4, u'Brittle'), (5, u'Coarse'), (6, u'Wooly'), (7, u'Kinky'), (8, u'Blond'), (10, u'Unknown/Not documened'), (12, u'Other unknown abnormality'), (11, u'Other')]) # This field type is a guess
    anus_position = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Anus position', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Unknown/Not documented')])
    anus_position_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe abnormally positioned anus', blank=True) # This field type is a guess
    arm_symmetry_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Arm symmetry', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    arm_symmetry_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe arm asymmetry', blank=True) # This field type is a guess
    arm_span_measure = models.FloatField(help_text=u'', null=True, verbose_name=u'Arm span measurement (cm)/Marfan/ED', blank=True)
    leg_symmetry_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Leg symmetry ', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    leg_symmetry_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe leg asymmetry', blank=True) # This field type is a guess
    patellae = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Patellae', choices=[(1, u'Present'), (2, u'Absent')])
    joint_hypermobility_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Joint hypermobility', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    joint_hypermobility_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe joint hypermobility', blank=True) # This field type is a guess
    contractures_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Contractures', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    contractures_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe contractures', blank=True) # This field type is a guess
    right_palm_length = models.FloatField(help_text=u'Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name=u'Right palm length (cm)', blank=True)
    right_mf_length = models.FloatField(help_text=u'Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name=u'Right middle finger length (cm)', blank=True)
    right_mf_palm_ratio = models.FloatField(help_text=u'', null=True, verbose_name=u'Right MF palm ratio', blank=True)
    left_palm_length = models.FloatField(help_text=u'Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher.', null=True, verbose_name=u'Left palm length (cm)', blank=True)
    left_mf_length = models.FloatField(help_text=u'Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name=u'Left middle finger length (cm)', blank=True)
    left_mf_palm_ratio = models.FloatField(help_text=u'', null=True, verbose_name=u'Left  MF palm ratio', blank=True)
    dermatoglyphic_pattern = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Dermatoglyphic pattern', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Unknown/Not documented')])
    hand_right_d2 = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Right hand digit 2', choices=[(1, u'Ulnar loop'), (2, u'Radial loop'), (3, u'Whorl'), (4, u'Double loop'), (5, u'Arch'), (6, u'Tented arch'), (7, u'Medial')])
    hand_right_d4 = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Right hand digit 4', choices=[(1, u'Ulnar loop'), (2, u'Radial loop'), (3, u'Whorl'), (4, u'Double loop'), (5, u'Arch'), (6, u'Tented arch'), (7, u'Medial')])
    hand_left_d1 = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Left hand digit 1', choices=[(1, u'Ulnar loop'), (2, u'Radial loop'), (3, u'Whorl'), (4, u'Double loop'), (5, u'Arch'), (6, u'Tented arch'), (7, u'Medial')])
    hand_left_d3 = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Left hand digit 3', choices=[(1, u'Ulnar loop'), (2, u'Radial loop'), (3, u'Whorl'), (4, u'Double loop'), (5, u'Arch'), (6, u'Tented arch'), (7, u'Medial')])
    hand_left_d5 = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Left hand digit 5', choices=[(1, u'Ulnar loop'), (2, u'Radial loop'), (3, u'Whorl'), (4, u'Double loop'), (5, u'Arch'), (6, u'Tented arch'), (7, u'Medial')])
    dermatoglyphic_pattern_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Other comments regarding dermatoglyphic pattern on hands', blank=True) # This field type is a guess
    hand_creases = models.IntegerField(max_length=2000, blank=True, help_text=u'Normal = 2 creases; Abnormal = 1 crease', null=True, verbose_name=u'Creases?', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Unknown/Not documented')])
    hand_crease_rt_details = models.IntegerField(help_text=u'', null=True, verbose_name=u'Right hand creases', blank=True, choices=[(1, u'Single palmer'), (2, u'Branched'), (4, u'Unknown/Not documented'), (3, u'Other')]) # This field type is a guess
    hand_crease_lt_detail = models.IntegerField(help_text=u'', null=True, verbose_name=u'Left hand creases', blank=True, choices=[(1, u'Single palmer'), (2, u'Branched'), (4, u'Unknown/Not documented'), (3, u'Other')]) # This field type is a guess
    hand_other_features = models.IntegerField(help_text=u'', null=True, verbose_name=u'Features of fingers', blank=True, choices=[(10, u'None'), (1, u'Brachydactyly'), (2, u'Syndactyly'), (3, u'Postaxial Polydactyly'), (4, u'Preaxial Polydactyly'), (5, u'Camptodactyly'), (7, u'Ectrodactyly'), (8, u'Arachnodactyly'), (11, u'Clubbing'), (12, u'Clinodactyly'), (9, u'Unknown/Not documented'), (13, u'Other unknown feature'), (15, u'Other')]) # This field type is a guess
    arachnodactyl_side = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Location of arachnodactyly', choices=[(1, u'Both Hands'), (2, u'Right Hand only'), (3, u'Left Hand only'), (4, u'Unknown/Not documented')])
    clinodactyly_r_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Clinodactyly right', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    clinodactyly_l_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Clinodactyly left', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    foot_right_length = models.CharField(help_text=u'Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, max_length=2000, verbose_name=u'Right foot length (cm)', blank=True)
    foot_left_length = models.CharField(help_text=u'Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, max_length=2000, verbose_name=u'Left foot length (cm)', blank=True)
    foot_syndactyly_right_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'2-3 syndactyly right', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    foot_syndactyly_left_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'2-3 syndactyly left', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    feet_nails = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Foot nails', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Unknown/Not documented')])
    feet_nails_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe abnormal foot nails', blank=True) # This field type is a guess
    muscle_tone_strength = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Muscle tone and strength', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Unknown/Not documented')])
    muscle_tone_strength_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe muscle tone and strength', blank=True) # This field type is a guess
    reflexes = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Reflexes', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Unknown/Not documented')])
    reflexes_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe reflexes', blank=True) # This field type is a guess
    gait = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Gait', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Unknown/Not documented')])
    gait_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe gait', blank=True) # This field type is a guess
    diminished_pulses_loc = models.TextField(help_text=u'', null=True, verbose_name=u'Location of diminshed pulses', blank=True) # This field type is a guess
    absent_pulses_loc = models.TextField(help_text=u'', null=True, verbose_name=u'Location of absent pulses', blank=True) # This field type is a guess
    palpation = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Palpation', choices=[(1, u'Normal impulse'), (2, u'Heave'), (3, u'Thrill'), (4, u'Unknown/Not documente')])
    heaves_loc = models.IntegerField(help_text=u'', null=True, verbose_name=u'Location of Heave | Heave  - Specify', blank=True, choices=[(1, u'Left Ventricular'), (2, u'Right Ventricular'), (3, u'Unknown/Not documented'), (4, u'Other')]) # This field type is a guess
    thrill_loc = models.IntegerField(help_text=u'', null=True, verbose_name=u'Location of Thrill | Location of Thrill  - Specify', blank=True, choices=[(1, u'ULSB'), (2, u'URSB'), (3, u'Suprasternal notch'), (4, u'LLSB'), (5, u'Apex'), (7, u'Unknown/Not documented'), (6, u'Other')]) # This field type is a guess
    auscultation = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Auscultation', choices=[(1, u'Regular Rhythm'), (2, u'Irregular Rhythm'), (3, u'Hyperdynamic'), (4, u'Unknown/Not documented')])
    auscultation_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Describe auscultation', blank=True) # This field type is a guess
    click = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Click', choices=[(1, u'Absent'), (2, u'Present'), (3, u'Unknown/Not documented')])
    click_timing = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Timing of Click', choices=[(1, u'Early'), (2, u'Mid'), (3, u'Late'), (5, u'Unknown/Not documente')])
    click_loc = models.IntegerField(help_text=u'', null=True, verbose_name=u'Location of Click | Location of Click  - Specify', blank=True, choices=[(1, u'ULSB'), (2, u'URSB'), (3, u'Suprasternal notch'), (4, u'LLSB'), (5, u'Apex'), (7, u'Unknown/Not documented'), (6, u'Other')]) # This field type is a guess
    gallop = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Gallop', choices=[(1, u'Absent'), (2, u'Present'), (3, u'Unknown/Not documented')])
    gallop_spec = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Type of gallop', choices=[(1, u'S3'), (2, u'S4'), (3, u'Summation'), (4, u'Unknown/Not documented')])
    rub = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Rub', choices=[(1, u'Absent'), (2, u'Present'), (3, u'Unknown/Not documented')])
    rub_spec = models.IntegerField(help_text=u'', null=True, verbose_name=u'Describe rub | Describe rub  - Specify', blank=True, choices=[(1, u'Pleural'), (2, u'Pericardial'), (4, u'Unknown/Not documented'), (3, u'Other')]) # This field type is a guess
    pmi = models.IntegerField(help_text=u'', null=True, verbose_name=u'PMI | Specify PMI', blank=True, choices=[(1, u'Normal (5th left ICS MCL)'), (2, u'Dextrocardia'), (4, u'Unknown/Not documented'), (3, u'Other')]) # This field type is a guess
    second_heart_sound = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Second Heart Sound', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Widely split'), (4, u'Single'), (5, u'Loud'), (6, u'Narrowly split'), (7, u'Fixed split'), (8, u'Increased P2'), (9, u'Unknown/Not documented')])
    systolic_murmur_grade = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Systolic murmur grade (1 to 6)', blank=True)
    systolic_murmur_location = models.IntegerField(help_text=u'', null=True, verbose_name=u'Systolic murmur location | Systolic murmur location Other: Specify', blank=True, choices=[(1, u'LUSB'), (2, u'RUSB'), (3, u'MLSB'), (4, u'LLSB'), (5, u'LRSB'), (6, u'Apex'), (7, u'Post chest (R)'), (8, u'Post chest (L)'), (9, u'Under clavicle (R)'), (10, u'Under clavicle (L)'), (11, u'Right axillae'), (12, u'Left Axillae'), (14, u'Unknown/Not documented'), (13, u'Other')]) # This field type is a guess
    systolic_murmur_pitch = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Systolic murmur pitch', choices=[(1, u'High'), (2, u'Mid'), (3, u'Low'), (4, u'Unknown/Not documented')])
    systolic_murmur_radiation = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Systolic murmur radiation', blank=True)
    systolic_murmur_duration = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Systolic murmur duration/timing', choices=[(1, u'Early'), (2, u'Mid'), (3, u'Late'), (4, u'Holosystolic'), (5, u'Short'), (6, u'Ejection'), (7, u'Unknown/Not documented')])
    systolic_murmur_type = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Systolic murmur type', choices=[(1, u'Functional (or Innocent)'), (2, u'Pathological'), (3, u'Not determined'), (4, u'Unknown/Not documented')])
    diastolic_murmur_grade = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Diastolic murmur grade (1 to 4)', blank=True)
    diastolic_murmur_location = models.IntegerField(help_text=u'', null=True, verbose_name=u'Diastolic murmur location | Diastolic murmur location Other: Specify', blank=True, choices=[(1, u'LUSB'), (2, u'RUSB'), (3, u'MLSB'), (4, u'LLSB'), (5, u'LRSB'), (6, u'Apex'), (7, u'Post chest (R)'), (8, u'Post chest (L)'), (9, u'Under clavicle (R)'), (10, u'Under clavicle (L)'), (12, u'Unknown/Not documented'), (11, u'Other')]) # This field type is a guess
    diastolic_murmur_radiation = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Diastolic murmur radiation', blank=True)
    diastolic_murmur_duration = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Diastolic murmur duration/timing', choices=[(1, u'Early'), (2, u'Mid'), (3, u'Late'), (4, u'Short'), (5, u'Unknown/Not documented')])
    continuous_murmur_quality = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Continuous murmur quality', choices=[(1, u'Machinery'), (2, u'Blowing'), (3, u'Unknown/Not documented')])
    continuous_murmur_location = models.IntegerField(help_text=u'', null=True, verbose_name=u'Continuous murmur location | Continuous murmur location Other: Specify', blank=True, choices=[(1, u'LUSB'), (2, u'RUSB'), (3, u'MLSB'), (4, u'LLSB'), (5, u'LRSB'), (6, u'Apex'), (7, u'Post chest (R)'), (8, u'Post chest (L)'), (9, u'Under clavicle (R)'), (10, u'Under clavicle (L)'), (12, u'Uknown/Not documented'), (11, u'Other')]) # This field type is a guess
    carotid_bruit = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Carotid Bruit', choices=[(1, u'Absent'), (2, u'Present'), (3, u'Not documented')])
    venous_hum = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Venous Hum', choices=[(1, u'Absent'), (2, u'Present'), (3, u'Not documented')])
    current_breathing = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Current breathing', choices=[(1, u'Independent'), (2, u'Requires support'), (3, u'Unknown/Not documented')])
    lungs_clear_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Lungs clear', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    lungs_clear_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Lungs clear: Specify', blank=True) # This field type is a guess
    wheezes_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Wheezes', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    wheezes_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Wheezes: Specify', blank=True) # This field type is a guess
    rales_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Rales', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    rales_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Rales: Specify', blank=True) # This field type is a guess
    rhonchi_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Rhonchi', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    rhonchi_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Rhonchi: Specify', blank=True) # This field type is a guess
    cyanotic_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Cyanotic', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    cyanotic_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Cyanotic: Specify', blank=True) # This field type is a guess
    physical_exam_feedback = models.TextField(help_text=u'', null=True, verbose_name=u'Please provide any feedback for this form (for example: missing questions, questions not relevant for a disease area, ambiguities, places where a textbox could be replaced with discrete choices, missing discrete choices)', blank=True) # This field type is a guess
    ear_details_summary = models.CharField(help_text=u'1, Lowset | 2, Pits | 3, Tags | 4, Structural abnormality | 5, Not examined | 6, Unknown/Not documented', null=True, max_length=2000, verbose_name=u'Ears are/have', blank=True)
    ear_pits_details_summary = models.CharField(help_text=u'1, preauricular | 2, posterior auricular | 3, intra auricular | 4, Unknonwn/Not documented', null=True, max_length=2000, verbose_name=u'Pit type', blank=True)
    ear_tag_side_summary = models.CharField(help_text=u'1, Right | 2, Left', null=True, max_length=2000, verbose_name=u'Tag side', blank=True)
    ear_structural_abnormality_side_summary = models.CharField(help_text=u'1, Right | 2, Left | 3, Unknown/Not documented', null=True, max_length=2000, verbose_name=u'Ear structural abnormality side', blank=True)
    nose_abnormality_summary = models.CharField(help_text=u'8, None | 1, Alae nasi | 2, Nares | 3, Nasal appendages | 4, Nasal bridge | 5, Septum | 6, Tip | 7, Unknown/Not documented | 9, Other unknown abnormality | 10, Other', null=True, max_length=2000, verbose_name=u'Nose abnormalities', blank=True)
    mouth_teeth_abnormality_summary = models.CharField(help_text=u'5, None | 1, Micrognathism | 2, Myopathic facies | 3, Unknown/Not documented | 6, Other unknown abnormality | 4, Other', null=True, max_length=2000, verbose_name=u'Mouth and teeth abnormalities', blank=True)
    neck_mass_summary = models.CharField(help_text=u'7, None | 1, Gland | 2, Nodule | 3, Cyst | 4, Thyroid | 6, Unknown/Not documented | 8, Other unknown mass | 5, Other', null=True, max_length=2000, verbose_name=u'Neck masses | Specify other neck mass', blank=True)
    pectus_abnormality_summary = models.CharField(help_text=u'1, None  | 2, Pectus excavatum | 3, Pectus carinatum | 4, Unknown/Not documented | 5,  Other unknown abnormality | 6, Other', null=True, max_length=2000, verbose_name=u'Pectus abnormalities', blank=True)
    marfan_major_criteria_summary = models.CharField(help_text=u'17, None | 1, Skeletal: Arachnodactily- both wrist and thumb signs | 2, Skeletal: Pectus carinatum | 3, Skeletal: Pectus excavatum | 4, Skeletal: Pes planus | 5, Skeletal: Protrusio acetabulae | 6, Skeletal: Reduced elbow extension (<170 degrees) | 7, Skeletal: Scoliosis >20 degrees or spondylolithesis | 8, Skeletal: Upper to lower segment ratio<0.86 | 9, Skeletal: Span to height ration >1.05 | 10, CV: Aortic root dilatation | 11, CV: Dissection of ascending aorta | 12, Ocular: Ectopia lentis (lens dislocation) | 13, Neurologic: Lumbosacral dural estasia | 14, Genetics: Family History | 15, Genetics: Genetic mutations known to cause Marfan | 16, Genetics: Inheritance of DNA marker haplotype linked to MFS in family', null=True, max_length=2000, verbose_name=u'Ghent Criteria for Marfan Syndrome (Major Criteria/System)', blank=True)
    abdomen_organomegaly_summary = models.CharField(help_text=u'6, None | 1, Nephromegaly | 2, Hepatomegaly | 3, Splenomegaly | 4, Hepatosplenomegaly | 7, Unknown/Not documented | 8, Other unknown abnormality | 5, Other', null=True, max_length=2000, verbose_name=u'Organomegaly? | Please specify type of organomegaly', blank=True)
    hernias_summary = models.CharField(help_text=u'4, None | 1, Umbilical | 2, Inguinal | 3, Abdominal | 5, Unknown/Not documented | 6, Other unknown hernia | 7, Other', null=True, max_length=2000, verbose_name=u'Hernias | Describe other hernia', blank=True)
    birthmark_rash_summary = models.CharField(help_text=u'1, None | 2, cafe au lait spots | 3, capillary hemangioma | 4, cutis marmorata | 5, diffuse hypopigmented skin lesions | 6, Unknown/Not documented| 7, Other unknown abnormality |8, Other', null=True, max_length=2000, verbose_name=u'Birthmarks or rash | Describe other birthmark rash', blank=True)
    skin_conditions_summary = models.CharField(help_text=u'1, None | 2, Ichthyosis | 3, Unknown/Not documented | 4, Other unknown condition | 5, Other', null=True, max_length=2000, verbose_name=u'Other skin conditions', blank=True)
    patellae_absent_side_summary = models.CharField(help_text=u'1, Right | 2, Left', null=True, max_length=2000, verbose_name=u'Patellae absent side', blank=True)
    hand_right_d1_summary = models.CharField(help_text=u'1, Ulnar loop | 2, Radial loop | 3, Whorl | 4, Double loop | 5, Arch | 6, Tented arch | 7, Medial ', null=True, max_length=2000, verbose_name=u'Right hand digit 1', blank=True)
    hand_right_d3_summary = models.CharField(help_text=u'1, Ulnar loop | 2, Radial loop | 3, Whorl | 4, Double loop | 5, Arch | 6, Tented arch | 7, Medial ', null=True, max_length=2000, verbose_name=u'Right hand digit 3', blank=True)
    hand_right_d5_summary = models.CharField(help_text=u'1, Ulnar loop | 2, Radial loop | 3, Whorl | 4, Double loop | 5, Arch | 6, Tented arch | 7, Medial ', null=True, max_length=2000, verbose_name=u'Right hand digit 5', blank=True)
    hand_left_d2_summary = models.CharField(help_text=u'1, Ulnar loop | 2, Radial loop | 3, Whorl | 4, Double loop | 5, Arch | 6, Tented arch | 7, Medial ', null=True, max_length=2000, verbose_name=u'Left hand digit 2', blank=True)
    hand_left_d4_summary = models.CharField(help_text=u'1, Ulnar loop | 2, Radial loop | 3, Whorl | 4, Double loop | 5, Arch | 6, Tented arch | 7, Medial ', null=True, max_length=2000, verbose_name=u'Left hand digit 4', blank=True)
    hand_creases_side_summary = models.CharField(help_text=u'1, Right | 2, Left | 3, Unknown/Not documented', null=True, max_length=2000, verbose_name=u'Abnormal creases side', blank=True)
    hand_nails_summary = models.CharField(help_text=u'5, None |1, Creases | 2, Hypoplastic | 3, Pitted | 4, Prolonged | 6, Unknown/Not documented | 7, Other unknown abnormality | 8, Other', null=True, max_length=2000, verbose_name=u'Nail abnormalities', blank=True)
    pulses_summary = models.CharField(help_text=u'1, Equal | 2, Bounding | 3, Diminished | 4, Absent | 5, Radial femoral delay | 6, Unknown/Not documented', null=True, max_length=2000, verbose_name=u'Pulses', blank=True)
    first_heart_sound_summary = models.CharField(help_text=u'1, Normal | 2, Abnormal | 3, Widely split | 4, Unknown/Not documented', null=True, max_length=2000, verbose_name=u'First Heart Sound', blank=True)
    murmur_summary = models.CharField(help_text=u'1, Absent | 2, Systolic | 3, Diastolic | 4, Continuous | 5, Unknown/Not documented', null=True, max_length=2000, verbose_name=u'Murmur', blank=True)
    systolic_quality_summary = models.CharField(help_text=u'1, Stills, vibratory, musical, twangy | 2, Pulmonic flow | 3, Harsh | 4, Blowing or regurgitant | 5, Crescendo-decrescendo/to and fro | 6, Ejection | 7, Unknown/Not documented', null=True, max_length=2000, verbose_name=u'Systolic Quality/Characteristics', blank=True)
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'physicalexam'


class eardetails(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Ears are/have', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Ears are/have', choices=[(1, u'Lowset'), (2, u'Pits'), (3, u'Tags'), (4, u'Structural abnormality'), (5, u'Not examined'), (6, u'Unknown/Not documented')])
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'eardetails'


class earpitsdetails(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Pit type', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Pit type', choices=[(1, u'preauricular'), (2, u'posterior auricular'), (3, u'intra auricular'), (4, u'Unknonwn/Not documented')])
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'earpitsdetails'


class eartagside(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Tag side', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Tag side', choices=[(1, u'Right'), (2, u'Left')])
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'eartagside'


class earstructuralabnormalityside(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Ear structural abnormality side', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Ear structural abnormality side', choices=[(1, u'Right'), (2, u'Left'), (3, u'Unknown/Not documented')])
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'earstructuralabnormalityside'


class noseabnormality(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Nose abnormalities', blank=True)
    value = models.IntegerField(help_text=u'', null=True, verbose_name=u'Nose abnormalities', blank=True, choices=[(8, u'None'), (1, u'Alae nasi'), (2, u'Nares'), (3, u'Nasal appendages'), (4, u'Nasal bridge'), (5, u'Septum'), (6, u'Tip'), (7, u'Unknown/Not documented'), (9, u'Other unknown abnormality'), (10, u'Other')]) # This field type is a guess
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'noseabnormality'


class mouthteethabnormality(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Mouth and teeth abnormalities', blank=True)
    value = models.IntegerField(help_text=u'', null=True, verbose_name=u'Mouth and teeth abnormalities', blank=True, choices=[(5, u'None'), (1, u'Micrognathism'), (2, u'Myopathic facies'), (3, u'Unknown/Not documented'), (6, u'Other unknown abnormality'), (4, u'Other')]) # This field type is a guess
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'mouthteethabnormality'


class neckmass(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Neck masses | Specify other neck mass', blank=True)
    value = models.IntegerField(help_text=u'', null=True, verbose_name=u'Neck masses | Specify other neck mass', blank=True, choices=[(7, u'None'), (1, u'Gland'), (2, u'Nodule'), (3, u'Cyst'), (4, u'Thyroid'), (6, u'Unknown/Not documented'), (8, u'Other unknown mass'), (5, u'Other')]) # This field type is a guess
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'neckmass'


class pectusabnormality(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Pectus abnormalities', blank=True)
    value = models.IntegerField(help_text=u'', null=True, verbose_name=u'Pectus abnormalities', blank=True, choices=[(1, u'None'), (2, u'Pectus excavatum'), (3, u'Pectus carinatum'), (4, u'Unknown/Not documented'), (5, u'Other unknown abnormality'), (6, u'Other')]) # This field type is a guess
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'pectusabnormality'


class marfanmajorcriteria(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Ghent Criteria for Marfan Syndrome (Major Criteria/System)', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Ghent Criteria for Marfan Syndrome (Major Criteria/System)', choices=[(17, u'None'), (1, u'Skeletal: Arachnodactily- both wrist and thumb signs'), (2, u'Skeletal: Pectus carinatum'), (3, u'Skeletal: Pectus excavatum'), (4, u'Skeletal: Pes planus'), (5, u'Skeletal: Protrusio acetabulae'), (6, u'Skeletal: Reduced elbow extension (<170 degrees)'), (7, u'Skeletal: Scoliosis >20 degrees or spondylolithesis'), (8, u'Skeletal: Upper to lower segment ratio<0.86'), (9, u'Skeletal: Span to height ration >1.05'), (10, u'CV: Aortic root dilatation'), (11, u'CV: Dissection of ascending aorta'), (12, u'Ocular: Ectopia lentis (lens dislocation)'), (13, u'Neurologic: Lumbosacral dural estasia'), (14, u'Genetics: Family History'), (15, u'Genetics: Genetic mutations known to cause Marfan'), (16, u'Genetics: Inheritance of DNA marker haplotype linked to MFS in family')])
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'marfanmajorcriteria'


class abdomenorganomegaly(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Organomegaly? | Please specify type of organomegaly', blank=True)
    value = models.IntegerField(help_text=u'', null=True, verbose_name=u'Organomegaly? | Please specify type of organomegaly', blank=True, choices=[(6, u'None'), (1, u'Nephromegaly'), (2, u'Hepatomegaly'), (3, u'Splenomegaly'), (4, u'Hepatosplenomegaly'), (7, u'Unknown/Not documented'), (8, u'Other unknown abnormality'), (5, u'Other')]) # This field type is a guess
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'abdomenorganomegaly'


class hernias(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Hernias | Describe other hernia', blank=True)
    value = models.IntegerField(help_text=u'', null=True, verbose_name=u'Hernias | Describe other hernia', blank=True, choices=[(4, u'None'), (1, u'Umbilical'), (2, u'Inguinal'), (3, u'Abdominal'), (5, u'Unknown/Not documented'), (6, u'Other unknown hernia'), (7, u'Other')]) # This field type is a guess
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'hernias'


class birthmarkrash(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Birthmarks or rash | Describe other birthmark rash', blank=True)
    value = models.IntegerField(help_text=u'', null=True, verbose_name=u'Birthmarks or rash | Describe other birthmark rash', blank=True, choices=[(1, u'None'), (2, u'cafe au lait spots'), (3, u'capillary hemangioma'), (4, u'cutis marmorata'), (5, u'diffuse hypopigmented skin lesions'), (6, u'Unknown/Not documented'), (7, u'Other unknown abnormality'), (8, u'Other')]) # This field type is a guess
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'birthmarkrash'


class skinconditions(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Other skin conditions', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Other skin conditions', choices=[(1, u'None'), (2, u'Ichthyosis'), (3, u'Unknown/Not documented'), (4, u'Other unknown condition'), (5, u'Other')])
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'skinconditions'


class patellaeabsentside(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Patellae absent side', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Patellae absent side', choices=[(1, u'Right'), (2, u'Left')])
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'patellaeabsentside'


class handrightd1(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Right hand digit 1', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Right hand digit 1', choices=[(1, u'Ulnar loop'), (2, u'Radial loop'), (3, u'Whorl'), (4, u'Double loop'), (5, u'Arch'), (6, u'Tented arch'), (7, u'Medial')])
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'handrightd1'


class handrightd3(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Right hand digit 3', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Right hand digit 3', choices=[(1, u'Ulnar loop'), (2, u'Radial loop'), (3, u'Whorl'), (4, u'Double loop'), (5, u'Arch'), (6, u'Tented arch'), (7, u'Medial')])
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'handrightd3'


class handrightd5(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Right hand digit 5', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Right hand digit 5', choices=[(1, u'Ulnar loop'), (2, u'Radial loop'), (3, u'Whorl'), (4, u'Double loop'), (5, u'Arch'), (6, u'Tented arch'), (7, u'Medial')])
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'handrightd5'


class handleftd2(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Left hand digit 2', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Left hand digit 2', choices=[(1, u'Ulnar loop'), (2, u'Radial loop'), (3, u'Whorl'), (4, u'Double loop'), (5, u'Arch'), (6, u'Tented arch'), (7, u'Medial')])
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'handleftd2'


class handleftd4(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Left hand digit 4', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Left hand digit 4', choices=[(1, u'Ulnar loop'), (2, u'Radial loop'), (3, u'Whorl'), (4, u'Double loop'), (5, u'Arch'), (6, u'Tented arch'), (7, u'Medial')])
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'handleftd4'


class handcreasesside(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Abnormal creases side', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Abnormal creases side', choices=[(1, u'Right'), (2, u'Left'), (3, u'Unknown/Not documented')])
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'handcreasesside'


class handnails(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Nail abnormalities', blank=True)
    value = models.IntegerField(help_text=u'', null=True, verbose_name=u'Nail abnormalities', blank=True, choices=[(5, u'None'), (1, u'Creases'), (2, u'Hypoplastic'), (3, u'Pitted'), (4, u'Prolonged'), (6, u'Unknown/Not documented'), (7, u'Other unknown abnormality'), (8, u'Other')]) # This field type is a guess
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'handnails'


class pulses(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Pulses', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Pulses', choices=[(1, u'Equal'), (2, u'Bounding'), (3, u'Diminished'), (4, u'Absent'), (5, u'Radial femoral delay'), (6, u'Unknown/Not documented')])
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'pulses'


class firstheartsound(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'First Heart Sound', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'First Heart Sound', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Widely split'), (4, u'Unknown/Not documented')])
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'firstheartsound'


class murmur(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Murmur', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Murmur', choices=[(1, u'Absent'), (2, u'Systolic'), (3, u'Diastolic'), (4, u'Continuous'), (5, u'Unknown/Not documented')])
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'murmur'


class systolicquality(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Systolic Quality/Characteristics', blank=True)
    value = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Systolic Quality/Characteristics', blank=True)
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'systolicquality'


class OtherSkinFinding(models.Model):
    other_skin_finding = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'other skin finding', blank=True)
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'otherskinfinding'


class HearingImpairment(models.Model):
    age_of_onset = models.IntegerField(help_text=u'', null=True, verbose_name=u'Age of onset', blank=True, choices=[(1, u'congenital(at birth)'), (2, u'after birth up to 1 year'), (3, u'one year'), (4, u'two years'), (5, u'three years'), (6, u'four years'), (7, u'five years'), (8, u'six years'), (9, u'seven years'), (10, u'eight years'), (11, u'nine years'), (12, u'ten years'), (13, u'11 years'), (14, u'12 years'), (15, u'13 years'), (16, u'14 years'), (17, u'15 years'), (18, u'16 years'), (19, u'17 years'), (20, u'18 years'), (26, u'19 years'), (21, u'20 years'), (22, u'21-30'), (23, u'31-40'), (24, u'41-50'), (25, u'51-60'), (27, u'> 60 years')]) # This field type is a guess
    type_of_hearing_impairment = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Type of hearing impairment', choices=[(1, u'Sensorineural'), (2, u'Conductive'), (3, u'Unknown/Not documented')])
    hear_impair_laterality = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Impairment laterality', choices=[(1, u'Bilateral'), (2, u'Unilateral'), (3, u'Unknown/Not documented')])
    hear_impair_symmetric = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Symmetric impairment?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ear_side = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Impaired ear', choices=[(1, u'Left'), (2, u'Right'), (3, u'Unknown/Not documented')])
    hear_impair_severity = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Severity of impairment', choices=[(1, u'Mild'), (2, u'Mild-Moderate'), (3, u'Mild-Severe'), (4, u'Mild-Profound'), (5, u'Moderate'), (6, u'Moderate-Severe'), (7, u'Moderate-Profound'), (8, u'Profound'), (9, u'Unknown/Not documented')])
    hear_impair_severity_l = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Severity of left ear impairment', choices=[(1, u'Mild'), (2, u'Mild-Moderate'), (3, u'Mild-Severe'), (4, u'Mild-Profound'), (5, u'Moderate'), (6, u'Moderate-Severe'), (7, u'Moderate-Profound'), (8, u'Profound'), (9, u'Unknown/Not documented')])
    hear_impair_severity_r = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Severity of right ear impairment', choices=[(1, u'Mild'), (2, u'Mild-Moderate'), (3, u'Mild-Severe'), (4, u'Mild-Profound'), (5, u'Moderate'), (6, u'Moderate-Severe'), (7, u'Moderate-Profound'), (8, u'Profound'), (9, u'Unknown/Not documented')])
    hear_impaired_freq = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Impaired frequency', choices=[(1, u'All frequencies'), (2, u'High frequency'), (3, u'Low frequency'), (4, u'Cookie bite (mid frequency)'), (5, u'Unknown/Not documented')])
    hear_impaired_freq_l = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Left ear impaired frequency', choices=[(1, u'All frequencies'), (2, u'High frequency'), (3, u'Low frequency'), (4, u'Cookie bite (mid frequency)'), (5, u'Unknown/Not documented')])
    hear_impaired_freq_r = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Right ear impaired frequency', choices=[(1, u'All frequencies'), (2, u'High frequency'), (3, u'Low frequency'), (4, u'Cookie bite (mid frequency)'), (5, u'Unknown/Not documented')])
    hear_progressed_severity = models.NullBooleanField(help_text=u'', verbose_name=u'Has hearing impairment progressed in severity?', blank=True)
    fh_hear_imp_pedi = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Hearing impairment affected relative(s)', choices=[(1, u'Mother'), (2, u'Father'), (3, u'Sister'), (4, u'Brother'), (5, u'Maternal Grandmother'), (6, u'Maternal Grandfather'), (7, u'Paternal Grandmother'), (8, u'Paternal Grandfather'), (9, u'Maternal Aunt'), (10, u'Paternal Aunt'), (11, u'Maternal Uncle'), (12, u'Paternal Uncle'), (13, u'Maternal Cousin'), (14, u'Paternal Cousin')])
    fh_diabetes_pedi = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Diabetes affected relative(s)', choices=[(1, u'Mother'), (2, u'Father'), (3, u'Sister'), (4, u'Brother'), (5, u'Maternal Grandmother'), (6, u'Maternal Grandfather'), (7, u'Paternal Grandmother'), (8, u'Paternal Grandfather'), (9, u'Maternal Aunt'), (10, u'Paternal Aunt'), (11, u'Maternal Uncle'), (12, u'Paternal Uncle'), (13, u'Maternal Cousin'), (14, u'Paternal Cousin')])
    fh_prem_grey_pedi = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Premature greying of hair affected relative(s)', choices=[(1, u'Mother'), (2, u'Father'), (3, u'Sister'), (4, u'Brother'), (5, u'Maternal Grandmother'), (6, u'Maternal Grandfather'), (7, u'Paternal Grandmother'), (8, u'Paternal Grandfather'), (9, u'Maternal Aunt'), (10, u'Paternal Aunt'), (11, u'Maternal Uncle'), (12, u'Paternal Uncle'), (13, u'Maternal Cousin'), (14, u'Paternal Cousin')])
    fh_id_pedi = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Developmental delay, learning disability, or intellectual disability affected relative(s)', choices=[(1, u'Mother'), (2, u'Father'), (3, u'Sister'), (4, u'Brother'), (5, u'Maternal Grandmother'), (6, u'Maternal Grandfather'), (7, u'Paternal Grandmother'), (8, u'Paternal Grandfather'), (9, u'Maternal Aunt'), (10, u'Paternal Aunt'), (11, u'Maternal Uncle'), (12, u'Paternal Uncle'), (13, u'Maternal Cousin'), (14, u'Paternal Cousin')])
    fh_arthritis_pedi = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Arthritis affected relative(s)', choices=[(1, u'Mother'), (2, u'Father'), (3, u'Sister'), (4, u'Brother'), (5, u'Maternal Grandmother'), (6, u'Maternal Grandfather'), (7, u'Paternal Grandmother'), (8, u'Paternal Grandfather'), (9, u'Maternal Aunt'), (10, u'Paternal Aunt'), (11, u'Maternal Uncle'), (12, u'Paternal Uncle'), (13, u'Maternal Cousin'), (14, u'Paternal Cousin')])
    fh_whiteforelock_pedi = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'White forelock affected relative(s)', choices=[(1, u'Mother'), (2, u'Father'), (3, u'Sister'), (4, u'Brother'), (5, u'Maternal Grandmother'), (6, u'Maternal Grandfather'), (7, u'Paternal Grandmother'), (8, u'Paternal Grandfather'), (9, u'Maternal Aunt'), (10, u'Paternal Aunt'), (11, u'Maternal Uncle'), (12, u'Paternal Uncle'), (13, u'Maternal Cousin'), (14, u'Paternal Cousin')])
    fh_birthdefect_pedi = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Birth defect affected relative(s)', choices=[(1, u'Mother'), (2, u'Father'), (3, u'Sister'), (4, u'Brother'), (5, u'Maternal Grandmother'), (6, u'Maternal Grandfather'), (7, u'Paternal Grandmother'), (8, u'Paternal Grandfather'), (9, u'Maternal Aunt'), (10, u'Paternal Aunt'), (11, u'Maternal Uncle'), (12, u'Paternal Uncle'), (13, u'Maternal Cousin'), (14, u'Paternal Cousin')])
    fh_consanguinity_pedi = models.TextField(help_text=u'', null=True, verbose_name=u'Consanguinity details', blank=True) # This field type is a guess
    dystopia_canthorum = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Dystopia Canthorum', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ear_helical_structure = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Helical structure', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Unknown/Not documented')])
    ear_helical_laterality = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Abnormal helical structure laterality', choices=[(1, u'Unilateral'), (2, u'Bilateral'), (3, u'Unknown/Not documented')])
    ear_helical_abn_sym = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Symmetric abnormality?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    ear_helical_rl = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Abnormal helical structure side', choices=[(1, u'Right'), (2, u'Left')])
    ear_helical_details_l = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Left ear helical structure details', choices=[(1, u'Cupped'), (2, u'Thick helix'), (3, u'Hypoplastic'), (4, u'Darwinian tubercle'), (5, u'Prominent anti helix'), (6, u'Unknown/Not documented')])
    clavicles = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Clavicles', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Unknown/Not documented')])
    clavicles_details = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Abnormal clavicle details', choices=[(1, u'Absent'), (2, u'Hypoplastic'), (3, u'Unknown/Not documented')])
    hearing_known_diagnosis = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Known diagnosis', blank=True)
    hearing_suspected_diagnoses = models.TextField(help_text=u'', null=True, verbose_name=u'Suspected diagnoses', blank=True) # This field type is a guess
    hearing_impairment_feedback = models.TextField(help_text=u'', null=True, verbose_name=u'Please provide any feedback for this form (for example: missing questions, questions not relevant for a disease area, ambiguities, places where a textbox could be replaced with discrete choices, missing discrete choices)', blank=True) # This field type is a guess
    nb_exposures_summary = models.CharField(help_text=u'6, None | 1, Ventilator | 2, Jaundice | 3, Antibiotics | 4, Infections | 5, Other medications', null=True, max_length=2000, verbose_name=u'Newborn exposures', blank=True)
    familiy_history_summary = models.CharField(help_text=u'15, None | 1, Hearing impairment | 2, Thyroid Problems | 3, Diabetes | 4, Brachial cysts or clefts | 5, Premature greying of hair | 6, Abnormally shaped ears | 7, Developmental delay, learning disability, or intellectual disability | 8, Significant vision loss or night blindness | 9, Arthritis | 10, Kidney problems | 11, White forelock | 12, Heterochromia | 13, Birth defects | 14, Consanguinity', null=True, max_length=2000, verbose_name=u'Family history of', blank=True)
    fh_thryoid_imp_pedi_summary = models.CharField(help_text=u'1, Mother | 2, Father | 3, Sister | 4, Brother | 5, Maternal Grandmother | 6, Maternal Grandfather | 7, Paternal Grandmother | 8, Paternal Grandfather | 9, Maternal Aunt | 10, Paternal Aunt | 11, Maternal Uncle | 12, Paternal Uncle | 13, Maternal Cousin | 14, Paternal Cousin', null=True, max_length=2000, verbose_name=u'Thyroid problem affected relative(s)', blank=True)
    fh_brachial_pedi_summary = models.CharField(help_text=u'1, Mother | 2, Father | 3, Sister | 4, Brother | 5, Maternal Grandmother | 6, Maternal Grandfather | 7, Paternal Grandmother | 8, Paternal Grandfather | 9, Maternal Aunt | 10, Paternal Aunt | 11, Maternal Uncle | 12, Paternal Uncle | 13, Maternal Cousin | 14, Paternal Cousin', null=True, max_length=2000, verbose_name=u'Brachial cysts or cleft affected relative(s)', blank=True)
    fh_ab_ears_pedi_summary = models.CharField(help_text=u'1, Mother | 2, Father | 3, Sister | 4, Brother | 5, Maternal Grandmother | 6, Maternal Grandfather | 7, Paternal Grandmother | 8, Paternal Grandfather | 9, Maternal Aunt | 10, Paternal Aunt | 11, Maternal Uncle | 12, Paternal Uncle | 13, Maternal Cousin | 14, Paternal Cousin', null=True, max_length=2000, verbose_name=u'Abnormally shaped ears affected relative(s)', blank=True)
    fh_vision_pedi_summary = models.CharField(help_text=u'1, Mother | 2, Father | 3, Sister | 4, Brother | 5, Maternal Grandmother | 6, Maternal Grandfather | 7, Paternal Grandmother | 8, Paternal Grandfather | 9, Maternal Aunt | 10, Paternal Aunt | 11, Maternal Uncle | 12, Paternal Uncle | 13, Maternal Cousin | 14, Paternal Cousin', null=True, max_length=2000, verbose_name=u'Significant vision loss or night blindness affected relative(s)', blank=True)
    fh_kidney_pedi_summary = models.CharField(help_text=u'1, Mother | 2, Father | 3, Sister | 4, Brother | 5, Maternal Grandmother | 6, Maternal Grandfather | 7, Paternal Grandmother | 8, Paternal Grandfather | 9, Maternal Aunt | 10, Paternal Aunt | 11, Maternal Uncle | 12, Paternal Uncle | 13, Maternal Cousin | 14, Paternal Cousin', null=True, max_length=2000, verbose_name=u'Kidney problem affected relative(s)', blank=True)
    fh_heterochromia_pedi_summary = models.CharField(help_text=u'1, Mother | 2, Father | 3, Sister | 4, Brother | 5, Maternal Grandmother | 6, Maternal Grandfather | 7, Paternal Grandmother | 8, Paternal Grandfather | 9, Maternal Aunt | 10, Paternal Aunt | 11, Maternal Uncle | 12, Paternal Uncle | 13, Maternal Cousin | 14, Paternal Cousin', null=True, max_length=2000, verbose_name=u'Heterochromia affected relative(s)', blank=True)
    ear_helical_details_summary = models.CharField(help_text=u'1, Cupped | 2, Thick helix | 3, Hypoplastic | 4, Darwinian tubercle | 5, Prominent anti helix | 6, Unknown/Not documented', null=True, max_length=2000, verbose_name=u'Helical structure details', blank=True)
    ear_helical_details_r_summary = models.CharField(help_text=u'1, Cupped | 2, Thick helix | 3, Hypoplastic | 4, Darwinian tubercle | 5, Prominent anti helix | 6, Unknown/Not documented', null=True, max_length=2000, verbose_name=u'Right ear helical structure details', blank=True)
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'hearingimpairment'


class nbexposures(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Newborn exposures', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Newborn exposures', choices=[(6, u'None'), (1, u'Ventilator'), (2, u'Jaundice'), (3, u'Antibiotics'), (4, u'Infections'), (5, u'Other medications')])
    hearingimpairment = models.ForeignKey(HearingImpairment)

    class Meta:
	 db_table = 'nbexposures'


class familiyhistory(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Family history of', blank=True)
    value = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Family history of', blank=True)
    hearingimpairment = models.ForeignKey(HearingImpairment)

    class Meta:
	 db_table = 'familiyhistory'


class fhthryoidimppedi(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Thyroid problem affected relative(s)', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Thyroid problem affected relative(s)', choices=[(1, u'Mother'), (2, u'Father'), (3, u'Sister'), (4, u'Brother'), (5, u'Maternal Grandmother'), (6, u'Maternal Grandfather'), (7, u'Paternal Grandmother'), (8, u'Paternal Grandfather'), (9, u'Maternal Aunt'), (10, u'Paternal Aunt'), (11, u'Maternal Uncle'), (12, u'Paternal Uncle'), (13, u'Maternal Cousin'), (14, u'Paternal Cousin')])
    hearingimpairment = models.ForeignKey(HearingImpairment)

    class Meta:
	 db_table = 'fhthryoidimppedi'


class fhbrachialpedi(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Brachial cysts or cleft affected relative(s)', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Brachial cysts or cleft affected relative(s)', choices=[(1, u'Mother'), (2, u'Father'), (3, u'Sister'), (4, u'Brother'), (5, u'Maternal Grandmother'), (6, u'Maternal Grandfather'), (7, u'Paternal Grandmother'), (8, u'Paternal Grandfather'), (9, u'Maternal Aunt'), (10, u'Paternal Aunt'), (11, u'Maternal Uncle'), (12, u'Paternal Uncle'), (13, u'Maternal Cousin'), (14, u'Paternal Cousin')])
    hearingimpairment = models.ForeignKey(HearingImpairment)

    class Meta:
	 db_table = 'fhbrachialpedi'


class fhabearspedi(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Abnormally shaped ears affected relative(s)', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Abnormally shaped ears affected relative(s)', choices=[(1, u'Mother'), (2, u'Father'), (3, u'Sister'), (4, u'Brother'), (5, u'Maternal Grandmother'), (6, u'Maternal Grandfather'), (7, u'Paternal Grandmother'), (8, u'Paternal Grandfather'), (9, u'Maternal Aunt'), (10, u'Paternal Aunt'), (11, u'Maternal Uncle'), (12, u'Paternal Uncle'), (13, u'Maternal Cousin'), (14, u'Paternal Cousin')])
    hearingimpairment = models.ForeignKey(HearingImpairment)

    class Meta:
	 db_table = 'fhabearspedi'


class fhvisionpedi(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Significant vision loss or night blindness affected relative(s)', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Significant vision loss or night blindness affected relative(s)', choices=[(1, u'Mother'), (2, u'Father'), (3, u'Sister'), (4, u'Brother'), (5, u'Maternal Grandmother'), (6, u'Maternal Grandfather'), (7, u'Paternal Grandmother'), (8, u'Paternal Grandfather'), (9, u'Maternal Aunt'), (10, u'Paternal Aunt'), (11, u'Maternal Uncle'), (12, u'Paternal Uncle'), (13, u'Maternal Cousin'), (14, u'Paternal Cousin')])
    hearingimpairment = models.ForeignKey(HearingImpairment)

    class Meta:
	 db_table = 'fhvisionpedi'


class fhkidneypedi(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Kidney problem affected relative(s)', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Kidney problem affected relative(s)', choices=[(1, u'Mother'), (2, u'Father'), (3, u'Sister'), (4, u'Brother'), (5, u'Maternal Grandmother'), (6, u'Maternal Grandfather'), (7, u'Paternal Grandmother'), (8, u'Paternal Grandfather'), (9, u'Maternal Aunt'), (10, u'Paternal Aunt'), (11, u'Maternal Uncle'), (12, u'Paternal Uncle'), (13, u'Maternal Cousin'), (14, u'Paternal Cousin')])
    hearingimpairment = models.ForeignKey(HearingImpairment)

    class Meta:
	 db_table = 'fhkidneypedi'


class fhheterochromiapedi(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Heterochromia affected relative(s)', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Heterochromia affected relative(s)', choices=[(1, u'Mother'), (2, u'Father'), (3, u'Sister'), (4, u'Brother'), (5, u'Maternal Grandmother'), (6, u'Maternal Grandfather'), (7, u'Paternal Grandmother'), (8, u'Paternal Grandfather'), (9, u'Maternal Aunt'), (10, u'Paternal Aunt'), (11, u'Maternal Uncle'), (12, u'Paternal Uncle'), (13, u'Maternal Cousin'), (14, u'Paternal Cousin')])
    hearingimpairment = models.ForeignKey(HearingImpairment)

    class Meta:
	 db_table = 'fhheterochromiapedi'


class earhelicaldetails(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Helical structure details', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Helical structure details', choices=[(1, u'Cupped'), (2, u'Thick helix'), (3, u'Hypoplastic'), (4, u'Darwinian tubercle'), (5, u'Prominent anti helix'), (6, u'Unknown/Not documented')])
    hearingimpairment = models.ForeignKey(HearingImpairment)

    class Meta:
	 db_table = 'earhelicaldetails'


class earhelicaldetailsr(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Right ear helical structure details', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Right ear helical structure details', choices=[(1, u'Cupped'), (2, u'Thick helix'), (3, u'Hypoplastic'), (4, u'Darwinian tubercle'), (5, u'Prominent anti helix'), (6, u'Unknown/Not documented')])
    hearingimpairment = models.ForeignKey(HearingImpairment)

    class Meta:
	 db_table = 'earhelicaldetailsr'


class Antibiotic(models.Model):
    antibiotics = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'antibiotic exposure', blank=True)
    hearingimpairment = models.ForeignKey(HearingImpairment)

    class Meta:
	 db_table = 'antibiotic'


class Infection(models.Model):
    infections = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'infection exposure', blank=True)
    hearingimpairment = models.ForeignKey(HearingImpairment)

    class Meta:
	 db_table = 'infection'


class OtherMedication(models.Model):
    other_meds = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'other medication exposure', blank=True)
    hearingimpairment = models.ForeignKey(HearingImpairment)

    class Meta:
	 db_table = 'othermedication'


class IntellectualDisability(models.Model):
    id_susp_age = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Age at which intellectual disability was first suspected? (months)', blank=True)
    developpeds_eval = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Evaluated by developmental pediatrician?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    modified_checklist_for_autism_in_toddlers_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Modified Checklist for Autism in Toddlers results', blank=True) # This field type is a guess
    early_screening_of_autistic_traits_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Early Screening of Autistic Traits Questionnaire results', blank=True) # This field type is a guess
    first_year_inventory_spec = models.TextField(help_text=u'', null=True, verbose_name=u'First Year Inventory results', blank=True) # This field type is a guess
    adi_r_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Autism Diagnostic Interview-Revised (ADI-R) results', blank=True) # This field type is a guess
    ados_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Autism Diagnostic Observation Schedule (ADOS) results', blank=True) # This field type is a guess
    cars_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Childhood Autism Rating Scale (CARS) results', blank=True) # This field type is a guess
    aberrant_behavior_checklist_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Aberrant Behavior Checklist results', blank=True) # This field type is a guess
    social_communication_questionnaire_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Social Communication Questionnaire results', blank=True) # This field type is a guess
    vinelandii_adaptive_behavior_scale_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Vineland-II Adaptive Behavior Scale results', blank=True) # This field type is a guess
    pls4_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Preschool Language Scales-4 (PLS4) results', blank=True) # This field type is a guess
    vmi_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Beery Test of Visual Motor Integration (VMI) results', blank=True) # This field type is a guess
    kaufman_brief_intelligence_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Kaufman Brief Intelligence results', blank=True) # This field type is a guess
    other = models.TextField(help_text=u'', null=True, verbose_name=u'Describe other developmental screening tests and results', blank=True) # This field type is a guess
    autism_diagnosis = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Autism diagnosis?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    autism_diagnoser = models.IntegerField(help_text=u'', null=True, verbose_name=u'Who made diagnosis of autism? | Please specify which type of clinician made the autism diagnosis', blank=True, choices=[(1, u'Pediatrician'), (2, u'Developmental Pediatrician'), (3, u'Neurologist'), (5, u'Unknown/Not documented'), (4, u'Other')]) # This field type is a guess
    age_autism_diagnosis = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Age at autism diagnosis (years)', blank=True)
    autism_symptoms_social_inter = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Qualitative impairment in social interaction', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    autism_symptoms_eye_contact = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Poor eye contact', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    autism_symptoms_comm = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Qualitative impairment in communication ', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    autism_symptoms_rep_beh = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Restricted and repetitive behavior ', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    autism_symptoms_recip = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Lack of social or emotional reciprocity', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    autism_symptoms_rep_lang = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Stereotyped and repetitive use of language or idiosyncratic use of language', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    autism_symptoms_preocc = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Persistent preoccupation with parts of objects', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    autism_symptoms_comp_beh = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Compulsive behavior', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    autism_symptoms_sama = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Samaness (resistance to change)', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    autism_symptoms_ritual_beh = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Ritualistic behavior', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    autism_symptoms_self_inj = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Self injury', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    autism_symptoms_attn_def = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Attention deficit/poor attention', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    autism_symptoms_agg_beh = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Aggressive Behavior', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    autism_symptoms_spec = models.IntegerField(help_text=u'', null=True, verbose_name=u'Specify other autism symptoms', blank=True, choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')]) # This field type is a guess
    id_diagnoser = models.IntegerField(help_text=u'', null=True, verbose_name=u'Who made the diagnosis of intellectual disability? | Please specify which type of clinician made the intellectual disability diagnosis', blank=True, choices=[(1, u'Pediatrician'), (2, u'Developmental pediatrician'), (3, u'Neurologist'), (5, u'Unknown/Not documented'), (4, u'Other')]) # This field type is a guess
    dev_milestone_smile_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Smile', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    dev_milestone_smile_months = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Age first smiled (months)', blank=True)
    dev_milestone_roll_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Roll over', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    dev_milestone_roll_months = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Age first rolled over (months)', blank=True)
    dev_milestone_grasp_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Grasp object', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    dev_milestone_grasp_months = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Age first grasped object (months)', blank=True)
    dev_milestone_reach_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Reach for object', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    dev_milestone_reach_months = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Age reached for object (months)', blank=True)
    dev_milestone_crawl_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Crawl', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    dev_milestone_crawl_months = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Age first crawled (months)', blank=True)
    dev_milestone_hand_transfer_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Hand to hand transfer', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    dev_milestone_hand_transfer_months = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Age first hand to hand transfer (months)', blank=True)
    dev_milestone_feed_self_crackers_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Feed self crackers', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    dev_milestone_feed_self_crackers_months = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Age first fed self crackers (months)', blank=True)
    dev_milestone_pincer_grasp_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Pincer grasp', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    dev_milestone_pincer_grasp_months = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Age first pincer grasp (months)', blank=True)
    dev_milestone_words_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Words (mama/dada)', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    dev_milestone_words_months = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Age of first words (months)', blank=True)
    dev_milestone_stranger_anxiety_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Stranger anxiety', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    dev_milestone_stranger_anxiety_months = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Age first showed stranger anxiety (months)', blank=True)
    dev_milestone_stand_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Stand', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    dev_milestone_stand_months = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Age first stood (months)', blank=True)
    dev_milestone_drink_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Drink from cup', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    dev_milestone_drink_months = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Age first drank from cup(months)', blank=True)
    dev_milestone_remove_clothes_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Removes clothes', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    dev_milestone_remove_clothes_months = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Age first removed clothes (months)', blank=True)
    dev_milestone_stairs_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Climbs stairs', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    dev_milestone_stairs_months = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Age climbed stairs (months)', blank=True)
    dev_milestone_combine_words_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Combine words', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    dev_milestone_combine_words_months = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Age first combined words (months)', blank=True)
    dev_milestone_plurals_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Uses plurals', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    dev_milestone_plurals_months = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Age used plurals (months)', blank=True)
    dev_milestone_tricycle_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Pedals tricycle', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    dev_milestone_tricycle_months = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Age pedaled tricycle (months)', blank=True)
    dev_milestone_copy_circle_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Copy circle', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    dev_milestone_copy_circle_months = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Age first copied circle (months)', blank=True)
    dev_milestone_dress_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Dress self', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    dev_milestone_dress_months = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Age first dressed self (months)', blank=True)
    dev_milestone_balance_one_foot_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Balance one foot', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    dev_milestone_balance_one_foot_months = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Age first balanced on one foot (months)', blank=True)
    dev_milestone_square_bool = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Draws square', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    dev_milestone_square_months = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Age first drew square (months)', blank=True)
    mother_symptoms = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Does mother have similar symptoms of autism or intellectual disability?  (specify yes even if less severe)', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    maternal_fam_hist = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Maternal family history of autism or intellectual disability?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    brothers_symptoms = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Brothers with similar conditions?', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    behavior_disorders = models.IntegerField(help_text=u'', null=True, verbose_name=u'Behavior disorders', blank=True, choices=[(3, u'None'), (1, u'ADHD'), (2, u'Hyperactivity'), (5, u'Unknown/Not documented'), (4, u'Other')]) # This field type is a guess
    intellectual_disability_feedback = models.TextField(help_text=u'', null=True, verbose_name=u'Please provide any feedback for this form (for example: missing questions, questions not relevant for a disease area, ambiguities, places where a textbox could be replaced with discrete choices, missing discrete choices)', blank=True) # This field type is a guess
    developmental_screening_details_summary = models.CharField(help_text=u'14, None | 1, Modified Checklist for Autism in Toddlers | 2, Early Screening of Autistic Traits Questionnaire | 3, First Year Inventory | 4, Autism Diagnostic Interview-Revised (ADI-R) | 5, Autism Diagnostic Observation Schedule (ADOS) | 6, Childhood Autism Rating Scale (CARS) | 7, Aberrant Behavior Checklist | 8, Social Communication Questionnaire | 9, Vineland-II Adaptive Behavior Scale | 10, Preschool Language Scales-4 (PLS4) | 11, Beery Test of Visual Motor Integration (VMI) | 12, Kaufman Brief Intelligence | 15, Unknown/Not documented | 13, Other', null=True, max_length=2000, verbose_name=u'Developmental screening tests employed', blank=True)
    subj_weakness_summary = models.CharField(help_text=u'3, None | 1, Math | 2, Reading | 5, Unknown/Not documented | 4, Other', null=True, max_length=2000, verbose_name=u'Weakness in any particular subject matters?', blank=True)
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'intellectualdisability'


class developmentalscreeningdetails(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Developmental screening tests employed', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Developmental screening tests employed', choices=[(14, u'None'), (1, u'Modified Checklist for Autism in Toddlers'), (2, u'Early Screening of Autistic Traits Questionnaire'), (3, u'First Year Inventory'), (4, u'Autism Diagnostic Interview-Revised (ADI-R)'), (5, u'Autism Diagnostic Observation Schedule (ADOS)'), (6, u'Childhood Autism Rating Scale (CARS)'), (7, u'Aberrant Behavior Checklist'), (8, u'Social Communication Questionnaire'), (9, u'Vineland-II Adaptive Behavior Scale'), (10, u'Preschool Language Scales-4 (PLS4)'), (11, u'Beery Test of Visual Motor Integration (VMI)'), (12, u'Kaufman Brief Intelligence'), (15, u'Unknown/Not documented'), (13, u'Other')])
    intellectualdisability = models.ForeignKey(IntellectualDisability)

    class Meta:
	 db_table = 'developmentalscreeningdetails'


class subjweakness(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Weakness in any particular subject matters?', blank=True)
    value = models.IntegerField(help_text=u'', null=True, verbose_name=u'Weakness in any particular subject matters?', blank=True, choices=[(3, u'None'), (1, u'Math'), (2, u'Reading'), (5, u'Unknown/Not documented'), (4, u'Other')]) # This field type is a guess
    intellectualdisability = models.ForeignKey(IntellectualDisability)

    class Meta:
	 db_table = 'subjweakness'


class CardiacDiagnosi(models.Model):
    cardiac_presumed_dx = models.TextField(help_text=u'', null=True, verbose_name=u"Subject's presumed diagnosis", blank=True) # This field type is a guess
    cardiac_date_presumed_dx = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Date of presumed diagnosis (MM/YY)', blank=True)
    cardiac_reason_presumed_dx_oth = models.TextField(help_text=u'', null=True, verbose_name=u'Reason for consideration of presumed diagnosis/Other: Specify', blank=True) # This field type is a guess
    cardiac_reason_presumed_sym_other_dx = models.TextField(help_text=u'', null=True, verbose_name=u'Symptoms Other: Specify', blank=True) # This field type is a guess
    cardiac_date_confirmed_dx = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Date of Confirmed Diagnosis', blank=True)
    cardiac_method_confirm_oth_dx = models.TextField(help_text=u'', null=True, verbose_name=u'Method of confirmation of diagnosis/Other: Specify', blank=True) # This field type is a guess
    cardiac_method_confirm_sym_oth_dx = models.TextField(help_text=u'', null=True, verbose_name=u'Symptoms Other: Specify', blank=True) # This field type is a guess
    cardiac_sca_event = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Subject has had a prior sudden cardiac arrest (SCA) and survived.', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    cardiac_sca_age_event = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Age at the time of Sudden Cardiac Arrest', blank=True)
    cardiac_sca_event_description = models.TextField(help_text=u'', null=True, verbose_name=u'Describe the SCA event', blank=True) # This field type is a guess
    cardiac_chd_dx_other = models.TextField(help_text=u'', null=True, verbose_name=u'CHD Diagnosis (not listed)', blank=True) # This field type is a guess
    cardiac_ep_dx_other = models.TextField(help_text=u'', null=True, verbose_name=u'EP Diagnosis (not listed)', blank=True) # This field type is a guess
    card_tx_oth = models.TextField(help_text=u'', null=True, verbose_name=u'Cardiac treatment procedures/Other: Specify', blank=True) # This field type is a guess
    cardiac_reason_presumed_dx_summary = models.CharField(help_text=u'13, None | 1, Personal history | 2, Family history | 3, Clinical history | 4, Physical exam | 5, ECG | 6, ECHO | 7, Genetic test | 8, EST | 9, Holter Monitor | 10, Transtelephonic Monitoring (TTM) | 11, Electrophysiologic Studies | 12, Other', null=True, max_length=2000, verbose_name=u'Reason for consideration of presumed diagnosis ', blank=True)
    cardiac_reason_presumed_symptoms_dx_summary = models.CharField(help_text=u'1, None | 2, Syncope/fainted | 3, Chest discomfort/pain/pressure | 4, Racing heart beat/tachycardia | 5, Slow heart rate/bradycardia | 6, Skipped heart beat/palpatations | 7, Dizziness/lightheadedness/nearly fainted | 8, Shortness of breath (not asthma-related) | 9, Unexplained seizure/convulsion | 10, Easy fatigability | 11, Torsades de pointes | 12, Aborted Sudden Cardiac Arrest (ASA) | 13, Hearing Loss | 14, Other', null=True, max_length=2000, verbose_name=u'Symptoms described in personal/clinical history', blank=True)
    cardiac_method_confirmed_dx_summary = models.CharField(help_text=u'13, None | 1, Personal history | 2, Family history | 3, Clinical history | 4, Physical exam | 5, ECG | 6, ECHO | 7, Genetic test | 8, EST | 9, Holter Monitor | 10, Transtelephonic Monitoring (TTM) | 11, Electrophysiologic Studies | 12, Other', null=True, max_length=2000, verbose_name=u'Method of confirmation of diagnosis.  Check all that apply.', blank=True)
    cardiac_method_confirm_symptom_dx_summary = models.CharField(help_text=u'1, None | 2, Syncope/fainted | 3, Chest discomfort/pain/pressure | 4, Racing heart beat/tachycardia | 5, Slow heart rate/bradycardia | 6, Skipped heart beat/palpatations | 7, Dizziness/lightheadedness/nearly fainted | 8, Shortness of breath (not asthma-related) | 9, Unexplained seizure/convulsion | 10, Easy fatigability | 11, Torsades de pointes | 12, Aborted Sudden Cardiac Arrest (ASA) | 13, Hearing Loss | 14, Other', null=True, max_length=2000, verbose_name=u'Additional symptoms described in personal/clinical history (since diagnosis was confirmed).', blank=True)
    cardiac_chd_dx_confirmed_summary = models.CharField(help_text=u"1, None | 2, Anomalous Coronary Artery | 3, Aortic Valve Stenosis | 4, Arrhythmogenic right ventricular dysplasia (ARVD) | 5, Atrial Septal Defect (ASD) | 6, Atrioventricular Septal Defect (AVSD) | 7, Bicuspid Aortic Valve (BAV) | 8, Coarctation of the Aorta (CoA) | 9, Complete Atrioventricular Canal defect (CAVC) | 10, Dextrocardia | 11, Dialated Aortic Root | 12, Dilated Cardiomyopathy (DCM) | 13, Double Inlet Left Ventricle (DILV) | 14, Double Outlet Right Ventricle (DORV) | 15, Ebstein's Anomaly | 16, Heterotaxy Syndrome | 17, Hypertrophic Cardiomyopathy (HCM) | 18, Hypoplastic Left Heart Syndrome (HLHS) | 19, Hypoplastic Right Heart Syndrome (HRHS) | 20, Interrupted Aortic Arch (IAA) | 21, Left ventricular non-compaction (LVNC) | 22, Marfan Syndrome | 23, Mitral Stenosis | 24, Mitral Valve Prolapse (MVP) | 25, Myocarditis | 26, Patent Ductus Arteriosis (PDA) | 27, Patent Foramen Ovale (PFO) | 28, Pericarditis | 29, Pulmonary Atresia | 30, Pulmonary Hypertension (PHT) | 31, Pulmonary Valve Stenosis | 32, Restrictive cardiomyopathy (RCM) | 33, Single Ventricle Defects | 34, Scimitar Syndrome (SS) | 35, Partial Anomalous Pulmonary Venous Connection (PAPVC) | 36, Total Anomalous Pulmonary Venous Connection (TAPVC) | 37, Shone's Syndrome/Shone's Complex/Shone's Anomaly | 38, Tetralogy of Fallot (ToF) | 39, Transposition of the Great Arteries (TGA) | 40, dextro-Transposition of the Great Arteries (d-TGA) | 41, levo-Transposition of the Great Arteries (l-TGA) | 42, Tricuspid Atresia | 43, Truncus Arteriosus | 44, Ventricular Septal Defect (VSD) | 45, Other", null=True, max_length=2000, verbose_name=u'Congenital/Acquired heart defect diagnosis (Confirmed) | Other congenital/acquired heart defect diagnosis (Confirmed) ', blank=True)
    cardiac_ep_dx_confirmed_summary = models.CharField(help_text=u'1, None | 2, Atrial Fibrillation (A-Fib) | 3, Atrial Flutter | 4, Bradycardia | 5, Brugada Syndrome | 6, Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT) | 7, Chaotic Atrial Tachycardia | 8, Ectopic Atrial Tachycardia (EAT) | 9, First Degree AV Block | 10, Second Degree AV Block (Mobitz Type I Wenckebach) | 11, Second Degree AV Block (Mobitz Type II) | 12, Third Degree (or Complete) AV Block | 13,  Junctional Ectopic Tachycardia (JET) | 14, Long QT Syndrome (LQTS) | 15, Multifocal Atrial Tachycardia | 16, Premature Atrial Complexes (PAC) | 17, Premature Junctional Complexes (PJC) | 18, Premature Ventricular Complexes (PVC) | 19, Right bundle branch block (RBBB) | 20, Left bundle branch block (LBBB) | 21, Left Anterior Hemiblock | 22, Left Posterior Hemiblock | 23, Right ventricular conduction delay-RVCD (IRBBB) | 24, Intraventricular conduction delay-IVCD (nonspecific) | 25, Short QT Syndrome (SQTS) | 26, Supraventricular Tachycardia (SVT) | 27, Torsades de pointes | 28, Ventricular Fibrillation (V-Fib) | 29, Ventricular Flutter | 30, Ventricular Tachycardia (VT) | 31, Wolff-Parkinson-White Syndrome (WPW) | 32, Other', null=True, max_length=2000, verbose_name=u'Electrocardiographic diagnosis (Confirmed) | Other electrocardiographic diagnosis (Confirmed)', blank=True)
    card_tx_proc_summary = models.CharField(help_text=u'1, None | 2, Catheter Ablation | 3, Electrophysiologic Studies | 4, Implantable Cardioverter-Defibrillator | 5, Pacemaker | 6, Left cervical sympathetic denervation | 7, Other', null=True, max_length=2000, verbose_name=u'Cardiac treatment procedures done', blank=True)
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'cardiacdiagnosi'


class cardiacreasonpresumeddx(models.Model):
    label = models.CharField(help_text=u'Check all that apply.', null=True, max_length=2000, verbose_name=u'Reason for consideration of presumed diagnosis ', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'Check all that apply.', null=True, verbose_name=u'Reason for consideration of presumed diagnosis ', choices=[(13, u'None'), (1, u'Personal history'), (2, u'Family history'), (3, u'Clinical history'), (4, u'Physical exam'), (5, u'ECG'), (6, u'ECHO'), (7, u'Genetic test'), (8, u'EST'), (9, u'Holter Monitor'), (10, u'Transtelephonic Monitoring (TTM)'), (11, u'Electrophysiologic Studies'), (12, u'Other')])
    cardiacdiagnosi = models.ForeignKey(CardiacDiagnosi)

    class Meta:
	 db_table = 'cardiacreasonpresumeddx'


class cardiacreasonpresumedsymptomsdx(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Symptoms described in personal/clinical history', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Symptoms described in personal/clinical history', choices=[(1, u'None'), (2, u'Syncope/fainted'), (3, u'Chest discomfort/pain/pressure'), (4, u'Racing heart beat/tachycardia'), (5, u'Slow heart rate/bradycardia'), (6, u'Skipped heart beat/palpatations'), (7, u'Dizziness/lightheadedness/nearly fainted'), (8, u'Shortness of breath (not asthma-related)'), (9, u'Unexplained seizure/convulsion'), (10, u'Easy fatigability'), (11, u'Torsades de pointes'), (12, u'Aborted Sudden Cardiac Arrest (ASA)'), (13, u'Hearing Loss'), (14, u'Other')])
    cardiacdiagnosi = models.ForeignKey(CardiacDiagnosi)

    class Meta:
	 db_table = 'cardiacreasonpresumedsymptomsdx'


class cardiacmethodconfirmeddx(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Method of confirmation of diagnosis.  Check all that apply.', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Method of confirmation of diagnosis.  Check all that apply.', choices=[(13, u'None'), (1, u'Personal history'), (2, u'Family history'), (3, u'Clinical history'), (4, u'Physical exam'), (5, u'ECG'), (6, u'ECHO'), (7, u'Genetic test'), (8, u'EST'), (9, u'Holter Monitor'), (10, u'Transtelephonic Monitoring (TTM)'), (11, u'Electrophysiologic Studies'), (12, u'Other')])
    cardiacdiagnosi = models.ForeignKey(CardiacDiagnosi)

    class Meta:
	 db_table = 'cardiacmethodconfirmeddx'


class cardiacmethodconfirmsymptomdx(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Additional symptoms described in personal/clinical history (since diagnosis was confirmed).', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Additional symptoms described in personal/clinical history (since diagnosis was confirmed).', choices=[(1, u'None'), (2, u'Syncope/fainted'), (3, u'Chest discomfort/pain/pressure'), (4, u'Racing heart beat/tachycardia'), (5, u'Slow heart rate/bradycardia'), (6, u'Skipped heart beat/palpatations'), (7, u'Dizziness/lightheadedness/nearly fainted'), (8, u'Shortness of breath (not asthma-related)'), (9, u'Unexplained seizure/convulsion'), (10, u'Easy fatigability'), (11, u'Torsades de pointes'), (12, u'Aborted Sudden Cardiac Arrest (ASA)'), (13, u'Hearing Loss'), (14, u'Other')])
    cardiacdiagnosi = models.ForeignKey(CardiacDiagnosi)

    class Meta:
	 db_table = 'cardiacmethodconfirmsymptomdx'


class cardiacchddxconfirmed(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Congenital/Acquired heart defect diagnosis (Confirmed) | Other congenital/acquired heart defect diagnosis (Confirmed) ', blank=True)
    value = models.IntegerField(help_text=u'', null=True, verbose_name=u'Congenital/Acquired heart defect diagnosis (Confirmed) | Other congenital/acquired heart defect diagnosis (Confirmed) ', blank=True, choices=[(1, u'None'), (2, u'Anomalous Coronary Artery'), (3, u'Aortic Valve Stenosis'), (4, u'Arrhythmogenic right ventricular dysplasia (ARVD)'), (5, u'Atrial Septal Defect (ASD)'), (6, u'Atrioventricular Septal Defect (AVSD)'), (7, u'Bicuspid Aortic Valve (BAV)'), (8, u'Coarctation of the Aorta (CoA)'), (9, u'Complete Atrioventricular Canal defect (CAVC)'), (10, u'Dextrocardia'), (11, u'Dialated Aortic Root'), (12, u'Dilated Cardiomyopathy (DCM)'), (13, u'Double Inlet Left Ventricle (DILV)'), (14, u'Double Outlet Right Ventricle (DORV)'), (15, u"Ebstein's Anomaly"), (16, u'Heterotaxy Syndrome'), (17, u'Hypertrophic Cardiomyopathy (HCM)'), (18, u'Hypoplastic Left Heart Syndrome (HLHS)'), (19, u'Hypoplastic Right Heart Syndrome (HRHS)'), (20, u'Interrupted Aortic Arch (IAA)'), (21, u'Left ventricular non-compaction (LVNC)'), (22, u'Marfan Syndrome'), (23, u'Mitral Stenosis'), (24, u'Mitral Valve Prolapse (MVP)'), (25, u'Myocarditis'), (26, u'Patent Ductus Arteriosis (PDA)'), (27, u'Patent Foramen Ovale (PFO)'), (28, u'Pericarditis'), (29, u'Pulmonary Atresia'), (30, u'Pulmonary Hypertension (PHT)'), (31, u'Pulmonary Valve Stenosis'), (32, u'Restrictive cardiomyopathy (RCM)'), (33, u'Single Ventricle Defects'), (34, u'Scimitar Syndrome (SS)'), (35, u'Partial Anomalous Pulmonary Venous Connection (PAPVC)'), (36, u'Total Anomalous Pulmonary Venous Connection (TAPVC)'), (37, u"Shone's Syndrome/Shone's Complex/Shone's Anomaly"), (38, u'Tetralogy of Fallot (ToF)'), (39, u'Transposition of the Great Arteries (TGA)'), (40, u'dextro-Transposition of the Great Arteries (d-TGA)'), (41, u'levo-Transposition of the Great Arteries (l-TGA)'), (42, u'Tricuspid Atresia'), (43, u'Truncus Arteriosus'), (44, u'Ventricular Septal Defect (VSD)'), (45, u'Other')]) # This field type is a guess
    cardiacdiagnosi = models.ForeignKey(CardiacDiagnosi)

    class Meta:
	 db_table = 'cardiacchddxconfirmed'


class cardiacepdxconfirmed(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Electrocardiographic diagnosis (Confirmed) | Other electrocardiographic diagnosis (Confirmed)', blank=True)
    value = models.IntegerField(help_text=u'', null=True, verbose_name=u'Electrocardiographic diagnosis (Confirmed) | Other electrocardiographic diagnosis (Confirmed)', blank=True, choices=[(1, u'None'), (2, u'Atrial Fibrillation (A-Fib)'), (3, u'Atrial Flutter'), (4, u'Bradycardia'), (5, u'Brugada Syndrome'), (6, u'Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT)'), (7, u'Chaotic Atrial Tachycardia'), (8, u'Ectopic Atrial Tachycardia (EAT)'), (9, u'First Degree AV Block'), (10, u'Second Degree AV Block (Mobitz Type I Wenckebach)'), (11, u'Second Degree AV Block (Mobitz Type II)'), (12, u'Third Degree (or Complete) AV Block'), (13, u'Junctional Ectopic Tachycardia (JET)'), (14, u'Long QT Syndrome (LQTS)'), (15, u'Multifocal Atrial Tachycardia'), (16, u'Premature Atrial Complexes (PAC)'), (17, u'Premature Junctional Complexes (PJC)'), (18, u'Premature Ventricular Complexes (PVC)'), (19, u'Right bundle branch block (RBBB)'), (20, u'Left bundle branch block (LBBB)'), (21, u'Left Anterior Hemiblock'), (22, u'Left Posterior Hemiblock'), (23, u'Right ventricular conduction delay-RVCD (IRBBB)'), (24, u'Intraventricular conduction delay-IVCD (nonspecific)'), (25, u'Short QT Syndrome (SQTS)'), (26, u'Supraventricular Tachycardia (SVT)'), (27, u'Torsades de pointes'), (28, u'Ventricular Fibrillation (V-Fib)'), (29, u'Ventricular Flutter'), (30, u'Ventricular Tachycardia (VT)'), (31, u'Wolff-Parkinson-White Syndrome (WPW)'), (32, u'Other')]) # This field type is a guess
    cardiacdiagnosi = models.ForeignKey(CardiacDiagnosi)

    class Meta:
	 db_table = 'cardiacepdxconfirmed'


class cardtxproc(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Cardiac treatment procedures done', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Cardiac treatment procedures done', choices=[(1, u'None'), (2, u'Catheter Ablation'), (3, u'Electrophysiologic Studies'), (4, u'Implantable Cardioverter-Defibrillator'), (5, u'Pacemaker'), (6, u'Left cervical sympathetic denervation'), (7, u'Other')])
    cardiacdiagnosi = models.ForeignKey(CardiacDiagnosi)

    class Meta:
	 db_table = 'cardtxproc'


class CardiacMedication(models.Model):
    card_meds = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'cardiac medication', blank=True)
    cardiacdiagnosi = models.ForeignKey(CardiacDiagnosi)

    class Meta:
	 db_table = 'cardiacmedication'


class CardiacFamilyHistory(models.Model):
    cfhx_died_sids = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Any blood relative who died with SIDS / SUID (Sudden Infant Death Syndrome / Sudden Unexpected Infant Death).', choices=[(1, u'None'), (2, u'Mother'), (3, u'Father'), (4, u'Sister'), (5, u'Brother'), (6, u'Maternal Grandmother'), (7, u'Maternal Grandfather'), (8, u'Paternal Grandmother'), (9, u'Paternal Grandfather'), (10, u'Maternal Aunt'), (11, u'Paternal Aunt'), (12, u'Maternal Uncle'), (13, u'Paternal Uncle'), (14, u'Maternal Cousin'), (15, u'Paternal Cousin'), (16, u'Other')])
    cfhx_hcm = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Any blood relatives with Hypertrophic cardiomyopathy (HCM)', choices=[(1, u'None'), (2, u'Mother'), (3, u'Father'), (4, u'Sister'), (5, u'Brother'), (6, u'Maternal Grandmother'), (7, u'Maternal Grandfather'), (8, u'Paternal Grandmother'), (9, u'Paternal Grandfather'), (10, u'Maternal Aunt'), (11, u'Paternal Aunt'), (12, u'Maternal Uncle'), (13, u'Paternal Uncle'), (14, u'Maternal Cousin'), (15, u'Paternal Cousin'), (16, u'Other')])
    cfhx_rcm = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Any blood relatives with Restrictive cardiomyopathy (RCM)', choices=[(1, u'None'), (2, u'Mother'), (3, u'Father'), (4, u'Sister'), (5, u'Brother'), (6, u'Maternal Grandmother'), (7, u'Maternal Grandfather'), (8, u'Paternal Grandmother'), (9, u'Paternal Grandfather'), (10, u'Maternal Aunt'), (11, u'Paternal Aunt'), (12, u'Maternal Uncle'), (13, u'Paternal Uncle'), (14, u'Maternal Cousin'), (15, u'Paternal Cousin'), (16, u'Other')])
    cfhx_lqts = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Any blood relatives with Long QT syndrome (LQTS)', choices=[(1, u'None'), (2, u'Mother'), (3, u'Father'), (4, u'Sister'), (5, u'Brother'), (6, u'Maternal Grandmother'), (7, u'Maternal Grandfather'), (8, u'Paternal Grandmother'), (9, u'Paternal Grandfather'), (10, u'Maternal Aunt'), (11, u'Paternal Aunt'), (12, u'Maternal Uncle'), (13, u'Paternal Uncle'), (14, u'Maternal Cousin'), (15, u'Paternal Cousin'), (16, u'Other')])
    cfhx_brugada = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Any blood relatives with Brugada syndrome', choices=[(1, u'None'), (2, u'Mother'), (3, u'Father'), (4, u'Sister'), (5, u'Brother'), (6, u'Maternal Grandmother'), (7, u'Maternal Grandfather'), (8, u'Paternal Grandmother'), (9, u'Paternal Grandfather'), (10, u'Maternal Aunt'), (11, u'Paternal Aunt'), (12, u'Maternal Uncle'), (13, u'Paternal Uncle'), (14, u'Maternal Cousin'), (15, u'Paternal Cousin'), (16, u'Other')])
    cfhx_wpw = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Any blood relatives with WPW-Wolff-Parkinson-White', choices=[(1, u'None'), (2, u'Mother'), (3, u'Father'), (4, u'Sister'), (5, u'Brother'), (6, u'Maternal Grandmother'), (7, u'Maternal Grandfather'), (8, u'Paternal Grandmother'), (9, u'Paternal Grandfather'), (10, u'Maternal Aunt'), (11, u'Paternal Aunt'), (12, u'Maternal Uncle'), (13, u'Paternal Uncle'), (14, u'Maternal Cousin'), (15, u'Paternal Cousin'), (16, u'Other')])
    cfhx_pace_icd = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Any blood relatives with Pacemaker or implanted defibrillator (ICD)', choices=[(1, u'None'), (2, u'Mother'), (3, u'Father'), (4, u'Sister'), (5, u'Brother'), (6, u'Maternal Grandmother'), (7, u'Maternal Grandfather'), (8, u'Paternal Grandmother'), (9, u'Paternal Grandfather'), (10, u'Maternal Aunt'), (11, u'Paternal Aunt'), (12, u'Maternal Uncle'), (13, u'Paternal Uncle'), (14, u'Maternal Cousin'), (15, u'Paternal Cousin'), (16, u'Other')])
    cfhx_faint = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Any blood relatives with Unexplained fainting or passing out', choices=[(1, u'None'), (2, u'Mother'), (3, u'Father'), (4, u'Sister'), (5, u'Brother'), (6, u'Maternal Grandmother'), (7, u'Maternal Grandfather'), (8, u'Paternal Grandmother'), (9, u'Paternal Grandfather'), (10, u'Maternal Aunt'), (11, u'Paternal Aunt'), (12, u'Maternal Uncle'), (13, u'Paternal Uncle'), (14, u'Maternal Cousin'), (15, u'Paternal Cousin'), (16, u'Other')])
    cfhx_drowning = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Any blood relatives with Near drowning', choices=[(1, u'None'), (2, u'Mother'), (3, u'Father'), (4, u'Sister'), (5, u'Brother'), (6, u'Maternal Grandmother'), (7, u'Maternal Grandfather'), (8, u'Paternal Grandmother'), (9, u'Paternal Grandfather'), (10, u'Maternal Aunt'), (11, u'Paternal Aunt'), (12, u'Maternal Uncle'), (13, u'Paternal Uncle'), (14, u'Maternal Cousin'), (15, u'Paternal Cousin'), (16, u'Other')])
    cfhx_diabetes = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Any blood relatives with Diabetes', choices=[(1, u'None'), (2, u'Mother'), (3, u'Father'), (4, u'Sister'), (5, u'Brother'), (6, u'Maternal Grandmother'), (7, u'Maternal Grandfather'), (8, u'Paternal Grandmother'), (9, u'Paternal Grandfather'), (10, u'Maternal Aunt'), (11, u'Paternal Aunt'), (12, u'Maternal Uncle'), (13, u'Paternal Uncle'), (14, u'Maternal Cousin'), (15, u'Paternal Cousin'), (16, u'Other')])
    cfhx_explanation = models.TextField(help_text=u'', null=True, verbose_name=u'Explain the cardiac family history stated above', blank=True) # This field type is a guess
    cfhx_died_scd_summary = models.CharField(help_text=u'1, None | 2, Mother | 3, Father | 4, Sister | 5, Brother | 6, Maternal Grandmother | 7, Maternal Grandfather | 8, Paternal Grandmother | 9, Paternal Grandfather | 10, Maternal Aunt | 11, Paternal Aunt | 12, Maternal Uncle | 13, Paternal Uncle | 14, Maternal Cousin | 15, Paternal Cousin | 16, Other', null=True, max_length=2000, verbose_name=u'Any blood relative who died of heart problems or had an unexpected or unexplained sudden death (including drowning or unexplained car accident) before age 50.', blank=True)
    cfhx_survive_sca_summary = models.CharField(help_text=u'1, None | 2, Mother | 3, Father | 4, Sister | 5, Brother | 6, Maternal Grandmother | 7, Maternal Grandfather | 8, Paternal Grandmother | 9, Paternal Grandfather | 10, Maternal Aunt | 11, Paternal Aunt | 12, Maternal Uncle | 13, Paternal Uncle | 14, Maternal Cousin | 15, Paternal Cousin | 16, Other', null=True, max_length=2000, verbose_name=u'Any blood relative experienced a sudden cardiac arrest (SCA) before age 50 and survived.', blank=True)
    cfhx_dcm_summary = models.CharField(help_text=u'1, None | 2, Mother | 3, Father | 4, Sister | 5, Brother | 6, Maternal Grandmother | 7, Maternal Grandfather | 8, Paternal Grandmother | 9, Paternal Grandfather | 10, Maternal Aunt | 11, Paternal Aunt | 12, Maternal Uncle | 13, Paternal Uncle | 14, Maternal Cousin | 15, Paternal Cousin | 16, Other', null=True, max_length=2000, verbose_name=u'Any blood relatives with Dilated cardiomyopathy (DCM) or Dilated Left or Right Ventricle', blank=True)
    cfhx_arvc_summary = models.CharField(help_text=u'1, None | 2, Mother | 3, Father | 4, Sister | 5, Brother | 6, Maternal Grandmother | 7, Maternal Grandfather | 8, Paternal Grandmother | 9, Paternal Grandfather | 10, Maternal Aunt | 11, Paternal Aunt | 12, Maternal Uncle | 13, Paternal Uncle | 14, Maternal Cousin | 15, Paternal Cousin | 16, Other', null=True, max_length=2000, verbose_name=u'Any blood relatives with ARVC (Arrhythmogenic right ventricular cardiomyopathy)', blank=True)
    cfhx_sqts_summary = models.CharField(help_text=u'1, None | 2, Mother | 3, Father | 4, Sister | 5, Brother | 6, Maternal Grandmother | 7, Maternal Grandfather | 8, Paternal Grandmother | 9, Paternal Grandfather | 10, Maternal Aunt | 11, Paternal Aunt | 12, Maternal Uncle | 13, Paternal Uncle | 14, Maternal Cousin | 15, Paternal Cousin | 16, Other', null=True, max_length=2000, verbose_name=u'Any blood relatives with Short QT syndrome (SQTS)', blank=True)
    cfhx_cptv_summary = models.CharField(help_text=u'1, None | 2, Mother | 3, Father | 4, Sister | 5, Brother | 6, Maternal Grandmother | 7, Maternal Grandfather | 8, Paternal Grandmother | 9, Paternal Grandfather | 10, Maternal Aunt | 11, Paternal Aunt | 12, Maternal Uncle | 13, Paternal Uncle | 14, Maternal Cousin | 15, Paternal Cousin | 16, Other', null=True, max_length=2000, verbose_name=u'Any blood relatives with CPVT-Catecholaminergic polymorphic ventricular tachycardia', blank=True)
    cfhx_marfan_summary = models.CharField(help_text=u'1, None | 2, Mother | 3, Father | 4, Sister | 5, Brother | 6, Maternal Grandmother | 7, Maternal Grandfather | 8, Paternal Grandmother | 9, Paternal Grandfather | 10, Maternal Aunt | 11, Paternal Aunt | 12, Maternal Uncle | 13, Paternal Uncle | 14, Maternal Cousin | 15, Paternal Cousin | 16, Other', null=True, max_length=2000, verbose_name=u'Any blood relatives with Marfan syndrome (aortic rupture / dissection)', blank=True)
    cfhx_cad_mi_summary = models.CharField(help_text=u'1, None | 2, Mother | 3, Father | 4, Sister | 5, Brother | 6, Maternal Grandmother | 7, Maternal Grandfather | 8, Paternal Grandmother | 9, Paternal Grandfather | 10, Maternal Aunt | 11, Paternal Aunt | 12, Maternal Uncle | 13, Paternal Uncle | 14, Maternal Cousin | 15, Paternal Cousin | 16, Other', null=True, max_length=2000, verbose_name=u'Any blood relatives with Coronary artery disease with Myocardial Infarction (MI / Heart attack)', blank=True)
    cfhx_seizure_summary = models.CharField(help_text=u'1, None | 2, Mother | 3, Father | 4, Sister | 5, Brother | 6, Maternal Grandmother | 7, Maternal Grandfather | 8, Paternal Grandmother | 9, Paternal Grandfather | 10, Maternal Aunt | 11, Paternal Aunt | 12, Maternal Uncle | 13, Paternal Uncle | 14, Maternal Cousin | 15, Paternal Cousin | 16, Other', null=True, max_length=2000, verbose_name=u'Any blood relatives with Unexplained seizures', blank=True)
    cfhx_hypertension_summary = models.CharField(help_text=u'1, None | 2, Mother | 3, Father | 4, Sister | 5, Brother | 6, Maternal Grandmother | 7, Maternal Grandfather | 8, Paternal Grandmother | 9, Paternal Grandfather | 10, Maternal Aunt | 11, Paternal Aunt | 12, Maternal Uncle | 13, Paternal Uncle | 14, Maternal Cousin | 15, Paternal Cousin | 16, Other', null=True, max_length=2000, verbose_name=u'Any blood relatives with High blood pressure (Hypertension)', blank=True)
    cfhx_congen_deaf_summary = models.CharField(help_text=u'1, None | 2, Mother | 3, Father | 4, Sister | 5, Brother | 6, Maternal Grandmother | 7, Maternal Grandfather | 8, Paternal Grandmother | 9, Paternal Grandfather | 10, Maternal Aunt | 11, Paternal Aunt | 12, Maternal Uncle | 13, Paternal Uncle | 14, Maternal Cousin | 15, Paternal Cousin | 16, Other', null=True, max_length=2000, verbose_name=u'Any blood relatives with congenital deafness (Deaf at birth)', blank=True)
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'cardiacfamilyhistory'


class cfhxdiedscd(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Any blood relative who died of heart problems or had an unexpected or unexplained sudden death (including drowning or unexplained car accident) before age 50.', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Any blood relative who died of heart problems or had an unexpected or unexplained sudden death (including drowning or unexplained car accident) before age 50.', choices=[(1, u'None'), (2, u'Mother'), (3, u'Father'), (4, u'Sister'), (5, u'Brother'), (6, u'Maternal Grandmother'), (7, u'Maternal Grandfather'), (8, u'Paternal Grandmother'), (9, u'Paternal Grandfather'), (10, u'Maternal Aunt'), (11, u'Paternal Aunt'), (12, u'Maternal Uncle'), (13, u'Paternal Uncle'), (14, u'Maternal Cousin'), (15, u'Paternal Cousin'), (16, u'Other')])
    cardiacfamilyhistory = models.ForeignKey(CardiacFamilyHistory)

    class Meta:
	 db_table = 'cfhxdiedscd'


class cfhxsurvivesca(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Any blood relative experienced a sudden cardiac arrest (SCA) before age 50 and survived.', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Any blood relative experienced a sudden cardiac arrest (SCA) before age 50 and survived.', choices=[(1, u'None'), (2, u'Mother'), (3, u'Father'), (4, u'Sister'), (5, u'Brother'), (6, u'Maternal Grandmother'), (7, u'Maternal Grandfather'), (8, u'Paternal Grandmother'), (9, u'Paternal Grandfather'), (10, u'Maternal Aunt'), (11, u'Paternal Aunt'), (12, u'Maternal Uncle'), (13, u'Paternal Uncle'), (14, u'Maternal Cousin'), (15, u'Paternal Cousin'), (16, u'Other')])
    cardiacfamilyhistory = models.ForeignKey(CardiacFamilyHistory)

    class Meta:
	 db_table = 'cfhxsurvivesca'


class cfhxdcm(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Any blood relatives with Dilated cardiomyopathy (DCM) or Dilated Left or Right Ventricle', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Any blood relatives with Dilated cardiomyopathy (DCM) or Dilated Left or Right Ventricle', choices=[(1, u'None'), (2, u'Mother'), (3, u'Father'), (4, u'Sister'), (5, u'Brother'), (6, u'Maternal Grandmother'), (7, u'Maternal Grandfather'), (8, u'Paternal Grandmother'), (9, u'Paternal Grandfather'), (10, u'Maternal Aunt'), (11, u'Paternal Aunt'), (12, u'Maternal Uncle'), (13, u'Paternal Uncle'), (14, u'Maternal Cousin'), (15, u'Paternal Cousin'), (16, u'Other')])
    cardiacfamilyhistory = models.ForeignKey(CardiacFamilyHistory)

    class Meta:
	 db_table = 'cfhxdcm'


class cfhxarvc(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Any blood relatives with ARVC (Arrhythmogenic right ventricular cardiomyopathy)', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Any blood relatives with ARVC (Arrhythmogenic right ventricular cardiomyopathy)', choices=[(1, u'None'), (2, u'Mother'), (3, u'Father'), (4, u'Sister'), (5, u'Brother'), (6, u'Maternal Grandmother'), (7, u'Maternal Grandfather'), (8, u'Paternal Grandmother'), (9, u'Paternal Grandfather'), (10, u'Maternal Aunt'), (11, u'Paternal Aunt'), (12, u'Maternal Uncle'), (13, u'Paternal Uncle'), (14, u'Maternal Cousin'), (15, u'Paternal Cousin'), (16, u'Other')])
    cardiacfamilyhistory = models.ForeignKey(CardiacFamilyHistory)

    class Meta:
	 db_table = 'cfhxarvc'


class cfhxsqts(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Any blood relatives with Short QT syndrome (SQTS)', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Any blood relatives with Short QT syndrome (SQTS)', choices=[(1, u'None'), (2, u'Mother'), (3, u'Father'), (4, u'Sister'), (5, u'Brother'), (6, u'Maternal Grandmother'), (7, u'Maternal Grandfather'), (8, u'Paternal Grandmother'), (9, u'Paternal Grandfather'), (10, u'Maternal Aunt'), (11, u'Paternal Aunt'), (12, u'Maternal Uncle'), (13, u'Paternal Uncle'), (14, u'Maternal Cousin'), (15, u'Paternal Cousin'), (16, u'Other')])
    cardiacfamilyhistory = models.ForeignKey(CardiacFamilyHistory)

    class Meta:
	 db_table = 'cfhxsqts'


class cfhxcptv(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Any blood relatives with CPVT-Catecholaminergic polymorphic ventricular tachycardia', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Any blood relatives with CPVT-Catecholaminergic polymorphic ventricular tachycardia', choices=[(1, u'None'), (2, u'Mother'), (3, u'Father'), (4, u'Sister'), (5, u'Brother'), (6, u'Maternal Grandmother'), (7, u'Maternal Grandfather'), (8, u'Paternal Grandmother'), (9, u'Paternal Grandfather'), (10, u'Maternal Aunt'), (11, u'Paternal Aunt'), (12, u'Maternal Uncle'), (13, u'Paternal Uncle'), (14, u'Maternal Cousin'), (15, u'Paternal Cousin'), (16, u'Other')])
    cardiacfamilyhistory = models.ForeignKey(CardiacFamilyHistory)

    class Meta:
	 db_table = 'cfhxcptv'


class cfhxmarfan(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Any blood relatives with Marfan syndrome (aortic rupture / dissection)', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Any blood relatives with Marfan syndrome (aortic rupture / dissection)', choices=[(1, u'None'), (2, u'Mother'), (3, u'Father'), (4, u'Sister'), (5, u'Brother'), (6, u'Maternal Grandmother'), (7, u'Maternal Grandfather'), (8, u'Paternal Grandmother'), (9, u'Paternal Grandfather'), (10, u'Maternal Aunt'), (11, u'Paternal Aunt'), (12, u'Maternal Uncle'), (13, u'Paternal Uncle'), (14, u'Maternal Cousin'), (15, u'Paternal Cousin'), (16, u'Other')])
    cardiacfamilyhistory = models.ForeignKey(CardiacFamilyHistory)

    class Meta:
	 db_table = 'cfhxmarfan'


class cfhxcadmi(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Any blood relatives with Coronary artery disease with Myocardial Infarction (MI / Heart attack)', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Any blood relatives with Coronary artery disease with Myocardial Infarction (MI / Heart attack)', choices=[(1, u'None'), (2, u'Mother'), (3, u'Father'), (4, u'Sister'), (5, u'Brother'), (6, u'Maternal Grandmother'), (7, u'Maternal Grandfather'), (8, u'Paternal Grandmother'), (9, u'Paternal Grandfather'), (10, u'Maternal Aunt'), (11, u'Paternal Aunt'), (12, u'Maternal Uncle'), (13, u'Paternal Uncle'), (14, u'Maternal Cousin'), (15, u'Paternal Cousin'), (16, u'Other')])
    cardiacfamilyhistory = models.ForeignKey(CardiacFamilyHistory)

    class Meta:
	 db_table = 'cfhxcadmi'


class cfhxseizure(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Any blood relatives with Unexplained seizures', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Any blood relatives with Unexplained seizures', choices=[(1, u'None'), (2, u'Mother'), (3, u'Father'), (4, u'Sister'), (5, u'Brother'), (6, u'Maternal Grandmother'), (7, u'Maternal Grandfather'), (8, u'Paternal Grandmother'), (9, u'Paternal Grandfather'), (10, u'Maternal Aunt'), (11, u'Paternal Aunt'), (12, u'Maternal Uncle'), (13, u'Paternal Uncle'), (14, u'Maternal Cousin'), (15, u'Paternal Cousin'), (16, u'Other')])
    cardiacfamilyhistory = models.ForeignKey(CardiacFamilyHistory)

    class Meta:
	 db_table = 'cfhxseizure'


class cfhxhypertension(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Any blood relatives with High blood pressure (Hypertension)', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Any blood relatives with High blood pressure (Hypertension)', choices=[(1, u'None'), (2, u'Mother'), (3, u'Father'), (4, u'Sister'), (5, u'Brother'), (6, u'Maternal Grandmother'), (7, u'Maternal Grandfather'), (8, u'Paternal Grandmother'), (9, u'Paternal Grandfather'), (10, u'Maternal Aunt'), (11, u'Paternal Aunt'), (12, u'Maternal Uncle'), (13, u'Paternal Uncle'), (14, u'Maternal Cousin'), (15, u'Paternal Cousin'), (16, u'Other')])
    cardiacfamilyhistory = models.ForeignKey(CardiacFamilyHistory)

    class Meta:
	 db_table = 'cfhxhypertension'


class cfhxcongendeaf(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Any blood relatives with congenital deafness (Deaf at birth)', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Any blood relatives with congenital deafness (Deaf at birth)', choices=[(1, u'None'), (2, u'Mother'), (3, u'Father'), (4, u'Sister'), (5, u'Brother'), (6, u'Maternal Grandmother'), (7, u'Maternal Grandfather'), (8, u'Paternal Grandmother'), (9, u'Paternal Grandfather'), (10, u'Maternal Aunt'), (11, u'Paternal Aunt'), (12, u'Maternal Uncle'), (13, u'Paternal Uncle'), (14, u'Maternal Cousin'), (15, u'Paternal Cousin'), (16, u'Other')])
    cardiacfamilyhistory = models.ForeignKey(CardiacFamilyHistory)

    class Meta:
	 db_table = 'cfhxcongendeaf'


class EcgResult(models.Model):
    ecg_done = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Electrocardiogram done', choices=[(1, u'Yes'), (2, u'No')])
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'ecgresult'


class Ecg(models.Model):
    ecg_enrollment = models.IntegerField(help_text=u'', null=True, verbose_name=u'How would you categorize the ECG | Other test category', blank=True, choices=[(1, u'Initial test'), (2, u'Enrollment test'), (3, u'Post-enrollment test'), (4, u'Other')]) # This field type is a guess
    ecg_date = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Date of ECG', blank=True)
    ecg_time = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Time of ECG', blank=True)
    ecg_ventricular_rate = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Ventricular Rate / bpm for ECG', blank=True)
    ecg_pr_interval = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'PR Interval / msec for $ECG', blank=True)
    ecg_qrs_inter_machine = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'QRS Interval / msec  (ECG Computer) for ECG', blank=True)
    ecg_qt_inter_machine = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'QT Interval / msec   (ECG Computer) for ECG', blank=True)
    ecg_qtc_inter_machine = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'QTc Interval / msec   (ECG Computer) for ECG', blank=True)
    ecg_qtc_inter_manual = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'QTc Interval / msec   (Manual Calculation) for ECG', blank=True)
    ecg_p_axis_degree = models.CharField(help_text=u'NOTE: Must use positive numbers. (360 degrees minus X)', null=True, max_length=2000, verbose_name=u'P axis for ECG', blank=True)
    ecg_p_axis_type = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'P Axis Type for ECG', choices=[(1, u'Sinus (0 to +90 degree)'), (2, u'LRA (-1 to -90 degree)'), (3, u'HLA (+91 to +180 degree)'), (4, u'LLA (-91 to -179 or +181 to +270 degree)')])
    ecg_qrs_axis_degree = models.CharField(help_text=u'NOTE: Must use positive numbers. (360 degrees minus X)', null=True, max_length=2000, verbose_name=u'QRS axis for ECG', blank=True)
    ecg_qrs_axis_type = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'QRS Axis Type for ECG', choices=[(1, u'Normal'), (2, u'RAD (>+100 degree)'), (3, u'Rightward (+90 to +100 degree)'), (4, u'LAD (negative degree)')])
    ecg_twave_axis_degree = models.CharField(help_text=u'NOTE: Must use positive numbers. (360 degrees minus X)', null=True, max_length=2000, verbose_name=u'T wave axis for ECG', blank=True)
    ecg_twave_axis_type = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'T wave axis Type for ECG', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Wide QRS-T angle')])
    ecg_interp_arrhythmia = models.CharField(help_text=u'Check all that apply.', null=True, max_length=2000, verbose_name=u'ECG Interpretation: Arrhythmia/Conduction. ', blank=True)
    ecg_interp_structure = models.IntegerField(max_length=2000, blank=True, help_text=u'Check all that apply', null=True, verbose_name=u'ECG Interpretation: Structural. ', choices=[(1, u'None'), (2, u'Right atrial enlargement (RAE)'), (3, u'Left atrial enlargement (LAE)'), (4, u'Bi-atrial enlargement  (BAE)'), (5, u'Biventricular hypertrophy'), (6, u'Right ventricular hypertrophy (RVH)'), (7, u'Right ventricular hypertrophy (RVH) with strain'), (8, u'Left ventricular hypertrophy (LVH)'), (9, u'Left ventricular hypertrophy (LVH) with strain'), (10, u'Hypertrophic Cardiomyopathy (HCM)'), (11, u'Dilated Cardiomyopathy (DCM)'), (12, u'Dextrocardia')])
    ecg_interp_other = models.TextField(help_text=u'', null=True, verbose_name=u'ECG Interpretation:  Other (not listed above)', blank=True) # This field type is a guess
    ecg_result = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'ECG Result', choices=[(1, u'Normal'), (2, u'VON - Variant of Normal'), (3, u'Abnormal'), (4, u'Not Determined')])
    ecg_interp_rhythm_summary = models.CharField(help_text=u'10, None | 1, Normal Sinus Rhythm | 2, Normal Sinus Rhythm with Sinus Arrhythmia | 3, Normal Sinus Rhythm with Sinus Bradycardia | 4, Normal Sinus Rhythm with Sinus Tachycardia | 5, Low Right Atrial Rhythm | 6, Ectopic Atrial Rhythm | 7, Normal Sinus Rhythm alternating with Ectopic Atrial Rhythm | 8, Junctional Rhythm (accelerated or escape) | 9, Ventricular Rhythm (accelerated or escape)', null=True, max_length=2000, verbose_name=u'ECG Interpretation: Predominant Rhythm.  ', blank=True)
    ecg_interp_axis_summary = models.CharField(help_text=u'1, None | 2, Leftward Axis | 3, Left Axis Deviation (LAD) | 4, Left Superior Axis Deviation | 5, Rightward Axis | 6, Right Axis Deviation (RAD) | 7, Right Axis Deviation, northwest | 8, Indeterminate Axis | 9, Increased LV Forces | 10, ST elevation (Nonspecific) | 11, ST elevation (Ischemia) | 12, ST elevation (Strain) | 13, ST elevation (Early Repolarization) | 14, ST depression (Nonspecific) | 15, ST depression (Ischemia) | 16, ST depression (Strain) | 17, T wave inversion (Inferior) | 18, T wave inversion (Anterior) | 19, T wave inversion (Lateral) | 20, T wave abnormalities (Nonspecific) | 21, T wave abnormalities (Alternans) | 22, T wave abnormalities (Flat) | 23, T wave abnormalities (Late T wave peak) | 24, T wave abnormalities (Notched) | 25, T wave abnormalities (Biphasic) | 26, T wave abnormalities (Inverted) | 27, Q waves (Abnormal) | 28, Q waves (ULN) | 29, U waves (Abnormal) | 30, U waves (Prominent U Waves)', null=True, max_length=2000, verbose_name=u'ECG Interpretation: Axis.', blank=True)
    ecgresult = models.ForeignKey(EcgResult)

    class Meta:
	 db_table = 'ecg'


class ecginterprhythm(models.Model):
    label = models.CharField(help_text=u'Check all that apply', null=True, max_length=2000, verbose_name=u'ECG Interpretation: Predominant Rhythm.  ', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'Check all that apply', null=True, verbose_name=u'ECG Interpretation: Predominant Rhythm.  ', choices=[(10, u'None'), (1, u'Normal Sinus Rhythm'), (2, u'Normal Sinus Rhythm with Sinus Arrhythmia'), (3, u'Normal Sinus Rhythm with Sinus Bradycardia'), (4, u'Normal Sinus Rhythm with Sinus Tachycardia'), (5, u'Low Right Atrial Rhythm'), (6, u'Ectopic Atrial Rhythm'), (7, u'Normal Sinus Rhythm alternating with Ectopic Atrial Rhythm'), (8, u'Junctional Rhythm (accelerated or escape)'), (9, u'Ventricular Rhythm (accelerated or escape)')])
    ecg = models.ForeignKey(Ecg)

    class Meta:
	 db_table = 'ecginterprhythm'


class ecginterpaxis(models.Model):
    label = models.CharField(help_text=u'Check all that apply.', null=True, max_length=2000, verbose_name=u'ECG Interpretation: Axis.', blank=True)
    value = models.CharField(help_text=u'Check all that apply.', null=True, max_length=2000, verbose_name=u'ECG Interpretation: Axis.', blank=True)
    ecg = models.ForeignKey(Ecg)

    class Meta:
	 db_table = 'ecginterpaxis'


class EchoResult(models.Model):
    echo_done = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Echocardiogram done', choices=[(1, u'Yes'), (2, u'No')])
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'echoresult'


class EchoTest(models.Model):
    echo_enrollment = models.IntegerField(help_text=u'', null=True, verbose_name=u'How would you categorize the ECHO | Other test category', blank=True, choices=[(1, u'Initial test'), (2, u'Enrollment test'), (3, u'Post-enrollment test'), (4, u'Other')]) # This field type is a guess
    echo_date = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Date of ECHO', blank=True)
    echo_ht_report = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Height/cm on ECHO report', blank=True)
    echo_wt_report = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Weight/kg on ECHO report', blank=True)
    echo_bsa = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'BSA - Body Surface Area on ECHO report', blank=True)
    echo_ivsd = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'IVSd - (Diastolic septal thickness/cm) on ECHO report', blank=True)
    echo_ivsd_zscore = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'IVSd Zscore- (Diastolic septal thickness/zscore) on ECHO report', blank=True)
    echo_lvidd = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'LVIDd - (LV Diastolic dimension/cm) on ECHO report', blank=True)
    echo_lvidd_zscore = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'LVIDd Zscore- (LV Diastolic dimension/zscore) on ECHO report', blank=True)
    echo_lvids = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'LVIDs - (LV Systolic dimension/cm) on ECHO report', blank=True)
    echo_lvids_zscore = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'LVIDs Zscore- (LV Systolic dimension/zscore) on ECHO report', blank=True)
    echo_lvpwd = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'LVPWd - (LV diastolic wall thickness/cm) on ECHO report', blank=True)
    echo_lvpwd_zscore = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'LVPWd Zscore- (LV diastolic wall thickness/zscore) on ECHO report', blank=True)
    echo_lv_mass = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'LV mass - (M-mode LV mass-ASE corr./g) on ECHO report', blank=True)
    echo_lv_mass_zscore = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'LV mass Zscore- (M-mode LV mass-ASE corr./g/zscore) on ECHO report', blank=True)
    echo_lv_mass_index = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'LV mass index (g/h^2.7) on ECHO report', blank=True)
    echo_lv_vol_d_4c = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'LV volume, d (4C) - (mL) on ECHO report', blank=True)
    echo_lv_vol_d_2c = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'LV volume, d (2C) - (mL) on ECHO report', blank=True)
    echo_lv_vol_d_biplane = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'LV volume, d (biplane) - (mL) on ECHO report', blank=True)
    echo_lv_vol_s_4c = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'LV volume, s (4C) - (mL) on ECHO report', blank=True)
    echo_lv_vol_s_2c = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'LV volume, s (2C) - (mL) on ECHO report', blank=True)
    echo_lv_vol_s_biplane = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'LV volume, s (biplane) - (mL) on ECHO report', blank=True)
    echo_lv_vol_d_4c_index = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'LV volume, d (4C) index - (mL/m^2) on ECHO report', blank=True)
    echo_lv_vol_d_2c_index = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'LV volume, d (2C) index - (mL/m^2) on ECHO report', blank=True)
    echo_lv_vol_d_biplane_ind = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'LV volume, d (biplane) index - (mL/m^2) on ECHO report', blank=True)
    echo_aov_annulus = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'AoV annulus - (Aortic Annulus diameter/cm) on ECHO report', blank=True)
    echo_aov_annulus_zscore = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'AoV annulus Zscore- (Aortic Annulus diameter/zscore) on ECHO report', blank=True)
    echo_ao_root = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Ao Root - (Aortic Root diameter/cm) on ECHO report', blank=True)
    echo_ao_root_zscore = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Ao Root Zscore- (Aortic Root diameter/zscore) on ECHO report', blank=True)
    echo_ao_st_junct_s = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Ao ST junct, s - (Sinotubular junction diameter/cm) on ECHO report', blank=True)
    echo_ao_st_junct_s_zscore = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Ao ST junct, s Zscore- (Sinotubular junction diameter/zscore) on ECHO report', blank=True)
    echo_ao_asc_d = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Ao asc,d - (cm) on ECHO report', blank=True)
    echo_ao_asc_d_zscore = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Ao asc,d, Zscore on ECHO report', blank=True)
    echo_ao_dsc_d = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Ao dsc,d - (cm) on ECHO report', blank=True)
    echo_ao_dsc_d_zscore = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Ao dsc,d, Zscore on ECHO report', blank=True)
    echo_aov_area = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'AoV Area - (Aortic valve area/cm^2) on ECHO report', blank=True)
    echo_lv_sf = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'LV SF - (LV shortening fraction M-mode/%) on ECHO report', blank=True)
    echo_lv_ef = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'LV EF - (Ejection fraction M-mode/%) on ECHO report', blank=True)
    echo_lv_ef_4c = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'LV EF (4C) - (Ejection fraction/%) on ECHO report', blank=True)
    echo_lv_ef_2c = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'LV EF (2C) - (Ejection fraction/%) on ECHO report', blank=True)
    echo_lv_ef_biplane = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'LV EF (biplane) - (Ejection fraction/%) on ECHO report', blank=True)
    echo_lv_ef_aov = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'LV ejection time (AoV) - (msec) on ECHO report', blank=True)
    echo_lv_intra_avv = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'LV Intra AVV Time (MV) - (msec) on ECHO report', blank=True)
    echo_lv_mpi = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'LV MPI on ECHO report', blank=True)
    echo_lv_septal_annulus = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u"LV Diastolic Function: Septal annulus e' - (m/s) on ECHO report", blank=True)
    echo_lv_mitral_septal = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u"LV Diastolic Function: E/e' (mitral septal) on ECHO report", blank=True)
    echo_lv_mitral_lateral = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u"LV Diastolic Function: E/e' (mitral lateral) on ECHO report", blank=True)
    echo_lv_mitral_inflow = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'LV Diastolic Function: E/A (mitral inflow) on ECHO report', blank=True)
    echo_lvot_peak_vel = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'LVOTO Doppler: Peak velocity (m/s) on ECHO report', blank=True)
    echo_lvot_peak_grad = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'LVOTO Doppler: Peak gradient (mmHg) on ECHO report', blank=True)
    echo_lvot_mean_grad = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'LVOTO Doppler: Mean gradient (mmHg) on ECHO report', blank=True)
    echo_av_peak_vel = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Aortic Valve Doppler: Peak Velocity (m/s) on ECHO report', blank=True)
    echo_av_peak_grad = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Aortic Valve Doppler: Peak Gradient (mmHg) on ECHO report', blank=True)
    echo_av_mean_grad = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Aortic Valve Doppler: Mean Gradient (mmHg) on ECHO report', blank=True)
    echo_av_eject_time = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Aortic Valve Doppler: Ejection time (msec) on ECHO report', blank=True)
    echo_mv_peak_e = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Mitral Valve Doppler: Peak E (m/s) on ECHO report', blank=True)
    echo_mv_peak_a = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Mitral Valve Doppler: Peak A (m/s) on ECHO report', blank=True)
    echo_myocard_perf_index = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Myocardial Performance Index on ECHO report', blank=True)
    echo_samm = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Systolic Anterior Motion of Mitral Valve on ECHO report', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    echo_samm_degree = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Degree of SAMM on ECHO report', blank=True)
    echo_lvoto = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'LVOTO - (Left Ventricular Outflow Tract Obstruction) on ECHO report', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    echo_lvoto_gradient = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'LVOTO Gradient on ECHO report', choices=[(1, u'Mild'), (2, u'Moderate'), (3, u'Severe'), (4, u'Other')])
    echo_lvoto_gradient_oth = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'LVOTO Gradient Other - Specify on ECHO report', blank=True)
    echo_rvoto = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'RVOTO - (Right Ventricular Outflow Tract Obstruction) on ECHO report', choices=[(1, u'Yes'), (2, u'No'), (3, u'Unknown/Not documented')])
    echo_rvoto_gradient = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'RVOTO Gradient on ECHO report', choices=[(1, u'Mild'), (2, u'Moderate'), (3, u'Severe'), (4, u'Other')])
    echo_rvoto_gradient_oth = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'RVOTO Gradient Other - Specify on ECHO report', blank=True)
    echo_rv_chamber = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'RV chamber on ECHO report', choices=[(1, u'Normal'), (2, u'Abnormal')])
    echo_rv_specify = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'RV: Specify on ECHO report', blank=True)
    echo_lv_chamber = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'LV chamber on ECHO report', choices=[(1, u'Normal'), (2, u'Abnormal')])
    echo_lv_specify = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'LV: Specify on ECHO report', blank=True)
    echo_ra = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'RA on ECHO report', choices=[(1, u'Normal'), (2, u'Abnormal')])
    echo_ra_specify = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'RA: Specify on ECHO report', blank=True)
    echo_la = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'LA on ECHO report', choices=[(1, u'Normal'), (2, u'Abnormal')])
    echo_la_specify = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'LA: Specify on ECHO report', blank=True)
    echo_aortic_root = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Aortic Root on ECHO report', choices=[(1, u'Normal'), (2, u'Abnormal')])
    echo_aortic_root_specify = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Aortic Root: Specify on ECHO report', blank=True)
    echo_bicuspid_aortic_val = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Bicuspid aortic valve on ECHO report', choices=[(1, u'Yes'), (2, u'No'), (3, u'Not well seen')])
    echo_aortic_insuff = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Aortic valve insufficiency on ECHO report', choices=[(1, u'Yes'), (2, u'No')])
    echo_ai_severity = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Aortic valve insufficiency: Severity on ECHO report', choices=[(1, u'Trivial'), (2, u'Mild'), (3, u'Moderate'), (4, u'Severe')])
    echo_aortic_stenosis = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Aortic stenosis on ECHO report', choices=[(1, u'Yes'), (2, u'No')])
    echo_as_sever = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Aortic stenosis: Severity on ECHO report', choices=[(1, u'Trivial'), (2, u'Mild'), (3, u'Moderate'), (4, u'Severe')])
    echo_as_peak_grad = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'AS-Peak gradient (m/sec) on ECHO report', blank=True)
    echo_as_mean_grad = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'AS-Mean gradient (m/sec) on ECHO report', blank=True)
    echo_region_aortic_sten = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Region of aortic stenosis on ECHO report', choices=[(1, u'Valve'), (2, u'Subvalvular'), (3, u'Supravalvular'), (4, u'Other')])
    echo_region_as_oth = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Region of aortic stenosis: Specify on ECHO report', blank=True)
    echo_hcm = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Hypertrophic Cardiomyopathy on ECHO report', blank=True)
    echo_hcm_severity = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Hypertrophic Cardiomyopathy: Severity on ECHO report', choices=[(1, u'Trivial'), (2, u'Mild'), (3, u'Moderate'), (4, u'Severe')])
    echo_hypertrophy_loc = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Location of Hypertrophy on ECHO report', choices=[(1, u'Septal'), (2, u'Apical'), (3, u'Concentric'), (4, u'Other')])
    echo_hyper_other = models.TextField(help_text=u'', null=True, verbose_name=u'Location of Hypertrophy Other - Specify on ECHO report', blank=True) # This field type is a guess
    echo_pul_insuff = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Pulmonary valve insufficiency on ECHO report', choices=[(1, u'Yes'), (2, u'No')])
    echo_pi_severity = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Pulmonary valve insufficiency: Severity on ECHO report', choices=[(1, u'Trivial'), (2, u'Mild'), (3, u'Moderate'), (4, u'Severe')])
    echo_pul_stenosis = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Pulmonary stenosis on ECHO report', choices=[(1, u'Yes'), (2, u'No')])
    echo_ps_severity = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Pulmonary stenosis: Severity on ECHO report', choices=[(1, u'Trivial'), (2, u'Mild'), (3, u'Moderate'), (4, u'Severe')])
    echo_ps_peak_grad = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'PS-Peak gradient (m/sec) on ECHO report', blank=True)
    echo_ps_mean_grad = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'PS-Mean gradient (m/sec) on ECHO report', blank=True)
    echo_mit_insuff = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Mitral valve insufficiency on ECHO report', choices=[(1, u'Yes'), (2, u'No')])
    echo_mi_severity = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Mitral valve insufficiency: Severity on ECHO report', choices=[(1, u'Trivial'), (2, u'Mild'), (3, u'Moderate'), (4, u'Severe')])
    echo_mit_val_prolapse = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Mitral valve prolapse on ECHO report', choices=[(1, u'Yes'), (2, u'No')])
    echo_mvp_severity = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Mitral valve prolapse: Severity on ECHO report', choices=[(1, u'Trivial'), (2, u'Mild'), (3, u'Moderate'), (4, u'Severe')])
    echo_ms_gradient = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'MS gradient on ECHO report', choices=[(1, u'Yes'), (2, u'No')])
    echo_ms_grad_severity = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'MS gradient: Severity on ECHO report', choices=[(1, u'Trivial'), (2, u'Mild'), (3, u'Moderate'), (4, u'Severe')])
    echo_ms_jet_velocity = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'MS mean jet velocity (m/sec) on ECHO report', blank=True)
    echo_tri_insuff = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Tricuspid valve insufficiency on ECHO report', choices=[(1, u'Yes'), (2, u'No')])
    echo_ti_severity = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Tricuspid valve insufficiency: Severity on ECHO report', choices=[(1, u'Trivial'), (2, u'Mild'), (3, u'Moderate'), (4, u'Severe')])
    echo_tri_stenosis = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Tricuspid valve stenosis on ECHO report', choices=[(1, u'Yes'), (2, u'No')])
    echo_tri_sten_severity = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Tricuspid valve stenosis: Severity on ECHO report', choices=[(1, u'Trivial'), (2, u'Mild'), (3, u'Moderate'), (4, u'Severe')])
    echo_tri_sten_gradient = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'TS-Peak gradient (m/sec) on ECHO report', blank=True)
    echo_rv_pressure = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'RV pressure estimate (mm/Hg > right atrial v wave) on ECHO report', blank=True)
    echo_asd = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Atrial septal defect on ECHO report', choices=[(1, u'Yes'), (2, u'No'), (3, u'Not well seen')])
    echo_asd_severity = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'ASD: Size on ECHO report', choices=[(1, u'Small'), (2, u'Moderate'), (3, u'Large')])
    echo_asd_specify_small = models.TextField(help_text=u'', null=True, verbose_name=u'ASD (small): Specify (cm) on ECHO report', blank=True) # This field type is a guess
    echo_asd_specify_mod = models.TextField(help_text=u'', null=True, verbose_name=u'ASD (moderate): Specify (cm) on ECHO report', blank=True) # This field type is a guess
    echo_asd_specify_large = models.TextField(help_text=u'', null=True, verbose_name=u'ASD (large): Specify (cm) on ECHO report', blank=True) # This field type is a guess
    echo_pfo = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Patent foramen ovale on ECHO report', choices=[(1, u'Yes'), (2, u'No'), (3, u'Not well seen')])
    echo_pfo_severity = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'PFO: Specify on ECHO report', blank=True)
    echo_vsd = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Ventricular septal defect on ECHO report', choices=[(1, u'Yes'), (2, u'No'), (3, u'Not well seen')])
    echo_vsd_severity = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'VSD: Size on ECHO report', choices=[(1, u'Small'), (2, u'Moderate'), (3, u'Large')])
    echo_vsd_specify_small = models.TextField(help_text=u'', null=True, verbose_name=u'VSD (small): Specify on ECHO report', blank=True) # This field type is a guess
    echo_vsd_specify_mod = models.TextField(help_text=u'', null=True, verbose_name=u'ASD (moderate): Specify on ECHO report', blank=True) # This field type is a guess
    echo_vsd_specify_large = models.TextField(help_text=u'', null=True, verbose_name=u'ASD (large): Specify on ECHO report', blank=True) # This field type is a guess
    echo_pda = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Patent ductus arteriosus on ECHO report', choices=[(1, u'Yes'), (2, u'No'), (3, u'Not well seen')])
    echo_pda_severity = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'PDA: Severity on ECHO report', choices=[(1, u'Small'), (2, u'Moderate'), (3, u'Large')])
    echo_pda_specify_small = models.TextField(help_text=u'', null=True, verbose_name=u'PDA (small): Specify on ECHO report', blank=True) # This field type is a guess
    echo_pda_specify_mod = models.TextField(help_text=u'', null=True, verbose_name=u'PDA (moderate): Specify on ECHO report', blank=True) # This field type is a guess
    echo_pda_specify_large = models.TextField(help_text=u'', null=True, verbose_name=u'PDA (large): Specify on ECHO report', blank=True) # This field type is a guess
    echo_coarct = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Coarctation of the aorta on ECHO report', choices=[(1, u'Yes'), (2, u'No'), (3, u'Other')])
    echo_coarct_severity = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Coarctation of the aorta: Severity on ECHO report', choices=[(1, u'Mild'), (2, u'Moderate'), (3, u'Severe')])
    echo_coarct_sever_oth = models.TextField(help_text=u'', null=True, verbose_name=u'Coarctation of the aorta/Other: Specify on ECHO report', blank=True) # This field type is a guess
    echo_peri_effusion = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Pericardial effusion on ECHO report', choices=[(1, u'Yes'), (2, u'No')])
    echo_peri_eff_location = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Pericardial effusion: Location on ECHO report', choices=[(1, u'RA'), (2, u'RV'), (3, u'LA'), (4, u'LA'), (5, u'LV'), (6, u'Other')])
    echo_peri_eff_loc_oth = models.TextField(help_text=u'', null=True, verbose_name=u'Pericardial effusion/Other: Specify on ECHO report', blank=True) # This field type is a guess
    echo_peri_eff_size = models.TextField(help_text=u'', null=True, verbose_name=u'Pericardial effusion/Size: Specify on ECHO report', blank=True) # This field type is a guess
    echo_rt_coronary_art = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Right coronary artery on ECHO report', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not well seen'), (4, u'Unknown/Not documented')])
    echo_lt_coronary_main = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Left coronary artery _ Main on ECHO report', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not well seen'), (4, u'Unknown/Not documented')])
    echo_lt_coronary_ant_desc = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Left coronary artery _ Anterior descending on ECHO report', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not well seen'), (4, u'Unknown/Not documented')])
    echo_lt_coronary_circum = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Left coronary artery _ Circumflex on ECHO report', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not well seen'), (4, u'Unknown/Not documented')])
    echo_anom_ca_origin = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Anomalous origin of coronary artery on ECHO report', choices=[(1, u'Both from R sinus'), (2, u'Both from L sinus'), (3, u'Single'), (4, u'Intramural'), (5, u'Other')])
    echo_anom_ca_origin_oth = models.TextField(help_text=u'', null=True, verbose_name=u'Anomalous origin CA/Other: Specify on ECHO report', blank=True) # This field type is a guess
    echo_coronary_ostia = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Coronary artery ostia on ECHO report', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Not well seen'), (4, u'Not documented'), (5, u'Other')])
    echo_coronary_ostia_oth = models.TextField(help_text=u'', null=True, verbose_name=u'Coronary artery ostia Other - specify on ECHO report', blank=True) # This field type is a guess
    echo_aortic_arch = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Aortic Arch on ECHO report', choices=[(1, u'Normal branching'), (2, u'Right aortic arch'), (3, u'Aberrant Right subclavian'), (4, u'Double aortic arch'), (5, u'Other')])
    echo_aortic_arch_oth = models.TextField(help_text=u'', null=True, verbose_name=u'Aortic Arch other - Specify on ECHO report', blank=True) # This field type is a guess
    echo_number_pul_vein = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Number of pulmonary veins seen entering the left atrium on ECHO report', choices=[(1, u'4 veins'), (2, u'3 veins'), (3, u'2 veins'), (4, u'1 vein'), (5, u'Not well seen'), (6, u'Not documented')])
    echo_anom_pul_vein = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Anomalous pulmonary veins on ECHO report', choices=[(1, u'Yes'), (2, u'No'), (3, u'Not well seen')])
    echo_anom_pul_vein_spec = models.TextField(help_text=u'', null=True, verbose_name=u'Anomalous pulmonary veins: Specify on ECHO report', blank=True) # This field type is a guess
    echo_anom_ven_structure = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Anomalous venous structures on ECHO report', choices=[(1, u'Yes'), (2, u'No'), (3, u'Not well seen')])
    echo_anom_ven_location = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Anomalous venous structures location on ECHO report', choices=[(1, u'SVC'), (2, u'LSVC to CS'), (3, u'Bilateral SVC'), (4, u'Azygos vein continuation of interrupted inferior vena cava (IVC)'), (5, u'Other')])
    echo_anom_ven_loc_oth = models.TextField(help_text=u'', null=True, verbose_name=u'Anomalous venous structures location/Other: Specify on ECHO report', blank=True) # This field type is a guess
    echo_other_chd = models.TextField(help_text=u'', null=True, verbose_name=u'Other congenital heart disease or findings on ECHO report', blank=True) # This field type is a guess
    echo_comments_report = models.TextField(help_text=u'', null=True, verbose_name=u'Additional comments from ECHO report not listed above.', blank=True) # This field type is a guess
    echoresult = models.ForeignKey(EchoResult)

    class Meta:
	 db_table = 'echotest'


class EstResult(models.Model):
    est_done = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Exercise Stress Test done', choices=[(1, u'Yes'), (2, u'No')])
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'estresult'


class ExerciseStressTest(models.Model):
    est_enrollment = models.IntegerField(help_text=u'', null=True, verbose_name=u'How would you categorize the exercise stress test | Other test category', blank=True, choices=[(1, u'Initial test'), (2, u'Enrollment test'), (3, u'Post-enrollment test'), (4, u'Other')]) # This field type is a guess
    est_date = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Date of EST', blank=True)
    est_machine = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'EST performed on', choices=[(1, u'Stationary Bicycle'), (2, u'Ramp/Treadmill')])
    est_hr = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'EST Heart rate ', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Other')])
    est_hr_other = models.TextField(help_text=u'', null=True, verbose_name=u'EST Heart rate - Other: Specify', blank=True) # This field type is a guess
    est_hr_rest = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'EST Heart rate - rest', blank=True)
    est_hr_max = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'EST Heart rate - maximum', blank=True)
    est_hr_response = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'EST Heart rate response', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Other')])
    est_hr_response_oth = models.TextField(help_text=u'', null=True, verbose_name=u'EST Heart rate response Other - Specify', blank=True) # This field type is a guess
    est_bp = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'EST Blood pressure response', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Other')])
    est_bp_response = models.TextField(help_text=u'', null=True, verbose_name=u'EST Blood pressure response - Other: Specify', blank=True) # This field type is a guess
    est_bp_rest = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'EST Blood Pressure - rest', blank=True)
    est_bp_max = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'EST Blood Pressure - maximum', blank=True)
    est_o2_sat = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'EST Oxygen saturation', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Other')])
    est_o2_other = models.TextField(help_text=u'', null=True, verbose_name=u'EST Oxygen saturated - Other: Specify', blank=True) # This field type is a guess
    est_o2_sat_rest = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'EST Oxygen saturation - rest', blank=True)
    est_o2_sat_max = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'EST Oxygen saturation - maximum', blank=True)
    est_work_rate = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'EST Work rate', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Other')])
    est_work_rate_other = models.TextField(help_text=u'', null=True, verbose_name=u'EST Work rate - Other: Specify', blank=True) # This field type is a guess
    est_work_rate_watts = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'EST Work rate - Watts', blank=True)
    est_o2_consump = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'EST Oxygen consumption', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Other')])
    est_os_comsump_oth = models.TextField(help_text=u'', null=True, verbose_name=u'EST Oxygen consumption - Other: Specify', blank=True) # This field type is a guess
    est_os_comsump_rest_vo2 = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'EST Oxygen consumption - rest VO2 (L/min)', blank=True)
    est_os_comsump_max_vo2 = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'EST Oxygen consumption - max VO2 (L/min)', blank=True)
    est_os_comsump_max = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'EST Oxygen consumption - max (ml/kg/min)', blank=True)
    est_os_comsump_max_at = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'EST Oxygen consumption - Anerobic Threshold (AT)', blank=True)
    est_cardiac_output = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'EST Cardiac output', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Other')])
    est_cardiac_output_oth = models.TextField(help_text=u'', null=True, verbose_name=u'EST Cardiac output - Other: Specify', blank=True) # This field type is a guess
    est_cardiac_output_rest = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'EST Cardiac output - rest', blank=True)
    est_card_output_rest_ci = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'EST Cardiac output - rest - CI', blank=True)
    est_cardiac_output_max = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'EST Cardiac output - maximum', blank=True)
    est_card_output_max_mci = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'EST Cardiac output - maximum - MCI', blank=True)
    est_rhythm_other = models.TextField(help_text=u'', null=True, verbose_name=u'EST Rhythm - Other: Specify', blank=True) # This field type is a guess
    est_st_seg_change = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'EST ST segment changes', choices=[(1, u'None'), (2, u'Other')])
    est_st_seg_change_oth = models.TextField(help_text=u'', null=True, verbose_name=u'EST ST segment changes - Other: Specify', blank=True) # This field type is a guess
    est_symptom = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'EST Symptoms', choices=[(1, u'None'), (2, u'Other')])
    est_symptom_oth = models.TextField(help_text=u'', null=True, verbose_name=u'EST Symptoms - Other: Specify', blank=True) # This field type is a guess
    est_pul_func_rest = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'EST Pulmonary function (rest)', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Other')])
    est_pul_func_rest_oth = models.TextField(help_text=u'', null=True, verbose_name=u'EST Pulmonary function  (rest) - Other: Specify', blank=True) # This field type is a guess
    est_pul_func_reserve = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'EST Pulmonary function (reserve)', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Other')])
    est_pul_func_reserve_oth = models.TextField(help_text=u'', null=True, verbose_name=u'EST Pulmonary function (reserve) - Other: Specify', blank=True) # This field type is a guess
    est_pul_func_post = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'EST Pulmonary function (post)', choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Other')])
    est_pul_func_post_oth = models.TextField(help_text=u'', null=True, verbose_name=u'EST Pulmonary function (post) - Other: Specify', blank=True) # This field type is a guess
    est_pul_func_ve = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'EST Pulmonary function - VE', blank=True)
    est_pul_func_rq = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'EST Pulmonary function - RQ', blank=True)
    est_summary = models.TextField(help_text=u'', null=True, verbose_name=u'EST Summary', blank=True) # This field type is a guess
    est_rhythm_summary = models.CharField(help_text=u'1, Sinus | 2, PAC-Premature Atrial Complexes | 3, PVC-Premature Ventricular Complexes | 4, PVC Couplets | 5, Ventricular Tachycardia | 6, Supraventricular Tachycardia | 7, Ventricular Fibrillation | 8, First Degree AV Block | 9, Second Degree AV Block (Mobitz Type I Wenckebach) | 10, Second Degree AV Block (Mobitz Type II) | 11, Third Degree (or Complete) AV Block | 12, Atrial Fibrillation | 13, Atrial Flutter | 14, Atrial Tachycardia | 15, Bradycardia | 16, Junctional rhythm | 17, Ventricular fibrillation | 18, Prolonged QT Interval  | 19, Wolff-Parkinson-White | 20, Torsades de pointes | 21, Other', null=True, max_length=2000, verbose_name=u'EST Rhythm', blank=True)
    estresult = models.ForeignKey(EstResult)

    class Meta:
	 db_table = 'exercisestresstest'


class estrhythm(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'EST Rhythm', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'EST Rhythm', choices=[(1, u'Sinus'), (2, u'PAC-Premature Atrial Complexes'), (3, u'PVC-Premature Ventricular Complexes'), (4, u'PVC Couplets'), (5, u'Ventricular Tachycardia'), (6, u'Supraventricular Tachycardia'), (7, u'Ventricular Fibrillation'), (8, u'First Degree AV Block'), (9, u'Second Degree AV Block (Mobitz Type I Wenckebach)'), (10, u'Second Degree AV Block (Mobitz Type II)'), (11, u'Third Degree (or Complete) AV Block'), (12, u'Atrial Fibrillation'), (13, u'Atrial Flutter'), (14, u'Atrial Tachycardia'), (15, u'Bradycardia'), (16, u'Junctional rhythm'), (17, u'Ventricular fibrillation'), (18, u'Prolonged QT Interval'), (19, u'Wolff-Parkinson-White'), (20, u'Torsades de pointes'), (21, u'Other')])
    exercisestresstest = models.ForeignKey(ExerciseStressTest)

    class Meta:
	 db_table = 'estrhythm'


class HolterResult(models.Model):
    hm_done = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Holter Monitor test done', choices=[(1, u'Yes'), (2, u'No')])
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'holterresult'


class Hm(models.Model):
    hm_enrollment = models.IntegerField(help_text=u'', null=True, verbose_name=u'How would you categorize the holter monitor test | Other test category', blank=True, choices=[(1, u'Initial test'), (2, u'Enrollment test'), (3, u'Post-enrollment test'), (4, u'Other')]) # This field type is a guess
    hm_date = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Date of Holter Monitor test', blank=True)
    hm_hr_total = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Holter Heart Rate Data: Total beats', blank=True)
    hm_hr_min = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Holter Heart Rate Data: Min HR (bpm)', blank=True)
    hm_hr_avg = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Holter Heart Rate Data: Avg HR (bpm)', blank=True)
    hm_hr_max = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Holter Heart Rate Data: Max HR (bpm)', blank=True)
    hm_hr_var_asdnn5 = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Holter HR Variability: ASDNN 5 (msec)', blank=True)
    hm_hr_var_sdnn5 = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Holter HR Variability: SDANN 5 (msec)', blank=True)
    hm_hr_var_sdnn = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Holter HR Variability: SDNN (msec)', blank=True)
    hm_hr_var_rmssd = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Holter HR Variability: RMSSD (msec)', blank=True)
    hm_ve_total_beat = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Holter Ventricular Ectopy: Total VE Beats (%)', blank=True)
    hm_ve_vent_run = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Holter Ventricular Ectopy: Vent Runs', blank=True)
    hm_ve_beat = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Holter Ventricular Ectopy: Beats', blank=True)
    hm_ve_long = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Holter Ventricular Ectopy: Longest', blank=True)
    hm_ve_fast = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Holter Ventricular Ectopy: Fastest (bpm)', blank=True)
    hm_ve_triplet = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Holter Ventricular Ectopy: Triplets (Events)', blank=True)
    hm_ve_couplet = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Holter Ventricular Ectopy: Couplets (Events)', blank=True)
    hm_ve_ront = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Holter Ventricular Ectopy: R on T', blank=True)
    hm_ve_bi_trigem = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Holter Ventricular Ectopy: Bi/Trigeminy (Beats)', blank=True)
    hm_ve_max_ve_min = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Holter Ventricular Ectopy: Max VE/Minute  (Beats)', blank=True)
    hm_ve_max_ve_hr = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Holter Ventricular Ectopy: Max VE/Hour  (Beats)', blank=True)
    hm_ve_mean_hour = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Holter Ventricular Ectopy: Mean VE/Hour', blank=True)
    hm_ve_ve_1000 = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Holter Ventricular Ectopy: VE/1000 (% of rhythm)', blank=True)
    hm_sve_total_beat = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Holter Supraventricular Ectopy: Total SVE Beats (%)', blank=True)
    hm_sve_svt_run = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Holter Supraventricular Ectopy: SVT Runs', blank=True)
    hm_sve_beat = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Holter Supraventricular Ectopy: Beats', blank=True)
    hm_sve_long = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Holter Supraventricular Ectopy: Longest', blank=True)
    hm_sve_fast = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Holter Supraventricular Ectopy: Fastest (bpm)', blank=True)
    hm_sve_atr_pair = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Holter Supraventricular Ectopy: Atrial Pairs (Events)', blank=True)
    hm_sve_long_rr = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Holter Supraventricular Ectopy: Longest R-R (Longest Pause/sec)', blank=True)
    hm_sve_max_sve_min = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Holter Supraventricular Ectopy: Max SVE/Minute (Beats)', blank=True)
    hm_sve_max_sve_hour = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Holter Supraventricular Ectopy: Max SVE/Hour (Beats)', blank=True)
    hm_sve_mean_sve_hour = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Holter Supraventricular Ectopy: Mean SVE/Hour (Beats)', blank=True)
    hm_sve_sve_1000 = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Holter Supraventricular Ectopy: SVE/1000 (% of rhythm)', blank=True)
    hm_summary = models.IntegerField(help_text=u'', null=True, verbose_name=u'Holter Monitor Interpretation: Heart rate interpretation', blank=True, choices=[(1, u'Normal'), (2, u'Abnormal'), (3, u'Increased vagal tone'), (4, u'Increased sympathetic tone')]) # This field type is a guess
    hm_brady_percent = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Holter Monitor Interpretation: Bradycardia % of rhythm', blank=True)
    hm_avblock_percent = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Holter Monitor Interpretation: AV Block', choices=[(1, u'None'), (2, u'First degree'), (3, u'Second degree'), (4, u'Third degree')])
    hm_pr_interval = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Holter Monitor Interpretation: PR Interval', blank=True)
    hm_qrs_interval = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Holter Monitor Interpretation: QRS Interval', blank=True)
    hm_qtc_interval = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Holter Monitor Interpretation: QTc Interval', blank=True)
    hm_addit_info = models.TextField(help_text=u'', null=True, verbose_name=u'Holter Monitor Interpretation: Additional information ', blank=True) # This field type is a guess
    holterresult = models.ForeignKey(HolterResult)

    class Meta:
	 db_table = 'hm'


class CmriResult(models.Model):
    cmri_done = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Cardiac MRI done', choices=[(1, u'Yes'), (2, u'No')])
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'cmriresult'


class CardiacMri(models.Model):
    cmri_enrollment = models.IntegerField(help_text=u'', null=True, verbose_name=u'How would you categorize the cardiac MRI | Other test category', blank=True, choices=[(1, u'Initial test'), (2, u'Enrollment test'), (3, u'Post-enrollment test'), (4, u'Other')]) # This field type is a guess
    cmri_date = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Date of Cardiac MRI', blank=True)
    cmri_hypertrophy_loc = models.IntegerField(help_text=u'', null=True, verbose_name=u'Location of Hypertrophy | Location of Hypertrophy Other - Specify', blank=True, choices=[(1, u'Septal'), (2, u'Apical'), (3, u'Concentric'), (4, u'Other')]) # This field type is a guess
    cmri_summary = models.TextField(help_text=u'', null=True, verbose_name=u'Cardiac MRI Summary/Final report', blank=True) # This field type is a guess
    cmri_evidence_summary = models.CharField(help_text=u'6, None | 1, HCM- Hypertrophic cardiomyopathy | 2, LE- Myocardial late enhancement | 3, ARVD/C- Arrhythmogenic right ventricular dysplasia/cardiomyopathy | 4, LVNC- Left ventricular noncompaction | 5, DCM- Dilated cardiomyopathy', null=True, max_length=2000, verbose_name=u'Cardiac MRI Summary showed evidence of ', blank=True)
    cmriresult = models.ForeignKey(CmriResult)

    class Meta:
	 db_table = 'cardiacmri'


class cmrievidence(models.Model):
    label = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Cardiac MRI Summary showed evidence of ', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Cardiac MRI Summary showed evidence of ', choices=[(6, u'None'), (1, u'HCM- Hypertrophic cardiomyopathy'), (2, u'LE- Myocardial late enhancement'), (3, u'ARVD/C- Arrhythmogenic right ventricular dysplasia/cardiomyopathy'), (4, u'LVNC- Left ventricular noncompaction'), (5, u'DCM- Dilated cardiomyopathy')])
    cardiacmri = models.ForeignKey(CardiacMri)

    class Meta:
	 db_table = 'cmrievidence'


class CardiacCathProcedure(models.Model):
    ccath_done = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Cardiac catheterization done', choices=[(1, u'Yes'), (2, u'No')])
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'cardiaccathprocedure'


class CardiacCatherization(models.Model):
    ccath_enrollment = models.IntegerField(help_text=u'', null=True, verbose_name=u'How would you categorize the cardiac catherization | Other procedure category', blank=True, choices=[(1, u'Initial test'), (2, u'Enrollment test'), (3, u'Post-enrollment test'), (4, u'Other')]) # This field type is a guess
    ccath_date = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Date of Cardiac cathertization', blank=True)
    ccath_summary = models.TextField(help_text=u'', null=True, verbose_name=u'Cardiac catherization summary', blank=True) # This field type is a guess
    cardiaccathprocedure = models.ForeignKey(CardiacCathProcedure)

    class Meta:
	 db_table = 'cardiaccatherization'


class CardiacSurgery(models.Model):
    cardsurg_done = models.IntegerField(max_length=2000, blank=True, help_text=u'', null=True, verbose_name=u'Cardiac surgery done', choices=[(1, u'Yes'), (2, u'No')])
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'cardiacsurgery'


class CardiacSurgery2(models.Model):
    cardsurg_enrollment = models.IntegerField(help_text=u'', null=True, verbose_name=u'How would you categorize the cardiac surgery | Other procedure category', blank=True, choices=[(1, u'Initial test'), (2, u'Enrollment test'), (3, u'Post-enrollment test'), (4, u'Other')]) # This field type is a guess
    cardsurg_date = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Date of cardiac surgery', blank=True)
    cardsurg_name = models.CharField(help_text=u'', null=True, max_length=2000, verbose_name=u'Name of cardiac surgery', blank=True)
    cardsurg_summary = models.TextField(help_text=u'', null=True, verbose_name=u'cardiac surgery summary', blank=True) # This field type is a guess
    cardiacsurgery = models.ForeignKey(CardiacSurgery)

    class Meta:
	 db_table = 'cardiacsurgery2'


