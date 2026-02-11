# Lab 5 — Mini-MapReduce on EMR

## Files
- mapper.py — Python mapper (Hadoop streaming)
- reducer.py — Python reducer (Hadoop streaming)
- run_job.sh — example script to run the hadoop streaming job

## How to run (on EMR master node)
1. Place `mapper.py` and `reducer.py` in working directory and `chmod +x` them.
2. Upload dataset to HDFS:
   hdfs dfs -mkdir -p /user/hadoop/input
   hdfs dfs -put corpus.txt /user/hadoop/input/
3. Run job:
   hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
     -input /user/hadoop/input/ \
     -output /user/hadoop/output/ \
     -mapper mapper.py \
     -reducer reducer.py \
     -files mapper.py,reducer.py

## Experiments performed
- Scaling: ran on 2 core nodes and 4 core nodes; times recorded in `job_runtimes.log`.
- Input size: small vs large datasets; results in `experiment_results.txt`.
