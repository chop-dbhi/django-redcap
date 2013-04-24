class PriorGeneticTesting(models.Model):
    mito_combo_analysis${d}_loc = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Lab where $s combination mitochondrial analysis was performed', blank=True)

    class Meta:
	 db_table = 'PriorGeneticTesting'


class Deletion(models.Model):
    mito_combo_analysis${d}_sample = models.IntegerField(help_text='', null=True, verbose_name='Sample type for $s mitochondrial deletion analysis (from combined analysis $d1)', blank=True, choices=[(1, 'blood'), (2, 'urine'), (3, 'muscle'), (4, 'saliva'), (5, 'other')]) # This field type is a guess
    dc_deletion${d} = models.CharField(help_text='', null=True, max_length=2000, verbose_name='What was the $s disease causing deletion identified on $s2 mitochondrial deletion analysis (from $s1 combined analysis)?', blank=True)
    dc_deletion${d}_spec = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Other details for $s disease causing deletion on $s2 mitochondrial deletion analysis (from $s1 combined analysis)', blank=True)
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'Deletion'


class Variantofunknownsignificance(models.Model):
    vus${d} = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s variant of unknown significance on $s2 mitochondrial deletion analysis (from $s1 combined analysis)', blank=True)
    deletion = models.ForeignKey(Deletion)

    class Meta:
	 db_table = 'Variantofunknownsignificance'


class Panel(models.Model):
    targeted_mito_combo_panel${d}_type = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s panel performed (on $s1 combination analysis)?', blank=True)
    targeted_mito_combo_panel${d}_results = models.TextField(help_text='', null=True, verbose_name='Describe results of $s panel (on $s1 combined analysis)', blank=True) # This field type is a guess
    priorgenetictesting = models.ForeignKey(PriorGeneticTesting)

    class Meta:
	 db_table = 'Panel'


class Gene(models.Model):
    gene = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s gene on panel $d2 that contained mutation (on $s1 combined analysis)', blank=True)
    panel = models.ForeignKey(Panel)

    class Meta:
	 db_table = 'Gene'


class Mdnachange(models.Model):
    mdna_change = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s change in mDNA on $s3 gene on $s2 panel (on $s1 combined analysis)', blank=True)
    vus_mdna = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s variant of unknown significance on $s3 gene from $s2 panel (on $s1 combined analysis)', blank=True)
    panel = models.ForeignKey(Panel)

    class Meta:
	 db_table = 'Mdnachange'


