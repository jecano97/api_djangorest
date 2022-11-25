from django.db import models

# Create your models here.
class OMC23Nivel1(models.Model):
    idOmc23N1 = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idOmc23N1')
    codigo = models.CharField(max_length=9, null=False, unique=True)
    descriEng = models.CharField(max_length=100, null= False)
    descriSpa = models.CharField(max_length=110, null= False)
    definicionEng = models.CharField(max_length=200, null= False)
    definicionSpa = models.CharField(max_length=150, null= False)
    ejemploEng = models.CharField(max_length=300, null= False)
    ejemploSpa = models.CharField(max_length=400, null= False)
    anioReg = models.IntegerField(null=False)

    def __str__(self):
        return f'{self.codigo}: {self.descriSpa}'

    class Meta:
        db_table = "Omc23Nivel1"
        verbose_name = 'Omc23Nivel1'

class OMC23Nivel2(models.Model):
    idOmc23N2 = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idOmc23N2')
    numMat = models.IntegerField(blank= True, null= True)
    codigo = models.CharField(max_length=9, null=False, unique=True)
    descriEng = models.CharField(max_length=100, null= False)
    descriSpa = models.CharField(max_length=110,  null= False)
    definicionEng = models.CharField(max_length=300, blank= True, null= True)
    definicionSpa = models.CharField(max_length=470, blank= True, null= True)
    ejemploEng = models.CharField(max_length=300, blank= True, null= True)
    ejemploSpa = models.CharField(max_length=400, blank= True, null= True)
    regFinal = models.BooleanField(null= False)
    anioReg = models.IntegerField(null= False)
    regUsuario = models.BooleanField(blank=True,null= True)
    fk_Omc23N1 = models.ForeignKey(OMC23Nivel1, on_delete = models.CASCADE, db_column='fk_Omc23N1', verbose_name='Nivel 1')

    def __str__(self):
        return f'{self.codigo}: {self.descriSpa}'

    class Meta:
        db_table = "Omc23Nivel2"
        verbose_name = 'Omc23Nivel2'

class OMC23Nivel3(models.Model):
    idOmc23N3 = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idOmc23N3')
    numMat = models.IntegerField(blank= True, null= True)
    codigo = models.CharField(max_length=9, null=False, unique=True)
    descriEng = models.CharField(max_length=100, null=False)
    descriSpa = models.CharField(max_length=110, null=False)
    definicionEng = models.CharField(max_length=350, blank= True, null= True)
    definicionSpa = models.CharField(max_length=450, blank= True, null= True)
    ejemploEng = models.CharField(max_length=250, blank= True, null= True)
    ejemploSpa = models.CharField(max_length=300, blank= True, null= True)
    anioReg = models.IntegerField(null= False)
    regFinal = models.BooleanField(null= False)
    regUsuario = models.BooleanField(blank=True,null= True)
    fk_Omc23N2 = models.ForeignKey(OMC23Nivel2, on_delete=models.CASCADE, db_column='fk_Omc23N2', verbose_name='Nivel 2')

    def __str__(self):
        return f'{self.codigo}: {self.descriSpa}'
    
    class Meta:
        db_table = "Omc23Nivel3"
        verbose_name = 'Omc23Nivel3'

class OMC23Nivel4(models.Model):
    idOmc23N4 = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idOmc23N4')
    numMat = models.IntegerField(blank= True, null= True)
    codigo = models.CharField(max_length=11, null = False, unique=True)
    descriEng = models.CharField(max_length=100, null = False)
    descriSpa = models.CharField(max_length=110, null= False)
    definicionEng = models.CharField(max_length=350, blank= True, null= True)
    definicionSpa = models.CharField(max_length=400, blank= True, null= True)
    ejemploEng = models.CharField(max_length=300, blank= True, null= True)
    ejemploSpa = models.CharField(max_length=300, blank= True, null= True)
    anioReg = models.IntegerField(null= False)
    regFinal = models.BooleanField(null= False)
    regUsuario = models.BooleanField(blank=True,null= True)
    fk_Omc23N3 = models.ForeignKey(OMC23Nivel3, on_delete=models.CASCADE, db_column='fk_Omc23N3', verbose_name='Nivel 3')

    def __str__(self):
        return f'{self.codigo}: {self.descriSpa}'

    class Meta:
        db_table = "Omc23Nivel4"
        verbose_name = 'Omc23Nivel4'

class OMC23Nivel5(models.Model):
    idOmc23N5 = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idOmc23N5')
    numMat = models.IntegerField(blank= True, null= True)
    codigo = models.CharField(max_length=13, null=False, unique=True)
    descriEng = models.CharField(max_length=120, null=False)
    descriSpa = models.CharField(max_length=120, null=False)
    definicionEng = models.CharField(max_length=250, blank= True, null= True)
    definicionSpa = models.CharField(max_length=350, blank= True, null= True)
    ejemploEng = models.CharField(max_length=150, blank= True, null= True)
    ejemploSpa = models.CharField(max_length=150, blank= True, null= True)
    anioReg = models.IntegerField(null= False)
    regFinal = models.BooleanField(null= False)
    regUsuario = models.BooleanField(blank=True,null= True)
    fk_Omc23N4 = models.ForeignKey(OMC23Nivel4, on_delete=models.CASCADE, db_column='fk_Omc23N4', verbose_name='Nivel 4')

    def __str__(self):
        return f'{self.codigo}: {self.descriSpa}'

    class Meta:
        db_table = 'Omc23Nivel5'
        verbose_name = 'Omc23Nivel5'

class OMC23Nivel6(models.Model):
    idOmc23N6 = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idOmc23N6')
    numMat = models.IntegerField(blank= True, null= True)
    codigo = models.CharField(max_length=15, null=False, unique=True)
    descriEng = models.CharField(max_length=100, null= False)
    descriSpa = models.CharField(max_length=100, null= False)
    definicionEng = models.CharField(max_length=250, blank= True, null= True)
    definicionSpa = models.CharField(max_length=350, blank= True, null= True)
    ejemploEng = models.CharField(max_length=150, blank= True, null= True)
    ejemploSpa = models.CharField(max_length=150, blank= True, null= True)
    anioReg = models.IntegerField(null= False)
    regFinal = models.BooleanField(null= False)
    regUsuario = models.BooleanField(blank=True,null= True)
    fk_Omc23N5 = models.ForeignKey(OMC23Nivel5, on_delete=models.CASCADE, db_column='fk_Omc23N5', verbose_name='Nivel 5')

    def __str__(self):
        return f'{self.codigo}: {self.descriSpa}'

    class Meta:
        db_table = "Omc23Nivel6"
        verbose_name = 'Omc23Nivel6'