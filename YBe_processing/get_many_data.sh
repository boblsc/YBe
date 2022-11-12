#!/bin/bash
#SBATCH --job-name=YBe_process
#SBATCH --array=0-99
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=2GB

#SBATCH --time=24:00:00

#SBATCH --account=pi-lgrandi
#SBATCH --partition=xenon1t
#SBATCH --qos=xenon1t

#SBATCH --output=logs/logs-%J.txt
#SBATCH --error=logs/logs-%J.txt

SAMPLE_LIST=($(<run.list))
SAMPLE=${SAMPLE_LIST[${SLURM_ARRAY_TASK_ID}]}

module load singularity && singularity exec -B /project2,/dali,/scratch /project2/lgrandi/xenonnt/singularity-images/xenonnt-2022.09.1.simg python get_one.py ${SAMPLE}

