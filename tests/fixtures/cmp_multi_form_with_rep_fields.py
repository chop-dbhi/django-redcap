from django.db import models

class Record(models.Model):

    class Meta:
	 db_table = 'record'


class Demographic(models.Model):
    study_id = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Study ID', blank=True)
    gender = models.IntegerField(help_text='', null=True, verbose_name='Gender', blank=True, choices=[(0, 'Female'), (1, 'Male'), (2, 'Other')]) # This field type is a guess
    other_gender = models.IntegerField(help_text='Newborn Screening LTFU', null=True, verbose_name='Other gender | Please specify  gender', blank=True, choices=[(1, 'Not tested'), (2, 'XX genotype/Female'), (3, 'XY genotype/Male'), (4, "XXY Klinefelter's Syndrome"), (5, "XO Turner's Syndrome"), (6, 'XXXY syndrome'), (7, 'XXYY syndrome'), (8, 'Mosaic including XXXXY'), (9, 'Penta X syndrome'), (10, 'XYY'), (11, 'Unknown'), (12, 'Other')]) # This field type is a guess
    year_of_birth = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Year of birth (XXXX)', blank=True)
    ethnicity = models.IntegerField(help_text='', null=True, verbose_name='Ethnicity', blank=True, choices=[(1, 'Non-Hispanic'), (2, 'Hispanic or Latino'), (3, 'Unknown')]) # This field type is a guess
    ethnicity_followup = models.IntegerField(help_text='', null=True, verbose_name='Ethnicity follow-up', blank=True, choices=[(1, 'Ashkenazi Jewish'), (2, 'Amish'), (3, 'French Canadian'), (4, 'None of the above'), (5, 'Unknown')]) # This field type is a guess
    demographics_feedback = models.TextField(help_text='', null=True, verbose_name='Please provide any feedback for this form (for example: missing questions, questions not relevant for a disease area, ambiguities, places where a textbox could be replaced with discrete choices, missing discrete choices)', blank=True) # This field type is a guess
    race_summary = models.CharField(help_text='1, White | 2, Black or African American | 3, American Indian or Alaska Native | 4, Native Hawaiian or Other Pacific Islander | 5, Asian | 6, More than one race | 7, Unknown or Not reported', null=True, max_length=2000, verbose_name='Race', blank=True)
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'demographic'


class race(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Race', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Race', choices=[(1, 'White'), (2, 'Black or African American'), (3, 'American Indian or Alaska Native'), (4, 'Native Hawaiian or Other Pacific Islander'), (5, 'Asian'), (6, 'More than one race'), (7, 'Unknown or Not reported')])
    demographic = models.ForeignKey(Demographic)

    class Meta:
	 db_table = 'race'


class PediseqStudyId(models.Model):
    family_code = models.FloatField(help_text='', null=True, verbose_name='Family Code', blank=True)
    family_member_code = models.CharField(help_text='P - Proband, S - Sibling, M - Mother, F - Father', null=True, max_length=2000, verbose_name='Family Member', blank=True)
    other_family_member = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Other family member', blank=True)
    affected_status = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Affected Status', blank=True)
    validation_or_prospective = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Validation or Prospective', blank=True)
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'pediseqstudyid'


class StudyId(models.Model):
    original_study_id = models.CharField(help_text="Enter the subject's ID from the original consenting study (HLS, Mito, etc.)", null=True, max_length=2000, verbose_name='Original Study ID', blank=True)
    discarded_clinical = models.NullBooleanField(help_text='', verbose_name='Discarded Clinical Specimen?', blank=True)
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'studyid'


class BirthHistory(models.Model):
    birthweight = models.TextField(help_text='Please indicate out to one decimal place unless units are lbs. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name='Birthweight', blank=True) # This field type is a guess
    birth_length = models.TextField(help_text='Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name='Birth length', blank=True) # This field type is a guess
    birth_head_circumference = models.FloatField(help_text='Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name='Birth head circumference (cm)', blank=True)
    gestational_age_wks = models.IntegerField(help_text='Specify partial week in days below. If full term but exact month and days are unknown, specify 40 weeks and 0 days.', null=True, verbose_name='Gestational age full weeks', blank=True)
    gestational_age_days = models.IntegerField(help_text='', null=True, verbose_name='Gestation age days', blank=True)
    mother_birth_age = models.CharField(help_text='Please round up if the age is 6 months or more into the current year.', null=True, max_length=2000, verbose_name="Mother's age when child was born (years)", blank=True)
    gravida = models.IntegerField(help_text='', null=True, verbose_name='Gravida\n(Number of prior gestations including proband)', blank=True)
    para = models.IntegerField(help_text='', null=True, verbose_name='Para\n(Number of live births including the proband)', blank=True)
    assisted_reproduction_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Was any type of assisted reproduction (for example sperm donation, in vitro fertilization) used in the pregnancy for this child?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    assisted_reproduction_spec = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Please specify type of assisted reproduction', blank=True)
    miscarriages_no = models.IntegerField(help_text='', null=True, verbose_name='Number of spontaneous miscarriages', blank=True)
    still_births_no = models.IntegerField(help_text='', null=True, verbose_name='Number of still births', blank=True)
    terminations_no = models.IntegerField(help_text='', null=True, verbose_name='Number of terminations', blank=True)
    multiples_no = models.IntegerField(help_text='', null=True, verbose_name='Number of multiple births', blank=True)
    pn_exposure_med = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Medications during pregnancy', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ultrasound_no = models.IntegerField(help_text='', null=True, verbose_name='How many ultrasound tests do you want to enter?', blank=True)
    ultrasound_increased_reason = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Reason for increased number of ultrasounds?', blank=True)
    pn_exposure_alc_spec = models.TextField(help_text='', null=True, verbose_name='Specify prenatal alcohol exposure\n(Alcohol amount, time of exposure, duration of exposure)', blank=True) # This field type is a guess
    pn_exposure_tob_spec = models.TextField(help_text='', null=True, verbose_name='Specify prenatal tobacco exposures\n(Tobacco amount, time of exposure, duration of exposure)', blank=True) # This field type is a guess
    pn_exposure_inf_spec = models.TextField(help_text='', null=True, verbose_name='Specify prenatal infection exposures\n(Infection, time of exposure, duration of exposure, treatment)', blank=True) # This field type is a guess
    maternal_screening = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Maternal serum screening', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not performed'), (5, 'Not determined'), (4, 'Unknown/Not documented')])
    maternal_serum_type = models.TextField(help_text='', null=True, verbose_name='Type of maternal serum screening', blank=True) # This field type is a guess
    maternal_serum_spec = models.TextField(help_text='', null=True, verbose_name='Maternal serum screening revealed', blank=True) # This field type is a guess
    cvs = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='CVS', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not performed'), (6, 'Not determined'), (5, 'Recommended but declined'), (4, 'Unknown/Not documented')])
    cvs_spec = models.TextField(help_text='', null=True, verbose_name='CVS revealed', blank=True) # This field type is a guess
    amniocentesis = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Amniocentesis', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not performed'), (6, 'Not determined'), (5, 'Recommended but declined'), (4, 'Unknown/Not documented')])
    amniocentesis_spec = models.TextField(help_text='', null=True, verbose_name='Amniocentesis revealed', blank=True) # This field type is a guess
    fetal_activity = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Fetal activity was', choices=[(1, 'Normal'), (2, 'Reduced'), (3, 'Unknown/Not documented')])
    apgar_1 = models.IntegerField(help_text='', null=True, verbose_name='Apgar score at 1 minute of life', blank=True, choices=[(1, '0'), (2, '1'), (3, '2'), (4, '3'), (5, '4'), (6, '5'), (7, '6'), (8, '7'), (9, '8'), (10, '9'), (11, '10'), (12, 'Not performed'), (13, 'Unknown/Not documented')]) # This field type is a guess
    apgar_5 = models.IntegerField(help_text='', null=True, verbose_name='Apgar score at 5 minutes of life', blank=True, choices=[(1, '0'), (2, '1'), (3, '2'), (4, '3'), (5, '4'), (6, '5'), (7, '6'), (8, '7'), (9, '8'), (10, '9'), (11, '10'), (12, 'Not performed'), (13, 'Unknown/Not documented')]) # This field type is a guess
    neonatal_complications_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Neonatal complications', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    neonatal_complications_spec = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Neonatal complications included', blank=True)
    newborn_hearing_screen = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Newborn hearing screening', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not performed'), (5, 'Not determined'), (4, 'Unknown/Not document')])
    newborn_hearing_screen_ears_failed = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Failed ear', choices=[(1, 'Left'), (2, 'Right'), (3, 'Both'), (4, 'Unknown/Not documented')])
    newborn_metabolic_screening = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Newborn metabolic screening', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not performed'), (5, 'Not determined'), (4, 'Unknown/Not documented')])
    newborn_metabolic_screening_spec = models.TextField(help_text='', null=True, verbose_name='Describe abnormal newborn metabolic screening', blank=True) # This field type is a guess
    dol_went_home = models.FloatField(help_text='', null=True, verbose_name='Baby went home on day of life ', blank=True)
    birth_history_feedback = models.TextField(help_text='', null=True, verbose_name='Please provide any feedback for this form (for example: missing questions, questions not relevant for a disease area, ambiguities, places where a textbox could be replaced with discrete choices, missing discrete choices)', blank=True) # This field type is a guess
    prior_pregnancy_history_summary = models.CharField(help_text='5, None | 1, spontaneous miscarriages | 2, still births | 3, terminations | 4, multiples (twins, triples) | 6, Unknown/Not documented', null=True, max_length=2000, verbose_name='Did the mother have any of the following', blank=True)
    pregnancy_complications_summary = models.CharField(help_text='10, None | 1, Bleeding | 2, Eclampsia | 3, Pre-eclampsia | 4, Gestational diabetes | 5, Maternal seizures | 6, Maternal hypertension | 7, Polyhydramnios | 8, Oligohydramnios | 9, Preterm labor  | 11, Unknown/Not documented | 12, Other', null=True, max_length=2000, verbose_name='Pregnancy complications', blank=True)
    pn_exposure_summary = models.CharField(help_text='6, None | 1, Recreational drugs | 2, Alcohol | 3, Tobacco | 4, Infection | 5, Unknown/Not documented | 7, Other unknown exposures | 8, Other known exposures (specify below)', null=True, max_length=2000, verbose_name='Prenatal exposures', blank=True)
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'birthhistory'


class priorpregnancyhistory(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Did the mother have any of the following', blank=True)
    value = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Did the mother have any of the following', blank=True)
    birthhistory = models.ForeignKey(BirthHistory)

    class Meta:
	 db_table = 'priorpregnancyhistory'


class pregnancycomplications(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Pregnancy complications', blank=True)
    value = models.IntegerField(help_text='', null=True, verbose_name='Pregnancy complications', blank=True, choices=[(10, 'None'), (1, 'Bleeding'), (2, 'Eclampsia'), (3, 'Pre-eclampsia'), (4, 'Gestational diabetes'), (5, 'Maternal seizures'), (6, 'Maternal hypertension'), (7, 'Polyhydramnios'), (8, 'Oligohydramnios'), (9, 'Preterm labor'), (11, 'Unknown/Not documented'), (12, 'Other')]) # This field type is a guess
    birthhistory = models.ForeignKey(BirthHistory)

    class Meta:
	 db_table = 'pregnancycomplications'


class pnexposure(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Prenatal exposures', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Prenatal exposures', choices=[(6, 'None'), (1, 'Recreational drugs'), (2, 'Alcohol'), (3, 'Tobacco'), (4, 'Infection'), (5, 'Unknown/Not documented'), (7, 'Other unknown exposures'), (8, 'Other known exposures (specify below)')])
    birthhistory = models.ForeignKey(BirthHistory)

    class Meta:
	 db_table = 'pnexposure'


class Miscarriage(models.Model):
    miscarriages_gestational_age = models.TextField(help_text='', null=True, verbose_name='Gestational age of miscarriage', blank=True) # This field type is a guess
    birthhistory = models.ForeignKey(BirthHistory)

    class Meta:
	 db_table = 'miscarriage'


class StillBirth(models.Model):
    still_births_gestational_age = models.TextField(help_text='', null=True, verbose_name='Gestational age of still birth', blank=True) # This field type is a guess
    birthhistory = models.ForeignKey(BirthHistory)

    class Meta:
	 db_table = 'stillbirth'


class Termination(models.Model):
    terminations_gestational_age = models.TextField(help_text='', null=True, verbose_name='Gestational age of termination', blank=True) # This field type is a guess
    birthhistory = models.ForeignKey(BirthHistory)

    class Meta:
	 db_table = 'termination'


class MultipleBirth(models.Model):
    multiple_number = models.IntegerField(help_text='', null=True, verbose_name='Number of children in multiple birth', blank=True)
    multiple_gestational_age = models.TextField(help_text='', null=True, verbose_name='Gestation age of multiple birth', blank=True) # This field type is a guess
    birthhistory = models.ForeignKey(BirthHistory)

    class Meta:
	 db_table = 'multiplebirth'


class PrenatalMedication(models.Model):
    pn_med = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Specify prenatal medication', blank=True)
    birthhistory = models.ForeignKey(BirthHistory)

    class Meta:
	 db_table = 'prenatalmedication'


class Ultrasound(models.Model):
    ultrasound_weeks_gestation_drop = models.IntegerField(help_text='', null=True, verbose_name='ultrasound performed at (weeks gestation)', blank=True, choices=[(39, 'Unknown'), (1, '4 weeks + 1 day to 5 weeks'), (2, '5 weeks + 1 day to 6 weeks'), (3, '6 weeks + 1 day to 7 weeks'), (4, '7 weeks + 1 day to 8 weeks'), (5, '8 weeks + 1 day to 9 weeks'), (6, '9 weeks + 1 day to 10 weeks'), (7, '10 weeks + 1 day to 11 weeks'), (8, '11 weeks + 1 day to 12 weeks'), (9, '12 weeks + 1 day to 13 weeks'), (10, '13 weeks + 1 day to 14 weeks'), (11, '14 weeks + 1 day to 15 weeks'), (12, '15 weeks + 1 day to 16 weeks'), (13, '16 weeks + 1 day to 17 weeks'), (14, '17 weeks + 1 day to 18 weeks'), (15, '18 weeks + 1 day to 19 weeks'), (16, '19 weeks + 1 day to 20 weeks'), (17, '20 weeks + 1 day to 21 weeks'), (18, '21 weeks + 1 day to 22 weeks'), (19, '22 weeks + 1 day to 23 weeks'), (20, '23 weeks + 1 day to 24 weeks'), (21, '24 weeks + 1 day to 25 weeks'), (22, '25 weeks + 1 day to 26 weeks'), (23, '26 weeks + 1 day to 27 weeks'), (24, '27 weeks + 1 day to 28 weeks'), (25, '28 weeks + 1 day to 29 weeks'), (26, '29 weeks + 1 day to 30 weeks'), (27, '30 weeks + 1 day to 31 weeks'), (28, '31 weeks + 1 day to 32 weeks'), (29, '32 weeks + 1 day to 33 weeks'), (30, '33 weeks + 1 day to 34 weeks'), (31, '34 weeks + 1 day to 25 weeks'), (32, '35 weeks + 1 day to 36 weeks'), (33, '36 weeks + 1 day to 37 weeks'), (34, '37 weeks + 1 day to 38 weeks'), (35, '38 weeks + 1 day to 39 weeks'), (36, '39 weeks + 1 day to 40 weeks'), (37, '40 weeks + 1 day to 41 weeks'), (38, '41 weeks + 1 day to 42 weeks')]) # This field type is a guess
    ultrasound_normal_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='ultrasound within normal limits', choices=[(1, 'Yes'), (2, 'No'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    ultrasound_spec = models.TextField(help_text='', null=True, verbose_name='ultrasound significant for', blank=True) # This field type is a guess
    birthhistory = models.ForeignKey(BirthHistory)

    class Meta:
	 db_table = 'ultrasound'


class RecreationalDrugExposure(models.Model):
    pn_exposure_drug = models.CharField(help_text='(Drug, Drug amount, time of exposure, duration of pregnancy)', null=True, max_length=2000, verbose_name='Specify prenatal recreational drug exposure', blank=True)
    birthhistory = models.ForeignKey(BirthHistory)

    class Meta:
	 db_table = 'recreationaldrugexposure'


class PrenatalExposure(models.Model):
    pn_exposure_other_spec = models.CharField(help_text='(exposure, exposure amount, time of exposure, duration of pregnancy)', null=True, max_length=2000, verbose_name='Specify other prenatal exposure', blank=True)
    birthhistory = models.ForeignKey(BirthHistory)

    class Meta:
	 db_table = 'prenatalexposure'


class PriorGeneticTesting(models.Model):
    karyotype_date = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year of Karyotype', blank=True)
    karyotype_tissue = models.IntegerField(help_text='', null=True, verbose_name='Karyotype tissue studied | Specify other tissue studied', blank=True, choices=[(1, 'Amniotic fluid'), (2, 'Blood'), (3, 'Chorionic villi'), (4, 'Fibroblasts'), (5, 'Saliva'), (6, 'Unknown/Not documented'), (7, 'Other')]) # This field type is a guess
    karyotype_result = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Karyotype result', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    karyotype_spec = models.TextField(help_text='', null=True, verbose_name='Specify other karyotype abnormalities', blank=True) # This field type is a guess
    karyotype_location = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Lab where Karyotype was performed', blank=True)
    mito_analysis_type = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='What type(s) of mitochondrial DNA analysis was performed?', choices=[(1, 'Target point mutation analysis (without deletion analysis)'), (2, 'Whole mitochondrial genome sequencing'), (3, 'Deletion analysis (without targetted point mutation analysis)'), (4, 'Combination deletion and targetted mutation analysis panel'), (5, 'Other')])
    fragx_type = models.IntegerField(max_length=2000, blank=True, help_text='Example: GNE1 or 15q11', null=True, verbose_name='What were the results of the Fragile X testing?', choices=[(1, 'Full Mutation'), (2, 'Pre-Mutation'), (3, 'Normal'), (6, 'Inconclusive'), (5, 'Result not known'), (4, 'Results pending')])
    cardiac_gene_test_done = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Previous cardiac genetic testing done', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    cardiac_gene_sent_out = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Previous cardiac genetic testing sent to outside lab', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    cardiac_gene_lab = models.IntegerField(help_text='', null=True, verbose_name='Outside Lab test done at | Outside lab Other - Specify', blank=True, choices=[(1, 'Familion (Transgenomics)'), (2, 'Gene Dx'), (3, 'Harvard Partners'), (4, 'Medical Genetics Laboratories at Baylor College of Medicine'), (5, "Heart Institute Diagnostic Lab at Cincinnati Children's Hospital"), (7, 'Uknown/Not doucmented'), (6, 'Other')]) # This field type is a guess
    cardiac_gene_summary = models.TextField(help_text='', null=True, verbose_name='Previous Genetic testing results summary', blank=True) # This field type is a guess
    other_genetic_testing_spec = models.TextField(help_text='', null=True, verbose_name='Describe other genetic tests performed', blank=True) # This field type is a guess
    prior_genetic_testing_feedback = models.TextField(help_text='', null=True, verbose_name='Please provide any feedback for this form (for example: missing questions, questions not relevant for a disease area, ambiguities, places where a textbox could be replaced with discrete choices, missing discrete choices)', blank=True) # This field type is a guess
    genetic_tests_performed_summary = models.CharField(help_text=' 6, None | 1, Karyotype | 2, Microarray | 3, Sequence analysis of a single nuclear gene or group of nuclear genes | 8, Deletion or duplication analysis of a single nuclear gene or group of nuclear genes | 4, Nuclear exome/Genome sequencing | 5, Mitochondrial DNA analysis | 9, Methylation analysis | 10, Testing for Fragile X Syndrome | 7, Other', null=True, max_length=2000, verbose_name='Genetic tests performed', blank=True)
    karyotype_result_details_summary = models.CharField(help_text='1, Balanced reciprocal translocation | 2, Balanced Robertsonian translocation | 3, Delete | 4, Duplication | 5, Extra marker chromosome | 6, Trisomy 13 | 7, Trisomy 18 | 8, 22q11 deletion | 9, 45,  X | 10, 47, XXX | 11, 47, XXY | 12, 47, XYY | 13, Paracentric inversion | 14, Pericentric inversion | 15, Structural X chromosome | 16, Structural Y chromosome | 17, Unbalanced reciprocal translocation | 18, Unbalanced Robertsonian translocation | 19, Other', null=True, max_length=2000, verbose_name='Specify karyotype abnormalities', blank=True)
    gene_or_panel_summary = models.CharField(help_text='1, Single genes | 2, Gene panels', null=True, max_length=2000, verbose_name='Was the sequencing testing performed on single genes or gene panels (containing multiple genes)?', blank=True)
    targeted_mito_single_or_panel_summary = models.CharField(help_text='1, Single mutations | 2, Mutation Panels', null=True, max_length=2000, verbose_name='Was the targeted mutation analysis for single mutations or mutation panels?', blank=True)
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'priorgenetictesting'


class genetictestsperformed(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Genetic tests performed', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Genetic tests performed', choices=[(6, 'None'), (1, 'Karyotype'), (2, 'Microarray'), (3, 'Sequence analysis of a single nuclear gene or group of nuclear genes'), (8, 'Deletion or duplication analysis of a single nuclear gene or group of nuclear genes'), (4, 'Nuclear exome/Genome sequencing'), (5, 'Mitochondrial DNA analysis'), (9, 'Methylation analysis'), (10, 'Testing for Fragile X Syndrome'), (7, 'Other')])
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'genetictestsperformed'


class karyotyperesultdetails(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Specify karyotype abnormalities', blank=True)
    value = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Specify karyotype abnormalities', blank=True)
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'karyotyperesultdetails'


class geneorpanel(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Was the sequencing testing performed on single genes or gene panels (containing multiple genes)?', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Was the sequencing testing performed on single genes or gene panels (containing multiple genes)?', choices=[(1, 'Single genes'), (2, 'Gene panels')])
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'geneorpanel'


class targetedmitosingleorpanel(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Was the targeted mutation analysis for single mutations or mutation panels?', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Was the targeted mutation analysis for single mutations or mutation panels?', choices=[(1, 'Single mutations'), (2, 'Mutation Panels')])
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'targetedmitosingleorpanel'


class Microarray(models.Model):
    microarray_date = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year of microarray', blank=True)
    microarray_type = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Microarray type', choices=[(1, 'Oligonucleotide by aCGH'), (2, 'SNP'), (3, 'Targeted BAC'), (4, 'Whole genomic BAC'), (5, 'Unknown'), (6, 'Other')])
    microarray_type_spec = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Specify microarray type', blank=True)
    microarray_platform = models.IntegerField(help_text='', null=True, verbose_name='microarray platform | Specify microarray platform', blank=True, choices=[(1, 'Affymetrix'), (2, 'Agilent'), (3, 'Illumina'), (4, 'Nimblegen'), (5, 'Unknown/Not documented'), (6, 'Other')]) # This field type is a guess
    microarray_location = models.IntegerField(help_text='', null=True, verbose_name='Which laboratory performed microarray? | Specify microarray lab', blank=True, choices=[(1, 'Baylor'), (2, 'Provential'), (3, 'GeneDX'), (4, 'Transgenomic Familion'), (7, 'CHOP'), (5, 'Unknown'), (6, 'Other')]) # This field type is a guess
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'microarray'


class Variant(models.Model):
    variant_type = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Type of variant on microarray', choices=[(1, 'Deletion'), (2, 'Duplication'), (3, 'Run of homozygosity'), (4, 'Unknown')])
    variant_chromosome = models.IntegerField(help_text='', null=True, verbose_name='variant (on microarray) on chromosome', blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, 'X'), (24, 'Y')]) # This field type is a guess
    microarray = models.ForeignKey(Microarray)

    class Meta:
	 db_table = 'variant'


class GeneTest(models.Model):
    gene_result = models.CharField(help_text='Example: GNE1  Note: Results from gene panels should be entered under gene panel section.', null=True, max_length=2000, verbose_name='Gene tested $d', blank=True)
    gene_result_was_summary = models.CharField(help_text='1, Positive - disease-causing mutation identified | 2, Negative - no definite/possible disease-causing mutation identified | 3, Variant of uncertain significance | 6, Polymorphism | 4, Results pending | 5, Results not known', null=True, max_length=2000, verbose_name='Indicate ALL types of results identified in gene $d', blank=True)
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'genetest'


class generesultwas(models.Model):
    label = models.CharField(help_text='For example, if testing showed both a disease-causing mutation and a polymorphism, check positive and polymorphism.', null=True, max_length=2000, verbose_name='Indicate ALL types of results identified in gene $d', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='For example, if testing showed both a disease-causing mutation and a polymorphism, check positive and polymorphism.', null=True, verbose_name='Indicate ALL types of results identified in gene $d', choices=[(1, 'Positive - disease-causing mutation identified'), (2, 'Negative - no definite/possible disease-causing mutation identified'), (3, 'Variant of uncertain significance'), (6, 'Polymorphism'), (4, 'Results pending'), (5, 'Results not known')])
    genetest = models.ForeignKey(GeneTest)

    class Meta:
	 db_table = 'generesultwas'


class Mutation(models.Model):
    change_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for disease causing mutation (on gene test)', blank=True)
    change_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change  at protein level for disease causing mutation (on gene test)', blank=True)
    genetest = models.ForeignKey(GeneTest)

    class Meta:
	 db_table = 'mutation'


class VariantOfUnknownSignificance(models.Model):
    vus_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='variant of unknown significance at cDNA level (on gene test)', blank=True)
    vus_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='variant of unknown significance at protein level (on gene test)', blank=True)
    genetest = models.ForeignKey(GeneTest)

    class Meta:
	 db_table = 'variantofunknownsignificance'


class GenePanel(models.Model):
    gene_panel = models.CharField(help_text='For example, cardiomyopathy panel or hearing loss panel', null=True, max_length=2000, verbose_name='Name of gene panel performed', blank=True)
    panel_laboratory = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Which laboratory performed gene panel?', blank=True)
    panel_date_performed = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year panel was performed', blank=True)
    panel_list_gene = models.IntegerField(max_length=2000, blank=True, help_text='Optional', null=True, verbose_name='Would you like to list the genes that were on the panel?', choices=[(1, 'Yes'), (2, 'No')])
    panel_list_gene_entry = models.CharField(help_text='Example: PTPN11, HRAS, SOS1', null=True, max_length=2000, verbose_name='List genes on this panel (Separate with commas)', blank=True)
    panel_result_type_summary = models.CharField(help_text='1, Positive - disease-causing mutation identified | 2, Negative - no definite/possible disease-causing mutation identified | 3, Variant of uncertain significance | 4, Polymorphism | 5, Results pending | 6, Results not known', null=True, max_length=2000, verbose_name='Indicate ALL types of results identified on panel. ', blank=True)
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'genepanel'


class panelresulttype(models.Model):
    label = models.CharField(help_text='For example, if testing showed both a disease-causing mutation and a polymorphism, check positive and polymorphism.', null=True, max_length=2000, verbose_name='Indicate ALL types of results identified on panel. ', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='For example, if testing showed both a disease-causing mutation and a polymorphism, check positive and polymorphism.', null=True, verbose_name='Indicate ALL types of results identified on panel. ', choices=[(1, 'Positive - disease-causing mutation identified'), (2, 'Negative - no definite/possible disease-causing mutation identified'), (3, 'Variant of uncertain significance'), (4, 'Polymorphism'), (5, 'Results pending'), (6, 'Results not known')])
    genepanel = models.ForeignKey(GenePanel)

    class Meta:
	 db_table = 'panelresulttype'


class Gene(models.Model):
    gene_result = models.CharField(help_text='Example: GNE1', null=True, max_length=2000, verbose_name='gene tested on gene panel', blank=True)
    genepanel = models.ForeignKey(GenePanel)

    class Meta:
	 db_table = 'gene'


class Dcm(models.Model):
    change_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for disease-causing mutation on gene on gene panel ', blank=True)
    change_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for disease-causing mutation on gene on gene panel ', blank=True)
    gene = models.ForeignKey(Gene)

    class Meta:
	 db_table = 'dcm'


class VariantOfUnknownSignificance2(models.Model):
    vus_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='variant of unknown significance at cDNA level on gene on gene panel', blank=True)
    vus_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='variant of unknown significance at protein level on gene on gene panel', blank=True)
    gene = models.ForeignKey(Gene)

    class Meta:
	 db_table = 'variantofunknownsignificance2'


class SingleGeneDeletionDuplicationTest(models.Model):
    deldup_result = models.CharField(help_text='Example: GNE1', null=True, max_length=2000, verbose_name='Gene tested $d', blank=True)
    type_deldup_test = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Type of deletion/duplication testing performed', choices=[(1, 'MLPA'), (2, 'FISH'), (3, 'Unknown'), (4, 'Other')])
    deldup_result_was_summary = models.CharField(help_text='1, Positive - disease-causing deletion/duplication identified | 2, Negative - no definite/possible disease-causing deletion/duplication identified | 3, Variant of uncertain significance | 6, Polymorphism | 4, Results pending | 5, Results not known', null=True, max_length=2000, verbose_name='Indicate ALL types of results identified in gene $d', blank=True)
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'singlegenedeletionduplicationtest'


class deldupresultwas(models.Model):
    label = models.CharField(help_text='For example, if testing showed both a disease-causing mutation and a polymorphism, check positive and polymorphism.', null=True, max_length=2000, verbose_name='Indicate ALL types of results identified in gene $d', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='For example, if testing showed both a disease-causing mutation and a polymorphism, check positive and polymorphism.', null=True, verbose_name='Indicate ALL types of results identified in gene $d', choices=[(1, 'Positive - disease-causing deletion/duplication identified'), (2, 'Negative - no definite/possible disease-causing deletion/duplication identified'), (3, 'Variant of uncertain significance'), (6, 'Polymorphism'), (4, 'Results pending'), (5, 'Results not known')])
    singlegenedeletionduplicationtest = models.ForeignKey(SingleGeneDeletionDuplicationTest)

    class Meta:
	 db_table = 'deldupresultwas'


class DeletionDuplication(models.Model):
    change_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Deletion/Duplication at cDNA level for disease causing mutation (on deletion duplication  test)', blank=True)
    change_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Deletion/Duplication  at protein level for disease causing mutation (on deletion/duplication gene test)', blank=True)
    change_add_info_deldup = models.CharField(help_text='Example: Expected to result in exon skipping of exon 3', null=True, max_length=2000, verbose_name='Additional Information about deletion/duplication (if available) (on deletion/duplication test)', blank=True)
    singlegenedeletionduplicationtest = models.ForeignKey(SingleGeneDeletionDuplicationTest)

    class Meta:
	 db_table = 'deletionduplication'


class VariantOfUnknownSignificance3(models.Model):
    vus_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='variant of unknown significance at cDNA level (on deletion/duplication test)', blank=True)
    vus_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='variant of unknown significance at protein level (on deletion/duplication test)', blank=True)
    vus_add_info_deldup = models.CharField(help_text='Example: Expected to result in exon skipping of exon 3', null=True, max_length=2000, verbose_name='Additional Information about deletion/duplication VUS (on deletion/duplication test) (if available)', blank=True)
    singlegenedeletionduplicationtest = models.ForeignKey(SingleGeneDeletionDuplicationTest)

    class Meta:
	 db_table = 'variantofunknownsignificance3'


class TargetedTest(models.Model):
    targeted_mito_single_test = models.CharField(help_text='', null=True, max_length=2000, verbose_name='targeted mutation tested ', blank=True)
    targeted_mito_single_test_result = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='What was the result of the single mutation targeted test?', choices=[(1, 'Positive'), (2, 'Negative')])
    targeted_mito_single_test_sample_summary = models.CharField(help_text='1, blood | 2, urine | 3, muscle | 4, saliva | 5, other', null=True, max_length=2000, verbose_name='Tissue type tested for single mutation targeted test', blank=True)
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'targetedtest'


