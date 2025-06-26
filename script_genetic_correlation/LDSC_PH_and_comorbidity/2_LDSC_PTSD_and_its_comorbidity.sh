#!/usr/bin/env bash

#conda env create --file environment.yml
#source activate ldsc

#############
#PH and other diseases
#############
#PH	PH
#Hypertension	HTN
#Hypercholesterolaemia	HCL
#Atrial fibrillation 	AF
#Diabetes	Diabetes
#Asthma	Asthma
#COPD	COPD
#Heart failure	HF
#CoronaryAtherosclerosis CA



PH=PH.sumstats.gz
HTN=HTN.sumstats.gz
HCL=HCL.sumstats.gz
AF=AF.sumstats.gz
Diabetes=T2D.sumstats.gz
Asthma=asthma.sumstats.gz
COPD=COPD.sumstats.gz
HF=HF.sumstats.gz
CA=CA.sumstats.gz

ldsc=~/scratch/Python_libs/ldsc/ldsc.py

#############################genetic correlation#####################
# PH 
$ldsc \
--rg $PH,$HTN,$HCL,$AF,$Diabetes,$Asthma,$COPD,$HF,$CA \
--ref-ld-chr ~/scratch/415_LDSC/0_resource_data/eur_w_ld_chr/ \
--w-ld-chr ~/scratch/415_LDSC/0_resource_data/eur_w_ld_chr/ \
--out PH_to_others 

$ldsc \
--rg $HTN,$HCL,$AF,$Diabetes,$Asthma,$COPD,$HF,$CA \
--ref-ld-chr ~/scratch/415_LDSC/0_resource_data/eur_w_ld_chr/ \
--w-ld-chr ~/scratch/415_LDSC/0_resource_data/eur_w_ld_chr/ \
--out HTN_to_others 

$ldsc \
--rg $HCL,$AF,$Diabetes,$Asthma,$COPD,$HF,$CA \
--ref-ld-chr ~/scratch/415_LDSC/0_resource_data/eur_w_ld_chr/ \
--w-ld-chr ~/scratch/415_LDSC/0_resource_data/eur_w_ld_chr/ \
--out HCL_to_others 

$ldsc \
--rg $AF,$Diabetes,$Asthma,$COPD,$HF,$CA \
--ref-ld-chr ~/scratch/415_LDSC/0_resource_data/eur_w_ld_chr/ \
--w-ld-chr ~/scratch/415_LDSC/0_resource_data/eur_w_ld_chr/ \
--out AF_to_others 

$ldsc \
--rg $Diabetes,$Asthma,$COPD,$HF,$CA \
--ref-ld-chr ~/scratch/415_LDSC/0_resource_data/eur_w_ld_chr/ \
--w-ld-chr ~/scratch/415_LDSC/0_resource_data/eur_w_ld_chr/ \
--out Diabetes_to_others 

$ldsc \
--rg $Asthma,$COPD,$HF,$CA \
--ref-ld-chr ~/scratch/415_LDSC/0_resource_data/eur_w_ld_chr/ \
--w-ld-chr ~/scratch/415_LDSC/0_resource_data/eur_w_ld_chr/ \
--out Asthma_to_others 

$ldsc \
--rg $COPD,$HF,$CA \
--ref-ld-chr ~/scratch/415_LDSC/0_resource_data/eur_w_ld_chr/ \
--w-ld-chr ~/scratch/415_LDSC/0_resource_data/eur_w_ld_chr/ \
--out COPD_to_others 

$ldsc \
--rg $HF,$CA \
--ref-ld-chr ~/scratch/415_LDSC/0_resource_data/eur_w_ld_chr/ \
--w-ld-chr ~/scratch/415_LDSC/0_resource_data/eur_w_ld_chr/ \
--out HF_to_others 

