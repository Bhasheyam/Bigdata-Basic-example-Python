CREATE DATABASE IF NOT EXISTS cs595;
use cs595;
CREATE TABLE IF NOT EXISTS cs595.salaries (
name STRING,
jobTitle STRING,
agencyID STRING, 
agency STRING,
hireDate STRING,
annualSalary DOUBLE,
grossPay DOUBLE)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t';