class targetedmitosingletestsample(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Tissue type tested for single mutation targeted test', blank=True)
    value = models.IntegerField(help_text='', null=True, verbose_name='Tissue type tested for single mutation targeted test', blank=True, choices=[(1, 'blood'), (2, 'urine'), (3, 'muscle'), (4, 'saliva'), (5, 'other')]) # This field type is a guess
    targetedtest = models.ForeignKey(TargetedTest)

    class Meta:
	 db_table = 'targetedmitosingletestsample'


class MitochondrialPanel(models.Model):
    targeted_mito_panel_loc = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Laboratory that performed targeted mitochondrial panel', blank=True)
    targeted_mito_panel_date = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year targeted mitochondrial panel was performed', blank=True)
    targeted_mito_panel_type = models.CharField(help_text='', null=True, max_length=2000, verbose_name='What was the type of the targeted mitochondrial panel?', blank=True)
    targeted_mito_panel_results = models.IntegerField(help_text='', null=True, verbose_name='Results of targeted mitochondrial panel', blank=True, choices=[(1, 'Normal'), (2, 'Variant Positive')]) # This field type is a guess
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'mitochondrialpanel'


class Gene2(models.Model):
    gene = models.CharField(help_text='', null=True, max_length=2000, verbose_name='gene on targeted mitochondrial panel that contained mutation', blank=True)
    mitochondrialpanel = models.ForeignKey(MitochondrialPanel)

    class Meta:
	 db_table = 'gene2'


class MdnaChange(models.Model):
    mdna_change = models.CharField(help_text='', null=True, max_length=2000, verbose_name='change in mDNA on gene on targeted mitochondrial panel', blank=True)
    gene2 = models.ForeignKey(Gene2)

    class Meta:
	 db_table = 'mdnachange'


class MdnaVariantOfUnknownSignificance(models.Model):
    vus_mdna = models.CharField(help_text='', null=True, max_length=2000, verbose_name='variant of unknown significance on gene on  targeted mitochondrial panel', blank=True)
    mitochondrialpanel = models.ForeignKey(MitochondrialPanel)

    class Meta:
	 db_table = 'mdnavariantofunknownsignificance'


class WholeMitoGeneSeq(models.Model):
    whole_mito_sequencing_date = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year of whole mitochondrial genome sequencing', blank=True)
    whole_mito_sequencing_loc = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Lab where whole mitochondrial genome sequencing was performed', blank=True)
    whole_mito_sequencing_sample_summary = models.CharField(help_text='1, blood | 2, urine | 3, muscle | 4, saliva | 5, other', null=True, max_length=2000, verbose_name='Sample type for whole mitochondrial genome sequencing', blank=True)
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'wholemitogeneseq'


class wholemitosequencingsample(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Sample type for whole mitochondrial genome sequencing', blank=True)
    value = models.IntegerField(help_text='', null=True, verbose_name='Sample type for whole mitochondrial genome sequencing', blank=True, choices=[(1, 'blood'), (2, 'urine'), (3, 'muscle'), (4, 'saliva'), (5, 'other')]) # This field type is a guess
    wholemitogeneseq = models.ForeignKey(WholeMitoGeneSeq)

    class Meta:
	 db_table = 'wholemitosequencingsample'


class Mutation2(models.Model):
    dc_mutation_gene = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Gene in which disease causing mutation was located on whole mitochondrial sequencing', blank=True)
    dc_mutation_mdna_level = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Change at mDNA level for disease causing mutation on whole mitochondrial sequencing', blank=True)
    wholemitogeneseq = models.ForeignKey(WholeMitoGeneSeq)

    class Meta:
	 db_table = 'mutation2'


class VariantOfUnknownSignificance4(models.Model):
    vus_mdna_level = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Change at mDNA level for variant of unknown significance on whole mitochondrial sequencing', blank=True)
    wholemitogeneseq = models.ForeignKey(WholeMitoGeneSeq)

    class Meta:
	 db_table = 'variantofunknownsignificance4'


class WholeMitoDel(models.Model):
    mito_deletion_analsysis_date = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year of mitochondrial deletion analysis', blank=True)
    mito_deletion_analsysis_loc = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Lab where mitochondrial deletion analysis was performed', blank=True)
    mito_deletion_analsysis_sample_summary = models.CharField(help_text='1, blood | 2, urine | 3, muscle | 4, saliva | 5, other', null=True, max_length=2000, verbose_name='Sample type for mitochondrial deletion analysis', blank=True)
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'wholemitodel'


class mitodeletionanalsysissample(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Sample type for mitochondrial deletion analysis', blank=True)
    value = models.IntegerField(help_text='', null=True, verbose_name='Sample type for mitochondrial deletion analysis', blank=True, choices=[(1, 'blood'), (2, 'urine'), (3, 'muscle'), (4, 'saliva'), (5, 'other')]) # This field type is a guess
    wholemitodel = models.ForeignKey(WholeMitoDel)

    class Meta:
	 db_table = 'mitodeletionanalsysissample'


class Deletion(models.Model):
    dc_deletion = models.CharField(help_text='', null=True, max_length=2000, verbose_name='What was the disease causing deletion identified on mitochondrial deletion analysis?', blank=True)
    dc_deletion_spec = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Other details for disease causing deletion on mitochondrial deletion analysis', blank=True)
    wholemitodel = models.ForeignKey(WholeMitoDel)

    class Meta:
	 db_table = 'deletion'


class VariantOfUnknownSignificance5(models.Model):
    vus = models.CharField(help_text='', null=True, max_length=2000, verbose_name='variant of unknown significance on mitochondrial deletion analysis', blank=True)
    wholemitodel = models.ForeignKey(WholeMitoDel)

    class Meta:
	 db_table = 'variantofunknownsignificance5'


class MitoCombo(models.Model):
    mito_combo_analysis_date = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year of combination mitochondrial analysis', blank=True)
    mito_combo_analysis_loc = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Lab where combination mitochondrial analysis was performed', blank=True)
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'mitocombo'


class Deletion2(models.Model):
    mito_combo_analysis_sample_summary = models.CharField(help_text='1, blood | 2, urine | 3, muscle | 4, saliva | 5, other', null=True, max_length=2000, verbose_name='Sample type for mitochondrial deletion analysis (from combined analysis $d1)', blank=True)
    mitocombo = models.ForeignKey(MitoCombo)

    class Meta:
	 db_table = 'deletion2'


class mitocomboanalysissample(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Sample type for mitochondrial deletion analysis (from combined analysis $d1)', blank=True)
    value = models.IntegerField(help_text='', null=True, verbose_name='Sample type for mitochondrial deletion analysis (from combined analysis $d1)', blank=True, choices=[(1, 'blood'), (2, 'urine'), (3, 'muscle'), (4, 'saliva'), (5, 'other')]) # This field type is a guess
    deletion2 = models.ForeignKey(Deletion2)

    class Meta:
	 db_table = 'mitocomboanalysissample'


class Deletion3(models.Model):
    dc_deletion = models.CharField(help_text='', null=True, max_length=2000, verbose_name='What was the disease causing deletion identified on mitochondrial deletion analysis (from combined analysis)?', blank=True)
    dc_deletion_spec = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Other details for disease causing deletion on mitochondrial deletion analysis (from combined analysis)', blank=True)
    deletion2 = models.ForeignKey(Deletion2)

    class Meta:
	 db_table = 'deletion3'


class VariantOfUnknownSignificance6(models.Model):
    vus = models.CharField(help_text='', null=True, max_length=2000, verbose_name='variant of unknown significance on mitochondrial deletion analysis (from combined analysis)', blank=True)
    deletion2 = models.ForeignKey(Deletion2)

    class Meta:
	 db_table = 'variantofunknownsignificance6'


class Panel(models.Model):
    targeted_mito_combo_panel_type = models.CharField(help_text='', null=True, max_length=2000, verbose_name='panel performed (on combination analysis)?', blank=True)
    targeted_mito_combo_panel_results = models.TextField(help_text='', null=True, verbose_name='Describe results of panel (on combined analysis)', blank=True) # This field type is a guess
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'panel'


class Gene3(models.Model):
    gene = models.CharField(help_text='', null=True, max_length=2000, verbose_name='gene on panel that contained mutation (on combined analysis)', blank=True)
    panel = models.ForeignKey(Panel)

    class Meta:
	 db_table = 'gene3'


class MdnaChange2(models.Model):
    mdna_change = models.CharField(help_text='', null=True, max_length=2000, verbose_name='change in mDNA on gene on panel (on combined analysis)', blank=True)
    gene3 = models.ForeignKey(Gene3)

    class Meta:
	 db_table = 'mdnachange2'


class MdnaVariantOfUnknownSignificance2(models.Model):
    vus_mdna = models.CharField(help_text='', null=True, max_length=2000, verbose_name='variant of unknown significance on gene from panel (on combined analysis)', blank=True)
    panel = models.ForeignKey(Panel)

    class Meta:
	 db_table = 'mdnavariantofunknownsignificance2'


class MethylationAnalysisTest(models.Model):
    meth_gene_tested = models.CharField(help_text='Example: GNE1 or 15q11', null=True, max_length=2000, verbose_name='Gene/Region tested $d', blank=True)
    meth_cond_test = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Condition/s being tested for', blank=True)
    meth_result = models.IntegerField(max_length=2000, blank=True, help_text='For example, if testing showed both a disease-causing mutation and a polymorphism, check positive and polymorphism.', null=True, verbose_name='Indicate result methylation analysis identified in gene/region $d', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Inconclusive'), (5, 'Result not known'), (4, 'Results pending')])
    meth_add_info = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Additional Information about methylation testing  (if available)', blank=True)
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'methylationanalysistest'


class FragileXFullMutationRepeat(models.Model):
    fragx_full_mut = models.FloatField(help_text='', null=True, verbose_name='What was the size of the full mutation repeat?', blank=True)
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'fragilexfullmutationrepeat'


class FragileXPreMutationRepeat(models.Model):
    fragx_pre_mut = models.FloatField(help_text='', null=True, verbose_name='What was the size of the pre mutation repeat?', blank=True)
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'fragilexpremutationrepeat'


class FragileXNormalRepeat(models.Model):
    fragx_norm = models.FloatField(help_text='', null=True, verbose_name='What was the size of the normal repeat?', blank=True)
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'fragilexnormalrepeat'


class FragileXInconclusiveRepeat(models.Model):
    fragx_incon = models.FloatField(help_text='', null=True, verbose_name='What was the size of the inconclusive repeat?', blank=True)
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'fragilexinconclusiverepeat'


class PriorTesting(models.Model):
    prior_test_explain = models.TextField(help_text='', null=True, verbose_name="Many of the sections on this instrument ask if there is a history of abnormal results for a type of test. If you answer yes you can summarize the patient's result history by giving result value ranges. Regardless of whether there is a history of abnormal results you can also add results of individual tests and specify if each one was normal or abnormal. Please answer Yes or No to the history of abnormal results question, and then choose whether to summarize the results (if they were abnormal), enter results of individual tests, or if you have no specific data, skip both.", blank=True) # This field type is a guess
    blood_lactate_sum_bool = models.IntegerField(max_length=2000, blank=True, help_text='Answering yes will present a result summary section. This should be skipped if you would rather enter individual test results in the section below.', null=True, verbose_name='History of abnormal Blood Lactate results?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    blood_lactate_sum = models.TextField(help_text='', null=True, verbose_name='Blood Lactate range ', blank=True) # This field type is a guess
    blood_lactate_sum_comments = models.TextField(help_text='', null=True, verbose_name='Blood Lactate range result comment (quality concerns, normal range)', blank=True) # This field type is a guess
    blood_lactate_datapoints = models.NullBooleanField(help_text='', verbose_name='Would you like to enter individual Blood Lactate results?', blank=True)
    blood_pyruvate_sum_bool = models.IntegerField(max_length=2000, blank=True, help_text='Answering yes will present a result summary section. This should be skipped if you would rather enter individual test results in the section below.', null=True, verbose_name='History of abnormal Blood Pyruvate results?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    blood_pyruvate_sum = models.TextField(help_text='', null=True, verbose_name='Blood Pyruvate range ', blank=True) # This field type is a guess
    blood_pyruvate_sum_comments = models.TextField(help_text='', null=True, verbose_name='Blood Pyruvate range result comment (quality concerns, normal range)', blank=True) # This field type is a guess
    blood_pyruvate_datapoints = models.NullBooleanField(help_text='', verbose_name='Would you like to enter individual Blood Pyruvate results?', blank=True)
    csf_lactate_sum_bool = models.IntegerField(max_length=2000, blank=True, help_text='Answering yes will present a result summary section. This should be skipped if you would rather enter individual test results in the section below.', null=True, verbose_name='History of abnormal CSF Lactate results?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    csf_lactate_sum = models.TextField(help_text='', null=True, verbose_name='CSF Lactate range ', blank=True) # This field type is a guess
    csf_lactate_comments = models.TextField(help_text='', null=True, verbose_name='CSF Lactate range result comment (quality concerns, normal range)', blank=True) # This field type is a guess
    csf_lactate_datapoints = models.NullBooleanField(help_text='', verbose_name='Would you like to enter individual CSF Lactate results?', blank=True)
    csf_pyruvate_sum_bool = models.IntegerField(max_length=2000, blank=True, help_text='Answering yes will present a result summary section. This should be skipped if you would rather enter individual test results in the section below.', null=True, verbose_name='History of abnormal CSF Pyruvate results?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    csf_pyruvate_sum = models.TextField(help_text='', null=True, verbose_name='CSF Pyruvate range ', blank=True) # This field type is a guess
    csf_pyruvate_comments = models.CharField(help_text='', null=True, max_length=2000, verbose_name='CSF Pyruvate range result comment (quality concerns, normal range)', blank=True)
    csf_pyruvate_datapoints = models.NullBooleanField(help_text='', verbose_name='Would you like to enter individual CSF Pyruvate results?', blank=True)
    paa_sum_bool = models.IntegerField(max_length=2000, blank=True, help_text='Answering yes will present a result summary section. This should be skipped if you would rather enter individual test results in the section below.', null=True, verbose_name='History of abnormal PAA results?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    paa_sum = models.TextField(help_text='', null=True, verbose_name='PAA range ', blank=True) # This field type is a guess
    paa_comments = models.TextField(help_text='', null=True, verbose_name='PAA range result comment (quality concerns, normal range)', blank=True) # This field type is a guess
    paa_datapoints = models.NullBooleanField(help_text='', verbose_name='Would you like to enter individual PAA results?', blank=True)
    plasma_cn_acp_sum_bool = models.IntegerField(max_length=2000, blank=True, help_text='Answering yes will present a result summary section. This should be skipped if you would rather enter individual test results in the section below.', null=True, verbose_name='History of abnormal Plasma CN/ACP results?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    plasma_cn_acp_sum = models.TextField(help_text='', null=True, verbose_name='Plasma CN/ACP range ', blank=True) # This field type is a guess
    plasma_cn_acp_comments = models.TextField(help_text='', null=True, verbose_name='Plasma CN/ACP  range result comment (quality concerns, normal range)', blank=True) # This field type is a guess
    plasma_cn_acp_datapoints = models.NullBooleanField(help_text='', verbose_name='Would you like to enter individual Plasma CN/ACP results?', blank=True)
    uoa_sum_bool = models.IntegerField(max_length=2000, blank=True, help_text='Answering yes will present a result summary section. This should be skipped if you would rather enter individual test results in the section below.', null=True, verbose_name='History of abnormal UOA results?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    uoa_sum = models.TextField(help_text='', null=True, verbose_name='UOA range ', blank=True) # This field type is a guess
    uoa_comments = models.TextField(help_text='', null=True, verbose_name='UOA  range result comment (quality concerns, normal range)', blank=True) # This field type is a guess
    uoa_datapoints = models.NullBooleanField(help_text='', verbose_name='Would you like to enter individual UOA results?', blank=True)
    ck_sum_bool = models.IntegerField(max_length=2000, blank=True, help_text='Answering yes will present a result summary section. This should be skipped if you would rather enter individual test results in the section below.', null=True, verbose_name='History of abnormal CK results?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    ck_sum = models.TextField(help_text='', null=True, verbose_name='CK range ', blank=True) # This field type is a guess
    ck_comments = models.TextField(help_text='', null=True, verbose_name='CK range result comment (quality concerns, normal range)', blank=True) # This field type is a guess
    ck_datapoints = models.NullBooleanField(help_text='', verbose_name='Would you like to enter individual CK results?', blank=True)
    uric_acid_sum_bool = models.IntegerField(max_length=2000, blank=True, help_text='Answering yes will present a result summary section. This should be skipped if you would rather enter individual test results in the section below.', null=True, verbose_name='History of abnormal Uric acid results?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    uric_acid_sum = models.TextField(help_text='', null=True, verbose_name='Uric acid range ', blank=True) # This field type is a guess
    uric_acid_comments = models.TextField(help_text='', null=True, verbose_name='Uric acid range result comment (quality concerns, normal range)', blank=True) # This field type is a guess
    uric_acid_datapoints = models.NullBooleanField(help_text='', verbose_name='Would you like to enter individual Uric acid results?', blank=True)
    lfts_sum_bool = models.IntegerField(max_length=2000, blank=True, help_text='Answering yes will present a result summary section. This should be skipped if you would rather enter individual test results in the section below.', null=True, verbose_name='History of abnormal LFTs results?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    lfts_sum = models.TextField(help_text='', null=True, verbose_name='LFTs range ', blank=True) # This field type is a guess
    lfts_comments = models.TextField(help_text='', null=True, verbose_name='LFTs range result comment (quality concerns, normal range)', blank=True) # This field type is a guess
    lfts_datapoints = models.NullBooleanField(help_text='', verbose_name='Would you like to enter individual LFTs results?', blank=True)
    cbc_sum_bool = models.IntegerField(max_length=2000, blank=True, help_text='Answering yes will present a result summary section. This should be skipped if you would rather enter individual test results in the section below.', null=True, verbose_name='History of abnormal CBC results?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    cbc_sum = models.TextField(help_text='', null=True, verbose_name='CBC range ', blank=True) # This field type is a guess
    cbc_comments = models.TextField(help_text='', null=True, verbose_name='CBC range result comment (quality concerns, normal range)', blank=True) # This field type is a guess
    cbc_datapoints = models.NullBooleanField(help_text='', verbose_name='Would you like to enter individual CBC results?', blank=True)
    urinalysis_comments = models.TextField(help_text='', null=True, verbose_name='Urinalysis comment (quality concerns, normal range)', blank=True) # This field type is a guess
    urinalysis_datapoints = models.NullBooleanField(help_text='', verbose_name='Would you like to enter individual urinalysis results?', blank=True)
    cmp_sum_bool = models.IntegerField(max_length=2000, blank=True, help_text='Answering yes will present a result summary section. This should be skipped if you would rather enter individual test results in the section below.', null=True, verbose_name='History of abnormal Chemistry Panel results?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    cmp_glucose_sum = models.TextField(help_text='', null=True, verbose_name='Glucose level ', blank=True) # This field type is a guess
    cmp_calcium_sum = models.TextField(help_text='', null=True, verbose_name='Calcium level ', blank=True) # This field type is a guess
    cmp_sodium_sum = models.TextField(help_text='', null=True, verbose_name='Sodium level ', blank=True) # This field type is a guess
    cmp_potassium_sum = models.TextField(help_text='', null=True, verbose_name='Potassium level ', blank=True) # This field type is a guess
    cmp_bicarb_sum = models.TextField(help_text='', null=True, verbose_name='Bicarb level ', blank=True) # This field type is a guess
    cmp_chloride_sum = models.TextField(help_text='', null=True, verbose_name='Chloride level ', blank=True) # This field type is a guess
    cmp_bun_sum = models.TextField(help_text='', null=True, verbose_name='BUN level ', blank=True) # This field type is a guess
    cmp_creatinine_sum = models.TextField(help_text='', null=True, verbose_name='Creatinine level ', blank=True) # This field type is a guess
    cmp_albumin_sum = models.TextField(help_text='', null=True, verbose_name='Albumin level ', blank=True) # This field type is a guess
    cmp_total_protein_sum = models.TextField(help_text='', null=True, verbose_name='Total protein level ', blank=True) # This field type is a guess
    cmp_alp_sum = models.TextField(help_text='', null=True, verbose_name='ALP (Alkaline Phospatase) level ', blank=True) # This field type is a guess
    cmp_alt_sum = models.TextField(help_text='', null=True, verbose_name='ALT (Alanine aminotransferase) level ', blank=True) # This field type is a guess
    cmp_ast_sum = models.TextField(help_text='', null=True, verbose_name='AST (Aspartate aminotransferase) level ', blank=True) # This field type is a guess
    cmp_bilirubin_sum = models.TextField(help_text='', null=True, verbose_name='Bilirubin level ', blank=True) # This field type is a guess
    cmp_comments = models.TextField(help_text='', null=True, verbose_name='Chemistry Panel comments (quality concerns, normal ranges)', blank=True) # This field type is a guess
    cmp_datapoints = models.NullBooleanField(help_text='', verbose_name='Would you like to enter individual Chemistry panel results', blank=True)
    thyroid_study_comment = models.TextField(help_text='', null=True, verbose_name='Thyroid study comment (quality concerns)', blank=True) # This field type is a guess
    thyroid_datapoints = models.NullBooleanField(help_text='', verbose_name='Would you like to enter individual thyroid study results?', blank=True)
    renal_function_sum_bool = models.IntegerField(max_length=2000, blank=True, help_text='Answering yes will present a result summary section. This should be skipped if you would rather enter individual test results in the section below.', null=True, verbose_name='History of abnormal renal study results?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    renal_function_sum_urea_nitrogen = models.TextField(help_text='', null=True, verbose_name='Urea nitrogen range ', blank=True) # This field type is a guess
    renal_function_sum_sodium = models.TextField(help_text='', null=True, verbose_name='Sodium range ', blank=True) # This field type is a guess
    renal_function_sum_potassium = models.TextField(help_text='', null=True, verbose_name='Potassium range ', blank=True) # This field type is a guess
    renal_function_sum_bicarb = models.TextField(help_text='', null=True, verbose_name='Bicarb range ', blank=True) # This field type is a guess
    renal_function_sum_chloride = models.TextField(help_text='', null=True, verbose_name='Chloride range ', blank=True) # This field type is a guess
    renal_function_sum_creatinine = models.TextField(help_text='', null=True, verbose_name='Creatinine range ', blank=True) # This field type is a guess
    renal_function_sum_comment = models.TextField(help_text='', null=True, verbose_name='Renal function range result comment (quality concerns, normal range)', blank=True) # This field type is a guess
    renal_function_datapoints = models.NullBooleanField(help_text='', verbose_name='Would you like to enter individual renal function studies?', blank=True)
    sweat_sum_bool = models.IntegerField(max_length=2000, blank=True, help_text='Answering yes will present a result summary section. This should be skipped if you would rather enter individual test results in the section below.', null=True, verbose_name='History of abnormal sweat testing?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    sweat_sum = models.TextField(help_text='', null=True, verbose_name='Sweat test range ', blank=True) # This field type is a guess
    sweat_comments = models.TextField(help_text='', null=True, verbose_name='Sweat test range result comment (quality concerns, normal range)', blank=True) # This field type is a guess
    sweat_datapoints = models.NullBooleanField(help_text='', verbose_name='Would you like to enter individual Sweat test results?', blank=True)
    celiac_sum_bool = models.IntegerField(max_length=2000, blank=True, help_text='Answering yes will present a result summary section. This should be skipped if you would rather enter individual test results in the section below.', null=True, verbose_name='History of abnormal  testing for celiac disease?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    celiac_test_type_sum = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Type of testing for celiac disease', blank=True)
    celiac_sum = models.TextField(help_text='', null=True, verbose_name='Celiac disease range ', blank=True) # This field type is a guess
    celiac_comments = models.TextField(help_text='', null=True, verbose_name='Celiac disease test range result comment (quality concerns, normal range)', blank=True) # This field type is a guess
    celiac_datapoints = models.NullBooleanField(help_text='', verbose_name='Would you like to enter individual Celiac disease test results?', blank=True)
    biopsies_performed = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Biopsies performed', choices=[(6, 'None'), (1, 'Muscle'), (2, 'Skin'), (3, 'Liver'), (4, 'Brain'), (5, 'Bone Marrow'), (7, 'Other'), (8, 'Unknown/Not documented')])
    cardio_tests_performed = models.IntegerField(help_text='', null=True, verbose_name='Cardiovascular tests performed | Describe  cardiac testing', blank=True, choices=[(1, 'None'), (2, 'Electrocardiogram (ECG)'), (3, 'Echocardiogram (ECHO)'), (4, '24 Hour Monitoring (Holter Monitor)'), (5, 'Exercise Stress Test (EST)'), (6, 'Cardiac MRI'), (8, 'Unknown/Not documented'), (7, 'Other')]) # This field type is a guess
    musculoskeletal_tests_performed = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Musculoskeletal tests performed', choices=[(3, 'None'), (1, 'Electromyogram (EMG)'), (2, 'Nerve Conduction Velocity (NCV)'), (4, 'Unknown/Not documented')])
    prior_testing_feedback = models.TextField(help_text='', null=True, verbose_name='Please provide any feedback for this form (for example: missing questions, questions not relevant for a disease area, ambiguities, places where a textbox could be replaced with discrete choices, missing discrete choices)', blank=True) # This field type is a guess
    lab_tests_performed_summary = models.CharField(help_text='19, None | 1, Blood Lactate | 2, Blood Pyruvate | 3, CSF Lactate | 4, CSF Pyruvate | 5, PAA | 6, Plasma CN/ACP | 7, UOA | 8, CK | 9, Uric Acid | 10, LFTs | 11, CBC | 12, Urinalysis | 13, Chemistry Panel (CMP) | 14, Thyroid Function | 15, Renal Function | 16, Sweat Test | 17, Celiac Disease | 18, Unknown/Not documented', null=True, max_length=2000, verbose_name='Laboratory tests performed', blank=True)
    urinalysis_range_summary = models.CharField(help_text='1, Blood | 2, Protein | 3, Infection', null=True, max_length=2000, verbose_name='Presence of any of the following over all urinalsyses?', blank=True)
    thyroid_function_sum_summary = models.CharField(help_text='1, TSH elevation | 2, TSH decrease | 3, T4 elevation | 4, T4 decrease', null=True, max_length=2000, verbose_name='Thyroid function findings over time', blank=True)
    image_studies_performed_summary = models.CharField(help_text='6, None | 1, MRI | 2, Spectroscopy (MRS) | 3, CT | 4, Ultrasound | 5, Xray | 7, Endoscopy | 8, Unknown/Not documented', null=True, max_length=2000, verbose_name='Imaging studies performed', blank=True)
    vision_tests_performed_summary = models.CharField(help_text=' 2, None | 1, Electroretinogram (ERG) | 3, Other | 4, Unknown/Not documented', null=True, max_length=2000, verbose_name='Vision tests performed', blank=True)
    neurologic_tests_performed_summary = models.CharField(help_text='2, None | 1, Electroencephalogram (EEG) | 3, Unknown/Not documented', null=True, max_length=2000, verbose_name='Neurologic tests performed', blank=True)
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'priortesting'


class labtestsperformed(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Laboratory tests performed', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Laboratory tests performed', choices=[(19, 'None'), (1, 'Blood Lactate'), (2, 'Blood Pyruvate'), (3, 'CSF Lactate'), (4, 'CSF Pyruvate'), (5, 'PAA'), (6, 'Plasma CN/ACP'), (7, 'UOA'), (8, 'CK'), (9, 'Uric Acid'), (10, 'LFTs'), (11, 'CBC'), (12, 'Urinalysis'), (13, 'Chemistry Panel (CMP)'), (14, 'Thyroid Function'), (15, 'Renal Function'), (16, 'Sweat Test'), (17, 'Celiac Disease'), (18, 'Unknown/Not documented')])
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'labtestsperformed'


class urinalysisrange(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Presence of any of the following over all urinalsyses?', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Presence of any of the following over all urinalsyses?', choices=[(1, 'Blood'), (2, 'Protein'), (3, 'Infection')])
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'urinalysisrange'


class thyroidfunctionsum(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Thyroid function findings over time', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Thyroid function findings over time', choices=[(1, 'TSH elevation'), (2, 'TSH decrease'), (3, 'T4 elevation'), (4, 'T4 decrease')])
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'thyroidfunctionsum'


class imagestudiesperformed(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Imaging studies performed', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Imaging studies performed', choices=[(6, 'None'), (1, 'MRI'), (2, 'Spectroscopy (MRS)'), (3, 'CT'), (4, 'Ultrasound'), (5, 'Xray'), (7, 'Endoscopy'), (8, 'Unknown/Not documented')])
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'imagestudiesperformed'


class visiontestsperformed(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Vision tests performed', blank=True)
    value = models.IntegerField(help_text='', null=True, verbose_name='Vision tests performed', blank=True, choices=[(2, 'None'), (1, 'Electroretinogram (ERG)'), (3, 'Other'), (4, 'Unknown/Not documented')]) # This field type is a guess
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'visiontestsperformed'


class neurologictestsperformed(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Neurologic tests performed', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Neurologic tests performed', choices=[(2, 'None'), (1, 'Electroencephalogram (EEG)'), (3, 'Unknown/Not documented')])
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'neurologictestsperformed'


class BloodLactate(models.Model):
    blood_lactate_date = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year of Blood Lactate', blank=True)
    blood_lactate = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Blood Lactate result', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    blood_lactate_result = models.TextField(help_text='', null=True, verbose_name='Blood Lactate result ', blank=True) # This field type is a guess
    blood_lactate_location = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Lab where Blood Lactate was performed', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'bloodlactate'


class BloodPyruvate(models.Model):
    blood_pyruvate_date = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year of Blood Pyruvate', blank=True)
    blood_pyruvate = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='$ Blood Pyruvate result', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    blood_pyruvate_result = models.TextField(help_text='', null=True, verbose_name='Blood Pyruvate result ', blank=True) # This field type is a guess
    blood_pyruvate_location = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Lab where Blood Pyruvate was performed?', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'bloodpyruvate'


class CsfLactate(models.Model):
    csf_lactate_date = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year of CSF Lactate', blank=True)
    csf_lactate = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='CSF Lactate result', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    csf_lactate_result = models.TextField(help_text='', null=True, verbose_name='CSF Lactate result ', blank=True) # This field type is a guess
    csf_lactate_location = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Lab where CSF Lactate was performed?', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'csflactate'


class CsfPyruvate(models.Model):
    csf_pyruvate_date = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year of CSF Pyruvate', blank=True)
    csf_pyruvate = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='CSF Pyruvate result', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    csf_pyruvate_result = models.TextField(help_text='', null=True, verbose_name='CSF Pyruvate result ', blank=True) # This field type is a guess
    csf_pyruvate_location = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Lab where $ CSF Pyruvate was performed?', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'csfpyruvate'


class Paa(models.Model):
    paa_date = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year of PAA', blank=True)
    paa = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='PAA Pyruvate result', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    paa_result = models.TextField(help_text='', null=True, verbose_name='PAA result ', blank=True) # This field type is a guess
    paa_location = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Lab where was PAA performed?', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'paa'


class PlasmaCnacp(models.Model):
    plasma_cn_acp_date = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year of Plasma CN/ACP', blank=True)
    plasma_cn_acp = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Plasma CN/ACP result', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    plasma_cn_acp_result = models.TextField(help_text='', null=True, verbose_name='Plasma CN/ACP result ', blank=True) # This field type is a guess
    plasma_cn_acp_location = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Lab where Plasma CN/ACP was performed?', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'plasmacnacp'


class Uoa(models.Model):
    uoa_date = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year of UOA', blank=True)
    uoa = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='UOA result', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    uoa_result = models.TextField(help_text='', null=True, verbose_name='UOA result ', blank=True) # This field type is a guess
    uoa_location = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Lab where UOA  was performed?', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'uoa'


class Ck(models.Model):
    ck_date = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year of CK', blank=True)
    ck = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='CK result', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    ck_result = models.TextField(help_text='', null=True, verbose_name='CK result ', blank=True) # This field type is a guess
    ck_location = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Lab where CK was performed?', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'ck'


class UricAcid(models.Model):
    uric_acid_date = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year of Uric acid', blank=True)
    uric_acid = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Uric acid result', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    uric_acid_result = models.TextField(help_text='', null=True, verbose_name='Uric acid result ', blank=True) # This field type is a guess
    uric_acid_location = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Lab where Uric acid was performed?', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'uricacid'


class Lft(models.Model):
    lfts_date = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year of LFTs', blank=True)
    lfts = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='LFTs result', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    lfts_result = models.TextField(help_text='', null=True, verbose_name='LFTs result ', blank=True) # This field type is a guess
    lfts_location = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Lab where LFTs was performed?', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'lft'


class Cbc(models.Model):
    cbc_date = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year of CBC', blank=True)
    cbc = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='CBC result', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    cbc_result = models.TextField(help_text='', null=True, verbose_name='CBC result ', blank=True) # This field type is a guess
    cbc_location = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Lab where CBC was performed?', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'cbc'


class Urinalysi(models.Model):
    urinalysis_date = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year of  Urinalysis', blank=True)
    urinalysis = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Urinalysis result', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    urinalysis_location = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Lab where Urinalysis was performed?', blank=True)
    urinalysis_details_summary = models.CharField(help_text='1, Blood | 2, Protein | 3, Infection', null=True, max_length=2000, verbose_name='Presence of', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'urinalysi'


class urinalysisdetails(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Presence of', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Presence of', choices=[(1, 'Blood'), (2, 'Protein'), (3, 'Infection')])
    urinalysi = models.ForeignKey(Urinalysi)

    class Meta:
	 db_table = 'urinalysisdetails'


class ChemistryPanel(models.Model):
    cmp_glucose_level = models.TextField(help_text='', null=True, verbose_name='Glucose level ', blank=True) # This field type is a guess
    cmp_calcium_level = models.TextField(help_text='', null=True, verbose_name='Calcium level ', blank=True) # This field type is a guess
    cmp_electrolyte_sodium_level = models.TextField(help_text='', null=True, verbose_name='Sodium level ', blank=True) # This field type is a guess
    cmp_electrolyte_potassium_level = models.TextField(help_text='', null=True, verbose_name='Potassium level ', blank=True) # This field type is a guess
    cmp_electrolyte_bicarb_level = models.TextField(help_text='', null=True, verbose_name='Bicarb level ', blank=True) # This field type is a guess
    cmp_electrolyte_chloride_level = models.TextField(help_text='', null=True, verbose_name='Chloride level ', blank=True) # This field type is a guess
    cmp_bun_level = models.TextField(help_text='', null=True, verbose_name='BUN level ', blank=True) # This field type is a guess
    cmp_creatinine_level = models.TextField(help_text='', null=True, verbose_name='Creatinine level ', blank=True) # This field type is a guess
    cmp_albumin_level = models.TextField(help_text='', null=True, verbose_name='Albumin level ', blank=True) # This field type is a guess
    cmp_total_protein_level = models.TextField(help_text='', null=True, verbose_name='Total protein level ', blank=True) # This field type is a guess
    cmp_alp_level = models.TextField(help_text='', null=True, verbose_name='ALP (Alkaline Phospatase) level ', blank=True) # This field type is a guess
    cmp_alt_level = models.TextField(help_text='', null=True, verbose_name='ALT (Alanine aminotransferase) level ', blank=True) # This field type is a guess
    cmp_ast_level = models.TextField(help_text='', null=True, verbose_name='AST(Aspartate aminotransferase) level ', blank=True) # This field type is a guess
    cmp_bilirubin_level = models.TextField(help_text='', null=True, verbose_name='Bilirubin level ', blank=True) # This field type is a guess
    cmp_date = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year of chemistry panel', blank=True)
    cmp_location = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Lab where chemistry panel was performed', blank=True)
    cmp_misc_summary = models.CharField(help_text='1, Glucose | 2, Calcium | 3, All of the above within normal range', null=True, max_length=2000, verbose_name='Chemistry Panel Results (Part 1)\n\nAbnormal values', blank=True)
    cmp_electrolyte_summary = models.CharField(help_text='1, Sodium | 2, Potassium | 3, Bicarb | 4, Chloride | 5, All of the above within normal range', null=True, max_length=2000, verbose_name='Chemistry Panel Results (Part 2)\n\nAbnormal electrolytes', blank=True)
    cmp_kidney_summary = models.CharField(help_text='1, Blood Urea Nitrogen (BUN) | 2, Creatinine | 3, All of the above within normal range', null=True, max_length=2000, verbose_name='Chemistry Panel Results (Part 3)\n\nAbnormal Kidney values', blank=True)
    cmp_protein_summary = models.CharField(help_text='1, Albumin | 2, Total protein | 3, All of the above within normal range', null=True, max_length=2000, verbose_name='Chemistry Panel Results (Part 4)\n\nAbnormal protein values', blank=True)
    cmp_liver_summary = models.CharField(help_text='1, ALP (Alkaline Phosphatase) | 2, ALT (Alanine aminotransferase) | 3, AST (Aspartate aminotransferase) | 4, Bilirubin | 5, All of the above within normal range', null=True, max_length=2000, verbose_name='Chemistry Panel Results (Part 5)\n\nAbnormal liver values', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'chemistrypanel'


class cmpmisc(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Chemistry Panel Results (Part 1)\n\nAbnormal values', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Chemistry Panel Results (Part 1)\n\nAbnormal values', choices=[(1, 'Glucose'), (2, 'Calcium'), (3, 'All of the above within normal range')])
    chemistrypanel = models.ForeignKey(ChemistryPanel)

    class Meta:
	 db_table = 'cmpmisc'


class cmpelectrolyte(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Chemistry Panel Results (Part 2)\n\nAbnormal electrolytes', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Chemistry Panel Results (Part 2)\n\nAbnormal electrolytes', choices=[(1, 'Sodium'), (2, 'Potassium'), (3, 'Bicarb'), (4, 'Chloride'), (5, 'All of the above within normal range')])
    chemistrypanel = models.ForeignKey(ChemistryPanel)

    class Meta:
	 db_table = 'cmpelectrolyte'


class cmpkidney(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Chemistry Panel Results (Part 3)\n\nAbnormal Kidney values', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Chemistry Panel Results (Part 3)\n\nAbnormal Kidney values', choices=[(1, 'Blood Urea Nitrogen (BUN)'), (2, 'Creatinine'), (3, 'All of the above within normal range')])
    chemistrypanel = models.ForeignKey(ChemistryPanel)

    class Meta:
	 db_table = 'cmpkidney'


class cmpprotein(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Chemistry Panel Results (Part 4)\n\nAbnormal protein values', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Chemistry Panel Results (Part 4)\n\nAbnormal protein values', choices=[(1, 'Albumin'), (2, 'Total protein'), (3, 'All of the above within normal range')])
    chemistrypanel = models.ForeignKey(ChemistryPanel)

    class Meta:
	 db_table = 'cmpprotein'


class cmpliver(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Chemistry Panel Results (Part 5)\n\nAbnormal liver values', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Chemistry Panel Results (Part 5)\n\nAbnormal liver values', choices=[(1, 'ALP (Alkaline Phosphatase)'), (2, 'ALT (Alanine aminotransferase)'), (3, 'AST (Aspartate aminotransferase)'), (4, 'Bilirubin'), (5, 'All of the above within normal range')])
    chemistrypanel = models.ForeignKey(ChemistryPanel)

    class Meta:
	 db_table = 'cmpliver'


class ThyroidStudy(models.Model):
    thyroid_study_date = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year of thyroid study', blank=True)
    thyroid_study = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Thyroid study result', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    thyroid_function_location = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Lab where thyroid testing was performed?', blank=True)
    thyroid_study_function_summary = models.CharField(help_text='1, TSH elevation | 2, TSH decrease | 3, T4 elevation | 4, T4 decrease', null=True, max_length=2000, verbose_name='Thyroid function findings', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'thyroidstudy'


class thyroidstudyfunction(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Thyroid function findings', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Thyroid function findings', choices=[(1, 'TSH elevation'), (2, 'TSH decrease'), (3, 'T4 elevation'), (4, 'T4 decrease')])
    thyroidstudy = models.ForeignKey(ThyroidStudy)

    class Meta:
	 db_table = 'thyroidstudyfunction'


class RenalFunctionStudy(models.Model):
    renal_function_date = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Year of renal function study', blank=True)
    renal_function_urea_nitrogen = models.TextField(help_text='', null=True, verbose_name='Urea Nitrogen  on renal function study', blank=True) # This field type is a guess
    renal_function_electrolyte_sodium_level = models.TextField(help_text='', null=True, verbose_name='Sodium  on renal function study', blank=True) # This field type is a guess
    renal_function_electrolyte_potassium_level = models.TextField(help_text='', null=True, verbose_name='Potassium  on renal function study', blank=True) # This field type is a guess
    renal_function_electrolyte_bicarb_level = models.TextField(help_text='', null=True, verbose_name='Bicarb  on renal function study', blank=True) # This field type is a guess
    renal_function_electrolyte_chloride_level = models.TextField(help_text='', null=True, verbose_name='Chloride  on renal function study', blank=True) # This field type is a guess
    renal_function_creatinine = models.TextField(help_text='', null=True, verbose_name='Creatinine  on renal function study', blank=True) # This field type is a guess
    renal_function_location = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Lab where renal study was performed', blank=True)
    renal_function_summary = models.CharField(help_text='1, Urea Nitrogen | 2, Electrolytes | 3, Creatinine | 4, All of the above within normal range', null=True, max_length=2000, verbose_name='Abnormal Renal Function Study Results', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'renalfunctionstudy'


class renalfunction(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Abnormal Renal Function Study Results', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Abnormal Renal Function Study Results', choices=[(1, 'Urea Nitrogen'), (2, 'Electrolytes'), (3, 'Creatinine'), (4, 'All of the above within normal range')])
    renalfunctionstudy = models.ForeignKey(RenalFunctionStudy)

    class Meta:
	 db_table = 'renalfunction'


class SweatTest(models.Model):
    sweat_date = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year of Sweat test', blank=True)
    sweat = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Sweat test result', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    sweat_result = models.TextField(help_text='', null=True, verbose_name='Sweat test result ', blank=True) # This field type is a guess
    sweat_location = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Lab where Sweat test was performed?', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'sweattest'


class CeliacDiseaseTest(models.Model):
    celiac_date = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year of Celiac disease test', blank=True)
    celiac = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Celiac disease test result', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    celiac_test_type = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Celiac disease test type', blank=True)
    celiac_result = models.TextField(help_text='', null=True, verbose_name='Celiac disease test result ', blank=True) # This field type is a guess
    celiac_location = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Lab where Celiac disease test was performed?', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'celiacdiseasetest'


class Mri(models.Model):
    mri_date = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year of MRI', blank=True)
    mri = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='MRI result', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    mri_temp_bone_other_features = models.TextField(help_text='', null=True, verbose_name='Other temporal bone features', blank=True) # This field type is a guess
    mri_spec = models.TextField(help_text='', null=True, verbose_name='Specify MRI Result', blank=True) # This field type is a guess
    mri_location = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Where was MRI performed?', blank=True)
    mri_body_part_summary = models.CharField(help_text='1, Brain | 2, Kidney | 3, Abdomen | 4, Chest | 5, Muscle | 6, Head | 8, Temporal Bones | 7, Other', null=True, max_length=2000, verbose_name='Part of body screened on MRI | Specify  part of body screened', blank=True)
    mri_temp_bone_features_summary = models.CharField(help_text='1, Cochlear Nerve Hypoplasia | 2, EVA | 3, Other', null=True, max_length=2000, verbose_name='Temporal bone features', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'mri'


class mribodypart(models.Model):
    label = models.CharField(help_text='Please enter cardiac MRIs in CMRI Results instrument if the cardiac intake forms will be used.', null=True, max_length=2000, verbose_name='Part of body screened on MRI | Specify  part of body screened', blank=True)
    value = models.IntegerField(help_text='Please enter cardiac MRIs in CMRI Results instrument if the cardiac intake forms will be used.', null=True, verbose_name='Part of body screened on MRI | Specify  part of body screened', blank=True, choices=[(1, 'Brain'), (2, 'Kidney'), (3, 'Abdomen'), (4, 'Chest'), (5, 'Muscle'), (6, 'Head'), (8, 'Temporal Bones'), (7, 'Other')]) # This field type is a guess
    mri = models.ForeignKey(Mri)

    class Meta:
	 db_table = 'mribodypart'


class mritempbonefeatures(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Temporal bone features', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Temporal bone features', choices=[(1, 'Cochlear Nerve Hypoplasia'), (2, 'EVA'), (3, 'Other')])
    mri = models.ForeignKey(Mri)

    class Meta:
	 db_table = 'mritempbonefeatures'


class BrainSpectroscopyMr(models.Model):
    mrs_date = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year of spectroscopy (MRS)', blank=True)
    mrs = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='spectroscopy (MRS) result', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    mrs_spec = models.TextField(help_text='', null=True, verbose_name='Specify spectroscopy (MRS) result', blank=True) # This field type is a guess
    mrs_location = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Where was spectroscopy (MRS) performed?', blank=True)
    mrs_body_part_summary = models.CharField(help_text='1, Brain | 2, Kidney | 3, Abdomen | 4, Chest | 5, Muscle | 6, Head | 7, Other', null=True, max_length=2000, verbose_name='Part of body screened on spectroscopy  (MRS) | Specify  part of body screened', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'brainspectroscopymr'


class mrsbodypart(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Part of body screened on spectroscopy  (MRS) | Specify  part of body screened', blank=True)
    value = models.IntegerField(help_text='', null=True, verbose_name='Part of body screened on spectroscopy  (MRS) | Specify  part of body screened', blank=True, choices=[(1, 'Brain'), (2, 'Kidney'), (3, 'Abdomen'), (4, 'Chest'), (5, 'Muscle'), (6, 'Head'), (7, 'Other')]) # This field type is a guess
    brainspectroscopymr = models.ForeignKey(BrainSpectroscopyMr)

    class Meta:
	 db_table = 'mrsbodypart'


class Ct(models.Model):
    ct_date = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year of CT', blank=True)
    ct = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='CT result', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    ct_temp_bone_other_features = models.TextField(help_text='', null=True, verbose_name='Other temporal bone features', blank=True) # This field type is a guess
    ct_spec = models.TextField(help_text='', null=True, verbose_name='Specify CT result', blank=True) # This field type is a guess
    ct_location = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Where was CT performed?', blank=True)
    ct_body_part_summary = models.CharField(help_text='1, Brain | 2, Kidney | 3, Abdomen | 4, Chest | 5, Muscle | 6, Head | 8, Temporal Bones | 7, Other', null=True, max_length=2000, verbose_name='Part of body screened on CT | Specify  part of body screened', blank=True)
    ct_temp_bone_features_summary = models.CharField(help_text='1, Cochlear Nerve Hypoplasia | 2, EVA | 3, Other', null=True, max_length=2000, verbose_name='Temporal bone features', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'ct'


class ctbodypart(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Part of body screened on CT | Specify  part of body screened', blank=True)
    value = models.IntegerField(help_text='', null=True, verbose_name='Part of body screened on CT | Specify  part of body screened', blank=True, choices=[(1, 'Brain'), (2, 'Kidney'), (3, 'Abdomen'), (4, 'Chest'), (5, 'Muscle'), (6, 'Head'), (8, 'Temporal Bones'), (7, 'Other')]) # This field type is a guess
    ct = models.ForeignKey(Ct)

    class Meta:
	 db_table = 'ctbodypart'


class cttempbonefeatures(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Temporal bone features', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Temporal bone features', choices=[(1, 'Cochlear Nerve Hypoplasia'), (2, 'EVA'), (3, 'Other')])
    ct = models.ForeignKey(Ct)

    class Meta:
	 db_table = 'cttempbonefeatures'


class Ultrasound2(models.Model):
    us_date = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year of US', blank=True)
    us = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='US result', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    us_renal_laterality = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Laterality of abnormal renal ultrasound findings', choices=[(1, 'Unilateral'), (2, 'Bilateral')])
    us_spec = models.TextField(help_text='', null=True, verbose_name='Specify US result', blank=True) # This field type is a guess
    us_location = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Where was US performed?', blank=True)
    us_body_part_summary = models.CharField(help_text='1, Brain | 2, Kidney | 3, Abdomen | 4, Chest | 5, Muscle | 6, Head | 7, Other', null=True, max_length=2000, verbose_name='Part of body screened on US | Specify  part of body screened', blank=True)
    us_renal_finding_summary = models.CharField(help_text='1, Cysts | 2, Hypoplasia | 3, Aplasia | 4, Duplicated Ureters | 5, Horseshoe | 6, Other', null=True, max_length=2000, verbose_name='Renal ultrasound finding details', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'ultrasound2'


class usbodypart(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Part of body screened on US | Specify  part of body screened', blank=True)
    value = models.IntegerField(help_text='', null=True, verbose_name='Part of body screened on US | Specify  part of body screened', blank=True, choices=[(1, 'Brain'), (2, 'Kidney'), (3, 'Abdomen'), (4, 'Chest'), (5, 'Muscle'), (6, 'Head'), (7, 'Other')]) # This field type is a guess
    ultrasound2 = models.ForeignKey(Ultrasound2)

    class Meta:
	 db_table = 'usbodypart'


class usrenalfinding(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Renal ultrasound finding details', blank=True)
    value = models.IntegerField(help_text='', null=True, verbose_name='Renal ultrasound finding details', blank=True, choices=[(1, 'Cysts'), (2, 'Hypoplasia'), (3, 'Aplasia'), (4, 'Duplicated Ureters'), (5, 'Horseshoe'), (6, 'Other')]) # This field type is a guess
    ultrasound2 = models.ForeignKey(Ultrasound2)

    class Meta:
	 db_table = 'usrenalfinding'


class Xray(models.Model):
    xray_date = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year of Xray', blank=True)
    xray = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Xray result', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    xray_spec = models.TextField(help_text='', null=True, verbose_name='Specify Xray result', blank=True) # This field type is a guess
    xray_location = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Where was Xray performed?', blank=True)
    xray_body_part_summary = models.CharField(help_text='1, Brain | 2, Kidney | 3, Abdomen | 4, Chest | 5, Muscle | 6, Head | 7, Other', null=True, max_length=2000, verbose_name='Part of body screened on Xray | Specify  part of body screened', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'xray'


class xraybodypart(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Part of body screened on Xray | Specify  part of body screened', blank=True)
    value = models.IntegerField(help_text='', null=True, verbose_name='Part of body screened on Xray | Specify  part of body screened', blank=True, choices=[(1, 'Brain'), (2, 'Kidney'), (3, 'Abdomen'), (4, 'Chest'), (5, 'Muscle'), (6, 'Head'), (7, 'Other')]) # This field type is a guess
    xray = models.ForeignKey(Xray)

    class Meta:
	 db_table = 'xraybodypart'


class Endoscopy(models.Model):
    endo_date = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year of Endoscopy', blank=True)
    endo = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Endoscopy result | Specify  Type of Endoscopy ', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    endo_spec = models.TextField(help_text='', null=True, verbose_name='Specify Endoscopy Result', blank=True) # This field type is a guess
    endo_location = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Where was Endoscopy performed?', blank=True)
    endo_body_part_summary = models.CharField(help_text='1, Gastroscopy or Upper endoscopy (mouth, oesophagus, stomach and duodenum) | 2, Colonoscopy | 3, Flexible sigmoidoscopy | 4, Proctoscopy (anal canal) | 5, Cytoscopy (bladder) | 6, Ureteroscopy | 8, Endoscopic ultrasound | 7, Other', null=True, max_length=2000, verbose_name='Type of Endoscopy ', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'endoscopy'


class endobodypart(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Type of Endoscopy ', blank=True)
    value = models.TextField(help_text='', null=True, verbose_name='Type of Endoscopy ', blank=True) # This field type is a guess
    endoscopy = models.ForeignKey(Endoscopy)

    class Meta:
	 db_table = 'endobodypart'


class MuscleBiopsy(models.Model):
    muscle_biopsy_date = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year of muscle biopsy', blank=True)
    muscle_biopsy_result = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='General pathological analysis of muscle biopsy', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    muscle_biopsy_spec = models.TextField(help_text='', null=True, verbose_name='Specify abnormal result for muscle biopsy', db_column='muscle_biopsy_spec ', blank=True) # Field renamed to remove spaces. Field renamed to remove ending underscore Field name made lowercase. This field type is a guess
    muscle_biopsy_mito_test_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Mitochondrial testing done on muscle biopsy', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    muscle_biopsy_mito_test_type_summary = models.CharField(help_text='1, PDH | 2, OXPHOS | 3, ETC Enzymes | 4, Coenzyme Q10 | 5, Mitochondrial DNA Content', null=True, max_length=2000, verbose_name='Type of testing performed on muscle biopsy | Results of ', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'musclebiopsy'


class musclebiopsymitotesttype(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Type of testing performed on muscle biopsy | Results of ', blank=True)
    value = models.IntegerField(help_text='', null=True, verbose_name='Type of testing performed on muscle biopsy | Results of ', blank=True, choices=[(1, 'PDH'), (2, 'OXPHOS'), (3, 'ETC Enzymes'), (4, 'Coenzyme Q10'), (5, 'Mitochondrial DNA Content')]) # This field type is a guess
    musclebiopsy = models.ForeignKey(MuscleBiopsy)

    class Meta:
	 db_table = 'musclebiopsymitotesttype'


class SkinBiopsy(models.Model):
    skin_biopsy_date = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year of skin biopsy', blank=True)
    skin_biopsy_result = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='General pathological analysis of skin biopsy', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    skin_biopsy_spec = models.TextField(help_text='', null=True, verbose_name='Specify abnormal result for skin biopsy', blank=True) # This field type is a guess
    skin_biopsy_mito_test_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Mitochondrial testing done on skin biopsy', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    skin_biopsy_mito_test_type_summary = models.CharField(help_text='1, PDH | 2, OXPHOS | 3, ETC Enzymes | 4, Coenzyme Q10 | 5, Mitochondrial DNA Content', null=True, max_length=2000, verbose_name='Type of testing performed on skin biopsy | Results of ', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'skinbiopsy'


class skinbiopsymitotesttype(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Type of testing performed on skin biopsy | Results of ', blank=True)
    value = models.IntegerField(help_text='', null=True, verbose_name='Type of testing performed on skin biopsy | Results of ', blank=True, choices=[(1, 'PDH'), (2, 'OXPHOS'), (3, 'ETC Enzymes'), (4, 'Coenzyme Q10'), (5, 'Mitochondrial DNA Content')]) # This field type is a guess
    skinbiopsy = models.ForeignKey(SkinBiopsy)

    class Meta:
	 db_table = 'skinbiopsymitotesttype'


class LiverBiopsy(models.Model):
    liver_biopsy_date = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year of liver biopsy', blank=True)
    liver_biopsy_result = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='General pathological analysis of liver biopsy', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    liver_biopsy_spec = models.TextField(help_text='', null=True, verbose_name='Specify abnormal result for liver biopsy', blank=True) # This field type is a guess
    liver_biopsy_mito_test_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Mitochondrial testing done on liver biopsy', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    liver_biopsy_mito_test_type_summary = models.CharField(help_text='1, PDH | 2, OXPHOS | 3, ETC Enzymes | 4, Coenzyme Q10 | 5, Mitochondrial DNA Content', null=True, max_length=2000, verbose_name='Type of testing performed on liver biopsy | Results of ', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'liverbiopsy'


class liverbiopsymitotesttype(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Type of testing performed on liver biopsy | Results of ', blank=True)
    value = models.IntegerField(help_text='', null=True, verbose_name='Type of testing performed on liver biopsy | Results of ', blank=True, choices=[(1, 'PDH'), (2, 'OXPHOS'), (3, 'ETC Enzymes'), (4, 'Coenzyme Q10'), (5, 'Mitochondrial DNA Content')]) # This field type is a guess
    liverbiopsy = models.ForeignKey(LiverBiopsy)

    class Meta:
	 db_table = 'liverbiopsymitotesttype'


class BrainBiopsy(models.Model):
    brain_biopsy_date = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year of brain biopsy', blank=True)
    brain_biopsy_result = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='General pathological analysis of brain biopsy', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    brain_biopsy_spec = models.TextField(help_text='', null=True, verbose_name='Specify abnormal result for brain biopsy', blank=True) # This field type is a guess
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'brainbiopsy'


class BoneMarrow(models.Model):
    bone_marrow_biopsy_date = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year of bone marrow biopsy', blank=True)
    bone_marrow_biopsy_result = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='General pathological analysis of bone marrow biopsy', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    bone_marrow_biopsy_spec = models.TextField(help_text='', null=True, verbose_name='Specify abnormal result for bone marrow biopsy', blank=True) # This field type is a guess
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'bonemarrow'


class OtherBiopsy(models.Model):
    other_biopsy_type = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Specify other biopsy type', blank=True)
    other_biopsy_date = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year of other biopsy', blank=True)
    other_biopsy_result = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='General pathological analysis of other biopsy', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    other_biopsy_spec = models.TextField(help_text='', null=True, verbose_name='Specify abnormal result for other biopsy', blank=True) # This field type is a guess
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'otherbiopsy'


class ElectroretinogramErg(models.Model):
    erg_date = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year of electroretinogram (ERG)', blank=True)
    erg = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Electroretinogram (ERG) result', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    erg_spec = models.TextField(help_text='', null=True, verbose_name='Specify Electroretinogram (ERG) result', blank=True) # This field type is a guess
    erg_location = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Where was electroretinogram performed?', blank=True)
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'electroretinogramerg'


class ElectroencephalogramEeg(models.Model):
    eeg = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Electroencephalogram (EEG) result', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    eeg_spec = models.TextField(help_text='', null=True, verbose_name='Specify Electroencephalogram (EEG) result', blank=True) # This field type is a guess
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'electroencephalogrameeg'


class ElectromyogramEmg(models.Model):
    emg = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Electromyogram (EMG) results', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    emg_spec = models.TextField(help_text='', null=True, verbose_name='Specify Electromyogram (EMG) results', blank=True) # This field type is a guess
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'electromyogramemg'


class NerveConductionVelocityNcv(models.Model):
    ncv = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Nerve Conduction Velocity (NCV) results', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    ncv_spec = models.TextField(help_text='', null=True, verbose_name='Specify Nerve Conduction Velocity (NCV) results', blank=True) # This field type is a guess
    priortesting = models.ForeignKey(PriorTesting)

    class Meta:
	 db_table = 'nerveconductionvelocityncv'


class FamilyHistory(models.Model):
    suspected_inheritance = models.IntegerField(help_text='', null=True, verbose_name='Suspected mode of  inheritance', blank=True, choices=[(1, 'Autosomal dominant'), (2, 'Autosomal recessive'), (3, 'X-linked dominant'), (4, 'X-linked recessive'), (5, 'Multifactorial'), (6, 'Mitochondrial inheritance'), (7, 'Unknown/Not documented')]) # This field type is a guess
    mat_ancestry = models.CharField(help_text='Separate with commas.  Example: Irish, English, Scottish', null=True, max_length=2000, verbose_name='Maternal ancestry', blank=True)
    pat_ancestry = models.CharField(help_text='Separate with commas.  Example: Irish, English, Scottish', null=True, max_length=2000, verbose_name='Paternal ancestry', blank=True)
    consanguinity_identified = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Consanguinity identified?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    consanguinity_spec = models.TextField(help_text='', null=True, verbose_name='Consanguinity details', blank=True) # This field type is a guess
    occupation_mother = models.CharField(help_text='', null=True, max_length=2000, verbose_name="Mother's occupation", blank=True)
    occupation_father = models.CharField(help_text='', null=True, max_length=2000, verbose_name="Father's occupation", blank=True)
    father_affected = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Father suspected to be affected by same condition as proband?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    father_alive = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Father alive?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    current_age = models.IntegerField(help_text='', null=True, verbose_name="Father's current age", blank=True)
    father_age_at_death = models.IntegerField(help_text='', null=True, verbose_name="Father's age at death", blank=True)
    father_cause_of_death = models.CharField(help_text='', null=True, max_length=2000, verbose_name="Father's cause of death", blank=True)
    mother_affected = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Mother suspected to be affected by same condition as proband?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    mother_alive = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Mother alive?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    mother_age = models.IntegerField(help_text='', null=True, verbose_name="Mother's current age", blank=True)
    mother_age_at_death = models.IntegerField(help_text='', null=True, verbose_name="Mother's age at death", blank=True)
    mother_cause_of_death = models.CharField(help_text='', null=True, max_length=2000, verbose_name="Mother's cause of death", blank=True)
    full_brothers = models.IntegerField(help_text='', null=True, verbose_name='Number of full brothers with same parents', blank=True)
    full_sisters = models.IntegerField(help_text='', null=True, verbose_name='Number of full sisters with same parents', blank=True)
    sibling_dx = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Are any of the brothers or sisters suspected to have the same medical condition as the proband?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    sibling_dx_spec = models.TextField(help_text='(Please specify which sibling, diagnosis, age at diagnosis, and relevant symptoms)', null=True, verbose_name='Sibling diagnosis details', blank=True) # This field type is a guess
    children = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Does the proband have any children?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    sons = models.IntegerField(help_text='', null=True, verbose_name='Number of sons', blank=True)
    daughters = models.IntegerField(help_text='', null=True, verbose_name='Number of daughters', blank=True)
    other_family = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Any other family members with symptoms similar to proband other than those described above?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    family_history_feedback = models.TextField(help_text='', null=True, verbose_name='Please provide any feedback for this form (for example: missing questions, questions not relevant for a disease area, ambiguities, places where a textbox could be replaced with discrete choices, missing discrete choices)', blank=True) # This field type is a guess
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'familyhistory'


class OtherFamilyMembersWithSimilarSymptom(models.Model):
    other_family_side = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Which side of the family is the family member on?', choices=[(1, 'Maternal'), (2, 'Paternal'), (3, 'Unknown/Not documented')])
    other_family_rel = models.CharField(max_length=2000, db_column='other_family_rel ', blank=True, help_text='Ex: First cousin, aunt, etc.', null=True, verbose_name='What is the relationship of the family member to the proband?') # Field renamed to remove spaces. Field renamed to remove ending underscore Field name made lowercase.
    other_family_symptoms = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Describe the symptoms of the family member.', blank=True)
    familyhistory = models.ForeignKey(FamilyHistory)

    class Meta:
	 db_table = 'otherfamilymemberswithsimilarsymptom'


class DevelopmentalHistory(models.Model):
    age_rolled_over = models.FloatField(help_text='Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name='Age first rolled over (months)', blank=True)
    age_sat = models.FloatField(help_text='Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name='Age when first sat (months)', blank=True)
    age_walk = models.FloatField(help_text='Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name='Age when first walked (months)', blank=True)
    age_speech = models.FloatField(help_text='Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name='Age of first word (months)', blank=True)
    speech_delay = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='History of speech delay?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    speech_delay_spec = models.TextField(help_text='', null=True, verbose_name='Speech delay details', blank=True) # This field type is a guess
    current_speech = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Current speech', choices=[(1, 'Normal'), (2, 'Delayed'), (3, 'Nonverbal'), (4, 'Unknown/Not documented')])
    motor_delay = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='History of motor delay?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    motor_delay_spec = models.TextField(help_text='', null=True, verbose_name='Motor delay details', blank=True) # This field type is a guess
    current_motor_ability = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Current motor ability', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Unknown/Not documented')])
    articulation_issues = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Articulation issues?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    articulation_issues_spec = models.TextField(help_text='', null=True, verbose_name='Articulation issues details', blank=True) # This field type is a guess
    balance_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Any balance or coordination problems?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    balance_spec = models.TextField(help_text='', null=True, verbose_name='Describe balance or coordination problems', blank=True) # This field type is a guess
    other_milestones_delay_spec = models.TextField(help_text='', null=True, verbose_name='Specify other developmental delays', blank=True) # This field type is a guess
    developmental_quotient_dq = models.FloatField(help_text='', null=True, verbose_name='Developmental Quotient (DQ)', blank=True)
    iq = models.FloatField(help_text='', null=True, verbose_name='Intelligence Quotient (IQ)', blank=True)
    developmental_regression = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Any developmental regression or loss of skills?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    grade_level = models.TextField(help_text='', null=True, verbose_name='Current school level/grade or most recent school level/grade completed', blank=True) # This field type is a guess
    repeat_grade = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Ever had to repeat a grade?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    grade_repeat_spec = models.TextField(help_text='', null=True, verbose_name='Grade repeated details', blank=True) # This field type is a guess
    iep_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Receiving Current Early Intervention, IEP, or Special Education regime?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    iep_spec = models.TextField(help_text='(Age range when received services, specific developmental areas that were focused on, etc.)', null=True, verbose_name='Please specify details about IEP, Current Early Intervention, or Special Education Regime', blank=True) # This field type is a guess
    avg_grade_perfomance = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Current average grade performance', choices=[(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E'), (6, 'F'), (7, 'Unknown/Not documented')])
    autism_diagnosis_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Autism Spectrum Diagnosis', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    asd_id_link = models.TextField(help_text='', null=True, verbose_name='If this subject has an autism spectrum disorder or intellectual disability, please consider completing the full Intellectual Disability questionnaire.', blank=True) # This field type is a guess
    autism_spectrum_features = models.TextField(help_text='', null=True, verbose_name='Autism spectrum features | Describe other autism spectrum features present', blank=True) # This field type is a guess
    beh_issues_spec = models.TextField(help_text='', null=True, verbose_name='Please specify any behavioral issues not described above.', blank=True) # This field type is a guess
    developmental_history_feedback = models.TextField(help_text='', null=True, verbose_name='Please provide any feedback for this form (for example: missing questions, questions not relevant for a disease area, ambiguities, places where a textbox could be replaced with discrete choices, missing discrete choices)', blank=True) # This field type is a guess
    developmental_regression_area_summary = models.CharField(help_text='1, Speech | 2, Motor | 3, Cognition | 4, Social skills', null=True, max_length=2000, verbose_name='Area of regression/loss of skill | Describe loss of ', blank=True)
    current_therapies_summary = models.CharField(help_text='5, None | 1, Physical therapy | 2, Occupational therapy | 3, Speech therapy | 4, Vision therapy | 6, Unknown/Not documented', null=True, max_length=2000, verbose_name='Current therapies', blank=True)
    autism_spectum_summary = models.CharField(help_text='1, Autism | 2, Asperger Syndrome | 3, PDD-NOS (pervasive developmental disorder, not otherwise specified) | 4, Unclassified | 5, Unknown/Not documented', null=True, max_length=2000, verbose_name='Autism spectrum category', blank=True)
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'developmentalhistory'


class developmentalregressionarea(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Area of regression/loss of skill | Describe loss of ', blank=True)
    value = models.IntegerField(help_text='', null=True, verbose_name='Area of regression/loss of skill | Describe loss of ', blank=True, choices=[(1, 'Speech'), (2, 'Motor'), (3, 'Cognition'), (4, 'Social skills')]) # This field type is a guess
    developmentalhistory = models.ForeignKey(DevelopmentalHistory)

    class Meta:
	 db_table = 'developmentalregressionarea'


class currenttherapies(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Current therapies', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Current therapies', choices=[(5, 'None'), (1, 'Physical therapy'), (2, 'Occupational therapy'), (3, 'Speech therapy'), (4, 'Vision therapy'), (6, 'Unknown/Not documented')])
    developmentalhistory = models.ForeignKey(DevelopmentalHistory)

    class Meta:
	 db_table = 'currenttherapies'


class autismspectum(models.Model):
    label = models.CharField(help_text='ID ', null=True, max_length=2000, verbose_name='Autism spectrum category', blank=True)
    value = models.CharField(help_text='ID ', null=True, max_length=2000, verbose_name='Autism spectrum category', blank=True)
    developmentalhistory = models.ForeignKey(DevelopmentalHistory)

    class Meta:
	 db_table = 'autismspectum'


class ReviewOfSystem(models.Model):
    ros_growth_normal_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='History of abnormal growth', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_growth_spec = models.TextField(help_text='', null=True, verbose_name='Describe abnormal growth', blank=True) # This field type is a guess
    ros_odors_details = models.IntegerField(help_text='', null=True, verbose_name='Unusual odors | Describe other unusual odor', blank=True, choices=[(1, 'None'), (2, 'Sweet (maple syrup)'), (3, 'Fishy'), (4, 'Foul'), (5, 'Musty'), (6, 'Unknown/Not documented'), (7, 'Other')]) # This field type is a guess
    ros_decompensation_w_illness_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Decompensation with illness', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_decompensation_w_illness_spec = models.TextField(help_text='', null=True, verbose_name='Describe decompensation with illness', blank=True) # This field type is a guess
    ros_anesthetic_problems_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Anesthetic problems (hypersensitivity)', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_anesthetic_problems_spec = models.TextField(help_text='', null=True, verbose_name='Describe anesthetic problems', blank=True) # This field type is a guess
    ros_general_other = models.TextField(help_text='', null=True, verbose_name='Describe any other general issues', blank=True) # This field type is a guess
    ros_psychiatric_problems_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Psychiatric problems', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_psychiatric_problems_spec = models.TextField(help_text='', null=True, verbose_name='Describe psychiatric problems', blank=True) # This field type is a guess
    ros_sleep_disturbances_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Sleep disturbances', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_sleep_disturbances_spec = models.TextField(help_text='', null=True, verbose_name='Describe sleep disturbances', blank=True) # This field type is a guess
    ros_stereotypies_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Stereotypies', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_stereotypies_spec = models.TextField(help_text='', null=True, verbose_name='Describe stereotypies', blank=True) # This field type is a guess
    ros_inattention_o_hyper_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Inattention or hyperactivity', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_inattention_o_hyper_spec = models.TextField(help_text='', null=True, verbose_name='Describe inattention or hyperactivity', blank=True) # This field type is a guess
    ros_behavior_other_spec = models.TextField(help_text='', null=True, verbose_name='Describe other behavior issues', blank=True) # This field type is a guess
    ros_patient_resembles = models.IntegerField(help_text='', null=True, verbose_name='Patient resembles', blank=True, choices=[(1, 'Mother'), (2, 'Father'), (3, 'Both'), (4, 'Neither'), (5, 'Unknown/Not documented')]) # This field type is a guess
    ros_headaches_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Chronic headaches or migraines', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_headaches_freq = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Frequency of chronic headaches or migraines', choices=[(1, 'Daily'), (2, 'Weekly'), (3, 'Monthly'), (4, 'Yearly'), (5, 'Less than Yearly'), (6, 'Unknown/Not documented')])
    ros_optho = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Opthalmologic eval', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not performed'), (5, 'Not determined'), (4, 'Unknown/Not documented')])
    ros_vision_concerns_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Vision concerns or known opthalmologic conditions', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_optho_structural_findings = models.IntegerField(help_text='', null=True, verbose_name='Structural findings detail', blank=True, choices=[(6, 'None'), (1, 'microphalmia'), (2, 'cataract'), (3, 'anterior chamber defect'), (4, 'coloboma'), (5, 'optic nerve hypoplasia'), (7, 'Unknown/Not documented'), (8, 'Other')]) # This field type is a guess
    ros_vision_concerns = models.IntegerField(help_text='', null=True, verbose_name='Additional vision conditions', blank=True, choices=[(11, 'None'), (1, 'CPEO'), (2, 'Optic atrophy'), (4, 'Nyctalopia'), (5, 'Hyperopia'), (6, 'Nystagmus'), (7, 'Strabismus'), (8, 'Corneal Clouding'), (9, 'Retinoblastoma'), (10, 'Other')]) # This field type is a guess
    ros_hearing_concerns_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Hearing concerns', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_hearing_concerns_description = models.TextField(help_text='', null=True, verbose_name='Please consider filling out the Hearing Impairment instrument.', blank=True) # This field type is a guess
    ros_hearing_concerns_spec = models.TextField(help_text='Please skip if also filling out hearing impairment intake', null=True, verbose_name='Describe hearing concerns', blank=True) # This field type is a guess
    ros_audio_eval = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Audiology evaluation', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not performed'), (5, 'Not determined'), (4, 'Unknown/Undocumented')])
    ros_audio_eval_spec = models.TextField(help_text='', null=True, verbose_name='Describe abnormal audiology eval', blank=True) # This field type is a guess
    ros_swallowing_difficulties_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Swallowing difficulties', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_swallowing_difficulties_spec = models.TextField(help_text='', null=True, verbose_name='Describe swallowing difficulties', blank=True) # This field type is a guess
    ros_cardiac_anomalies_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Congenital heart defects', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_cardiac_anomalies_spec = models.TextField(help_text='', null=True, verbose_name='Describe congenital heart defects', blank=True) # This field type is a guess
    ros_arrhythmias = models.IntegerField(help_text='', null=True, verbose_name='Arrhythmias | Describe other arrhythmias', blank=True, choices=[(18, 'None'), (1, 'Atrial Fibrillation (A-Fib)'), (2, 'Atrial Flutter'), (3, 'Bradycardia'), (4, 'Brugada Syndrome'), (5, 'Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT)'), (6, 'Heart Block'), (7, 'Long QT Syndrome (LQTS)'), (8, 'Premature Atrial Complexes (PAC)'), (9, 'Premature Ventricular Complexes (PVC)'), (10, 'Short QT Syndrome (SQTS)'), (11, 'Supraventricular Tachycardia (SVT)'), (12, 'Tachycardia'), (13, 'Torsades de pointes'), (14, 'Ventricular Fibrillation (V-Fib)'), (15, 'Ventricular Flutter'), (16, 'Wolff-Parkinson-White Syndrome (WPW)'), (17, 'Other')]) # This field type is a guess
    ros_other_cv_issues_spec = models.TextField(help_text='', null=True, verbose_name='Describe other cardiovascular issues', blank=True) # This field type is a guess
    ros_wheezing_o_asthma_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Wheezing or asthma', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_wheezing_o_asthma_spec = models.TextField(help_text='', null=True, verbose_name='Describe wheezing or asthma', blank=True) # This field type is a guess
    ros_sleep_apnea_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Sleep apnea', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_sleep_apnea_spec = models.TextField(help_text='', null=True, verbose_name='Describe sleep apnea', blank=True) # This field type is a guess
    ros_prior_intubation_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Prior intubation', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_age_intubated = models.TextField(help_text='', null=True, verbose_name='Age at intubation', blank=True) # This field type is a guess
    ros_intubation_removed = models.NullBooleanField(help_text='', verbose_name='Has intubation been removed?', blank=True)
    ros_age_intubation_removed = models.TextField(help_text='', null=True, verbose_name='Age at intubation removal', blank=True) # This field type is a guess
    ros_pulmonary_other = models.TextField(help_text='', null=True, verbose_name='Describe other pulmonary issues', blank=True) # This field type is a guess
    ros_gast_reflux_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Gasteroesophageal reflux', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_gast_reflux_spec = models.TextField(help_text='', null=True, verbose_name='Describe gasteroesophageal reflux', blank=True) # This field type is a guess
    ros_current_feeding = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Current feeding', choices=[(1, 'Oral'), (2, 'Tube Fed'), (3, 'Both'), (4, 'Unknown/No documented')])
    ros_frequent_vomiting_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Frequent vomiting', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_frequent_vomiting_spec = models.TextField(help_text='', null=True, verbose_name='Describe frequent vomiting', blank=True) # This field type is a guess
    ros_diarrhea = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Diarrhea', choices=[(1, 'History of diarrhea'), (2, 'Resolved by medication'), (3, 'Currently has diarrhea'), (4, 'Currently on medication'), (5, 'No history of diarrhea'), (6, 'Unknown/Not documented')])
    ros_feeding_history = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Feeding history', choices=[(1, 'Always Oral'), (2, 'G-tube'), (3, 'N-tube'), (4, 'J-tube'), (5, 'Unknown/Not documented')])
    ros_gtube_age_placement = models.TextField(help_text='', null=True, verbose_name='Age at G-tube placement', blank=True) # This field type is a guess
    ros_gtube_removed = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Has G-tube been removed', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_gtube_age_removed = models.TextField(help_text='', null=True, verbose_name='Age at G-tube removal', blank=True) # This field type is a guess
    ros_ntube_age_placement = models.TextField(help_text='', null=True, verbose_name='Age at N-tube placement', blank=True) # This field type is a guess
    ros_ntube_removed = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Has N-tube been removed', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_ntube_age_removed = models.TextField(help_text='', null=True, verbose_name='Age at N-tube removal', blank=True) # This field type is a guess
    ros_jtube_age_placement = models.TextField(help_text='', null=True, verbose_name='Age at J-tube placement', blank=True) # This field type is a guess
    ros_jtube_removed = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Has J-tube been removed', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_jtube_age_removed = models.TextField(help_text='', null=True, verbose_name='Age at J-tube removal', blank=True) # This field type is a guess
    ros_fail_thrive_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='History of failure to thrive', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_fail_thrive_spec = models.TextField(help_text='', null=True, verbose_name='Describe history of failure to thrive', blank=True) # This field type is a guess
    ros_liver_problems_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Liver problems', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_liver_problems_spec = models.TextField(help_text='', null=True, verbose_name='Describe liver problems', blank=True) # This field type is a guess
    ros_gi_other_spec = models.TextField(help_text='', null=True, verbose_name='Describe other GI issues', blank=True) # This field type is a guess
    ros_hema_prot_dysuria_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Hematuria, proteinura or dysuria', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_hema_prot_dysuria_spec = models.TextField(help_text='', null=True, verbose_name='Describe hematuria, proteinura or dysuria', blank=True) # This field type is a guess
    ros_known_renal_anomalies_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Renal anomalies', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_known_renal_anomalies_spec = models.TextField(help_text='', null=True, verbose_name='Describe renal anomalies', blank=True) # This field type is a guess
    ros_renal_tubular_acidosis_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Renal tubular acidosis', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_renal_tubular_acidosis_spec = models.TextField(help_text='', null=True, verbose_name='Describe renal tubular acidosis', blank=True) # This field type is a guess
    ros_renal_other_spec = models.TextField(help_text='', null=True, verbose_name='Describe other renal issues', blank=True) # This field type is a guess
    ros_tanner_scale = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Tanner Scale', choices=[(1, 'Tanner I'), (2, 'Tanner II'), (3, 'Tanner III'), (4, 'Tanner IV'), (5, 'Tanner V'), (6, 'Unknown/Not documented')])
    ros_puberty_timing = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Puberty timing', choices=[(1, 'Normal'), (2, 'Delayed'), (3, 'Early'), (4, 'Too early to tell'), (5, 'Unknown/Not documented')])
    ros_menarche = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='First menarche occurred', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented'), (4, 'Not applicable')])
    ros_menarche_date = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Date of menarche (month/year)', blank=True)
    ros_diabetes_mellitus_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Diabetes mellitus', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_diabetes_mellitus_spec = models.TextField(help_text='', null=True, verbose_name='Describe diabetes mellitus', blank=True) # This field type is a guess
    ros_known_hormone_problem_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Hormonal imbalance/problems', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_known_hormone_adrenal_cortex_medulla = models.IntegerField(help_text='', null=True, verbose_name='Adrenal Cortex/medulla hormonal imbalance', blank=True, choices=[(1, 'None'), (2, 'Aldosterone'), (3, 'Cortisol'), (4, 'Epinephrine'), (5, 'Norepinephrine'), (6, 'Unknown/Not documented'), (7, 'Other')]) # This field type is a guess
    ros_known_hormone_gonadal = models.IntegerField(help_text='', null=True, verbose_name='Gonadal hormonal imbalance', blank=True, choices=[(1, 'None'), (2, 'Testosterone'), (3, 'Progesterone'), (4, 'Estrogen'), (5, 'hCG'), (6, 'Unknown/Not documented'), (7, 'Other')]) # This field type is a guess
    ros_known_hormone_problem_spec = models.TextField(help_text='', null=True, verbose_name='Please any other known hormone problems', blank=True) # This field type is a guess
    ros_hirsutism_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Hirsutism', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_hirsutism_spec = models.TextField(help_text='', null=True, verbose_name='Describe hirsutism', blank=True) # This field type is a guess
    ros_endocrine_other_spec = models.TextField(help_text='', null=True, verbose_name='Describe other endocrine issues', blank=True) # This field type is a guess
    ros_easy_bruising_bleeding_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Easy bruising or bleeding', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_easy_bruising_bleeding_spec = models.TextField(help_text='', null=True, verbose_name='Describe bruising or bleeding', blank=True) # This field type is a guess
    ros_blood_clots_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Blood clots', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_blood_clots_spec = models.TextField(help_text='', null=True, verbose_name='Describe blood clots', blank=True) # This field type is a guess
    ros_anemia_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Anemia', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_anemia_spec = models.TextField(help_text='', null=True, verbose_name='Please describe anemia', blank=True) # This field type is a guess
    ros_hematologic_other = models.TextField(help_text='', null=True, verbose_name='Describe other hematologic issues', blank=True) # This field type is a guess
    ros_muscle_strength = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Muscle strength history', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Unknown/Not documented')])
    ros_muscle_strength_spec = models.TextField(help_text='', null=True, verbose_name='Describe abnormal muscle strength history', blank=True) # This field type is a guess
    ros_muscle_bulk = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Muscle bulk history', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Unknown/Not documented')])
    ros_muscle_bulk_spec = models.TextField(help_text='', null=True, verbose_name='Describe abnormal muscle bulk history', blank=True) # This field type is a guess
    ros_hypotonia_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Hypotonia', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_hypotonia_spec = models.TextField(help_text='', null=True, verbose_name='Describe hypotonia', blank=True) # This field type is a guess
    ros_fatigue = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Fatigue', choices=[(4, 'None'), (1, 'Chronic Fatigue'), (2, 'Fatigues easily'), (3, 'Low Energy'), (5, 'Unknown/Not documented')])
    ros_fractures_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Fractures', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_fractues_spec = models.TextField(help_text='', null=True, verbose_name='Describe fractures', blank=True) # This field type is a guess
    ros_spine_curvature = models.IntegerField(help_text='', null=True, verbose_name='Spine Curvature', blank=True, choices=[(6, 'Normal'), (1, 'Kyphosis'), (2, 'Lordosis'), (3, 'Scoliosis'), (5, 'Kyphoscoliosis'), (7, 'Unknown/Not documented'), (4, 'Other')]) # This field type is a guess
    ros_joint_laxity_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Joint laxity', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_joint_laxity_spec = models.TextField(help_text='', null=True, verbose_name='Describe joint laxity', blank=True) # This field type is a guess
    ros_musculoskeletal_other_spec = models.TextField(help_text='', null=True, verbose_name='Describe other musculoskeletal issues', blank=True) # This field type is a guess
    ros_seizures_freq = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Seizures', choices=[(7, 'None'), (1, 'Rare (1-5)'), (2, 'daily'), (3, 'weekly'), (4, 'monthly'), (5, 'yearly'), (6, 'Febrile only'), (8, 'Unknown/Not documented')])
    ros_seizures_spec = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Type of seizure', blank=True)
    ros_seizures_onset_age = models.TextField(help_text='', null=True, verbose_name='Age of onset of seizures', blank=True) # This field type is a guess
    ros_seizures_require_med_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Seizures require seizure medication', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_seizures_med_controlled_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Seizures controlled by seizure medication', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_peripheral_neuropathy_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Peripheral neuropathy', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_peripheral_neuropathy_spec = models.TextField(help_text='', null=True, verbose_name='Describe peripheral neuropathy', blank=True) # This field type is a guess
    ros_movement_disorders_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Movement disorders', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_movement_disorders_spec = models.TextField(help_text='', null=True, verbose_name='Describe movement disorders', blank=True) # This field type is a guess
    ros_neurologic_other_spec = models.TextField(help_text='', null=True, verbose_name='Describe other neurologic issues', blank=True) # This field type is a guess
    ros_frequent_illness_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Frequent illness', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_frequent_illness_spec = models.TextField(help_text='', null=True, verbose_name='Describe frequent illness', blank=True) # This field type is a guess
    ros_immunologic_other_spec = models.TextField(help_text='', null=True, verbose_name='Describe other immunologic issues', blank=True) # This field type is a guess
    ros_lipomas_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Lipomas', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ros_lipomas_spec = models.TextField(help_text='', null=True, verbose_name='Describe lipomas', blank=True) # This field type is a guess
    ros_dermatologic_other_spec = models.TextField(help_text='', null=True, verbose_name='Describe other dermatologic issues', blank=True) # This field type is a guess
    ros_other_notes_spec = models.TextField(help_text='', null=True, verbose_name='Additional notes', blank=True) # This field type is a guess
    ros_feedback = models.TextField(help_text='', null=True, verbose_name='Please provide any feedback for this form (for example: missing questions, questions not relevant for a disease area, ambiguities, places where a textbox could be replaced with discrete choices, missing discrete choices)', blank=True) # This field type is a guess
    ros_retinal_findings_summary = models.CharField(help_text='4, None | 1, Retinal pigmentary difference | 2, Retinopathy | 3, Retinitis pigmentosa | 5, Unknown/Not documented | 6, Other', null=True, max_length=2000, verbose_name='Retinal findings', blank=True)
    ros_optho_acuity_findings_summary = models.CharField(help_text='6, None | 1, myopia | 2, farsighted | 3, blind | 4, amblyopia | 5, astigmatism | 7, Unknown/Not documented | 8, Other', null=True, max_length=2000, verbose_name='Acuity findings detail', blank=True)
    ros_dental_problems_summary = models.CharField(help_text='6, None | 1, Caries | 2, Oligodontia | 3, Rotting | 4, Dental crowding | 8, Unknown/Not documented | 7, Other unknown problem | 5, Other', null=True, max_length=2000, verbose_name='Dental problems', blank=True)
    ros_cardiac_muscle_hypertrophy_summary = models.CharField(help_text='7, None | 1, Hypertrophic Cardiomyopathy | 2, Dilated Cardiomyopathy | 3, Left Ventricular Noncompaction | 4, Restrictive Cardiomyopathy | 5, Arrhythmogenic Right Ventricular Dysplasia (ARVD) | 6, Other', null=True, max_length=2000, verbose_name='Cardiomyopathy', blank=True)
    ros_constipation_summary = models.CharField(help_text='1, History of constipation | 2, Resolved by medication | 3, Currently has constipation | 4, Currently on medication | 5, No history of constipation | 6, Unknown/Not documented', null=True, max_length=2000, verbose_name='Constipation', blank=True)
    ros_genitalia_summary = models.CharField(help_text='6, None | 1, Undescended teste | 2, Hypospadias | 3, Freckling | 4, Labial abnormality | 7, Unknown/Not documented | 8, Other unknown abnormality | 5, Other', null=True, max_length=2000, verbose_name='Genitalia abnormality', blank=True)
    ros_known_hormone_hypothalmic_pituitary_summary = models.CharField(help_text='1, None | 2, GnRH | 3, TRH | 4, Dopamine | 5, CRH | 6, GHRH/Somatostatin | 7, Vasopressor | 8, Oxytocin | 9, FSH | 10, FSHB | 11, LH | 12, LHB | 13, TSH | 14, TSHB | 15, CGA | 16, Prolactin | 17, POMC | 18, ACTH | 19, GH | 20, Unkonwn/Not documented | 21, Other', null=True, max_length=2000, verbose_name='Hypothalamic-pituitary hormonal imbalance', blank=True)
    ros_known_hormone_thyroid_parathyroid_summary = models.CharField(help_text='1, None | 2, Thyroid hormone (T3 and/or T4) | 3, Calcitonin | 4, PTH | 5, Unknown/Not documented | 6, Other', null=True, max_length=2000, verbose_name='Thyroid/Parathyroid hormonal imbalance', blank=True)
    ros_allergies_summary = models.CharField(help_text='6, None | 1, Medication | 2, Food | 3, Seasonal or environmental | 4, Unknown/Not documented | 7, Other unknown allergy | 5, Other ', null=True, max_length=2000, verbose_name='Known allergies', blank=True)
    ros_rashes_eczema_birthmarks_summary = models.CharField(help_text='1, None | 2, Cafe au lait spots | 3, Capillary hemangioma | 4, Cutis marmorata | 5, Diffuse hypopigmented skin lesions | 6, Unknown/Not documented| 7, Other unknown abnormality | 8, Other', null=True, max_length=2000, verbose_name='Birthmarks or rash | Describe other birthmark rash', blank=True)
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'reviewofsystem'


class rosretinalfindings(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Retinal findings', blank=True)
    value = models.IntegerField(help_text='', null=True, verbose_name='Retinal findings', blank=True, choices=[(4, 'None'), (1, 'Retinal pigmentary difference'), (2, 'Retinopathy'), (3, 'Retinitis pigmentosa'), (5, 'Unknown/Not documented'), (6, 'Other')]) # This field type is a guess
    reviewofsystem = models.ForeignKey(ReviewOfSystem)

    class Meta:
	 db_table = 'rosretinalfindings'


class rosopthoacuityfindings(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Acuity findings detail', blank=True)
    value = models.IntegerField(help_text='', null=True, verbose_name='Acuity findings detail', blank=True, choices=[(6, 'None'), (1, 'myopia'), (2, 'farsighted'), (3, 'blind'), (4, 'amblyopia'), (5, 'astigmatism'), (7, 'Unknown/Not documented'), (8, 'Other')]) # This field type is a guess
    reviewofsystem = models.ForeignKey(ReviewOfSystem)

    class Meta:
	 db_table = 'rosopthoacuityfindings'


class rosdentalproblems(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Dental problems', blank=True)
    value = models.IntegerField(help_text='', null=True, verbose_name='Dental problems', blank=True, choices=[(6, 'None'), (1, 'Caries'), (2, 'Oligodontia'), (3, 'Rotting'), (4, 'Dental crowding'), (8, 'Unknown/Not documented'), (7, 'Other unknown problem'), (5, 'Other')]) # This field type is a guess
    reviewofsystem = models.ForeignKey(ReviewOfSystem)

    class Meta:
	 db_table = 'rosdentalproblems'


class roscardiacmusclehypertrophy(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Cardiomyopathy', blank=True)
    value = models.IntegerField(help_text='', null=True, verbose_name='Cardiomyopathy', blank=True, choices=[(7, 'None'), (1, 'Hypertrophic Cardiomyopathy'), (2, 'Dilated Cardiomyopathy'), (3, 'Left Ventricular Noncompaction'), (4, 'Restrictive Cardiomyopathy'), (5, 'Arrhythmogenic Right Ventricular Dysplasia (ARVD)'), (6, 'Other')]) # This field type is a guess
    reviewofsystem = models.ForeignKey(ReviewOfSystem)

    class Meta:
	 db_table = 'roscardiacmusclehypertrophy'


class rosconstipation(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Constipation', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Constipation', choices=[(1, 'History of constipation'), (2, 'Resolved by medication'), (3, 'Currently has constipation'), (4, 'Currently on medication'), (5, 'No history of constipation'), (6, 'Unknown/Not documented')])
    reviewofsystem = models.ForeignKey(ReviewOfSystem)

    class Meta:
	 db_table = 'rosconstipation'


class rosgenitalia(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Genitalia abnormality', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Genitalia abnormality', choices=[(6, 'None'), (1, 'Undescended teste'), (2, 'Hypospadias'), (3, 'Freckling'), (4, 'Labial abnormality'), (7, 'Unknown/Not documented'), (8, 'Other unknown abnormality'), (5, 'Other')])
    reviewofsystem = models.ForeignKey(ReviewOfSystem)

    class Meta:
	 db_table = 'rosgenitalia'


class rosknownhormonehypothalmicpituitary(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Hypothalamic-pituitary hormonal imbalance', blank=True)
    value = models.IntegerField(help_text='', null=True, verbose_name='Hypothalamic-pituitary hormonal imbalance', blank=True, choices=[(1, 'None'), (2, 'GnRH'), (3, 'TRH'), (4, 'Dopamine'), (5, 'CRH'), (6, 'GHRH/Somatostatin'), (7, 'Vasopressor'), (8, 'Oxytocin'), (9, 'FSH'), (10, 'FSHB'), (11, 'LH'), (12, 'LHB'), (13, 'TSH'), (14, 'TSHB'), (15, 'CGA'), (16, 'Prolactin'), (17, 'POMC'), (18, 'ACTH'), (19, 'GH'), (20, 'Unkonwn/Not documented'), (21, 'Other')]) # This field type is a guess
    reviewofsystem = models.ForeignKey(ReviewOfSystem)

    class Meta:
	 db_table = 'rosknownhormonehypothalmicpituitary'


class rosknownhormonethyroidparathyroid(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Thyroid/Parathyroid hormonal imbalance', blank=True)
    value = models.IntegerField(help_text='', null=True, verbose_name='Thyroid/Parathyroid hormonal imbalance', blank=True, choices=[(1, 'None'), (2, 'Thyroid hormone (T3 and/or T4)'), (3, 'Calcitonin'), (4, 'PTH'), (5, 'Unknown/Not documented'), (6, 'Other')]) # This field type is a guess
    reviewofsystem = models.ForeignKey(ReviewOfSystem)

    class Meta:
	 db_table = 'rosknownhormonethyroidparathyroid'


class rosallergies(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Known allergies', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Known allergies', choices=[(6, 'None'), (1, 'Medication'), (2, 'Food'), (3, 'Seasonal or environmental'), (4, 'Unknown/Not documented'), (7, 'Other unknown allergy'), (5, 'Other')])
    reviewofsystem = models.ForeignKey(ReviewOfSystem)

    class Meta:
	 db_table = 'rosallergies'


class rosrasheseczemabirthmarks(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Birthmarks or rash | Describe other birthmark rash', blank=True)
    value = models.IntegerField(help_text='', null=True, verbose_name='Birthmarks or rash | Describe other birthmark rash', blank=True, choices=[(1, 'None'), (2, 'Cafe au lait spots'), (3, 'Capillary hemangioma'), (4, 'Cutis marmorata'), (5, 'Diffuse hypopigmented skin lesions'), (6, 'Unknown/Not documented'), (7, 'Other unknown abnormality'), (8, 'Other')]) # This field type is a guess
    reviewofsystem = models.ForeignKey(ReviewOfSystem)

    class Meta:
	 db_table = 'rosrasheseczemabirthmarks'


class OtherGenitaliaAbnormality(models.Model):
    ros_other_genitalia_abnormality = models.CharField(help_text='', null=True, max_length=2000, verbose_name='other genitalia abnormality', blank=True)
    reviewofsystem = models.ForeignKey(ReviewOfSystem)

    class Meta:
	 db_table = 'othergenitaliaabnormality'


class MedicationAllergy(models.Model):
    ros_allergies_medication = models.CharField(help_text='', null=True, max_length=2000, verbose_name='medication allergy', blank=True)
    reviewofsystem = models.ForeignKey(ReviewOfSystem)

    class Meta:
	 db_table = 'medicationallergy'


class FoodAllergy(models.Model):
    ros_allergies_food = models.CharField(help_text='', null=True, max_length=2000, verbose_name='food allergy', blank=True)
    reviewofsystem = models.ForeignKey(ReviewOfSystem)

    class Meta:
	 db_table = 'foodallergy'


class OtherAllergy(models.Model):
    ros_allergies_other = models.CharField(help_text='', null=True, max_length=2000, verbose_name='other allergry', blank=True)
    reviewofsystem = models.ForeignKey(ReviewOfSystem)

    class Meta:
	 db_table = 'otherallergy'


class Surgery(models.Model):
    ros_surgeries = models.TextField(help_text='Please specify age, reason, and treatment/type of surgery. If filling out cardiac intake forms, please describe any Cardiac Surgeries in the appropriate question there instead of here.', null=True, verbose_name='Significant surgery', blank=True) # This field type is a guess
    reviewofsystem = models.ForeignKey(ReviewOfSystem)

    class Meta:
	 db_table = 'surgery'


class Hospitalization(models.Model):
    ros_hospita = models.TextField(help_text='Please specify age, reason for hospitalization', null=True, verbose_name='Significant hospitalization', blank=True) # This field type is a guess
    reviewofsystem = models.ForeignKey(ReviewOfSystem)

    class Meta:
	 db_table = 'hospitalization'


class Medication(models.Model):
    ros_medication = models.TextField(help_text='', null=True, verbose_name='current medication (if known)', blank=True) # This field type is a guess
    reviewofsystem = models.ForeignKey(ReviewOfSystem)

    class Meta:
	 db_table = 'medication'


class PhysicalExam(models.Model):
    age_of_exam = models.TextField(help_text='', null=True, verbose_name='Age of exam', blank=True) # This field type is a guess
    height = models.TextField(help_text='Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name='Height', blank=True) # This field type is a guess
    weight = models.TextField(help_text='Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name='Weight', blank=True) # This field type is a guess
    head_cir = models.FloatField(help_text='Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name='Head circumference (cm)', blank=True)
    head_shape = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Head shape', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Unknown/Not documented')])
    head_shape_spec = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Specify abnormal head shape', blank=True)
    anterior_fontanel_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Anterior fontanelle open and flat', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    anterior_fontanel_spec = models.TextField(help_text='', null=True, verbose_name='Describe fontanelle', blank=True) # This field type is a guess
    forehead = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Forehead', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Unknown/Not documented')])
    forehead_spec = models.TextField(help_text='', null=True, verbose_name='Describe abnormal forehead', blank=True) # This field type is a guess
    eyes_measured = models.NullBooleanField(help_text='', verbose_name='Eyes measured', blank=True)
    icd = models.FloatField(help_text='Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name='Inner Canthal Distance (mm)', blank=True)
    ocd = models.FloatField(help_text='Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name='Outer Canthal Distance (mm)', blank=True)
    ipd = models.FloatField(help_text='Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name='Inter Pupillary Distance (mm)', blank=True)
    ipd_source = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Inter Pupillary Distance (IPD) was', choices=[(1, 'measured'), (2, 'calculated')])
    w_index = models.FloatField(help_text='', null=True, verbose_name='W Index', blank=True)
    epicanthal_folds_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Epicanthal folds', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    epicanthal_folds_spec = models.TextField(help_text='', null=True, verbose_name='Describe epicanthal folds', blank=True) # This field type is a guess
    heterochromia_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Heterochromia', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ears = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Ears', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Unknown/Not documented')])
    ear_lowset = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Lowset ear(s)', choices=[(1, 'Right'), (2, 'Left'), (3, 'Unknown/Not documented')])
    ear_pit_side = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Pit side', choices=[(1, 'Right'), (2, 'Left'), (3, 'Unknown/Not documented')])
    ear_pits_no_r = models.IntegerField(help_text='', null=True, verbose_name='Number of pits right', blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, 'Unknown/Not documented')]) # This field type is a guess
    ear_pits_no_l = models.IntegerField(help_text='', null=True, verbose_name='Number of pits left', blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, 'Unknown/Not documented')]) # This field type is a guess
    ear_tags_no_r = models.IntegerField(help_text='', null=True, verbose_name='Number of tags right', blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, 'Unknown/Not documented')]) # This field type is a guess
    ear_tags_no_l = models.IntegerField(help_text='', null=True, verbose_name='Number of tags left', blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, 'Unknown/Not documented')]) # This field type is a guess
    ear_abnormality_type_r = models.TextField(help_text='', null=True, verbose_name='Type of right ear structural abnormality', blank=True) # This field type is a guess
    ear_abnormality_type_l = models.TextField(help_text='', null=True, verbose_name='Type of left ear structural abnormality', blank=True) # This field type is a guess
    ear_large_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Large ears?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ear_small_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Small ears?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ears_measured = models.NullBooleanField(help_text='', verbose_name='Ears measured?', blank=True)
    ear_length_r = models.FloatField(help_text='Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name='Right ear length (cm)', blank=True)
    ear_length_l = models.FloatField(help_text='Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name='Left ear length (cm)', blank=True)
    midface_abnormality = models.IntegerField(help_text='', null=True, verbose_name='Midface abnormalities', blank=True, choices=[(4, 'None'), (1, 'Midface Hypoplasia'), (2, 'Unknown/Not documented'), (3, 'Other unknown abnormality'), (5, 'Other')]) # This field type is a guess
    philtrum = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Philtrum', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Unknown/Not documented')])
    philtrum_spec = models.TextField(help_text='', null=True, verbose_name='Describe philtrum abnormalities', blank=True) # This field type is a guess
    palate_uvula_abnormality = models.IntegerField(help_text='', null=True, verbose_name='Palate/uvula abnormalities', blank=True, choices=[(4, 'None'), (1, 'Cleft'), (2, 'Arched'), (3, 'Narrowed'), (5, 'Other unknown abnormality'), (6, 'Other')]) # This field type is a guess
    cleft_spec = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Cleft type', choices=[(1, 'soft'), (2, 'hard'), (3, 'uvula')])
    chin = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Chin', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Unknown/Not documented')])
    chin_spec = models.TextField(help_text='', null=True, verbose_name='Describe chin abnormalities', blank=True) # This field type is a guess
    neck_webbing_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Neck webbing', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    neck_webbing_spec = models.TextField(help_text='', null=True, verbose_name='Describe neck webbing', blank=True) # This field type is a guess
    neck_jugular_venous_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Jugular venous distention present', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    neck_tracheostomy_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Tracheostomy present', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    neck_hairline = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Hairline', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Unknown/Not documented')])
    neck_hairline_spec = models.TextField(help_text='', null=True, verbose_name='Describe abnormal hairline', blank=True) # This field type is a guess
    thyroid_enlargement_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Thyroid enlargement', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    murmurs_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Murmurs', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    murmurs_spec = models.TextField(help_text='', null=True, verbose_name='Describe murmurs', blank=True) # This field type is a guess
    asym_chest_wall_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Asymmetrical chest wall', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    asym_chest_wall_spec = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Describe asymmetrical chest wall', blank=True)
    sternotomy_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Sternotomy ', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    thoractomy_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Thoracotomy', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    marfan_stigmata_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Marfan Stigmata/findings present', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    marfan_minor_criteria = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Ghent Criteria for Marfan Syndrome (Minor Criteria/System)', choices=[(16, 'None'), (1, 'Skeletal: Characteristic facies'), (2, 'Skeletal: High palate with dental crowding'), (3, 'Skeletal: Joint hypermobility'), (4, 'Skeletal: Pectus excavatum'), (5, 'CV: Calcified mitral annuls in patient'), (6, 'CV: Mitral valve prolapse'), (7, 'CV: Pulmonary artery dilation'), (8, 'CV: Other aortic dilation/ dissection'), (9, 'Ocular: Abnormal flat cornea'), (10, 'Ocular: Hypoplastic iris or cillary muscle causing decreased miosis'), (11, 'Ocular: Increased axial length of globe causing myopia'), (12, 'Pulmonary: Apical blebs'), (13, 'Pulmonary: Pneumothorax'), (14, 'Skin: Hernias'), (15, 'Skin: Striae atrophicae')])
    nipples = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Nipples (form and position)', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Unknown/Not documented')])
    nipples_spec = models.TextField(help_text='', null=True, verbose_name='Describe nipple abnormalities', blank=True) # This field type is a guess
    inter_nipple_dist = models.CharField(help_text='Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, max_length=2000, verbose_name='Inter nipple distance (cm)', blank=True)
    chest_cir = models.CharField(help_text='Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, max_length=2000, verbose_name='Chest circumference (cm)', blank=True)
    ipc_cc_ratio = models.FloatField(help_text='', null=True, verbose_name='Inter nipple distance chest circumference ratio', blank=True)
    nephromegaly_extent = models.FloatField(help_text='', null=True, verbose_name='Extent of Nephromegaly (cm)', blank=True)
    hepatomegaly_extent = models.FloatField(help_text='', null=True, verbose_name='Extent of Hepatomegaly (cm)', blank=True)
    splenomegaly_extent = models.FloatField(help_text='', null=True, verbose_name='Extent of Splenomegaly (cm)', blank=True)
    hepatosplenomegaly_extent = models.FloatField(help_text='', null=True, verbose_name='Extent of Hepatosplenomegaly (cm)', blank=True)
    other_organomegaly_extent = models.FloatField(help_text='', null=True, verbose_name='Extent of other Organomegaly (cm)', blank=True)
    hernia_inguinal_lat = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Inguinal hernia laterality', choices=[(1, 'Bilateral'), (2, 'Unilateral')])
    hernia_inguinal_side = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Inguinal hernia side', choices=[(1, 'Right'), (2, 'Left')])
    ascites_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Ascites present', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ascites_fluid_wave_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Ascites fluid wave', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ascites_spec = models.TextField(help_text='', null=True, verbose_name='Describe ascites', blank=True) # This field type is a guess
    spine_curvature = models.IntegerField(help_text='', null=True, verbose_name='Abnormal curvature of the spine | Type of curvature', blank=True, choices=[(1, 'None'), (2, 'Kyphosis'), (3, 'Lordosis'), (5, 'Scoliosis'), (6, 'Kyphoscoliosis'), (7, 'Unknown/Not documented'), (8, 'Other unknown abnormality'), (9, 'Other')]) # This field type is a guess
    sacral_abnormality = models.IntegerField(help_text='', null=True, verbose_name='Sacral abnormality | Type of sacral abnormality', blank=True, choices=[(10, 'None'), (1, 'abnormal crease'), (4, 'Meningomyelocele'), (5, 'Spina Bifida'), (6, 'Deep sacral simple'), (7, 'Unknown/Not documented'), (8, 'Other unknown abnormality'), (9, 'Other')]) # This field type is a guess
    skin_hyperextensibility_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Skin hyperextensibility', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    skin_hyperextensibility_spec = models.TextField(help_text='', null=True, verbose_name='Describe skin hyperextensibility', blank=True) # This field type is a guess
    hair_abnormal_spec = models.IntegerField(help_text='', null=True, verbose_name='Hair abnormalities', blank=True, choices=[(9, 'None'), (1, 'Alopecia'), (2, 'Hirsutism'), (3, 'Dry'), (4, 'Brittle'), (5, 'Coarse'), (6, 'Wooly'), (7, 'Kinky'), (8, 'Blond'), (10, 'Unknown/Not documened'), (12, 'Other unknown abnormality'), (11, 'Other')]) # This field type is a guess
    anus_position = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Anus position', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Unknown/Not documented')])
    anus_position_spec = models.TextField(help_text='', null=True, verbose_name='Describe abnormally positioned anus', blank=True) # This field type is a guess
    arm_symmetry_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Arm symmetry', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    arm_symmetry_spec = models.TextField(help_text='', null=True, verbose_name='Describe arm asymmetry', blank=True) # This field type is a guess
    arm_span_measure = models.FloatField(help_text='', null=True, verbose_name='Arm span measurement (cm)/Marfan/ED', blank=True)
    leg_symmetry_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Leg symmetry ', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    leg_symmetry_spec = models.TextField(help_text='', null=True, verbose_name='Describe leg asymmetry', blank=True) # This field type is a guess
    patellae = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Patellae', choices=[(1, 'Present'), (2, 'Absent')])
    joint_hypermobility_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Joint hypermobility', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    joint_hypermobility_spec = models.TextField(help_text='', null=True, verbose_name='Describe joint hypermobility', blank=True) # This field type is a guess
    contractures_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Contractures', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    contractures_spec = models.TextField(help_text='', null=True, verbose_name='Describe contractures', blank=True) # This field type is a guess
    right_palm_length = models.FloatField(help_text='Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name='Right palm length (cm)', blank=True)
    right_mf_length = models.FloatField(help_text='Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name='Right middle finger length (cm)', blank=True)
    right_mf_palm_ratio = models.FloatField(help_text='', null=True, verbose_name='Right MF palm ratio', blank=True)
    left_palm_length = models.FloatField(help_text='Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher.', null=True, verbose_name='Left palm length (cm)', blank=True)
    left_mf_length = models.FloatField(help_text='Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name='Left middle finger length (cm)', blank=True)
    left_mf_palm_ratio = models.FloatField(help_text='', null=True, verbose_name='Left  MF palm ratio', blank=True)
    dermatoglyphic_pattern = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Dermatoglyphic pattern', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Unknown/Not documented')])
    hand_right_d2 = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Right hand digit 2', choices=[(1, 'Ulnar loop'), (2, 'Radial loop'), (3, 'Whorl'), (4, 'Double loop'), (5, 'Arch'), (6, 'Tented arch'), (7, 'Medial')])
    hand_right_d4 = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Right hand digit 4', choices=[(1, 'Ulnar loop'), (2, 'Radial loop'), (3, 'Whorl'), (4, 'Double loop'), (5, 'Arch'), (6, 'Tented arch'), (7, 'Medial')])
    hand_left_d1 = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Left hand digit 1', choices=[(1, 'Ulnar loop'), (2, 'Radial loop'), (3, 'Whorl'), (4, 'Double loop'), (5, 'Arch'), (6, 'Tented arch'), (7, 'Medial')])
    hand_left_d3 = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Left hand digit 3', choices=[(1, 'Ulnar loop'), (2, 'Radial loop'), (3, 'Whorl'), (4, 'Double loop'), (5, 'Arch'), (6, 'Tented arch'), (7, 'Medial')])
    hand_left_d5 = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Left hand digit 5', choices=[(1, 'Ulnar loop'), (2, 'Radial loop'), (3, 'Whorl'), (4, 'Double loop'), (5, 'Arch'), (6, 'Tented arch'), (7, 'Medial')])
    dermatoglyphic_pattern_spec = models.TextField(help_text='', null=True, verbose_name='Other comments regarding dermatoglyphic pattern on hands', blank=True) # This field type is a guess
    hand_creases = models.IntegerField(max_length=2000, blank=True, help_text='Normal = 2 creases; Abnormal = 1 crease', null=True, verbose_name='Creases?', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Unknown/Not documented')])
    hand_crease_rt_details = models.IntegerField(help_text='', null=True, verbose_name='Right hand creases', blank=True, choices=[(1, 'Single palmer'), (2, 'Branched'), (4, 'Unknown/Not documented'), (3, 'Other')]) # This field type is a guess
    hand_crease_lt_detail = models.IntegerField(help_text='', null=True, verbose_name='Left hand creases', blank=True, choices=[(1, 'Single palmer'), (2, 'Branched'), (4, 'Unknown/Not documented'), (3, 'Other')]) # This field type is a guess
    hand_other_features = models.IntegerField(help_text='', null=True, verbose_name='Features of fingers', blank=True, choices=[(10, 'None'), (1, 'Brachydactyly'), (2, 'Syndactyly'), (3, 'Postaxial Polydactyly'), (4, 'Preaxial Polydactyly'), (5, 'Camptodactyly'), (7, 'Ectrodactyly'), (8, 'Arachnodactyly'), (11, 'Clubbing'), (12, 'Clinodactyly'), (9, 'Unknown/Not documented'), (13, 'Other unknown feature'), (15, 'Other')]) # This field type is a guess
    arachnodactyl_side = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Location of arachnodactyly', choices=[(1, 'Both Hands'), (2, 'Right Hand only'), (3, 'Left Hand only'), (4, 'Unknown/Not documented')])
    clinodactyly_r_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Clinodactyly right', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    clinodactyly_l_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Clinodactyly left', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    foot_right_length = models.CharField(help_text='Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, max_length=2000, verbose_name='Right foot length (cm)', blank=True)
    foot_left_length = models.CharField(help_text='Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, max_length=2000, verbose_name='Left foot length (cm)', blank=True)
    foot_syndactyly_right_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='2-3 syndactyly right', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    foot_syndactyly_left_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='2-3 syndactyly left', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    feet_nails = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Foot nails', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Unknown/Not documented')])
    feet_nails_spec = models.TextField(help_text='', null=True, verbose_name='Describe abnormal foot nails', blank=True) # This field type is a guess
    muscle_tone_strength = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Muscle tone and strength', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Unknown/Not documented')])
    muscle_tone_strength_spec = models.TextField(help_text='', null=True, verbose_name='Describe muscle tone and strength', blank=True) # This field type is a guess
    reflexes = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Reflexes', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Unknown/Not documented')])
    reflexes_spec = models.TextField(help_text='', null=True, verbose_name='Describe reflexes', blank=True) # This field type is a guess
    gait = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Gait', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Unknown/Not documented')])
    gait_spec = models.TextField(help_text='', null=True, verbose_name='Describe gait', blank=True) # This field type is a guess
    diminished_pulses_loc = models.TextField(help_text='', null=True, verbose_name='Location of diminshed pulses', blank=True) # This field type is a guess
    absent_pulses_loc = models.TextField(help_text='', null=True, verbose_name='Location of absent pulses', blank=True) # This field type is a guess
    palpation = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Palpation', choices=[(1, 'Normal impulse'), (2, 'Heave'), (3, 'Thrill'), (4, 'Unknown/Not documente')])
    heaves_loc = models.IntegerField(help_text='', null=True, verbose_name='Location of Heave | Heave  - Specify', blank=True, choices=[(1, 'Left Ventricular'), (2, 'Right Ventricular'), (3, 'Unknown/Not documented'), (4, 'Other')]) # This field type is a guess
    thrill_loc = models.IntegerField(help_text='', null=True, verbose_name='Location of Thrill | Location of Thrill  - Specify', blank=True, choices=[(1, 'ULSB'), (2, 'URSB'), (3, 'Suprasternal notch'), (4, 'LLSB'), (5, 'Apex'), (7, 'Unknown/Not documented'), (6, 'Other')]) # This field type is a guess
    auscultation = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Auscultation', choices=[(1, 'Regular Rhythm'), (2, 'Irregular Rhythm'), (3, 'Hyperdynamic'), (4, 'Unknown/Not documented')])
    auscultation_spec = models.TextField(help_text='', null=True, verbose_name='Describe auscultation', blank=True) # This field type is a guess
    click = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Click', choices=[(1, 'Absent'), (2, 'Present'), (3, 'Unknown/Not documented')])
    click_timing = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Timing of Click', choices=[(1, 'Early'), (2, 'Mid'), (3, 'Late'), (5, 'Unknown/Not documente')])
    click_loc = models.IntegerField(help_text='', null=True, verbose_name='Location of Click | Location of Click  - Specify', blank=True, choices=[(1, 'ULSB'), (2, 'URSB'), (3, 'Suprasternal notch'), (4, 'LLSB'), (5, 'Apex'), (7, 'Unknown/Not documented'), (6, 'Other')]) # This field type is a guess
    gallop = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Gallop', choices=[(1, 'Absent'), (2, 'Present'), (3, 'Unknown/Not documented')])
    gallop_spec = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Type of gallop', choices=[(1, 'S3'), (2, 'S4'), (3, 'Summation'), (4, 'Unknown/Not documented')])
    rub = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Rub', choices=[(1, 'Absent'), (2, 'Present'), (3, 'Unknown/Not documented')])
    rub_spec = models.IntegerField(help_text='', null=True, verbose_name='Describe rub | Describe rub  - Specify', blank=True, choices=[(1, 'Pleural'), (2, 'Pericardial'), (4, 'Unknown/Not documented'), (3, 'Other')]) # This field type is a guess
    pmi = models.IntegerField(help_text='', null=True, verbose_name='PMI | Specify PMI', blank=True, choices=[(1, 'Normal (5th left ICS MCL)'), (2, 'Dextrocardia'), (4, 'Unknown/Not documented'), (3, 'Other')]) # This field type is a guess
    second_heart_sound = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Second Heart Sound', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Widely split'), (4, 'Single'), (5, 'Loud'), (6, 'Narrowly split'), (7, 'Fixed split'), (8, 'Increased P2'), (9, 'Unknown/Not documented')])
    systolic_murmur_grade = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Systolic murmur grade (1 to 6)', blank=True)
    systolic_murmur_location = models.IntegerField(help_text='', null=True, verbose_name='Systolic murmur location | Systolic murmur location Other: Specify', blank=True, choices=[(1, 'LUSB'), (2, 'RUSB'), (3, 'MLSB'), (4, 'LLSB'), (5, 'LRSB'), (6, 'Apex'), (7, 'Post chest (R)'), (8, 'Post chest (L)'), (9, 'Under clavicle (R)'), (10, 'Under clavicle (L)'), (11, 'Right axillae'), (12, 'Left Axillae'), (14, 'Unknown/Not documented'), (13, 'Other')]) # This field type is a guess
    systolic_murmur_pitch = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Systolic murmur pitch', choices=[(1, 'High'), (2, 'Mid'), (3, 'Low'), (4, 'Unknown/Not documented')])
    systolic_murmur_radiation = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Systolic murmur radiation', blank=True)
    systolic_murmur_duration = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Systolic murmur duration/timing', choices=[(1, 'Early'), (2, 'Mid'), (3, 'Late'), (4, 'Holosystolic'), (5, 'Short'), (6, 'Ejection'), (7, 'Unknown/Not documented')])
    systolic_murmur_type = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Systolic murmur type', choices=[(1, 'Functional (or Innocent)'), (2, 'Pathological'), (3, 'Not determined'), (4, 'Unknown/Not documented')])
    diastolic_murmur_grade = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Diastolic murmur grade (1 to 4)', blank=True)
    diastolic_murmur_location = models.IntegerField(help_text='', null=True, verbose_name='Diastolic murmur location | Diastolic murmur location Other: Specify', blank=True, choices=[(1, 'LUSB'), (2, 'RUSB'), (3, 'MLSB'), (4, 'LLSB'), (5, 'LRSB'), (6, 'Apex'), (7, 'Post chest (R)'), (8, 'Post chest (L)'), (9, 'Under clavicle (R)'), (10, 'Under clavicle (L)'), (12, 'Unknown/Not documented'), (11, 'Other')]) # This field type is a guess
    diastolic_murmur_radiation = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Diastolic murmur radiation', blank=True)
    diastolic_murmur_duration = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Diastolic murmur duration/timing', choices=[(1, 'Early'), (2, 'Mid'), (3, 'Late'), (4, 'Short'), (5, 'Unknown/Not documented')])
    continuous_murmur_quality = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Continuous murmur quality', choices=[(1, 'Machinery'), (2, 'Blowing'), (3, 'Unknown/Not documented')])
    continuous_murmur_location = models.IntegerField(help_text='', null=True, verbose_name='Continuous murmur location | Continuous murmur location Other: Specify', blank=True, choices=[(1, 'LUSB'), (2, 'RUSB'), (3, 'MLSB'), (4, 'LLSB'), (5, 'LRSB'), (6, 'Apex'), (7, 'Post chest (R)'), (8, 'Post chest (L)'), (9, 'Under clavicle (R)'), (10, 'Under clavicle (L)'), (12, 'Uknown/Not documented'), (11, 'Other')]) # This field type is a guess
    carotid_bruit = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Carotid Bruit', choices=[(1, 'Absent'), (2, 'Present'), (3, 'Not documented')])
    venous_hum = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Venous Hum', choices=[(1, 'Absent'), (2, 'Present'), (3, 'Not documented')])
    current_breathing = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Current breathing', choices=[(1, 'Independent'), (2, 'Requires support'), (3, 'Unknown/Not documented')])
    lungs_clear_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Lungs clear', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    lungs_clear_spec = models.TextField(help_text='', null=True, verbose_name='Lungs clear: Specify', blank=True) # This field type is a guess
    wheezes_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Wheezes', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    wheezes_spec = models.TextField(help_text='', null=True, verbose_name='Wheezes: Specify', blank=True) # This field type is a guess
    rales_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Rales', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    rales_spec = models.TextField(help_text='', null=True, verbose_name='Rales: Specify', blank=True) # This field type is a guess
    rhonchi_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Rhonchi', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    rhonchi_spec = models.TextField(help_text='', null=True, verbose_name='Rhonchi: Specify', blank=True) # This field type is a guess
    cyanotic_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Cyanotic', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    cyanotic_spec = models.TextField(help_text='', null=True, verbose_name='Cyanotic: Specify', blank=True) # This field type is a guess
    physical_exam_feedback = models.TextField(help_text='', null=True, verbose_name='Please provide any feedback for this form (for example: missing questions, questions not relevant for a disease area, ambiguities, places where a textbox could be replaced with discrete choices, missing discrete choices)', blank=True) # This field type is a guess
    ear_details_summary = models.CharField(help_text='1, Lowset | 2, Pits | 3, Tags | 4, Structural abnormality | 5, Not examined | 6, Unknown/Not documented', null=True, max_length=2000, verbose_name='Ears are/have', blank=True)
    ear_pits_details_summary = models.CharField(help_text='1, preauricular | 2, posterior auricular | 3, intra auricular | 4, Unknonwn/Not documented', null=True, max_length=2000, verbose_name='Pit type', blank=True)
    ear_tag_side_summary = models.CharField(help_text='1, Right | 2, Left', null=True, max_length=2000, verbose_name='Tag side', blank=True)
    ear_structural_abnormality_side_summary = models.CharField(help_text='1, Right | 2, Left | 3, Unknown/Not documented', null=True, max_length=2000, verbose_name='Ear structural abnormality side', blank=True)
    nose_abnormality_summary = models.CharField(help_text='8, None | 1, Alae nasi | 2, Nares | 3, Nasal appendages | 4, Nasal bridge | 5, Septum | 6, Tip | 7, Unknown/Not documented | 9, Other unknown abnormality | 10, Other', null=True, max_length=2000, verbose_name='Nose abnormalities', blank=True)
    mouth_teeth_abnormality_summary = models.CharField(help_text='5, None | 1, Micrognathism | 2, Myopathic facies | 3, Unknown/Not documented | 6, Other unknown abnormality | 4, Other', null=True, max_length=2000, verbose_name='Mouth and teeth abnormalities', blank=True)
    neck_mass_summary = models.CharField(help_text='7, None | 1, Gland | 2, Nodule | 3, Cyst | 4, Thyroid | 6, Unknown/Not documented | 8, Other unknown mass | 5, Other', null=True, max_length=2000, verbose_name='Neck masses | Specify other neck mass', blank=True)
    pectus_abnormality_summary = models.CharField(help_text='1, None  | 2, Pectus excavatum | 3, Pectus carinatum | 4, Unknown/Not documented | 5,  Other unknown abnormality | 6, Other', null=True, max_length=2000, verbose_name='Pectus abnormalities', blank=True)
    marfan_major_criteria_summary = models.CharField(help_text='17, None | 1, Skeletal: Arachnodactily- both wrist and thumb signs | 2, Skeletal: Pectus carinatum | 3, Skeletal: Pectus excavatum | 4, Skeletal: Pes planus | 5, Skeletal: Protrusio acetabulae | 6, Skeletal: Reduced elbow extension (<170 degrees) | 7, Skeletal: Scoliosis >20 degrees or spondylolithesis | 8, Skeletal: Upper to lower segment ratio<0.86 | 9, Skeletal: Span to height ration >1.05 | 10, CV: Aortic root dilatation | 11, CV: Dissection of ascending aorta | 12, Ocular: Ectopia lentis (lens dislocation) | 13, Neurologic: Lumbosacral dural estasia | 14, Genetics: Family History | 15, Genetics: Genetic mutations known to cause Marfan | 16, Genetics: Inheritance of DNA marker haplotype linked to MFS in family', null=True, max_length=2000, verbose_name='Ghent Criteria for Marfan Syndrome (Major Criteria/System)', blank=True)
    abdomen_organomegaly_summary = models.CharField(help_text='6, None | 1, Nephromegaly | 2, Hepatomegaly | 3, Splenomegaly | 4, Hepatosplenomegaly | 7, Unknown/Not documented | 8, Other unknown abnormality | 5, Other', null=True, max_length=2000, verbose_name='Organomegaly? | Please specify type of organomegaly', blank=True)
    hernias_summary = models.CharField(help_text='4, None | 1, Umbilical | 2, Inguinal | 3, Abdominal | 5, Unknown/Not documented | 6, Other unknown hernia | 7, Other', null=True, max_length=2000, verbose_name='Hernias | Describe other hernia', blank=True)
    birthmark_rash_summary = models.CharField(help_text='1, None | 2, cafe au lait spots | 3, capillary hemangioma | 4, cutis marmorata | 5, diffuse hypopigmented skin lesions | 6, Unknown/Not documented| 7, Other unknown abnormality |8, Other', null=True, max_length=2000, verbose_name='Birthmarks or rash | Describe other birthmark rash', blank=True)
    skin_conditions_summary = models.CharField(help_text='1, None | 2, Ichthyosis | 3, Unknown/Not documented | 4, Other unknown condition | 5, Other', null=True, max_length=2000, verbose_name='Other skin conditions', blank=True)
    patellae_absent_side_summary = models.CharField(help_text='1, Right | 2, Left', null=True, max_length=2000, verbose_name='Patellae absent side', blank=True)
    hand_right_d1_summary = models.CharField(help_text='1, Ulnar loop | 2, Radial loop | 3, Whorl | 4, Double loop | 5, Arch | 6, Tented arch | 7, Medial ', null=True, max_length=2000, verbose_name='Right hand digit 1', blank=True)
    hand_right_d3_summary = models.CharField(help_text='1, Ulnar loop | 2, Radial loop | 3, Whorl | 4, Double loop | 5, Arch | 6, Tented arch | 7, Medial ', null=True, max_length=2000, verbose_name='Right hand digit 3', blank=True)
    hand_right_d5_summary = models.CharField(help_text='1, Ulnar loop | 2, Radial loop | 3, Whorl | 4, Double loop | 5, Arch | 6, Tented arch | 7, Medial ', null=True, max_length=2000, verbose_name='Right hand digit 5', blank=True)
    hand_left_d2_summary = models.CharField(help_text='1, Ulnar loop | 2, Radial loop | 3, Whorl | 4, Double loop | 5, Arch | 6, Tented arch | 7, Medial ', null=True, max_length=2000, verbose_name='Left hand digit 2', blank=True)
    hand_left_d4_summary = models.CharField(help_text='1, Ulnar loop | 2, Radial loop | 3, Whorl | 4, Double loop | 5, Arch | 6, Tented arch | 7, Medial ', null=True, max_length=2000, verbose_name='Left hand digit 4', blank=True)
    hand_creases_side_summary = models.CharField(help_text='1, Right | 2, Left | 3, Unknown/Not documented', null=True, max_length=2000, verbose_name='Abnormal creases side', blank=True)
    hand_nails_summary = models.CharField(help_text='5, None |1, Creases | 2, Hypoplastic | 3, Pitted | 4, Prolonged | 6, Unknown/Not documented | 7, Other unknown abnormality | 8, Other', null=True, max_length=2000, verbose_name='Nail abnormalities', blank=True)
    pulses_summary = models.CharField(help_text='1, Equal | 2, Bounding | 3, Diminished | 4, Absent | 5, Radial femoral delay | 6, Unknown/Not documented', null=True, max_length=2000, verbose_name='Pulses', blank=True)
    first_heart_sound_summary = models.CharField(help_text='1, Normal | 2, Abnormal | 3, Widely split | 4, Unknown/Not documented', null=True, max_length=2000, verbose_name='First Heart Sound', blank=True)
    murmur_summary = models.CharField(help_text='1, Absent | 2, Systolic | 3, Diastolic | 4, Continuous | 5, Unknown/Not documented', null=True, max_length=2000, verbose_name='Murmur', blank=True)
    systolic_quality_summary = models.CharField(help_text='1, Stills, vibratory, musical, twangy | 2, Pulmonic flow | 3, Harsh | 4, Blowing or regurgitant | 5, Crescendo-decrescendo/to and fro | 6, Ejection | 7, Unknown/Not documented', null=True, max_length=2000, verbose_name='Systolic Quality/Characteristics', blank=True)
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'physicalexam'


