Library project pipeline README file.

The pipeline for this project is triggered whenever new data files are received.

It takes the source data using Fabric pipelines and loads it into the staging area.

The next step in the pipeline validates and cleans up the data. The validation checks include searching for NULL values, duplicate checking,
date formats, checking date types are in the expected format.

Once the clean-up steps have been run, the final validation steps and row counts are carried out.

Data is then loaded into the aggregated and summary tables for visual analytics and Power BI reporting.