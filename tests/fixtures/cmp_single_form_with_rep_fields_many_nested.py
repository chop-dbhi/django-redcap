from django.db import models

class Record(models.Model):

    class Meta:
	 db_table = 'record'


class PriorGeneticTesting(models.Model):
    mito_combo_analysis_loc = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Lab where combination mitochondrial analysis was performed', blank=True)
    record = models.ForeignKey(Record)

    class Meta:
	 db_table = 'priorgenetictesting'


class Deletion(models.Model):
    mito_combo_analysis_sample_summary = models.CharField(help_text='1, blood | 2, urine | 3, muscle | 4, saliva | 5, other', null=True, max_length=2000, verbose_name='Sample type for mitochondrial deletion analysis (from combined analysis $d1)', blank=True)
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'deletion'


class mitocomboanalysissample(models.Model):
    label = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Sample type for mitochondrial deletion analysis (from combined analysis $d1)', blank=True)
    value = models.IntegerField(help_text='', null=True, verbose_name='Sample type for mitochondrial deletion analysis (from combined analysis $d1)', blank=True, choices=[(1, 'blood'), (2, 'urine'), (3, 'muscle'), (4, 'saliva'), (5, 'other')]) # This field type is a guess
    deletion = models.ForeignKey(Deletion)

    class Meta:
	 db_table = 'mitocomboanalysissample'


class Deletion2(models.Model):
    dc_deletion = models.CharField(help_text='', null=True, max_length=2000, verbose_name='What was the disease causing deletion identified on mitochondrial deletion analysis (from combined analysis)?', blank=True)
    dc_deletion_spec = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Other details for disease causing deletion on mitochondrial deletion analysis (from combined analysis)', blank=True)
    deletion = models.ForeignKey(Deletion)

    class Meta:
	 db_table = 'deletion2'


class VariantOfUnknownSignificance(models.Model):
    vus = models.CharField(help_text='', null=True, max_length=2000, verbose_name='variant of unknown significance on mitochondrial deletion analysis (from combined analysis)', blank=True)
    deletion2 = models.ForeignKey(Deletion2)

    class Meta:
	 db_table = 'variantofunknownsignificance'


class Panel(models.Model):
    targeted_mito_combo_panel_type = models.CharField(help_text='', null=True, max_length=2000, verbose_name='panel performed (on combination analysis)?', blank=True)
    targeted_mito_combo_panel_results = models.TextField(help_text='', null=True, verbose_name='Describe results of panel (on combined analysis)', blank=True) # This field type is a guess
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'panel'


class Gene(models.Model):
    gene = models.CharField(help_text='', null=True, max_length=2000, verbose_name='gene on panel that contained mutation (on combined analysis)', blank=True)
    panel = models.ForeignKey(Panel)

    class Meta:
	 db_table = 'gene'


class MdnaChange(models.Model):
    mdna_change = models.CharField(help_text='', null=True, max_length=2000, verbose_name='change in mDNA on gene on panel (on combined analysis)', blank=True)
    gene = models.ForeignKey(Gene)

    class Meta:
	 db_table = 'mdnachange'


class MdnaVariantOfUnknownSignificance(models.Model):
    vus_mdna = models.CharField(help_text='', null=True, max_length=2000, verbose_name='variant of unknown significance on gene from panel (on combined analysis)', blank=True)
    panel = models.ForeignKey(Panel)

    class Meta:
	 db_table = 'mdnavariantofunknownsignificance'