class eardetails(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Ears are/have', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Ears are/have', choices=[(1, 'Lowset'), (2, 'Pits'), (3, 'Tags'), (4, 'Structural abnormality'), (5, 'Not examined'), (6, 'Unknown/Not documented')])
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'eardetails'


class earpitsdetails(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Pit type', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Pit type', choices=[(1, 'preauricular'), (2, 'posterior auricular'), (3, 'intra auricular'), (4, 'Unknonwn/Not documented')])
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'earpitsdetails'


class eartagside(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Tag side', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Tag side', choices=[(1, 'Right'), (2, 'Left')])
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'eartagside'


class earstructuralabnormalityside(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Ear structural abnormality side', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Ear structural abnormality side', choices=[(1, 'Right'), (2, 'Left'), (3, 'Unknown/Not documented')])
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'earstructuralabnormalityside'


class noseabnormality(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Nose abnormalities', blank=True)
    value = models.IntegerField(help_text='', null=True, verbose_name='Nose abnormalities', blank=True, choices=[(8, 'None'), (1, 'Alae nasi'), (2, 'Nares'), (3, 'Nasal appendages'), (4, 'Nasal bridge'), (5, 'Septum'), (6, 'Tip'), (7, 'Unknown/Not documented'), (9, 'Other unknown abnormality'), (10, 'Other')]) # This field type is a guess
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'noseabnormality'


class mouthteethabnormality(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Mouth and teeth abnormalities', blank=True)
    value = models.IntegerField(help_text='', null=True, verbose_name='Mouth and teeth abnormalities', blank=True, choices=[(5, 'None'), (1, 'Micrognathism'), (2, 'Myopathic facies'), (3, 'Unknown/Not documented'), (6, 'Other unknown abnormality'), (4, 'Other')]) # This field type is a guess
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'mouthteethabnormality'


class neckmass(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Neck masses | Specify other neck mass', blank=True)
    value = models.IntegerField(help_text='', null=True, verbose_name='Neck masses | Specify other neck mass', blank=True, choices=[(7, 'None'), (1, 'Gland'), (2, 'Nodule'), (3, 'Cyst'), (4, 'Thyroid'), (6, 'Unknown/Not documented'), (8, 'Other unknown mass'), (5, 'Other')]) # This field type is a guess
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'neckmass'


class pectusabnormality(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Pectus abnormalities', blank=True)
    value = models.IntegerField(help_text='', null=True, verbose_name='Pectus abnormalities', blank=True, choices=[(1, 'None'), (2, 'Pectus excavatum'), (3, 'Pectus carinatum'), (4, 'Unknown/Not documented'), (5, 'Other unknown abnormality'), (6, 'Other')]) # This field type is a guess
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'pectusabnormality'


class marfanmajorcriteria(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Ghent Criteria for Marfan Syndrome (Major Criteria/System)', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Ghent Criteria for Marfan Syndrome (Major Criteria/System)', choices=[(17, 'None'), (1, 'Skeletal: Arachnodactily- both wrist and thumb signs'), (2, 'Skeletal: Pectus carinatum'), (3, 'Skeletal: Pectus excavatum'), (4, 'Skeletal: Pes planus'), (5, 'Skeletal: Protrusio acetabulae'), (6, 'Skeletal: Reduced elbow extension (<170 degrees)'), (7, 'Skeletal: Scoliosis >20 degrees or spondylolithesis'), (8, 'Skeletal: Upper to lower segment ratio<0.86'), (9, 'Skeletal: Span to height ration >1.05'), (10, 'CV: Aortic root dilatation'), (11, 'CV: Dissection of ascending aorta'), (12, 'Ocular: Ectopia lentis (lens dislocation)'), (13, 'Neurologic: Lumbosacral dural estasia'), (14, 'Genetics: Family History'), (15, 'Genetics: Genetic mutations known to cause Marfan'), (16, 'Genetics: Inheritance of DNA marker haplotype linked to MFS in family')])
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'marfanmajorcriteria'


class abdomenorganomegaly(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Organomegaly? | Please specify type of organomegaly', blank=True)
    value = models.IntegerField(help_text='', null=True, verbose_name='Organomegaly? | Please specify type of organomegaly', blank=True, choices=[(6, 'None'), (1, 'Nephromegaly'), (2, 'Hepatomegaly'), (3, 'Splenomegaly'), (4, 'Hepatosplenomegaly'), (7, 'Unknown/Not documented'), (8, 'Other unknown abnormality'), (5, 'Other')]) # This field type is a guess
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'abdomenorganomegaly'


class hernias(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Hernias | Describe other hernia', blank=True)
    value = models.IntegerField(help_text='', null=True, verbose_name='Hernias | Describe other hernia', blank=True, choices=[(4, 'None'), (1, 'Umbilical'), (2, 'Inguinal'), (3, 'Abdominal'), (5, 'Unknown/Not documented'), (6, 'Other unknown hernia'), (7, 'Other')]) # This field type is a guess
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'hernias'


class birthmarkrash(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Birthmarks or rash | Describe other birthmark rash', blank=True)
    value = models.IntegerField(help_text='', null=True, verbose_name='Birthmarks or rash | Describe other birthmark rash', blank=True, choices=[(1, 'None'), (2, 'cafe au lait spots'), (3, 'capillary hemangioma'), (4, 'cutis marmorata'), (5, 'diffuse hypopigmented skin lesions'), (6, 'Unknown/Not documented'), (7, 'Other unknown abnormality'), (8, 'Other')]) # This field type is a guess
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'birthmarkrash'


class skinconditions(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Other skin conditions', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Other skin conditions', choices=[(1, 'None'), (2, 'Ichthyosis'), (3, 'Unknown/Not documented'), (4, 'Other unknown condition'), (5, 'Other')])
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'skinconditions'


class patellaeabsentside(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Patellae absent side', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Patellae absent side', choices=[(1, 'Right'), (2, 'Left')])
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'patellaeabsentside'


class handrightd1(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Right hand digit 1', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Right hand digit 1', choices=[(1, 'Ulnar loop'), (2, 'Radial loop'), (3, 'Whorl'), (4, 'Double loop'), (5, 'Arch'), (6, 'Tented arch'), (7, 'Medial')])
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'handrightd1'


class handrightd3(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Right hand digit 3', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Right hand digit 3', choices=[(1, 'Ulnar loop'), (2, 'Radial loop'), (3, 'Whorl'), (4, 'Double loop'), (5, 'Arch'), (6, 'Tented arch'), (7, 'Medial')])
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'handrightd3'


class handrightd5(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Right hand digit 5', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Right hand digit 5', choices=[(1, 'Ulnar loop'), (2, 'Radial loop'), (3, 'Whorl'), (4, 'Double loop'), (5, 'Arch'), (6, 'Tented arch'), (7, 'Medial')])
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'handrightd5'


class handleftd2(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Left hand digit 2', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Left hand digit 2', choices=[(1, 'Ulnar loop'), (2, 'Radial loop'), (3, 'Whorl'), (4, 'Double loop'), (5, 'Arch'), (6, 'Tented arch'), (7, 'Medial')])
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'handleftd2'


class handleftd4(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Left hand digit 4', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Left hand digit 4', choices=[(1, 'Ulnar loop'), (2, 'Radial loop'), (3, 'Whorl'), (4, 'Double loop'), (5, 'Arch'), (6, 'Tented arch'), (7, 'Medial')])
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'handleftd4'


class handcreasesside(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Abnormal creases side', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Abnormal creases side', choices=[(1, 'Right'), (2, 'Left'), (3, 'Unknown/Not documented')])
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'handcreasesside'


class handnails(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Nail abnormalities', blank=True)
    value = models.IntegerField(help_text='', null=True, verbose_name='Nail abnormalities', blank=True, choices=[(5, 'None'), (1, 'Creases'), (2, 'Hypoplastic'), (3, 'Pitted'), (4, 'Prolonged'), (6, 'Unknown/Not documented'), (7, 'Other unknown abnormality'), (8, 'Other')]) # This field type is a guess
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'handnails'


class pulses(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Pulses', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Pulses', choices=[(1, 'Equal'), (2, 'Bounding'), (3, 'Diminished'), (4, 'Absent'), (5, 'Radial femoral delay'), (6, 'Unknown/Not documented')])
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'pulses'


class firstheartsound(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='First Heart Sound', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='First Heart Sound', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Widely split'), (4, 'Unknown/Not documented')])
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'firstheartsound'


class murmur(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Murmur', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Murmur', choices=[(1, 'Absent'), (2, 'Systolic'), (3, 'Diastolic'), (4, 'Continuous'), (5, 'Unknown/Not documented')])
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'murmur'


class systolicquality(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Systolic Quality/Characteristics', blank=True)
    value = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Systolic Quality/Characteristics', blank=True)
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'systolicquality'


class OtherSkinFinding(models.Model):
    other_skin_finding = models.CharField(help_text='', null=True, max_length=2000, verbose_name='other skin finding', blank=True)
    physicalexam = models.ForeignKey(PhysicalExam)

    class Meta:
	 db_table = 'otherskinfinding'


class HearingImpairment(models.Model):
    age_of_onset = models.IntegerField(help_text='', null=True, verbose_name='Age of onset', blank=True, choices=[(1, 'congenital(at birth)'), (2, 'after birth up to 1 year'), (3, 'one year'), (4, 'two years'), (5, 'three years'), (6, 'four years'), (7, 'five years'), (8, 'six years'), (9, 'seven years'), (10, 'eight years'), (11, 'nine years'), (12, 'ten years'), (13, '11 years'), (14, '12 years'), (15, '13 years'), (16, '14 years'), (17, '15 years'), (18, '16 years'), (19, '17 years'), (20, '18 years'), (26, '19 years'), (21, '20 years'), (22, '21-30'), (23, '31-40'), (24, '41-50'), (25, '51-60'), (27, '> 60 years')]) # This field type is a guess
    type_of_hearing_impairment = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Type of hearing impairment', choices=[(1, 'Sensorineural'), (2, 'Conductive'), (3, 'Unknown/Not documented')])
    hear_impair_laterality = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Impairment laterality', choices=[(1, 'Bilateral'), (2, 'Unilateral'), (3, 'Unknown/Not documented')])
    hear_impair_symmetric = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Symmetric impairment?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ear_side = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Impaired ear', choices=[(1, 'Left'), (2, 'Right'), (3, 'Unknown/Not documented')])
    hear_impair_severity = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Severity of impairment', choices=[(1, 'Mild'), (2, 'Mild-Moderate'), (3, 'Mild-Severe'), (4, 'Mild-Profound'), (5, 'Moderate'), (6, 'Moderate-Severe'), (7, 'Moderate-Profound'), (8, 'Profound'), (9, 'Unknown/Not documented')])
    hear_impair_severity_l = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Severity of left ear impairment', choices=[(1, 'Mild'), (2, 'Mild-Moderate'), (3, 'Mild-Severe'), (4, 'Mild-Profound'), (5, 'Moderate'), (6, 'Moderate-Severe'), (7, 'Moderate-Profound'), (8, 'Profound'), (9, 'Unknown/Not documented')])
    hear_impair_severity_r = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Severity of right ear impairment', choices=[(1, 'Mild'), (2, 'Mild-Moderate'), (3, 'Mild-Severe'), (4, 'Mild-Profound'), (5, 'Moderate'), (6, 'Moderate-Severe'), (7, 'Moderate-Profound'), (8, 'Profound'), (9, 'Unknown/Not documented')])
    hear_impaired_freq = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Impaired frequency', choices=[(1, 'All frequencies'), (2, 'High frequency'), (3, 'Low frequency'), (4, 'Cookie bite (mid frequency)'), (5, 'Unknown/Not documented')])
    hear_impaired_freq_l = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Left ear impaired frequency', choices=[(1, 'All frequencies'), (2, 'High frequency'), (3, 'Low frequency'), (4, 'Cookie bite (mid frequency)'), (5, 'Unknown/Not documented')])
    hear_impaired_freq_r = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Right ear impaired frequency', choices=[(1, 'All frequencies'), (2, 'High frequency'), (3, 'Low frequency'), (4, 'Cookie bite (mid frequency)'), (5, 'Unknown/Not documented')])
    hear_progressed_severity = models.NullBooleanField(help_text='', verbose_name='Has hearing impairment progressed in severity?', blank=True)
    fh_hear_imp_pedi = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Hearing impairment affected relative(s)', choices=[(1, 'Mother'), (2, 'Father'), (3, 'Sister'), (4, 'Brother'), (5, 'Maternal Grandmother'), (6, 'Maternal Grandfather'), (7, 'Paternal Grandmother'), (8, 'Paternal Grandfather'), (9, 'Maternal Aunt'), (10, 'Paternal Aunt'), (11, 'Maternal Uncle'), (12, 'Paternal Uncle'), (13, 'Maternal Cousin'), (14, 'Paternal Cousin')])
    fh_diabetes_pedi = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Diabetes affected relative(s)', choices=[(1, 'Mother'), (2, 'Father'), (3, 'Sister'), (4, 'Brother'), (5, 'Maternal Grandmother'), (6, 'Maternal Grandfather'), (7, 'Paternal Grandmother'), (8, 'Paternal Grandfather'), (9, 'Maternal Aunt'), (10, 'Paternal Aunt'), (11, 'Maternal Uncle'), (12, 'Paternal Uncle'), (13, 'Maternal Cousin'), (14, 'Paternal Cousin')])
    fh_prem_grey_pedi = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Premature greying of hair affected relative(s)', choices=[(1, 'Mother'), (2, 'Father'), (3, 'Sister'), (4, 'Brother'), (5, 'Maternal Grandmother'), (6, 'Maternal Grandfather'), (7, 'Paternal Grandmother'), (8, 'Paternal Grandfather'), (9, 'Maternal Aunt'), (10, 'Paternal Aunt'), (11, 'Maternal Uncle'), (12, 'Paternal Uncle'), (13, 'Maternal Cousin'), (14, 'Paternal Cousin')])
    fh_id_pedi = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Developmental delay, learning disability, or intellectual disability affected relative(s)', choices=[(1, 'Mother'), (2, 'Father'), (3, 'Sister'), (4, 'Brother'), (5, 'Maternal Grandmother'), (6, 'Maternal Grandfather'), (7, 'Paternal Grandmother'), (8, 'Paternal Grandfather'), (9, 'Maternal Aunt'), (10, 'Paternal Aunt'), (11, 'Maternal Uncle'), (12, 'Paternal Uncle'), (13, 'Maternal Cousin'), (14, 'Paternal Cousin')])
    fh_arthritis_pedi = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Arthritis affected relative(s)', choices=[(1, 'Mother'), (2, 'Father'), (3, 'Sister'), (4, 'Brother'), (5, 'Maternal Grandmother'), (6, 'Maternal Grandfather'), (7, 'Paternal Grandmother'), (8, 'Paternal Grandfather'), (9, 'Maternal Aunt'), (10, 'Paternal Aunt'), (11, 'Maternal Uncle'), (12, 'Paternal Uncle'), (13, 'Maternal Cousin'), (14, 'Paternal Cousin')])
    fh_whiteforelock_pedi = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='White forelock affected relative(s)', choices=[(1, 'Mother'), (2, 'Father'), (3, 'Sister'), (4, 'Brother'), (5, 'Maternal Grandmother'), (6, 'Maternal Grandfather'), (7, 'Paternal Grandmother'), (8, 'Paternal Grandfather'), (9, 'Maternal Aunt'), (10, 'Paternal Aunt'), (11, 'Maternal Uncle'), (12, 'Paternal Uncle'), (13, 'Maternal Cousin'), (14, 'Paternal Cousin')])
    fh_birthdefect_pedi = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Birth defect affected relative(s)', choices=[(1, 'Mother'), (2, 'Father'), (3, 'Sister'), (4, 'Brother'), (5, 'Maternal Grandmother'), (6, 'Maternal Grandfather'), (7, 'Paternal Grandmother'), (8, 'Paternal Grandfather'), (9, 'Maternal Aunt'), (10, 'Paternal Aunt'), (11, 'Maternal Uncle'), (12, 'Paternal Uncle'), (13, 'Maternal Cousin'), (14, 'Paternal Cousin')])
    fh_consanguinity_pedi = models.TextField(help_text='', null=True, verbose_name='Consanguinity details', blank=True) # This field type is a guess
    dystopia_canthorum = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Dystopia Canthorum', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ear_helical_structure = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Helical structure', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Unknown/Not documented')])
    ear_helical_laterality = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Abnormal helical structure laterality', choices=[(1, 'Unilateral'), (2, 'Bilateral'), (3, 'Unknown/Not documented')])
    ear_helical_abn_sym = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Symmetric abnormality?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    ear_helical_rl = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Abnormal helical structure side', choices=[(1, 'Right'), (2, 'Left')])
    ear_helical_details_l = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Left ear helical structure details', choices=[(1, 'Cupped'), (2, 'Thick helix'), (3, 'Hypoplastic'), (4, 'Darwinian tubercle'), (5, 'Prominent anti helix'), (6, 'Unknown/Not documented')])
    clavicles = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Clavicles', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Unknown/Not documented')])
    clavicles_details = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Abnormal clavicle details', choices=[(1, 'Absent'), (2, 'Hypoplastic'), (3, 'Unknown/Not documented')])
    hearing_known_diagnosis = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Known diagnosis', blank=True)
    hearing_suspected_diagnoses = models.TextField(help_text='', null=True, verbose_name='Suspected diagnoses', blank=True) # This field type is a guess
    hearing_impairment_feedback = models.TextField(help_text='', null=True, verbose_name='Please provide any feedback for this form (for example: missing questions, questions not relevant for a disease area, ambiguities, places where a textbox could be replaced with discrete choices, missing discrete choices)', blank=True) # This field type is a guess
    nb_exposures_summary = models.CharField(help_text='6, None | 1, Ventilator | 2, Jaundice | 3, Antibiotics | 4, Infections | 5, Other medications', null=True, max_length=2000, verbose_name='Newborn exposures', blank=True)
    familiy_history_summary = models.CharField(help_text='15, None | 1, Hearing impairment | 2, Thyroid Problems | 3, Diabetes | 4, Brachial cysts or clefts | 5, Premature greying of hair | 6, Abnormally shaped ears | 7, Developmental delay, learning disability, or intellectual disability | 8, Significant vision loss or night blindness | 9, Arthritis | 10, Kidney problems | 11, White forelock | 12, Heterochromia | 13, Birth defects | 14, Consanguinity', null=True, max_length=2000, verbose_name='Family history of', blank=True)
    fh_thryoid_imp_pedi_summary = models.CharField(help_text='1, Mother | 2, Father | 3, Sister | 4, Brother | 5, Maternal Grandmother | 6, Maternal Grandfather | 7, Paternal Grandmother | 8, Paternal Grandfather | 9, Maternal Aunt | 10, Paternal Aunt | 11, Maternal Uncle | 12, Paternal Uncle | 13, Maternal Cousin | 14, Paternal Cousin', null=True, max_length=2000, verbose_name='Thyroid problem affected relative(s)', blank=True)
    fh_brachial_pedi_summary = models.CharField(help_text='1, Mother | 2, Father | 3, Sister | 4, Brother | 5, Maternal Grandmother | 6, Maternal Grandfather | 7, Paternal Grandmother | 8, Paternal Grandfather | 9, Maternal Aunt | 10, Paternal Aunt | 11, Maternal Uncle | 12, Paternal Uncle | 13, Maternal Cousin | 14, Paternal Cousin', null=True, max_length=2000, verbose_name='Brachial cysts or cleft affected relative(s)', blank=True)
    fh_ab_ears_pedi_summary = models.CharField(help_text='1, Mother | 2, Father | 3, Sister | 4, Brother | 5, Maternal Grandmother | 6, Maternal Grandfather | 7, Paternal Grandmother | 8, Paternal Grandfather | 9, Maternal Aunt | 10, Paternal Aunt | 11, Maternal Uncle | 12, Paternal Uncle | 13, Maternal Cousin | 14, Paternal Cousin', null=True, max_length=2000, verbose_name='Abnormally shaped ears affected relative(s)', blank=True)
    fh_vision_pedi_summary = models.CharField(help_text='1, Mother | 2, Father | 3, Sister | 4, Brother | 5, Maternal Grandmother | 6, Maternal Grandfather | 7, Paternal Grandmother | 8, Paternal Grandfather | 9, Maternal Aunt | 10, Paternal Aunt | 11, Maternal Uncle | 12, Paternal Uncle | 13, Maternal Cousin | 14, Paternal Cousin', null=True, max_length=2000, verbose_name='Significant vision loss or night blindness affected relative(s)', blank=True)
    fh_kidney_pedi_summary = models.CharField(help_text='1, Mother | 2, Father | 3, Sister | 4, Brother | 5, Maternal Grandmother | 6, Maternal Grandfather | 7, Paternal Grandmother | 8, Paternal Grandfather | 9, Maternal Aunt | 10, Paternal Aunt | 11, Maternal Uncle | 12, Paternal Uncle | 13, Maternal Cousin | 14, Paternal Cousin', null=True, max_length=2000, verbose_name='Kidney problem affected relative(s)', blank=True)
    fh_heterochromia_pedi_summary = models.CharField(help_text='1, Mother | 2, Father | 3, Sister | 4, Brother | 5, Maternal Grandmother | 6, Maternal Grandfather | 7, Paternal Grandmother | 8, Paternal Grandfather | 9, Maternal Aunt | 10, Paternal Aunt | 11, Maternal Uncle | 12, Paternal Uncle | 13, Maternal Cousin | 14, Paternal Cousin', null=True, max_length=2000, verbose_name='Heterochromia affected relative(s)', blank=True)
    ear_helical_details_summary = models.CharField(help_text='1, Cupped | 2, Thick helix | 3, Hypoplastic | 4, Darwinian tubercle | 5, Prominent anti helix | 6, Unknown/Not documented', null=True, max_length=2000, verbose_name='Helical structure details', blank=True)
    ear_helical_details_r_summary = models.CharField(help_text='1, Cupped | 2, Thick helix | 3, Hypoplastic | 4, Darwinian tubercle | 5, Prominent anti helix | 6, Unknown/Not documented', null=True, max_length=2000, verbose_name='Right ear helical structure details', blank=True)
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'hearingimpairment'


class nbexposures(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Newborn exposures', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Newborn exposures', choices=[(6, 'None'), (1, 'Ventilator'), (2, 'Jaundice'), (3, 'Antibiotics'), (4, 'Infections'), (5, 'Other medications')])
    hearingimpairment = models.ForeignKey(HearingImpairment)

    class Meta:
	 db_table = 'nbexposures'


class familiyhistory(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Family history of', blank=True)
    value = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Family history of', blank=True)
    hearingimpairment = models.ForeignKey(HearingImpairment)

    class Meta:
	 db_table = 'familiyhistory'


class fhthryoidimppedi(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Thyroid problem affected relative(s)', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Thyroid problem affected relative(s)', choices=[(1, 'Mother'), (2, 'Father'), (3, 'Sister'), (4, 'Brother'), (5, 'Maternal Grandmother'), (6, 'Maternal Grandfather'), (7, 'Paternal Grandmother'), (8, 'Paternal Grandfather'), (9, 'Maternal Aunt'), (10, 'Paternal Aunt'), (11, 'Maternal Uncle'), (12, 'Paternal Uncle'), (13, 'Maternal Cousin'), (14, 'Paternal Cousin')])
    hearingimpairment = models.ForeignKey(HearingImpairment)

    class Meta:
	 db_table = 'fhthryoidimppedi'


class fhbrachialpedi(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Brachial cysts or cleft affected relative(s)', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Brachial cysts or cleft affected relative(s)', choices=[(1, 'Mother'), (2, 'Father'), (3, 'Sister'), (4, 'Brother'), (5, 'Maternal Grandmother'), (6, 'Maternal Grandfather'), (7, 'Paternal Grandmother'), (8, 'Paternal Grandfather'), (9, 'Maternal Aunt'), (10, 'Paternal Aunt'), (11, 'Maternal Uncle'), (12, 'Paternal Uncle'), (13, 'Maternal Cousin'), (14, 'Paternal Cousin')])
    hearingimpairment = models.ForeignKey(HearingImpairment)

    class Meta:
	 db_table = 'fhbrachialpedi'


class fhabearspedi(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Abnormally shaped ears affected relative(s)', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Abnormally shaped ears affected relative(s)', choices=[(1, 'Mother'), (2, 'Father'), (3, 'Sister'), (4, 'Brother'), (5, 'Maternal Grandmother'), (6, 'Maternal Grandfather'), (7, 'Paternal Grandmother'), (8, 'Paternal Grandfather'), (9, 'Maternal Aunt'), (10, 'Paternal Aunt'), (11, 'Maternal Uncle'), (12, 'Paternal Uncle'), (13, 'Maternal Cousin'), (14, 'Paternal Cousin')])
    hearingimpairment = models.ForeignKey(HearingImpairment)

    class Meta:
	 db_table = 'fhabearspedi'


class fhvisionpedi(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Significant vision loss or night blindness affected relative(s)', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Significant vision loss or night blindness affected relative(s)', choices=[(1, 'Mother'), (2, 'Father'), (3, 'Sister'), (4, 'Brother'), (5, 'Maternal Grandmother'), (6, 'Maternal Grandfather'), (7, 'Paternal Grandmother'), (8, 'Paternal Grandfather'), (9, 'Maternal Aunt'), (10, 'Paternal Aunt'), (11, 'Maternal Uncle'), (12, 'Paternal Uncle'), (13, 'Maternal Cousin'), (14, 'Paternal Cousin')])
    hearingimpairment = models.ForeignKey(HearingImpairment)

    class Meta:
	 db_table = 'fhvisionpedi'


class fhkidneypedi(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Kidney problem affected relative(s)', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Kidney problem affected relative(s)', choices=[(1, 'Mother'), (2, 'Father'), (3, 'Sister'), (4, 'Brother'), (5, 'Maternal Grandmother'), (6, 'Maternal Grandfather'), (7, 'Paternal Grandmother'), (8, 'Paternal Grandfather'), (9, 'Maternal Aunt'), (10, 'Paternal Aunt'), (11, 'Maternal Uncle'), (12, 'Paternal Uncle'), (13, 'Maternal Cousin'), (14, 'Paternal Cousin')])
    hearingimpairment = models.ForeignKey(HearingImpairment)

    class Meta:
	 db_table = 'fhkidneypedi'


class fhheterochromiapedi(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Heterochromia affected relative(s)', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Heterochromia affected relative(s)', choices=[(1, 'Mother'), (2, 'Father'), (3, 'Sister'), (4, 'Brother'), (5, 'Maternal Grandmother'), (6, 'Maternal Grandfather'), (7, 'Paternal Grandmother'), (8, 'Paternal Grandfather'), (9, 'Maternal Aunt'), (10, 'Paternal Aunt'), (11, 'Maternal Uncle'), (12, 'Paternal Uncle'), (13, 'Maternal Cousin'), (14, 'Paternal Cousin')])
    hearingimpairment = models.ForeignKey(HearingImpairment)

    class Meta:
	 db_table = 'fhheterochromiapedi'


class earhelicaldetails(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Helical structure details', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Helical structure details', choices=[(1, 'Cupped'), (2, 'Thick helix'), (3, 'Hypoplastic'), (4, 'Darwinian tubercle'), (5, 'Prominent anti helix'), (6, 'Unknown/Not documented')])
    hearingimpairment = models.ForeignKey(HearingImpairment)

    class Meta:
	 db_table = 'earhelicaldetails'


class earhelicaldetailsr(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Right ear helical structure details', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Right ear helical structure details', choices=[(1, 'Cupped'), (2, 'Thick helix'), (3, 'Hypoplastic'), (4, 'Darwinian tubercle'), (5, 'Prominent anti helix'), (6, 'Unknown/Not documented')])
    hearingimpairment = models.ForeignKey(HearingImpairment)

    class Meta:
	 db_table = 'earhelicaldetailsr'


class Antibiotic(models.Model):
    antibiotics = models.CharField(help_text='', null=True, max_length=2000, verbose_name='antibiotic exposure', blank=True)
    hearingimpairment = models.ForeignKey(HearingImpairment)

    class Meta:
	 db_table = 'antibiotic'


class Infection(models.Model):
    infections = models.CharField(help_text='', null=True, max_length=2000, verbose_name='infection exposure', blank=True)
    hearingimpairment = models.ForeignKey(HearingImpairment)

    class Meta:
	 db_table = 'infection'


class OtherMedication(models.Model):
    other_meds = models.CharField(help_text='', null=True, max_length=2000, verbose_name='other medication exposure', blank=True)
    hearingimpairment = models.ForeignKey(HearingImpairment)

    class Meta:
	 db_table = 'othermedication'


class IntellectualDisability(models.Model):
    id_susp_age = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Age at which intellectual disability was first suspected? (months)', blank=True)
    developpeds_eval = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Evaluated by developmental pediatrician?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    modified_checklist_for_autism_in_toddlers_spec = models.TextField(help_text='', null=True, verbose_name='Modified Checklist for Autism in Toddlers results', blank=True) # This field type is a guess
    early_screening_of_autistic_traits_spec = models.TextField(help_text='', null=True, verbose_name='Early Screening of Autistic Traits Questionnaire results', blank=True) # This field type is a guess
    first_year_inventory_spec = models.TextField(help_text='', null=True, verbose_name='First Year Inventory results', blank=True) # This field type is a guess
    adi_r_spec = models.TextField(help_text='', null=True, verbose_name='Autism Diagnostic Interview-Revised (ADI-R) results', blank=True) # This field type is a guess
    ados_spec = models.TextField(help_text='', null=True, verbose_name='Autism Diagnostic Observation Schedule (ADOS) results', blank=True) # This field type is a guess
    cars_spec = models.TextField(help_text='', null=True, verbose_name='Childhood Autism Rating Scale (CARS) results', blank=True) # This field type is a guess
    aberrant_behavior_checklist_spec = models.TextField(help_text='', null=True, verbose_name='Aberrant Behavior Checklist results', blank=True) # This field type is a guess
    social_communication_questionnaire_spec = models.TextField(help_text='', null=True, verbose_name='Social Communication Questionnaire results', blank=True) # This field type is a guess
    vinelandii_adaptive_behavior_scale_spec = models.TextField(help_text='', null=True, verbose_name='Vineland-II Adaptive Behavior Scale results', blank=True) # This field type is a guess
    pls4_spec = models.TextField(help_text='', null=True, verbose_name='Preschool Language Scales-4 (PLS4) results', blank=True) # This field type is a guess
    vmi_spec = models.TextField(help_text='', null=True, verbose_name='Beery Test of Visual Motor Integration (VMI) results', blank=True) # This field type is a guess
    kaufman_brief_intelligence_spec = models.TextField(help_text='', null=True, verbose_name='Kaufman Brief Intelligence results', blank=True) # This field type is a guess
    other = models.TextField(help_text='', null=True, verbose_name='Describe other developmental screening tests and results', blank=True) # This field type is a guess
    autism_diagnosis = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Autism diagnosis?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    autism_diagnoser = models.IntegerField(help_text='', null=True, verbose_name='Who made diagnosis of autism? | Please specify which type of clinician made the autism diagnosis', blank=True, choices=[(1, 'Pediatrician'), (2, 'Developmental Pediatrician'), (3, 'Neurologist'), (5, 'Unknown/Not documented'), (4, 'Other')]) # This field type is a guess
    age_autism_diagnosis = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Age at autism diagnosis (years)', blank=True)
    autism_symptoms_social_inter = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Qualitative impairment in social interaction', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    autism_symptoms_eye_contact = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Poor eye contact', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    autism_symptoms_comm = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Qualitative impairment in communication ', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    autism_symptoms_rep_beh = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Restricted and repetitive behavior ', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    autism_symptoms_recip = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Lack of social or emotional reciprocity', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    autism_symptoms_rep_lang = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Stereotyped and repetitive use of language or idiosyncratic use of language', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    autism_symptoms_preocc = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Persistent preoccupation with parts of objects', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    autism_symptoms_comp_beh = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Compulsive behavior', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    autism_symptoms_sama = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Samaness (resistance to change)', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    autism_symptoms_ritual_beh = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Ritualistic behavior', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    autism_symptoms_self_inj = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Self injury', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    autism_symptoms_attn_def = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Attention deficit/poor attention', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    autism_symptoms_agg_beh = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Aggressive Behavior', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    autism_symptoms_spec = models.IntegerField(help_text='', null=True, verbose_name='Specify other autism symptoms', blank=True, choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')]) # This field type is a guess
    id_diagnoser = models.IntegerField(help_text='', null=True, verbose_name='Who made the diagnosis of intellectual disability? | Please specify which type of clinician made the intellectual disability diagnosis', blank=True, choices=[(1, 'Pediatrician'), (2, 'Developmental pediatrician'), (3, 'Neurologist'), (5, 'Unknown/Not documented'), (4, 'Other')]) # This field type is a guess
    dev_milestone_smile_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Smile', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    dev_milestone_smile_months = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Age first smiled (months)', blank=True)
    dev_milestone_roll_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Roll over', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    dev_milestone_roll_months = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Age first rolled over (months)', blank=True)
    dev_milestone_grasp_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Grasp object', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    dev_milestone_grasp_months = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Age first grasped object (months)', blank=True)
    dev_milestone_reach_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Reach for object', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    dev_milestone_reach_months = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Age reached for object (months)', blank=True)
    dev_milestone_crawl_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Crawl', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    dev_milestone_crawl_months = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Age first crawled (months)', blank=True)
    dev_milestone_hand_transfer_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Hand to hand transfer', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    dev_milestone_hand_transfer_months = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Age first hand to hand transfer (months)', blank=True)
    dev_milestone_feed_self_crackers_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Feed self crackers', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    dev_milestone_feed_self_crackers_months = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Age first fed self crackers (months)', blank=True)
    dev_milestone_pincer_grasp_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Pincer grasp', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    dev_milestone_pincer_grasp_months = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Age first pincer grasp (months)', blank=True)
    dev_milestone_words_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Words (mama/dada)', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    dev_milestone_words_months = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Age of first words (months)', blank=True)
    dev_milestone_stranger_anxiety_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Stranger anxiety', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    dev_milestone_stranger_anxiety_months = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Age first showed stranger anxiety (months)', blank=True)
    dev_milestone_stand_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Stand', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    dev_milestone_stand_months = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Age first stood (months)', blank=True)
    dev_milestone_drink_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Drink from cup', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    dev_milestone_drink_months = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Age first drank from cup(months)', blank=True)
    dev_milestone_remove_clothes_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Removes clothes', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    dev_milestone_remove_clothes_months = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Age first removed clothes (months)', blank=True)
    dev_milestone_stairs_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Climbs stairs', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    dev_milestone_stairs_months = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Age climbed stairs (months)', blank=True)
    dev_milestone_combine_words_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Combine words', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    dev_milestone_combine_words_months = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Age first combined words (months)', blank=True)
    dev_milestone_plurals_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Uses plurals', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    dev_milestone_plurals_months = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Age used plurals (months)', blank=True)
    dev_milestone_tricycle_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Pedals tricycle', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    dev_milestone_tricycle_months = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Age pedaled tricycle (months)', blank=True)
    dev_milestone_copy_circle_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Copy circle', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    dev_milestone_copy_circle_months = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Age first copied circle (months)', blank=True)
    dev_milestone_dress_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Dress self', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    dev_milestone_dress_months = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Age first dressed self (months)', blank=True)
    dev_milestone_balance_one_foot_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Balance one foot', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    dev_milestone_balance_one_foot_months = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Age first balanced on one foot (months)', blank=True)
    dev_milestone_square_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Draws square', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    dev_milestone_square_months = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Age first drew square (months)', blank=True)
    mother_symptoms = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Does mother have similar symptoms of autism or intellectual disability?  (specify yes even if less severe)', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    maternal_fam_hist = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Maternal family history of autism or intellectual disability?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    brothers_symptoms = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Brothers with similar conditions?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    behavior_disorders = models.IntegerField(help_text='', null=True, verbose_name='Behavior disorders', blank=True, choices=[(3, 'None'), (1, 'ADHD'), (2, 'Hyperactivity'), (5, 'Unknown/Not documented'), (4, 'Other')]) # This field type is a guess
    intellectual_disability_feedback = models.TextField(help_text='', null=True, verbose_name='Please provide any feedback for this form (for example: missing questions, questions not relevant for a disease area, ambiguities, places where a textbox could be replaced with discrete choices, missing discrete choices)', blank=True) # This field type is a guess
    developmental_screening_details_summary = models.CharField(help_text='14, None | 1, Modified Checklist for Autism in Toddlers | 2, Early Screening of Autistic Traits Questionnaire | 3, First Year Inventory | 4, Autism Diagnostic Interview-Revised (ADI-R) | 5, Autism Diagnostic Observation Schedule (ADOS) | 6, Childhood Autism Rating Scale (CARS) | 7, Aberrant Behavior Checklist | 8, Social Communication Questionnaire | 9, Vineland-II Adaptive Behavior Scale | 10, Preschool Language Scales-4 (PLS4) | 11, Beery Test of Visual Motor Integration (VMI) | 12, Kaufman Brief Intelligence | 15, Unknown/Not documented | 13, Other', null=True, max_length=2000, verbose_name='Developmental screening tests employed', blank=True)
    subj_weakness_summary = models.CharField(help_text='3, None | 1, Math | 2, Reading | 5, Unknown/Not documented | 4, Other', null=True, max_length=2000, verbose_name='Weakness in any particular subject matters?', blank=True)
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'intellectualdisability'


