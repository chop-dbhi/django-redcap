class PriorGeneticTesting(models.Model):
    whole_mito_sequencing${d}_sample = models.IntegerField(help_text='', null=True, verbose_name='Sample type for $s whole mitochondrial genome sequencing', blank=True, choices=[(1, 'blood'), (2, 'urine'), (3, 'muscle'), (4, 'saliva'), (5, 'other')]) # This field type is a guess
    whole_mito_sequencing${d}_date = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year of $s whole mitochondrial genome sequencing', blank=True)
    whole_mito_sequencing${d}_loc = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Lab where $s whole mitochondrial genome sequencing was performed', blank=True)
    dc_mutation${d}_gene = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Gene in which $s disease causing mutation was located on $s1 whole mitochondrial sequencing', blank=True)
    dc_mutation${d}_mdna_level = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Change at mDNA level for $s disease causing mutation on $s1 whole mitochondrial sequencing', blank=True)
    vus${d}_mdna_level = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Change at mDNA level for $s variant of unknown significance on $s1 whole mitochondrial sequencing', blank=True)

    class Meta:
	 db_table = 'PriorGeneticTesting'