class developmentalscreeningdetails(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Developmental screening tests employed', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Developmental screening tests employed', choices=[(14, 'None'), (1, 'Modified Checklist for Autism in Toddlers'), (2, 'Early Screening of Autistic Traits Questionnaire'), (3, 'First Year Inventory'), (4, 'Autism Diagnostic Interview-Revised (ADI-R)'), (5, 'Autism Diagnostic Observation Schedule (ADOS)'), (6, 'Childhood Autism Rating Scale (CARS)'), (7, 'Aberrant Behavior Checklist'), (8, 'Social Communication Questionnaire'), (9, 'Vineland-II Adaptive Behavior Scale'), (10, 'Preschool Language Scales-4 (PLS4)'), (11, 'Beery Test of Visual Motor Integration (VMI)'), (12, 'Kaufman Brief Intelligence'), (15, 'Unknown/Not documented'), (13, 'Other')])
    intellectualdisability = models.ForeignKey(IntellectualDisability)

    class Meta:
	 db_table = 'developmentalscreeningdetails'


class subjweakness(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Weakness in any particular subject matters?', blank=True)
    value = models.IntegerField(help_text='', null=True, verbose_name='Weakness in any particular subject matters?', blank=True, choices=[(3, 'None'), (1, 'Math'), (2, 'Reading'), (5, 'Unknown/Not documented'), (4, 'Other')]) # This field type is a guess
    intellectualdisability = models.ForeignKey(IntellectualDisability)

    class Meta:
	 db_table = 'subjweakness'


class CardiacDiagnosi(models.Model):
    cardiac_presumed_dx = models.TextField(help_text='', null=True, verbose_name="Subject's presumed diagnosis", blank=True) # This field type is a guess
    cardiac_date_presumed_dx = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Date of presumed diagnosis (MM/YY)', blank=True)
    cardiac_reason_presumed_dx_oth = models.TextField(help_text='', null=True, verbose_name='Reason for consideration of presumed diagnosis/Other: Specify', blank=True) # This field type is a guess
    cardiac_reason_presumed_sym_other_dx = models.TextField(help_text='', null=True, verbose_name='Symptoms Other: Specify', blank=True) # This field type is a guess
    cardiac_date_confirmed_dx = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Date of Confirmed Diagnosis', blank=True)
    cardiac_method_confirm_oth_dx = models.TextField(help_text='', null=True, verbose_name='Method of confirmation of diagnosis/Other: Specify', blank=True) # This field type is a guess
    cardiac_method_confirm_sym_oth_dx = models.TextField(help_text='', null=True, verbose_name='Symptoms Other: Specify', blank=True) # This field type is a guess
    cardiac_sca_event = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Subject has had a prior sudden cardiac arrest (SCA) and survived.', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    cardiac_sca_age_event = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Age at the time of Sudden Cardiac Arrest', blank=True)
    cardiac_sca_event_description = models.TextField(help_text='', null=True, verbose_name='Describe the SCA event', blank=True) # This field type is a guess
    cardiac_chd_dx_other = models.TextField(help_text='', null=True, verbose_name='CHD Diagnosis (not listed)', blank=True) # This field type is a guess
    cardiac_ep_dx_other = models.TextField(help_text='', null=True, verbose_name='EP Diagnosis (not listed)', blank=True) # This field type is a guess
    card_tx_oth = models.TextField(help_text='', null=True, verbose_name='Cardiac treatment procedures/Other: Specify', blank=True) # This field type is a guess
    cardiac_reason_presumed_dx_summary = models.CharField(help_text='13, None | 1, Personal history | 2, Family history | 3, Clinical history | 4, Physical exam | 5, ECG | 6, ECHO | 7, Genetic test | 8, EST | 9, Holter Monitor | 10, Transtelephonic Monitoring (TTM) | 11, Electrophysiologic Studies | 12, Other', null=True, max_length=2000, verbose_name='Reason for consideration of presumed diagnosis ', blank=True)
    cardiac_reason_presumed_symptoms_dx_summary = models.CharField(help_text='1, None | 2, Syncope/fainted | 3, Chest discomfort/pain/pressure | 4, Racing heart beat/tachycardia | 5, Slow heart rate/bradycardia | 6, Skipped heart beat/palpatations | 7, Dizziness/lightheadedness/nearly fainted | 8, Shortness of breath (not asthma-related) | 9, Unexplained seizure/convulsion | 10, Easy fatigability | 11, Torsades de pointes | 12, Aborted Sudden Cardiac Arrest (ASA) | 13, Hearing Loss | 14, Other', null=True, max_length=2000, verbose_name='Symptoms described in personal/clinical history', blank=True)
    cardiac_method_confirmed_dx_summary = models.CharField(help_text='13, None | 1, Personal history | 2, Family history | 3, Clinical history | 4, Physical exam | 5, ECG | 6, ECHO | 7, Genetic test | 8, EST | 9, Holter Monitor | 10, Transtelephonic Monitoring (TTM) | 11, Electrophysiologic Studies | 12, Other', null=True, max_length=2000, verbose_name='Method of confirmation of diagnosis.  Check all that apply.', blank=True)
    cardiac_method_confirm_symptom_dx_summary = models.CharField(help_text='1, None | 2, Syncope/fainted | 3, Chest discomfort/pain/pressure | 4, Racing heart beat/tachycardia | 5, Slow heart rate/bradycardia | 6, Skipped heart beat/palpatations | 7, Dizziness/lightheadedness/nearly fainted | 8, Shortness of breath (not asthma-related) | 9, Unexplained seizure/convulsion | 10, Easy fatigability | 11, Torsades de pointes | 12, Aborted Sudden Cardiac Arrest (ASA) | 13, Hearing Loss | 14, Other', null=True, max_length=2000, verbose_name='Additional symptoms described in personal/clinical history (since diagnosis was confirmed).', blank=True)
    cardiac_chd_dx_confirmed_summary = models.CharField(help_text="1, None | 2, Anomalous Coronary Artery | 3, Aortic Valve Stenosis | 4, Arrhythmogenic right ventricular dysplasia (ARVD) | 5, Atrial Septal Defect (ASD) | 6, Atrioventricular Septal Defect (AVSD) | 7, Bicuspid Aortic Valve (BAV) | 8, Coarctation of the Aorta (CoA) | 9, Complete Atrioventricular Canal defect (CAVC) | 10, Dextrocardia | 11, Dialated Aortic Root | 12, Dilated Cardiomyopathy (DCM) | 13, Double Inlet Left Ventricle (DILV) | 14, Double Outlet Right Ventricle (DORV) | 15, Ebstein's Anomaly | 16, Heterotaxy Syndrome | 17, Hypertrophic Cardiomyopathy (HCM) | 18, Hypoplastic Left Heart Syndrome (HLHS) | 19, Hypoplastic Right Heart Syndrome (HRHS) | 20, Interrupted Aortic Arch (IAA) | 21, Left ventricular non-compaction (LVNC) | 22, Marfan Syndrome | 23, Mitral Stenosis | 24, Mitral Valve Prolapse (MVP) | 25, Myocarditis | 26, Patent Ductus Arteriosis (PDA) | 27, Patent Foramen Ovale (PFO) | 28, Pericarditis | 29, Pulmonary Atresia | 30, Pulmonary Hypertension (PHT) | 31, Pulmonary Valve Stenosis | 32, Restrictive cardiomyopathy (RCM) | 33, Single Ventricle Defects | 34, Scimitar Syndrome (SS) | 35, Partial Anomalous Pulmonary Venous Connection (PAPVC) | 36, Total Anomalous Pulmonary Venous Connection (TAPVC) | 37, Shone's Syndrome/Shone's Complex/Shone's Anomaly | 38, Tetralogy of Fallot (ToF) | 39, Transposition of the Great Arteries (TGA) | 40, dextro-Transposition of the Great Arteries (d-TGA) | 41, levo-Transposition of the Great Arteries (l-TGA) | 42, Tricuspid Atresia | 43, Truncus Arteriosus | 44, Ventricular Septal Defect (VSD) | 45, Other", null=True, max_length=2000, verbose_name='Congenital/Acquired heart defect diagnosis (Confirmed) | Other congenital/acquired heart defect diagnosis (Confirmed) ', blank=True)
    cardiac_ep_dx_confirmed_summary = models.CharField(help_text='1, None | 2, Atrial Fibrillation (A-Fib) | 3, Atrial Flutter | 4, Bradycardia | 5, Brugada Syndrome | 6, Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT) | 7, Chaotic Atrial Tachycardia | 8, Ectopic Atrial Tachycardia (EAT) | 9, First Degree AV Block | 10, Second Degree AV Block (Mobitz Type I Wenckebach) | 11, Second Degree AV Block (Mobitz Type II) | 12, Third Degree (or Complete) AV Block | 13,  Junctional Ectopic Tachycardia (JET) | 14, Long QT Syndrome (LQTS) | 15, Multifocal Atrial Tachycardia | 16, Premature Atrial Complexes (PAC) | 17, Premature Junctional Complexes (PJC) | 18, Premature Ventricular Complexes (PVC) | 19, Right bundle branch block (RBBB) | 20, Left bundle branch block (LBBB) | 21, Left Anterior Hemiblock | 22, Left Posterior Hemiblock | 23, Right ventricular conduction delay-RVCD (IRBBB) | 24, Intraventricular conduction delay-IVCD (nonspecific) | 25, Short QT Syndrome (SQTS) | 26, Supraventricular Tachycardia (SVT) | 27, Torsades de pointes | 28, Ventricular Fibrillation (V-Fib) | 29, Ventricular Flutter | 30, Ventricular Tachycardia (VT) | 31, Wolff-Parkinson-White Syndrome (WPW) | 32, Other', null=True, max_length=2000, verbose_name='Electrocardiographic diagnosis (Confirmed) | Other electrocardiographic diagnosis (Confirmed)', blank=True)
    card_tx_proc_summary = models.CharField(help_text='1, None | 2, Catheter Ablation | 3, Electrophysiologic Studies | 4, Implantable Cardioverter-Defibrillator | 5, Pacemaker | 6, Left cervical sympathetic denervation | 7, Other', null=True, max_length=2000, verbose_name='Cardiac treatment procedures done', blank=True)
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'cardiacdiagnosi'


class cardiacreasonpresumeddx(models.Model):
    label = models.CharField(help_text='Check all that apply.', null=True, max_length=2000, verbose_name='Reason for consideration of presumed diagnosis ', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='Check all that apply.', null=True, verbose_name='Reason for consideration of presumed diagnosis ', choices=[(13, 'None'), (1, 'Personal history'), (2, 'Family history'), (3, 'Clinical history'), (4, 'Physical exam'), (5, 'ECG'), (6, 'ECHO'), (7, 'Genetic test'), (8, 'EST'), (9, 'Holter Monitor'), (10, 'Transtelephonic Monitoring (TTM)'), (11, 'Electrophysiologic Studies'), (12, 'Other')])
    cardiacdiagnosi = models.ForeignKey(CardiacDiagnosi)

    class Meta:
	 db_table = 'cardiacreasonpresumeddx'


class cardiacreasonpresumedsymptomsdx(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Symptoms described in personal/clinical history', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Symptoms described in personal/clinical history', choices=[(1, 'None'), (2, 'Syncope/fainted'), (3, 'Chest discomfort/pain/pressure'), (4, 'Racing heart beat/tachycardia'), (5, 'Slow heart rate/bradycardia'), (6, 'Skipped heart beat/palpatations'), (7, 'Dizziness/lightheadedness/nearly fainted'), (8, 'Shortness of breath (not asthma-related)'), (9, 'Unexplained seizure/convulsion'), (10, 'Easy fatigability'), (11, 'Torsades de pointes'), (12, 'Aborted Sudden Cardiac Arrest (ASA)'), (13, 'Hearing Loss'), (14, 'Other')])
    cardiacdiagnosi = models.ForeignKey(CardiacDiagnosi)

    class Meta:
	 db_table = 'cardiacreasonpresumedsymptomsdx'


class cardiacmethodconfirmeddx(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Method of confirmation of diagnosis.  Check all that apply.', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Method of confirmation of diagnosis.  Check all that apply.', choices=[(13, 'None'), (1, 'Personal history'), (2, 'Family history'), (3, 'Clinical history'), (4, 'Physical exam'), (5, 'ECG'), (6, 'ECHO'), (7, 'Genetic test'), (8, 'EST'), (9, 'Holter Monitor'), (10, 'Transtelephonic Monitoring (TTM)'), (11, 'Electrophysiologic Studies'), (12, 'Other')])
    cardiacdiagnosi = models.ForeignKey(CardiacDiagnosi)

    class Meta:
	 db_table = 'cardiacmethodconfirmeddx'


class cardiacmethodconfirmsymptomdx(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Additional symptoms described in personal/clinical history (since diagnosis was confirmed).', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Additional symptoms described in personal/clinical history (since diagnosis was confirmed).', choices=[(1, 'None'), (2, 'Syncope/fainted'), (3, 'Chest discomfort/pain/pressure'), (4, 'Racing heart beat/tachycardia'), (5, 'Slow heart rate/bradycardia'), (6, 'Skipped heart beat/palpatations'), (7, 'Dizziness/lightheadedness/nearly fainted'), (8, 'Shortness of breath (not asthma-related)'), (9, 'Unexplained seizure/convulsion'), (10, 'Easy fatigability'), (11, 'Torsades de pointes'), (12, 'Aborted Sudden Cardiac Arrest (ASA)'), (13, 'Hearing Loss'), (14, 'Other')])
    cardiacdiagnosi = models.ForeignKey(CardiacDiagnosi)

    class Meta:
	 db_table = 'cardiacmethodconfirmsymptomdx'


class cardiacchddxconfirmed(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Congenital/Acquired heart defect diagnosis (Confirmed) | Other congenital/acquired heart defect diagnosis (Confirmed) ', blank=True)
    value = models.IntegerField(help_text='', null=True, verbose_name='Congenital/Acquired heart defect diagnosis (Confirmed) | Other congenital/acquired heart defect diagnosis (Confirmed) ', blank=True, choices=[(1, 'None'), (2, 'Anomalous Coronary Artery'), (3, 'Aortic Valve Stenosis'), (4, 'Arrhythmogenic right ventricular dysplasia (ARVD)'), (5, 'Atrial Septal Defect (ASD)'), (6, 'Atrioventricular Septal Defect (AVSD)'), (7, 'Bicuspid Aortic Valve (BAV)'), (8, 'Coarctation of the Aorta (CoA)'), (9, 'Complete Atrioventricular Canal defect (CAVC)'), (10, 'Dextrocardia'), (11, 'Dialated Aortic Root'), (12, 'Dilated Cardiomyopathy (DCM)'), (13, 'Double Inlet Left Ventricle (DILV)'), (14, 'Double Outlet Right Ventricle (DORV)'), (15, "Ebstein's Anomaly"), (16, 'Heterotaxy Syndrome'), (17, 'Hypertrophic Cardiomyopathy (HCM)'), (18, 'Hypoplastic Left Heart Syndrome (HLHS)'), (19, 'Hypoplastic Right Heart Syndrome (HRHS)'), (20, 'Interrupted Aortic Arch (IAA)'), (21, 'Left ventricular non-compaction (LVNC)'), (22, 'Marfan Syndrome'), (23, 'Mitral Stenosis'), (24, 'Mitral Valve Prolapse (MVP)'), (25, 'Myocarditis'), (26, 'Patent Ductus Arteriosis (PDA)'), (27, 'Patent Foramen Ovale (PFO)'), (28, 'Pericarditis'), (29, 'Pulmonary Atresia'), (30, 'Pulmonary Hypertension (PHT)'), (31, 'Pulmonary Valve Stenosis'), (32, 'Restrictive cardiomyopathy (RCM)'), (33, 'Single Ventricle Defects'), (34, 'Scimitar Syndrome (SS)'), (35, 'Partial Anomalous Pulmonary Venous Connection (PAPVC)'), (36, 'Total Anomalous Pulmonary Venous Connection (TAPVC)'), (37, "Shone's Syndrome/Shone's Complex/Shone's Anomaly"), (38, 'Tetralogy of Fallot (ToF)'), (39, 'Transposition of the Great Arteries (TGA)'), (40, 'dextro-Transposition of the Great Arteries (d-TGA)'), (41, 'levo-Transposition of the Great Arteries (l-TGA)'), (42, 'Tricuspid Atresia'), (43, 'Truncus Arteriosus'), (44, 'Ventricular Septal Defect (VSD)'), (45, 'Other')]) # This field type is a guess
    cardiacdiagnosi = models.ForeignKey(CardiacDiagnosi)

    class Meta:
	 db_table = 'cardiacchddxconfirmed'


class cardiacepdxconfirmed(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Electrocardiographic diagnosis (Confirmed) | Other electrocardiographic diagnosis (Confirmed)', blank=True)
    value = models.IntegerField(help_text='', null=True, verbose_name='Electrocardiographic diagnosis (Confirmed) | Other electrocardiographic diagnosis (Confirmed)', blank=True, choices=[(1, 'None'), (2, 'Atrial Fibrillation (A-Fib)'), (3, 'Atrial Flutter'), (4, 'Bradycardia'), (5, 'Brugada Syndrome'), (6, 'Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT)'), (7, 'Chaotic Atrial Tachycardia'), (8, 'Ectopic Atrial Tachycardia (EAT)'), (9, 'First Degree AV Block'), (10, 'Second Degree AV Block (Mobitz Type I Wenckebach)'), (11, 'Second Degree AV Block (Mobitz Type II)'), (12, 'Third Degree (or Complete) AV Block'), (13, 'Junctional Ectopic Tachycardia (JET)'), (14, 'Long QT Syndrome (LQTS)'), (15, 'Multifocal Atrial Tachycardia'), (16, 'Premature Atrial Complexes (PAC)'), (17, 'Premature Junctional Complexes (PJC)'), (18, 'Premature Ventricular Complexes (PVC)'), (19, 'Right bundle branch block (RBBB)'), (20, 'Left bundle branch block (LBBB)'), (21, 'Left Anterior Hemiblock'), (22, 'Left Posterior Hemiblock'), (23, 'Right ventricular conduction delay-RVCD (IRBBB)'), (24, 'Intraventricular conduction delay-IVCD (nonspecific)'), (25, 'Short QT Syndrome (SQTS)'), (26, 'Supraventricular Tachycardia (SVT)'), (27, 'Torsades de pointes'), (28, 'Ventricular Fibrillation (V-Fib)'), (29, 'Ventricular Flutter'), (30, 'Ventricular Tachycardia (VT)'), (31, 'Wolff-Parkinson-White Syndrome (WPW)'), (32, 'Other')]) # This field type is a guess
    cardiacdiagnosi = models.ForeignKey(CardiacDiagnosi)

    class Meta:
	 db_table = 'cardiacepdxconfirmed'


class cardtxproc(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Cardiac treatment procedures done', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Cardiac treatment procedures done', choices=[(1, 'None'), (2, 'Catheter Ablation'), (3, 'Electrophysiologic Studies'), (4, 'Implantable Cardioverter-Defibrillator'), (5, 'Pacemaker'), (6, 'Left cervical sympathetic denervation'), (7, 'Other')])
    cardiacdiagnosi = models.ForeignKey(CardiacDiagnosi)

    class Meta:
	 db_table = 'cardtxproc'


class CardiacMedication(models.Model):
    card_meds = models.CharField(help_text='', null=True, max_length=2000, verbose_name='cardiac medication', blank=True)
    cardiacdiagnosi = models.ForeignKey(CardiacDiagnosi)

    class Meta:
	 db_table = 'cardiacmedication'


class CardiacFamilyHistory(models.Model):
    cfhx_died_sids = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Any blood relative who died with SIDS / SUID (Sudden Infant Death Syndrome / Sudden Unexpected Infant Death).', choices=[(1, 'None'), (2, 'Mother'), (3, 'Father'), (4, 'Sister'), (5, 'Brother'), (6, 'Maternal Grandmother'), (7, 'Maternal Grandfather'), (8, 'Paternal Grandmother'), (9, 'Paternal Grandfather'), (10, 'Maternal Aunt'), (11, 'Paternal Aunt'), (12, 'Maternal Uncle'), (13, 'Paternal Uncle'), (14, 'Maternal Cousin'), (15, 'Paternal Cousin'), (16, 'Other')])
    cfhx_hcm = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Any blood relatives with Hypertrophic cardiomyopathy (HCM)', choices=[(1, 'None'), (2, 'Mother'), (3, 'Father'), (4, 'Sister'), (5, 'Brother'), (6, 'Maternal Grandmother'), (7, 'Maternal Grandfather'), (8, 'Paternal Grandmother'), (9, 'Paternal Grandfather'), (10, 'Maternal Aunt'), (11, 'Paternal Aunt'), (12, 'Maternal Uncle'), (13, 'Paternal Uncle'), (14, 'Maternal Cousin'), (15, 'Paternal Cousin'), (16, 'Other')])
    cfhx_rcm = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Any blood relatives with Restrictive cardiomyopathy (RCM)', choices=[(1, 'None'), (2, 'Mother'), (3, 'Father'), (4, 'Sister'), (5, 'Brother'), (6, 'Maternal Grandmother'), (7, 'Maternal Grandfather'), (8, 'Paternal Grandmother'), (9, 'Paternal Grandfather'), (10, 'Maternal Aunt'), (11, 'Paternal Aunt'), (12, 'Maternal Uncle'), (13, 'Paternal Uncle'), (14, 'Maternal Cousin'), (15, 'Paternal Cousin'), (16, 'Other')])
    cfhx_lqts = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Any blood relatives with Long QT syndrome (LQTS)', choices=[(1, 'None'), (2, 'Mother'), (3, 'Father'), (4, 'Sister'), (5, 'Brother'), (6, 'Maternal Grandmother'), (7, 'Maternal Grandfather'), (8, 'Paternal Grandmother'), (9, 'Paternal Grandfather'), (10, 'Maternal Aunt'), (11, 'Paternal Aunt'), (12, 'Maternal Uncle'), (13, 'Paternal Uncle'), (14, 'Maternal Cousin'), (15, 'Paternal Cousin'), (16, 'Other')])
    cfhx_brugada = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Any blood relatives with Brugada syndrome', choices=[(1, 'None'), (2, 'Mother'), (3, 'Father'), (4, 'Sister'), (5, 'Brother'), (6, 'Maternal Grandmother'), (7, 'Maternal Grandfather'), (8, 'Paternal Grandmother'), (9, 'Paternal Grandfather'), (10, 'Maternal Aunt'), (11, 'Paternal Aunt'), (12, 'Maternal Uncle'), (13, 'Paternal Uncle'), (14, 'Maternal Cousin'), (15, 'Paternal Cousin'), (16, 'Other')])
    cfhx_wpw = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Any blood relatives with WPW-Wolff-Parkinson-White', choices=[(1, 'None'), (2, 'Mother'), (3, 'Father'), (4, 'Sister'), (5, 'Brother'), (6, 'Maternal Grandmother'), (7, 'Maternal Grandfather'), (8, 'Paternal Grandmother'), (9, 'Paternal Grandfather'), (10, 'Maternal Aunt'), (11, 'Paternal Aunt'), (12, 'Maternal Uncle'), (13, 'Paternal Uncle'), (14, 'Maternal Cousin'), (15, 'Paternal Cousin'), (16, 'Other')])
    cfhx_pace_icd = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Any blood relatives with Pacemaker or implanted defibrillator (ICD)', choices=[(1, 'None'), (2, 'Mother'), (3, 'Father'), (4, 'Sister'), (5, 'Brother'), (6, 'Maternal Grandmother'), (7, 'Maternal Grandfather'), (8, 'Paternal Grandmother'), (9, 'Paternal Grandfather'), (10, 'Maternal Aunt'), (11, 'Paternal Aunt'), (12, 'Maternal Uncle'), (13, 'Paternal Uncle'), (14, 'Maternal Cousin'), (15, 'Paternal Cousin'), (16, 'Other')])
    cfhx_faint = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Any blood relatives with Unexplained fainting or passing out', choices=[(1, 'None'), (2, 'Mother'), (3, 'Father'), (4, 'Sister'), (5, 'Brother'), (6, 'Maternal Grandmother'), (7, 'Maternal Grandfather'), (8, 'Paternal Grandmother'), (9, 'Paternal Grandfather'), (10, 'Maternal Aunt'), (11, 'Paternal Aunt'), (12, 'Maternal Uncle'), (13, 'Paternal Uncle'), (14, 'Maternal Cousin'), (15, 'Paternal Cousin'), (16, 'Other')])
    cfhx_drowning = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Any blood relatives with Near drowning', choices=[(1, 'None'), (2, 'Mother'), (3, 'Father'), (4, 'Sister'), (5, 'Brother'), (6, 'Maternal Grandmother'), (7, 'Maternal Grandfather'), (8, 'Paternal Grandmother'), (9, 'Paternal Grandfather'), (10, 'Maternal Aunt'), (11, 'Paternal Aunt'), (12, 'Maternal Uncle'), (13, 'Paternal Uncle'), (14, 'Maternal Cousin'), (15, 'Paternal Cousin'), (16, 'Other')])
    cfhx_diabetes = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Any blood relatives with Diabetes', choices=[(1, 'None'), (2, 'Mother'), (3, 'Father'), (4, 'Sister'), (5, 'Brother'), (6, 'Maternal Grandmother'), (7, 'Maternal Grandfather'), (8, 'Paternal Grandmother'), (9, 'Paternal Grandfather'), (10, 'Maternal Aunt'), (11, 'Paternal Aunt'), (12, 'Maternal Uncle'), (13, 'Paternal Uncle'), (14, 'Maternal Cousin'), (15, 'Paternal Cousin'), (16, 'Other')])
    cfhx_explanation = models.TextField(help_text='', null=True, verbose_name='Explain the cardiac family history stated above', blank=True) # This field type is a guess
    cfhx_died_scd_summary = models.CharField(help_text='1, None | 2, Mother | 3, Father | 4, Sister | 5, Brother | 6, Maternal Grandmother | 7, Maternal Grandfather | 8, Paternal Grandmother | 9, Paternal Grandfather | 10, Maternal Aunt | 11, Paternal Aunt | 12, Maternal Uncle | 13, Paternal Uncle | 14, Maternal Cousin | 15, Paternal Cousin | 16, Other', null=True, max_length=2000, verbose_name='Any blood relative who died of heart problems or had an unexpected or unexplained sudden death (including drowning or unexplained car accident) before age 50.', blank=True)
    cfhx_survive_sca_summary = models.CharField(help_text='1, None | 2, Mother | 3, Father | 4, Sister | 5, Brother | 6, Maternal Grandmother | 7, Maternal Grandfather | 8, Paternal Grandmother | 9, Paternal Grandfather | 10, Maternal Aunt | 11, Paternal Aunt | 12, Maternal Uncle | 13, Paternal Uncle | 14, Maternal Cousin | 15, Paternal Cousin | 16, Other', null=True, max_length=2000, verbose_name='Any blood relative experienced a sudden cardiac arrest (SCA) before age 50 and survived.', blank=True)
    cfhx_dcm_summary = models.CharField(help_text='1, None | 2, Mother | 3, Father | 4, Sister | 5, Brother | 6, Maternal Grandmother | 7, Maternal Grandfather | 8, Paternal Grandmother | 9, Paternal Grandfather | 10, Maternal Aunt | 11, Paternal Aunt | 12, Maternal Uncle | 13, Paternal Uncle | 14, Maternal Cousin | 15, Paternal Cousin | 16, Other', null=True, max_length=2000, verbose_name='Any blood relatives with Dilated cardiomyopathy (DCM) or Dilated Left or Right Ventricle', blank=True)
    cfhx_arvc_summary = models.CharField(help_text='1, None | 2, Mother | 3, Father | 4, Sister | 5, Brother | 6, Maternal Grandmother | 7, Maternal Grandfather | 8, Paternal Grandmother | 9, Paternal Grandfather | 10, Maternal Aunt | 11, Paternal Aunt | 12, Maternal Uncle | 13, Paternal Uncle | 14, Maternal Cousin | 15, Paternal Cousin | 16, Other', null=True, max_length=2000, verbose_name='Any blood relatives with ARVC (Arrhythmogenic right ventricular cardiomyopathy)', blank=True)
    cfhx_sqts_summary = models.CharField(help_text='1, None | 2, Mother | 3, Father | 4, Sister | 5, Brother | 6, Maternal Grandmother | 7, Maternal Grandfather | 8, Paternal Grandmother | 9, Paternal Grandfather | 10, Maternal Aunt | 11, Paternal Aunt | 12, Maternal Uncle | 13, Paternal Uncle | 14, Maternal Cousin | 15, Paternal Cousin | 16, Other', null=True, max_length=2000, verbose_name='Any blood relatives with Short QT syndrome (SQTS)', blank=True)
    cfhx_cptv_summary = models.CharField(help_text='1, None | 2, Mother | 3, Father | 4, Sister | 5, Brother | 6, Maternal Grandmother | 7, Maternal Grandfather | 8, Paternal Grandmother | 9, Paternal Grandfather | 10, Maternal Aunt | 11, Paternal Aunt | 12, Maternal Uncle | 13, Paternal Uncle | 14, Maternal Cousin | 15, Paternal Cousin | 16, Other', null=True, max_length=2000, verbose_name='Any blood relatives with CPVT-Catecholaminergic polymorphic ventricular tachycardia', blank=True)
    cfhx_marfan_summary = models.CharField(help_text='1, None | 2, Mother | 3, Father | 4, Sister | 5, Brother | 6, Maternal Grandmother | 7, Maternal Grandfather | 8, Paternal Grandmother | 9, Paternal Grandfather | 10, Maternal Aunt | 11, Paternal Aunt | 12, Maternal Uncle | 13, Paternal Uncle | 14, Maternal Cousin | 15, Paternal Cousin | 16, Other', null=True, max_length=2000, verbose_name='Any blood relatives with Marfan syndrome (aortic rupture / dissection)', blank=True)
    cfhx_cad_mi_summary = models.CharField(help_text='1, None | 2, Mother | 3, Father | 4, Sister | 5, Brother | 6, Maternal Grandmother | 7, Maternal Grandfather | 8, Paternal Grandmother | 9, Paternal Grandfather | 10, Maternal Aunt | 11, Paternal Aunt | 12, Maternal Uncle | 13, Paternal Uncle | 14, Maternal Cousin | 15, Paternal Cousin | 16, Other', null=True, max_length=2000, verbose_name='Any blood relatives with Coronary artery disease with Myocardial Infarction (MI / Heart attack)', blank=True)
    cfhx_seizure_summary = models.CharField(help_text='1, None | 2, Mother | 3, Father | 4, Sister | 5, Brother | 6, Maternal Grandmother | 7, Maternal Grandfather | 8, Paternal Grandmother | 9, Paternal Grandfather | 10, Maternal Aunt | 11, Paternal Aunt | 12, Maternal Uncle | 13, Paternal Uncle | 14, Maternal Cousin | 15, Paternal Cousin | 16, Other', null=True, max_length=2000, verbose_name='Any blood relatives with Unexplained seizures', blank=True)
    cfhx_hypertension_summary = models.CharField(help_text='1, None | 2, Mother | 3, Father | 4, Sister | 5, Brother | 6, Maternal Grandmother | 7, Maternal Grandfather | 8, Paternal Grandmother | 9, Paternal Grandfather | 10, Maternal Aunt | 11, Paternal Aunt | 12, Maternal Uncle | 13, Paternal Uncle | 14, Maternal Cousin | 15, Paternal Cousin | 16, Other', null=True, max_length=2000, verbose_name='Any blood relatives with High blood pressure (Hypertension)', blank=True)
    cfhx_congen_deaf_summary = models.CharField(help_text='1, None | 2, Mother | 3, Father | 4, Sister | 5, Brother | 6, Maternal Grandmother | 7, Maternal Grandfather | 8, Paternal Grandmother | 9, Paternal Grandfather | 10, Maternal Aunt | 11, Paternal Aunt | 12, Maternal Uncle | 13, Paternal Uncle | 14, Maternal Cousin | 15, Paternal Cousin | 16, Other', null=True, max_length=2000, verbose_name='Any blood relatives with congenital deafness (Deaf at birth)', blank=True)
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'cardiacfamilyhistory'


class cfhxdiedscd(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Any blood relative who died of heart problems or had an unexpected or unexplained sudden death (including drowning or unexplained car accident) before age 50.', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Any blood relative who died of heart problems or had an unexpected or unexplained sudden death (including drowning or unexplained car accident) before age 50.', choices=[(1, 'None'), (2, 'Mother'), (3, 'Father'), (4, 'Sister'), (5, 'Brother'), (6, 'Maternal Grandmother'), (7, 'Maternal Grandfather'), (8, 'Paternal Grandmother'), (9, 'Paternal Grandfather'), (10, 'Maternal Aunt'), (11, 'Paternal Aunt'), (12, 'Maternal Uncle'), (13, 'Paternal Uncle'), (14, 'Maternal Cousin'), (15, 'Paternal Cousin'), (16, 'Other')])
    cardiacfamilyhistory = models.ForeignKey(CardiacFamilyHistory)

    class Meta:
	 db_table = 'cfhxdiedscd'


class cfhxsurvivesca(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Any blood relative experienced a sudden cardiac arrest (SCA) before age 50 and survived.', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Any blood relative experienced a sudden cardiac arrest (SCA) before age 50 and survived.', choices=[(1, 'None'), (2, 'Mother'), (3, 'Father'), (4, 'Sister'), (5, 'Brother'), (6, 'Maternal Grandmother'), (7, 'Maternal Grandfather'), (8, 'Paternal Grandmother'), (9, 'Paternal Grandfather'), (10, 'Maternal Aunt'), (11, 'Paternal Aunt'), (12, 'Maternal Uncle'), (13, 'Paternal Uncle'), (14, 'Maternal Cousin'), (15, 'Paternal Cousin'), (16, 'Other')])
    cardiacfamilyhistory = models.ForeignKey(CardiacFamilyHistory)

    class Meta:
	 db_table = 'cfhxsurvivesca'


class cfhxdcm(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Any blood relatives with Dilated cardiomyopathy (DCM) or Dilated Left or Right Ventricle', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Any blood relatives with Dilated cardiomyopathy (DCM) or Dilated Left or Right Ventricle', choices=[(1, 'None'), (2, 'Mother'), (3, 'Father'), (4, 'Sister'), (5, 'Brother'), (6, 'Maternal Grandmother'), (7, 'Maternal Grandfather'), (8, 'Paternal Grandmother'), (9, 'Paternal Grandfather'), (10, 'Maternal Aunt'), (11, 'Paternal Aunt'), (12, 'Maternal Uncle'), (13, 'Paternal Uncle'), (14, 'Maternal Cousin'), (15, 'Paternal Cousin'), (16, 'Other')])
    cardiacfamilyhistory = models.ForeignKey(CardiacFamilyHistory)

    class Meta:
	 db_table = 'cfhxdcm'


class cfhxarvc(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Any blood relatives with ARVC (Arrhythmogenic right ventricular cardiomyopathy)', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Any blood relatives with ARVC (Arrhythmogenic right ventricular cardiomyopathy)', choices=[(1, 'None'), (2, 'Mother'), (3, 'Father'), (4, 'Sister'), (5, 'Brother'), (6, 'Maternal Grandmother'), (7, 'Maternal Grandfather'), (8, 'Paternal Grandmother'), (9, 'Paternal Grandfather'), (10, 'Maternal Aunt'), (11, 'Paternal Aunt'), (12, 'Maternal Uncle'), (13, 'Paternal Uncle'), (14, 'Maternal Cousin'), (15, 'Paternal Cousin'), (16, 'Other')])
    cardiacfamilyhistory = models.ForeignKey(CardiacFamilyHistory)

    class Meta:
	 db_table = 'cfhxarvc'


class cfhxsqts(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Any blood relatives with Short QT syndrome (SQTS)', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Any blood relatives with Short QT syndrome (SQTS)', choices=[(1, 'None'), (2, 'Mother'), (3, 'Father'), (4, 'Sister'), (5, 'Brother'), (6, 'Maternal Grandmother'), (7, 'Maternal Grandfather'), (8, 'Paternal Grandmother'), (9, 'Paternal Grandfather'), (10, 'Maternal Aunt'), (11, 'Paternal Aunt'), (12, 'Maternal Uncle'), (13, 'Paternal Uncle'), (14, 'Maternal Cousin'), (15, 'Paternal Cousin'), (16, 'Other')])
    cardiacfamilyhistory = models.ForeignKey(CardiacFamilyHistory)

    class Meta:
	 db_table = 'cfhxsqts'


class cfhxcptv(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Any blood relatives with CPVT-Catecholaminergic polymorphic ventricular tachycardia', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Any blood relatives with CPVT-Catecholaminergic polymorphic ventricular tachycardia', choices=[(1, 'None'), (2, 'Mother'), (3, 'Father'), (4, 'Sister'), (5, 'Brother'), (6, 'Maternal Grandmother'), (7, 'Maternal Grandfather'), (8, 'Paternal Grandmother'), (9, 'Paternal Grandfather'), (10, 'Maternal Aunt'), (11, 'Paternal Aunt'), (12, 'Maternal Uncle'), (13, 'Paternal Uncle'), (14, 'Maternal Cousin'), (15, 'Paternal Cousin'), (16, 'Other')])
    cardiacfamilyhistory = models.ForeignKey(CardiacFamilyHistory)

    class Meta:
	 db_table = 'cfhxcptv'


class cfhxmarfan(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Any blood relatives with Marfan syndrome (aortic rupture / dissection)', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Any blood relatives with Marfan syndrome (aortic rupture / dissection)', choices=[(1, 'None'), (2, 'Mother'), (3, 'Father'), (4, 'Sister'), (5, 'Brother'), (6, 'Maternal Grandmother'), (7, 'Maternal Grandfather'), (8, 'Paternal Grandmother'), (9, 'Paternal Grandfather'), (10, 'Maternal Aunt'), (11, 'Paternal Aunt'), (12, 'Maternal Uncle'), (13, 'Paternal Uncle'), (14, 'Maternal Cousin'), (15, 'Paternal Cousin'), (16, 'Other')])
    cardiacfamilyhistory = models.ForeignKey(CardiacFamilyHistory)

    class Meta:
	 db_table = 'cfhxmarfan'


class cfhxcadmi(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Any blood relatives with Coronary artery disease with Myocardial Infarction (MI / Heart attack)', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Any blood relatives with Coronary artery disease with Myocardial Infarction (MI / Heart attack)', choices=[(1, 'None'), (2, 'Mother'), (3, 'Father'), (4, 'Sister'), (5, 'Brother'), (6, 'Maternal Grandmother'), (7, 'Maternal Grandfather'), (8, 'Paternal Grandmother'), (9, 'Paternal Grandfather'), (10, 'Maternal Aunt'), (11, 'Paternal Aunt'), (12, 'Maternal Uncle'), (13, 'Paternal Uncle'), (14, 'Maternal Cousin'), (15, 'Paternal Cousin'), (16, 'Other')])
    cardiacfamilyhistory = models.ForeignKey(CardiacFamilyHistory)

    class Meta:
	 db_table = 'cfhxcadmi'


class cfhxseizure(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Any blood relatives with Unexplained seizures', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Any blood relatives with Unexplained seizures', choices=[(1, 'None'), (2, 'Mother'), (3, 'Father'), (4, 'Sister'), (5, 'Brother'), (6, 'Maternal Grandmother'), (7, 'Maternal Grandfather'), (8, 'Paternal Grandmother'), (9, 'Paternal Grandfather'), (10, 'Maternal Aunt'), (11, 'Paternal Aunt'), (12, 'Maternal Uncle'), (13, 'Paternal Uncle'), (14, 'Maternal Cousin'), (15, 'Paternal Cousin'), (16, 'Other')])
    cardiacfamilyhistory = models.ForeignKey(CardiacFamilyHistory)

    class Meta:
	 db_table = 'cfhxseizure'


class cfhxhypertension(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Any blood relatives with High blood pressure (Hypertension)', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Any blood relatives with High blood pressure (Hypertension)', choices=[(1, 'None'), (2, 'Mother'), (3, 'Father'), (4, 'Sister'), (5, 'Brother'), (6, 'Maternal Grandmother'), (7, 'Maternal Grandfather'), (8, 'Paternal Grandmother'), (9, 'Paternal Grandfather'), (10, 'Maternal Aunt'), (11, 'Paternal Aunt'), (12, 'Maternal Uncle'), (13, 'Paternal Uncle'), (14, 'Maternal Cousin'), (15, 'Paternal Cousin'), (16, 'Other')])
    cardiacfamilyhistory = models.ForeignKey(CardiacFamilyHistory)

    class Meta:
	 db_table = 'cfhxhypertension'


class cfhxcongendeaf(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Any blood relatives with congenital deafness (Deaf at birth)', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Any blood relatives with congenital deafness (Deaf at birth)', choices=[(1, 'None'), (2, 'Mother'), (3, 'Father'), (4, 'Sister'), (5, 'Brother'), (6, 'Maternal Grandmother'), (7, 'Maternal Grandfather'), (8, 'Paternal Grandmother'), (9, 'Paternal Grandfather'), (10, 'Maternal Aunt'), (11, 'Paternal Aunt'), (12, 'Maternal Uncle'), (13, 'Paternal Uncle'), (14, 'Maternal Cousin'), (15, 'Paternal Cousin'), (16, 'Other')])
    cardiacfamilyhistory = models.ForeignKey(CardiacFamilyHistory)

    class Meta:
	 db_table = 'cfhxcongendeaf'


class EcgResult(models.Model):
    ecg_done = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Electrocardiogram done', choices=[(1, 'Yes'), (2, 'No')])
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'ecgresult'


class Ecg(models.Model):
    ecg_enrollment = models.IntegerField(help_text='', null=True, verbose_name='How would you categorize the ECG | Other test category', blank=True, choices=[(1, 'Initial test'), (2, 'Enrollment test'), (3, 'Post-enrollment test'), (4, 'Other')]) # This field type is a guess
    ecg_date = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Date of ECG', blank=True)
    ecg_time = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Time of ECG', blank=True)
    ecg_ventricular_rate = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Ventricular Rate / bpm for ECG', blank=True)
    ecg_pr_interval = models.CharField(help_text='', null=True, max_length=2000, verbose_name='PR Interval / msec for $ECG', blank=True)
    ecg_qrs_inter_machine = models.CharField(help_text='', null=True, max_length=2000, verbose_name='QRS Interval / msec  (ECG Computer) for ECG', blank=True)
    ecg_qt_inter_machine = models.CharField(help_text='', null=True, max_length=2000, verbose_name='QT Interval / msec   (ECG Computer) for ECG', blank=True)
    ecg_qtc_inter_machine = models.CharField(help_text='', null=True, max_length=2000, verbose_name='QTc Interval / msec   (ECG Computer) for ECG', blank=True)
    ecg_qtc_inter_manual = models.CharField(help_text='', null=True, max_length=2000, verbose_name='QTc Interval / msec   (Manual Calculation) for ECG', blank=True)
    ecg_p_axis_degree = models.CharField(help_text='NOTE: Must use positive numbers. (360 degrees minus X)', null=True, max_length=2000, verbose_name='P axis for ECG', blank=True)
    ecg_p_axis_type = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='P Axis Type for ECG', choices=[(1, 'Sinus (0 to +90 degree)'), (2, 'LRA (-1 to -90 degree)'), (3, 'HLA (+91 to +180 degree)'), (4, 'LLA (-91 to -179 or +181 to +270 degree)')])
    ecg_qrs_axis_degree = models.CharField(help_text='NOTE: Must use positive numbers. (360 degrees minus X)', null=True, max_length=2000, verbose_name='QRS axis for ECG', blank=True)
    ecg_qrs_axis_type = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='QRS Axis Type for ECG', choices=[(1, 'Normal'), (2, 'RAD (>+100 degree)'), (3, 'Rightward (+90 to +100 degree)'), (4, 'LAD (negative degree)')])
    ecg_twave_axis_degree = models.CharField(help_text='NOTE: Must use positive numbers. (360 degrees minus X)', null=True, max_length=2000, verbose_name='T wave axis for ECG', blank=True)
    ecg_twave_axis_type = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='T wave axis Type for ECG', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Wide QRS-T angle')])
    ecg_interp_arrhythmia = models.CharField(help_text='Check all that apply.', null=True, max_length=2000, verbose_name='ECG Interpretation: Arrhythmia/Conduction. ', blank=True)
    ecg_interp_structure = models.IntegerField(max_length=2000, blank=True, help_text='Check all that apply', null=True, verbose_name='ECG Interpretation: Structural. ', choices=[(1, 'None'), (2, 'Right atrial enlargement (RAE)'), (3, 'Left atrial enlargement (LAE)'), (4, 'Bi-atrial enlargement  (BAE)'), (5, 'Biventricular hypertrophy'), (6, 'Right ventricular hypertrophy (RVH)'), (7, 'Right ventricular hypertrophy (RVH) with strain'), (8, 'Left ventricular hypertrophy (LVH)'), (9, 'Left ventricular hypertrophy (LVH) with strain'), (10, 'Hypertrophic Cardiomyopathy (HCM)'), (11, 'Dilated Cardiomyopathy (DCM)'), (12, 'Dextrocardia')])
    ecg_interp_other = models.TextField(help_text='', null=True, verbose_name='ECG Interpretation:  Other (not listed above)', blank=True) # This field type is a guess
    ecg_result = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='ECG Result', choices=[(1, 'Normal'), (2, 'VON - Variant of Normal'), (3, 'Abnormal'), (4, 'Not Determined')])
    ecg_interp_rhythm_summary = models.CharField(help_text='10, None | 1, Normal Sinus Rhythm | 2, Normal Sinus Rhythm with Sinus Arrhythmia | 3, Normal Sinus Rhythm with Sinus Bradycardia | 4, Normal Sinus Rhythm with Sinus Tachycardia | 5, Low Right Atrial Rhythm | 6, Ectopic Atrial Rhythm | 7, Normal Sinus Rhythm alternating with Ectopic Atrial Rhythm | 8, Junctional Rhythm (accelerated or escape) | 9, Ventricular Rhythm (accelerated or escape)', null=True, max_length=2000, verbose_name='ECG Interpretation: Predominant Rhythm.  ', blank=True)
    ecg_interp_axis_summary = models.CharField(help_text='1, None | 2, Leftward Axis | 3, Left Axis Deviation (LAD) | 4, Left Superior Axis Deviation | 5, Rightward Axis | 6, Right Axis Deviation (RAD) | 7, Right Axis Deviation, northwest | 8, Indeterminate Axis | 9, Increased LV Forces | 10, ST elevation (Nonspecific) | 11, ST elevation (Ischemia) | 12, ST elevation (Strain) | 13, ST elevation (Early Repolarization) | 14, ST depression (Nonspecific) | 15, ST depression (Ischemia) | 16, ST depression (Strain) | 17, T wave inversion (Inferior) | 18, T wave inversion (Anterior) | 19, T wave inversion (Lateral) | 20, T wave abnormalities (Nonspecific) | 21, T wave abnormalities (Alternans) | 22, T wave abnormalities (Flat) | 23, T wave abnormalities (Late T wave peak) | 24, T wave abnormalities (Notched) | 25, T wave abnormalities (Biphasic) | 26, T wave abnormalities (Inverted) | 27, Q waves (Abnormal) | 28, Q waves (ULN) | 29, U waves (Abnormal) | 30, U waves (Prominent U Waves)', null=True, max_length=2000, verbose_name='ECG Interpretation: Axis.', blank=True)
    ecgresult = models.ForeignKey(EcgResult)

    class Meta:
	 db_table = 'ecg'


class ecginterprhythm(models.Model):
    label = models.CharField(help_text='Check all that apply', null=True, max_length=2000, verbose_name='ECG Interpretation: Predominant Rhythm.  ', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='Check all that apply', null=True, verbose_name='ECG Interpretation: Predominant Rhythm.  ', choices=[(10, 'None'), (1, 'Normal Sinus Rhythm'), (2, 'Normal Sinus Rhythm with Sinus Arrhythmia'), (3, 'Normal Sinus Rhythm with Sinus Bradycardia'), (4, 'Normal Sinus Rhythm with Sinus Tachycardia'), (5, 'Low Right Atrial Rhythm'), (6, 'Ectopic Atrial Rhythm'), (7, 'Normal Sinus Rhythm alternating with Ectopic Atrial Rhythm'), (8, 'Junctional Rhythm (accelerated or escape)'), (9, 'Ventricular Rhythm (accelerated or escape)')])
    ecg = models.ForeignKey(Ecg)

    class Meta:
	 db_table = 'ecginterprhythm'


class ecginterpaxis(models.Model):
    label = models.CharField(help_text='Check all that apply.', null=True, max_length=2000, verbose_name='ECG Interpretation: Axis.', blank=True)
    value = models.CharField(help_text='Check all that apply.', null=True, max_length=2000, verbose_name='ECG Interpretation: Axis.', blank=True)
    ecg = models.ForeignKey(Ecg)

    class Meta:
	 db_table = 'ecginterpaxis'


class EchoResult(models.Model):
    echo_done = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Echocardiogram done', choices=[(1, 'Yes'), (2, 'No')])
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'echoresult'


class EchoTest(models.Model):
    echo_enrollment = models.IntegerField(help_text='', null=True, verbose_name='How would you categorize the ECHO | Other test category', blank=True, choices=[(1, 'Initial test'), (2, 'Enrollment test'), (3, 'Post-enrollment test'), (4, 'Other')]) # This field type is a guess
    echo_date = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Date of ECHO', blank=True)
    echo_ht_report = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Height/cm on ECHO report', blank=True)
    echo_wt_report = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Weight/kg on ECHO report', blank=True)
    echo_bsa = models.CharField(help_text='', null=True, max_length=2000, verbose_name='BSA - Body Surface Area on ECHO report', blank=True)
    echo_ivsd = models.CharField(help_text='', null=True, max_length=2000, verbose_name='IVSd - (Diastolic septal thickness/cm) on ECHO report', blank=True)
    echo_ivsd_zscore = models.CharField(help_text='', null=True, max_length=2000, verbose_name='IVSd Zscore- (Diastolic septal thickness/zscore) on ECHO report', blank=True)
    echo_lvidd = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LVIDd - (LV Diastolic dimension/cm) on ECHO report', blank=True)
    echo_lvidd_zscore = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LVIDd Zscore- (LV Diastolic dimension/zscore) on ECHO report', blank=True)
    echo_lvids = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LVIDs - (LV Systolic dimension/cm) on ECHO report', blank=True)
    echo_lvids_zscore = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LVIDs Zscore- (LV Systolic dimension/zscore) on ECHO report', blank=True)
    echo_lvpwd = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LVPWd - (LV diastolic wall thickness/cm) on ECHO report', blank=True)
    echo_lvpwd_zscore = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LVPWd Zscore- (LV diastolic wall thickness/zscore) on ECHO report', blank=True)
    echo_lv_mass = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV mass - (M-mode LV mass-ASE corr./g) on ECHO report', blank=True)
    echo_lv_mass_zscore = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV mass Zscore- (M-mode LV mass-ASE corr./g/zscore) on ECHO report', blank=True)
    echo_lv_mass_index = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV mass index (g/h^2.7) on ECHO report', blank=True)
    echo_lv_vol_d_4c = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV volume, d (4C) - (mL) on ECHO report', blank=True)
    echo_lv_vol_d_2c = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV volume, d (2C) - (mL) on ECHO report', blank=True)
    echo_lv_vol_d_biplane = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV volume, d (biplane) - (mL) on ECHO report', blank=True)
    echo_lv_vol_s_4c = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV volume, s (4C) - (mL) on ECHO report', blank=True)
    echo_lv_vol_s_2c = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV volume, s (2C) - (mL) on ECHO report', blank=True)
    echo_lv_vol_s_biplane = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV volume, s (biplane) - (mL) on ECHO report', blank=True)
    echo_lv_vol_d_4c_index = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV volume, d (4C) index - (mL/m^2) on ECHO report', blank=True)
    echo_lv_vol_d_2c_index = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV volume, d (2C) index - (mL/m^2) on ECHO report', blank=True)
    echo_lv_vol_d_biplane_ind = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV volume, d (biplane) index - (mL/m^2) on ECHO report', blank=True)
    echo_aov_annulus = models.CharField(help_text='', null=True, max_length=2000, verbose_name='AoV annulus - (Aortic Annulus diameter/cm) on ECHO report', blank=True)
    echo_aov_annulus_zscore = models.CharField(help_text='', null=True, max_length=2000, verbose_name='AoV annulus Zscore- (Aortic Annulus diameter/zscore) on ECHO report', blank=True)
    echo_ao_root = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Ao Root - (Aortic Root diameter/cm) on ECHO report', blank=True)
    echo_ao_root_zscore = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Ao Root Zscore- (Aortic Root diameter/zscore) on ECHO report', blank=True)
    echo_ao_st_junct_s = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Ao ST junct, s - (Sinotubular junction diameter/cm) on ECHO report', blank=True)
    echo_ao_st_junct_s_zscore = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Ao ST junct, s Zscore- (Sinotubular junction diameter/zscore) on ECHO report', blank=True)
    echo_ao_asc_d = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Ao asc,d - (cm) on ECHO report', blank=True)
    echo_ao_asc_d_zscore = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Ao asc,d, Zscore on ECHO report', blank=True)
    echo_ao_dsc_d = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Ao dsc,d - (cm) on ECHO report', blank=True)
    echo_ao_dsc_d_zscore = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Ao dsc,d, Zscore on ECHO report', blank=True)
    echo_aov_area = models.CharField(help_text='', null=True, max_length=2000, verbose_name='AoV Area - (Aortic valve area/cm^2) on ECHO report', blank=True)
    echo_lv_sf = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV SF - (LV shortening fraction M-mode/%) on ECHO report', blank=True)
    echo_lv_ef = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV EF - (Ejection fraction M-mode/%) on ECHO report', blank=True)
    echo_lv_ef_4c = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV EF (4C) - (Ejection fraction/%) on ECHO report', blank=True)
    echo_lv_ef_2c = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV EF (2C) - (Ejection fraction/%) on ECHO report', blank=True)
    echo_lv_ef_biplane = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV EF (biplane) - (Ejection fraction/%) on ECHO report', blank=True)
    echo_lv_ef_aov = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV ejection time (AoV) - (msec) on ECHO report', blank=True)
    echo_lv_intra_avv = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV Intra AVV Time (MV) - (msec) on ECHO report', blank=True)
    echo_lv_mpi = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV MPI on ECHO report', blank=True)
    echo_lv_septal_annulus = models.CharField(help_text='', null=True, max_length=2000, verbose_name="LV Diastolic Function: Septal annulus e' - (m/s) on ECHO report", blank=True)
    echo_lv_mitral_septal = models.CharField(help_text='', null=True, max_length=2000, verbose_name="LV Diastolic Function: E/e' (mitral septal) on ECHO report", blank=True)
    echo_lv_mitral_lateral = models.CharField(help_text='', null=True, max_length=2000, verbose_name="LV Diastolic Function: E/e' (mitral lateral) on ECHO report", blank=True)
    echo_lv_mitral_inflow = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV Diastolic Function: E/A (mitral inflow) on ECHO report', blank=True)
    echo_lvot_peak_vel = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LVOTO Doppler: Peak velocity (m/s) on ECHO report', blank=True)
    echo_lvot_peak_grad = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LVOTO Doppler: Peak gradient (mmHg) on ECHO report', blank=True)
    echo_lvot_mean_grad = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LVOTO Doppler: Mean gradient (mmHg) on ECHO report', blank=True)
    echo_av_peak_vel = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Aortic Valve Doppler: Peak Velocity (m/s) on ECHO report', blank=True)
    echo_av_peak_grad = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Aortic Valve Doppler: Peak Gradient (mmHg) on ECHO report', blank=True)
    echo_av_mean_grad = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Aortic Valve Doppler: Mean Gradient (mmHg) on ECHO report', blank=True)
    echo_av_eject_time = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Aortic Valve Doppler: Ejection time (msec) on ECHO report', blank=True)
    echo_mv_peak_e = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Mitral Valve Doppler: Peak E (m/s) on ECHO report', blank=True)
    echo_mv_peak_a = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Mitral Valve Doppler: Peak A (m/s) on ECHO report', blank=True)
    echo_myocard_perf_index = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Myocardial Performance Index on ECHO report', blank=True)
    echo_samm = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Systolic Anterior Motion of Mitral Valve on ECHO report', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    echo_samm_degree = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Degree of SAMM on ECHO report', blank=True)
    echo_lvoto = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='LVOTO - (Left Ventricular Outflow Tract Obstruction) on ECHO report', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    echo_lvoto_gradient = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='LVOTO Gradient on ECHO report', choices=[(1, 'Mild'), (2, 'Moderate'), (3, 'Severe'), (4, 'Other')])
    echo_lvoto_gradient_oth = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LVOTO Gradient Other - Specify on ECHO report', blank=True)
    echo_rvoto = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='RVOTO - (Right Ventricular Outflow Tract Obstruction) on ECHO report', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    echo_rvoto_gradient = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='RVOTO Gradient on ECHO report', choices=[(1, 'Mild'), (2, 'Moderate'), (3, 'Severe'), (4, 'Other')])
    echo_rvoto_gradient_oth = models.CharField(help_text='', null=True, max_length=2000, verbose_name='RVOTO Gradient Other - Specify on ECHO report', blank=True)
    echo_rv_chamber = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='RV chamber on ECHO report', choices=[(1, 'Normal'), (2, 'Abnormal')])
    echo_rv_specify = models.CharField(help_text='', null=True, max_length=2000, verbose_name='RV: Specify on ECHO report', blank=True)
    echo_lv_chamber = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='LV chamber on ECHO report', choices=[(1, 'Normal'), (2, 'Abnormal')])
    echo_lv_specify = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV: Specify on ECHO report', blank=True)
    echo_ra = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='RA on ECHO report', choices=[(1, 'Normal'), (2, 'Abnormal')])
    echo_ra_specify = models.CharField(help_text='', null=True, max_length=2000, verbose_name='RA: Specify on ECHO report', blank=True)
    echo_la = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='LA on ECHO report', choices=[(1, 'Normal'), (2, 'Abnormal')])
    echo_la_specify = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LA: Specify on ECHO report', blank=True)
    echo_aortic_root = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Aortic Root on ECHO report', choices=[(1, 'Normal'), (2, 'Abnormal')])
    echo_aortic_root_specify = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Aortic Root: Specify on ECHO report', blank=True)
    echo_bicuspid_aortic_val = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Bicuspid aortic valve on ECHO report', choices=[(1, 'Yes'), (2, 'No'), (3, 'Not well seen')])
    echo_aortic_insuff = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Aortic valve insufficiency on ECHO report', choices=[(1, 'Yes'), (2, 'No')])
    echo_ai_severity = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Aortic valve insufficiency: Severity on ECHO report', choices=[(1, 'Trivial'), (2, 'Mild'), (3, 'Moderate'), (4, 'Severe')])
    echo_aortic_stenosis = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Aortic stenosis on ECHO report', choices=[(1, 'Yes'), (2, 'No')])
    echo_as_sever = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Aortic stenosis: Severity on ECHO report', choices=[(1, 'Trivial'), (2, 'Mild'), (3, 'Moderate'), (4, 'Severe')])
    echo_as_peak_grad = models.CharField(help_text='', null=True, max_length=2000, verbose_name='AS-Peak gradient (m/sec) on ECHO report', blank=True)
    echo_as_mean_grad = models.CharField(help_text='', null=True, max_length=2000, verbose_name='AS-Mean gradient (m/sec) on ECHO report', blank=True)
    echo_region_aortic_sten = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Region of aortic stenosis on ECHO report', choices=[(1, 'Valve'), (2, 'Subvalvular'), (3, 'Supravalvular'), (4, 'Other')])
    echo_region_as_oth = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Region of aortic stenosis: Specify on ECHO report', blank=True)
    echo_hcm = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Hypertrophic Cardiomyopathy on ECHO report', blank=True)
    echo_hcm_severity = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Hypertrophic Cardiomyopathy: Severity on ECHO report', choices=[(1, 'Trivial'), (2, 'Mild'), (3, 'Moderate'), (4, 'Severe')])
    echo_hypertrophy_loc = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Location of Hypertrophy on ECHO report', choices=[(1, 'Septal'), (2, 'Apical'), (3, 'Concentric'), (4, 'Other')])
    echo_hyper_other = models.TextField(help_text='', null=True, verbose_name='Location of Hypertrophy Other - Specify on ECHO report', blank=True) # This field type is a guess
    echo_pul_insuff = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Pulmonary valve insufficiency on ECHO report', choices=[(1, 'Yes'), (2, 'No')])
    echo_pi_severity = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Pulmonary valve insufficiency: Severity on ECHO report', choices=[(1, 'Trivial'), (2, 'Mild'), (3, 'Moderate'), (4, 'Severe')])
    echo_pul_stenosis = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Pulmonary stenosis on ECHO report', choices=[(1, 'Yes'), (2, 'No')])
    echo_ps_severity = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Pulmonary stenosis: Severity on ECHO report', choices=[(1, 'Trivial'), (2, 'Mild'), (3, 'Moderate'), (4, 'Severe')])
    echo_ps_peak_grad = models.CharField(help_text='', null=True, max_length=2000, verbose_name='PS-Peak gradient (m/sec) on ECHO report', blank=True)
    echo_ps_mean_grad = models.CharField(help_text='', null=True, max_length=2000, verbose_name='PS-Mean gradient (m/sec) on ECHO report', blank=True)
    echo_mit_insuff = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Mitral valve insufficiency on ECHO report', choices=[(1, 'Yes'), (2, 'No')])
    echo_mi_severity = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Mitral valve insufficiency: Severity on ECHO report', choices=[(1, 'Trivial'), (2, 'Mild'), (3, 'Moderate'), (4, 'Severe')])
    echo_mit_val_prolapse = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Mitral valve prolapse on ECHO report', choices=[(1, 'Yes'), (2, 'No')])
    echo_mvp_severity = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Mitral valve prolapse: Severity on ECHO report', choices=[(1, 'Trivial'), (2, 'Mild'), (3, 'Moderate'), (4, 'Severe')])
    echo_ms_gradient = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='MS gradient on ECHO report', choices=[(1, 'Yes'), (2, 'No')])
    echo_ms_grad_severity = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='MS gradient: Severity on ECHO report', choices=[(1, 'Trivial'), (2, 'Mild'), (3, 'Moderate'), (4, 'Severe')])
    echo_ms_jet_velocity = models.CharField(help_text='', null=True, max_length=2000, verbose_name='MS mean jet velocity (m/sec) on ECHO report', blank=True)
    echo_tri_insuff = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Tricuspid valve insufficiency on ECHO report', choices=[(1, 'Yes'), (2, 'No')])
    echo_ti_severity = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Tricuspid valve insufficiency: Severity on ECHO report', choices=[(1, 'Trivial'), (2, 'Mild'), (3, 'Moderate'), (4, 'Severe')])
    echo_tri_stenosis = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Tricuspid valve stenosis on ECHO report', choices=[(1, 'Yes'), (2, 'No')])
    echo_tri_sten_severity = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Tricuspid valve stenosis: Severity on ECHO report', choices=[(1, 'Trivial'), (2, 'Mild'), (3, 'Moderate'), (4, 'Severe')])
    echo_tri_sten_gradient = models.CharField(help_text='', null=True, max_length=2000, verbose_name='TS-Peak gradient (m/sec) on ECHO report', blank=True)
    echo_rv_pressure = models.CharField(help_text='', null=True, max_length=2000, verbose_name='RV pressure estimate (mm/Hg > right atrial v wave) on ECHO report', blank=True)
    echo_asd = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Atrial septal defect on ECHO report', choices=[(1, 'Yes'), (2, 'No'), (3, 'Not well seen')])
    echo_asd_severity = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='ASD: Size on ECHO report', choices=[(1, 'Small'), (2, 'Moderate'), (3, 'Large')])
    echo_asd_specify_small = models.TextField(help_text='', null=True, verbose_name='ASD (small): Specify (cm) on ECHO report', blank=True) # This field type is a guess
    echo_asd_specify_mod = models.TextField(help_text='', null=True, verbose_name='ASD (moderate): Specify (cm) on ECHO report', blank=True) # This field type is a guess
    echo_asd_specify_large = models.TextField(help_text='', null=True, verbose_name='ASD (large): Specify (cm) on ECHO report', blank=True) # This field type is a guess
    echo_pfo = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Patent foramen ovale on ECHO report', choices=[(1, 'Yes'), (2, 'No'), (3, 'Not well seen')])
    echo_pfo_severity = models.CharField(help_text='', null=True, max_length=2000, verbose_name='PFO: Specify on ECHO report', blank=True)
    echo_vsd = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Ventricular septal defect on ECHO report', choices=[(1, 'Yes'), (2, 'No'), (3, 'Not well seen')])
    echo_vsd_severity = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='VSD: Size on ECHO report', choices=[(1, 'Small'), (2, 'Moderate'), (3, 'Large')])
    echo_vsd_specify_small = models.TextField(help_text='', null=True, verbose_name='VSD (small): Specify on ECHO report', blank=True) # This field type is a guess
    echo_vsd_specify_mod = models.TextField(help_text='', null=True, verbose_name='ASD (moderate): Specify on ECHO report', blank=True) # This field type is a guess
    echo_vsd_specify_large = models.TextField(help_text='', null=True, verbose_name='ASD (large): Specify on ECHO report', blank=True) # This field type is a guess
    echo_pda = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Patent ductus arteriosus on ECHO report', choices=[(1, 'Yes'), (2, 'No'), (3, 'Not well seen')])
    echo_pda_severity = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='PDA: Severity on ECHO report', choices=[(1, 'Small'), (2, 'Moderate'), (3, 'Large')])
    echo_pda_specify_small = models.TextField(help_text='', null=True, verbose_name='PDA (small): Specify on ECHO report', blank=True) # This field type is a guess
    echo_pda_specify_mod = models.TextField(help_text='', null=True, verbose_name='PDA (moderate): Specify on ECHO report', blank=True) # This field type is a guess
    echo_pda_specify_large = models.TextField(help_text='', null=True, verbose_name='PDA (large): Specify on ECHO report', blank=True) # This field type is a guess
    echo_coarct = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Coarctation of the aorta on ECHO report', choices=[(1, 'Yes'), (2, 'No'), (3, 'Other')])
    echo_coarct_severity = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Coarctation of the aorta: Severity on ECHO report', choices=[(1, 'Mild'), (2, 'Moderate'), (3, 'Severe')])
    echo_coarct_sever_oth = models.TextField(help_text='', null=True, verbose_name='Coarctation of the aorta/Other: Specify on ECHO report', blank=True) # This field type is a guess
    echo_peri_effusion = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Pericardial effusion on ECHO report', choices=[(1, 'Yes'), (2, 'No')])
    echo_peri_eff_location = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Pericardial effusion: Location on ECHO report', choices=[(1, 'RA'), (2, 'RV'), (3, 'LA'), (4, 'LA'), (5, 'LV'), (6, 'Other')])
    echo_peri_eff_loc_oth = models.TextField(help_text='', null=True, verbose_name='Pericardial effusion/Other: Specify on ECHO report', blank=True) # This field type is a guess
    echo_peri_eff_size = models.TextField(help_text='', null=True, verbose_name='Pericardial effusion/Size: Specify on ECHO report', blank=True) # This field type is a guess
    echo_rt_coronary_art = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Right coronary artery on ECHO report', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not well seen'), (4, 'Unknown/Not documented')])
    echo_lt_coronary_main = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Left coronary artery _ Main on ECHO report', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not well seen'), (4, 'Unknown/Not documented')])
    echo_lt_coronary_ant_desc = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Left coronary artery _ Anterior descending on ECHO report', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not well seen'), (4, 'Unknown/Not documented')])
    echo_lt_coronary_circum = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Left coronary artery _ Circumflex on ECHO report', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not well seen'), (4, 'Unknown/Not documented')])
    echo_anom_ca_origin = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Anomalous origin of coronary artery on ECHO report', choices=[(1, 'Both from R sinus'), (2, 'Both from L sinus'), (3, 'Single'), (4, 'Intramural'), (5, 'Other')])
    echo_anom_ca_origin_oth = models.TextField(help_text='', null=True, verbose_name='Anomalous origin CA/Other: Specify on ECHO report', blank=True) # This field type is a guess
    echo_coronary_ostia = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Coronary artery ostia on ECHO report', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not well seen'), (4, 'Not documented'), (5, 'Other')])
    echo_coronary_ostia_oth = models.TextField(help_text='', null=True, verbose_name='Coronary artery ostia Other - specify on ECHO report', blank=True) # This field type is a guess
    echo_aortic_arch = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Aortic Arch on ECHO report', choices=[(1, 'Normal branching'), (2, 'Right aortic arch'), (3, 'Aberrant Right subclavian'), (4, 'Double aortic arch'), (5, 'Other')])
    echo_aortic_arch_oth = models.TextField(help_text='', null=True, verbose_name='Aortic Arch other - Specify on ECHO report', blank=True) # This field type is a guess
    echo_number_pul_vein = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Number of pulmonary veins seen entering the left atrium on ECHO report', choices=[(1, '4 veins'), (2, '3 veins'), (3, '2 veins'), (4, '1 vein'), (5, 'Not well seen'), (6, 'Not documented')])
    echo_anom_pul_vein = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Anomalous pulmonary veins on ECHO report', choices=[(1, 'Yes'), (2, 'No'), (3, 'Not well seen')])
    echo_anom_pul_vein_spec = models.TextField(help_text='', null=True, verbose_name='Anomalous pulmonary veins: Specify on ECHO report', blank=True) # This field type is a guess
    echo_anom_ven_structure = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Anomalous venous structures on ECHO report', choices=[(1, 'Yes'), (2, 'No'), (3, 'Not well seen')])
    echo_anom_ven_location = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Anomalous venous structures location on ECHO report', choices=[(1, 'SVC'), (2, 'LSVC to CS'), (3, 'Bilateral SVC'), (4, 'Azygos vein continuation of interrupted inferior vena cava (IVC)'), (5, 'Other')])
    echo_anom_ven_loc_oth = models.TextField(help_text='', null=True, verbose_name='Anomalous venous structures location/Other: Specify on ECHO report', blank=True) # This field type is a guess
    echo_other_chd = models.TextField(help_text='', null=True, verbose_name='Other congenital heart disease or findings on ECHO report', blank=True) # This field type is a guess
    echo_comments_report = models.TextField(help_text='', null=True, verbose_name='Additional comments from ECHO report not listed above.', blank=True) # This field type is a guess
    echoresult = models.ForeignKey(EchoResult)

    class Meta:
	 db_table = 'echotest'


class EstResult(models.Model):
    est_done = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Exercise Stress Test done', choices=[(1, 'Yes'), (2, 'No')])
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'estresult'


class ExerciseStressTest(models.Model):
    est_enrollment = models.IntegerField(help_text='', null=True, verbose_name='How would you categorize the exercise stress test | Other test category', blank=True, choices=[(1, 'Initial test'), (2, 'Enrollment test'), (3, 'Post-enrollment test'), (4, 'Other')]) # This field type is a guess
    est_date = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Date of EST', blank=True)
    est_machine = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='EST performed on', choices=[(1, 'Stationary Bicycle'), (2, 'Ramp/Treadmill')])
    est_hr = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='EST Heart rate ', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Other')])
    est_hr_other = models.TextField(help_text='', null=True, verbose_name='EST Heart rate - Other: Specify', blank=True) # This field type is a guess
    est_hr_rest = models.CharField(help_text='', null=True, max_length=2000, verbose_name='EST Heart rate - rest', blank=True)
    est_hr_max = models.CharField(help_text='', null=True, max_length=2000, verbose_name='EST Heart rate - maximum', blank=True)
    est_hr_response = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='EST Heart rate response', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Other')])
    est_hr_response_oth = models.TextField(help_text='', null=True, verbose_name='EST Heart rate response Other - Specify', blank=True) # This field type is a guess
    est_bp = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='EST Blood pressure response', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Other')])
    est_bp_response = models.TextField(help_text='', null=True, verbose_name='EST Blood pressure response - Other: Specify', blank=True) # This field type is a guess
    est_bp_rest = models.CharField(help_text='', null=True, max_length=2000, verbose_name='EST Blood Pressure - rest', blank=True)
    est_bp_max = models.CharField(help_text='', null=True, max_length=2000, verbose_name='EST Blood Pressure - maximum', blank=True)
    est_o2_sat = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='EST Oxygen saturation', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Other')])
    est_o2_other = models.TextField(help_text='', null=True, verbose_name='EST Oxygen saturated - Other: Specify', blank=True) # This field type is a guess
    est_o2_sat_rest = models.CharField(help_text='', null=True, max_length=2000, verbose_name='EST Oxygen saturation - rest', blank=True)
    est_o2_sat_max = models.CharField(help_text='', null=True, max_length=2000, verbose_name='EST Oxygen saturation - maximum', blank=True)
    est_work_rate = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='EST Work rate', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Other')])
    est_work_rate_other = models.TextField(help_text='', null=True, verbose_name='EST Work rate - Other: Specify', blank=True) # This field type is a guess
    est_work_rate_watts = models.CharField(help_text='', null=True, max_length=2000, verbose_name='EST Work rate - Watts', blank=True)
    est_o2_consump = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='EST Oxygen consumption', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Other')])
    est_os_comsump_oth = models.TextField(help_text='', null=True, verbose_name='EST Oxygen consumption - Other: Specify', blank=True) # This field type is a guess
    est_os_comsump_rest_vo2 = models.CharField(help_text='', null=True, max_length=2000, verbose_name='EST Oxygen consumption - rest VO2 (L/min)', blank=True)
    est_os_comsump_max_vo2 = models.CharField(help_text='', null=True, max_length=2000, verbose_name='EST Oxygen consumption - max VO2 (L/min)', blank=True)
    est_os_comsump_max = models.CharField(help_text='', null=True, max_length=2000, verbose_name='EST Oxygen consumption - max (ml/kg/min)', blank=True)
    est_os_comsump_max_at = models.CharField(help_text='', null=True, max_length=2000, verbose_name='EST Oxygen consumption - Anerobic Threshold (AT)', blank=True)
    est_cardiac_output = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='EST Cardiac output', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Other')])
    est_cardiac_output_oth = models.TextField(help_text='', null=True, verbose_name='EST Cardiac output - Other: Specify', blank=True) # This field type is a guess
    est_cardiac_output_rest = models.CharField(help_text='', null=True, max_length=2000, verbose_name='EST Cardiac output - rest', blank=True)
    est_card_output_rest_ci = models.CharField(help_text='', null=True, max_length=2000, verbose_name='EST Cardiac output - rest - CI', blank=True)
    est_cardiac_output_max = models.CharField(help_text='', null=True, max_length=2000, verbose_name='EST Cardiac output - maximum', blank=True)
    est_card_output_max_mci = models.CharField(help_text='', null=True, max_length=2000, verbose_name='EST Cardiac output - maximum - MCI', blank=True)
    est_rhythm_other = models.TextField(help_text='', null=True, verbose_name='EST Rhythm - Other: Specify', blank=True) # This field type is a guess
    est_st_seg_change = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='EST ST segment changes', choices=[(1, 'None'), (2, 'Other')])
    est_st_seg_change_oth = models.TextField(help_text='', null=True, verbose_name='EST ST segment changes - Other: Specify', blank=True) # This field type is a guess
    est_symptom = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='EST Symptoms', choices=[(1, 'None'), (2, 'Other')])
    est_symptom_oth = models.TextField(help_text='', null=True, verbose_name='EST Symptoms - Other: Specify', blank=True) # This field type is a guess
    est_pul_func_rest = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='EST Pulmonary function (rest)', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Other')])
    est_pul_func_rest_oth = models.TextField(help_text='', null=True, verbose_name='EST Pulmonary function  (rest) - Other: Specify', blank=True) # This field type is a guess
    est_pul_func_reserve = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='EST Pulmonary function (reserve)', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Other')])
    est_pul_func_reserve_oth = models.TextField(help_text='', null=True, verbose_name='EST Pulmonary function (reserve) - Other: Specify', blank=True) # This field type is a guess
    est_pul_func_post = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='EST Pulmonary function (post)', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Other')])
    est_pul_func_post_oth = models.TextField(help_text='', null=True, verbose_name='EST Pulmonary function (post) - Other: Specify', blank=True) # This field type is a guess
    est_pul_func_ve = models.CharField(help_text='', null=True, max_length=2000, verbose_name='EST Pulmonary function - VE', blank=True)
    est_pul_func_rq = models.CharField(help_text='', null=True, max_length=2000, verbose_name='EST Pulmonary function - RQ', blank=True)
    est_summary = models.TextField(help_text='', null=True, verbose_name='EST Summary', blank=True) # This field type is a guess
    est_rhythm_summary = models.CharField(help_text='1, Sinus | 2, PAC-Premature Atrial Complexes | 3, PVC-Premature Ventricular Complexes | 4, PVC Couplets | 5, Ventricular Tachycardia | 6, Supraventricular Tachycardia | 7, Ventricular Fibrillation | 8, First Degree AV Block | 9, Second Degree AV Block (Mobitz Type I Wenckebach) | 10, Second Degree AV Block (Mobitz Type II) | 11, Third Degree (or Complete) AV Block | 12, Atrial Fibrillation | 13, Atrial Flutter | 14, Atrial Tachycardia | 15, Bradycardia | 16, Junctional rhythm | 17, Ventricular fibrillation | 18, Prolonged QT Interval  | 19, Wolff-Parkinson-White | 20, Torsades de pointes | 21, Other', null=True, max_length=2000, verbose_name='EST Rhythm', blank=True)
    estresult = models.ForeignKey(EstResult)

    class Meta:
	 db_table = 'exercisestresstest'


class estrhythm(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='EST Rhythm', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='EST Rhythm', choices=[(1, 'Sinus'), (2, 'PAC-Premature Atrial Complexes'), (3, 'PVC-Premature Ventricular Complexes'), (4, 'PVC Couplets'), (5, 'Ventricular Tachycardia'), (6, 'Supraventricular Tachycardia'), (7, 'Ventricular Fibrillation'), (8, 'First Degree AV Block'), (9, 'Second Degree AV Block (Mobitz Type I Wenckebach)'), (10, 'Second Degree AV Block (Mobitz Type II)'), (11, 'Third Degree (or Complete) AV Block'), (12, 'Atrial Fibrillation'), (13, 'Atrial Flutter'), (14, 'Atrial Tachycardia'), (15, 'Bradycardia'), (16, 'Junctional rhythm'), (17, 'Ventricular fibrillation'), (18, 'Prolonged QT Interval'), (19, 'Wolff-Parkinson-White'), (20, 'Torsades de pointes'), (21, 'Other')])
    exercisestresstest = models.ForeignKey(ExerciseStressTest)

    class Meta:
	 db_table = 'estrhythm'


class HolterResult(models.Model):
    hm_done = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Holter Monitor test done', choices=[(1, 'Yes'), (2, 'No')])
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'holterresult'


class Hm(models.Model):
    hm_enrollment = models.IntegerField(help_text='', null=True, verbose_name='How would you categorize the holter monitor test | Other test category', blank=True, choices=[(1, 'Initial test'), (2, 'Enrollment test'), (3, 'Post-enrollment test'), (4, 'Other')]) # This field type is a guess
    hm_date = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Date of Holter Monitor test', blank=True)
    hm_hr_total = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Holter Heart Rate Data: Total beats', blank=True)
    hm_hr_min = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Holter Heart Rate Data: Min HR (bpm)', blank=True)
    hm_hr_avg = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Holter Heart Rate Data: Avg HR (bpm)', blank=True)
    hm_hr_max = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Holter Heart Rate Data: Max HR (bpm)', blank=True)
    hm_hr_var_asdnn5 = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Holter HR Variability: ASDNN 5 (msec)', blank=True)
    hm_hr_var_sdnn5 = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Holter HR Variability: SDANN 5 (msec)', blank=True)
    hm_hr_var_sdnn = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Holter HR Variability: SDNN (msec)', blank=True)
    hm_hr_var_rmssd = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Holter HR Variability: RMSSD (msec)', blank=True)
    hm_ve_total_beat = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Holter Ventricular Ectopy: Total VE Beats (%)', blank=True)
    hm_ve_vent_run = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Holter Ventricular Ectopy: Vent Runs', blank=True)
    hm_ve_beat = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Holter Ventricular Ectopy: Beats', blank=True)
    hm_ve_long = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Holter Ventricular Ectopy: Longest', blank=True)
    hm_ve_fast = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Holter Ventricular Ectopy: Fastest (bpm)', blank=True)
    hm_ve_triplet = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Holter Ventricular Ectopy: Triplets (Events)', blank=True)
    hm_ve_couplet = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Holter Ventricular Ectopy: Couplets (Events)', blank=True)
    hm_ve_ront = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Holter Ventricular Ectopy: R on T', blank=True)
    hm_ve_bi_trigem = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Holter Ventricular Ectopy: Bi/Trigeminy (Beats)', blank=True)
    hm_ve_max_ve_min = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Holter Ventricular Ectopy: Max VE/Minute  (Beats)', blank=True)
    hm_ve_max_ve_hr = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Holter Ventricular Ectopy: Max VE/Hour  (Beats)', blank=True)
    hm_ve_mean_hour = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Holter Ventricular Ectopy: Mean VE/Hour', blank=True)
    hm_ve_ve_1000 = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Holter Ventricular Ectopy: VE/1000 (% of rhythm)', blank=True)
    hm_sve_total_beat = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Holter Supraventricular Ectopy: Total SVE Beats (%)', blank=True)
    hm_sve_svt_run = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Holter Supraventricular Ectopy: SVT Runs', blank=True)
    hm_sve_beat = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Holter Supraventricular Ectopy: Beats', blank=True)
    hm_sve_long = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Holter Supraventricular Ectopy: Longest', blank=True)
    hm_sve_fast = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Holter Supraventricular Ectopy: Fastest (bpm)', blank=True)
    hm_sve_atr_pair = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Holter Supraventricular Ectopy: Atrial Pairs (Events)', blank=True)
    hm_sve_long_rr = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Holter Supraventricular Ectopy: Longest R-R (Longest Pause/sec)', blank=True)
    hm_sve_max_sve_min = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Holter Supraventricular Ectopy: Max SVE/Minute (Beats)', blank=True)
    hm_sve_max_sve_hour = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Holter Supraventricular Ectopy: Max SVE/Hour (Beats)', blank=True)
    hm_sve_mean_sve_hour = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Holter Supraventricular Ectopy: Mean SVE/Hour (Beats)', blank=True)
    hm_sve_sve_1000 = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Holter Supraventricular Ectopy: SVE/1000 (% of rhythm)', blank=True)
    hm_summary = models.IntegerField(help_text='', null=True, verbose_name='Holter Monitor Interpretation: Heart rate interpretation', blank=True, choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Increased vagal tone'), (4, 'Increased sympathetic tone')]) # This field type is a guess
    hm_brady_percent = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Holter Monitor Interpretation: Bradycardia % of rhythm', blank=True)
    hm_avblock_percent = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Holter Monitor Interpretation: AV Block', choices=[(1, 'None'), (2, 'First degree'), (3, 'Second degree'), (4, 'Third degree')])
    hm_pr_interval = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Holter Monitor Interpretation: PR Interval', blank=True)
    hm_qrs_interval = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Holter Monitor Interpretation: QRS Interval', blank=True)
    hm_qtc_interval = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Holter Monitor Interpretation: QTc Interval', blank=True)
    hm_addit_info = models.TextField(help_text='', null=True, verbose_name='Holter Monitor Interpretation: Additional information ', blank=True) # This field type is a guess
    holterresult = models.ForeignKey(HolterResult)

    class Meta:
	 db_table = 'hm'


class CmriResult(models.Model):
    cmri_done = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Cardiac MRI done', choices=[(1, 'Yes'), (2, 'No')])
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'cmriresult'


class CardiacMri(models.Model):
    cmri_enrollment = models.IntegerField(help_text='', null=True, verbose_name='How would you categorize the cardiac MRI | Other test category', blank=True, choices=[(1, 'Initial test'), (2, 'Enrollment test'), (3, 'Post-enrollment test'), (4, 'Other')]) # This field type is a guess
    cmri_date = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Date of Cardiac MRI', blank=True)
    cmri_hypertrophy_loc = models.IntegerField(help_text='', null=True, verbose_name='Location of Hypertrophy | Location of Hypertrophy Other - Specify', blank=True, choices=[(1, 'Septal'), (2, 'Apical'), (3, 'Concentric'), (4, 'Other')]) # This field type is a guess
    cmri_summary = models.TextField(help_text='', null=True, verbose_name='Cardiac MRI Summary/Final report', blank=True) # This field type is a guess
    cmri_evidence_summary = models.CharField(help_text='6, None | 1, HCM- Hypertrophic cardiomyopathy | 2, LE- Myocardial late enhancement | 3, ARVD/C- Arrhythmogenic right ventricular dysplasia/cardiomyopathy | 4, LVNC- Left ventricular noncompaction | 5, DCM- Dilated cardiomyopathy', null=True, max_length=2000, verbose_name='Cardiac MRI Summary showed evidence of ', blank=True)
    cmriresult = models.ForeignKey(CmriResult)

    class Meta:
	 db_table = 'cardiacmri'


class cmrievidence(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Cardiac MRI Summary showed evidence of ', blank=True)
    value = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Cardiac MRI Summary showed evidence of ', choices=[(6, 'None'), (1, 'HCM- Hypertrophic cardiomyopathy'), (2, 'LE- Myocardial late enhancement'), (3, 'ARVD/C- Arrhythmogenic right ventricular dysplasia/cardiomyopathy'), (4, 'LVNC- Left ventricular noncompaction'), (5, 'DCM- Dilated cardiomyopathy')])
    cardiacmri = models.ForeignKey(CardiacMri)

    class Meta:
	 db_table = 'cmrievidence'


class CardiacCathProcedure(models.Model):
    ccath_done = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Cardiac catheterization done', choices=[(1, 'Yes'), (2, 'No')])
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'cardiaccathprocedure'


class CardiacCatherization(models.Model):
    ccath_enrollment = models.IntegerField(help_text='', null=True, verbose_name='How would you categorize the cardiac catherization | Other procedure category', blank=True, choices=[(1, 'Initial test'), (2, 'Enrollment test'), (3, 'Post-enrollment test'), (4, 'Other')]) # This field type is a guess
    ccath_date = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Date of Cardiac cathertization', blank=True)
    ccath_summary = models.TextField(help_text='', null=True, verbose_name='Cardiac catherization summary', blank=True) # This field type is a guess
    cardiaccathprocedure = models.ForeignKey(CardiacCathProcedure)

    class Meta:
	 db_table = 'cardiaccatherization'


class CardiacSurgery(models.Model):
    cardsurg_done = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Cardiac surgery done', choices=[(1, 'Yes'), (2, 'No')])
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'cardiacsurgery'


class CardiacSurgery2(models.Model):
    cardsurg_enrollment = models.IntegerField(help_text='', null=True, verbose_name='How would you categorize the cardiac surgery | Other procedure category', blank=True, choices=[(1, 'Initial test'), (2, 'Enrollment test'), (3, 'Post-enrollment test'), (4, 'Other')]) # This field type is a guess
    cardsurg_date = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Date of cardiac surgery', blank=True)
    cardsurg_name = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Name of cardiac surgery', blank=True)
    cardsurg_summary = models.TextField(help_text='', null=True, verbose_name='cardiac surgery summary', blank=True) # This field type is a guess
    cardiacsurgery = models.ForeignKey(CardiacSurgery)

    class Meta:
	 db_table = 'cardiacsurgery2'


