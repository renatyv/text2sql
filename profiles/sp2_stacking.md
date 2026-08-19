---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T08:09:27.880617Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-ewtiyl9t/stacking.sqlite
schema: main
---

# eda

```sql
CREATE TABLE eda (name TEXT, version INTEGER, feature TEXT, type TEXT, "range" BLOB, drop_user INTEGER CHECK (drop_user IN (0, 1)), drop_correlation INTEGER CHECK (drop_correlation IN (0, 1)), target INTEGER CHECK (target IN (0, 1)));
```

## Rows

- total=1547

| column | latest | sample | sample |
|---|---|---|---|
| name | water quality 2 | oil spill | smoke detection iot |
| version | 3 | 1 | 2 |
| feature | pH | f_3 | NC0.5 |
| type | num | num | null |
| range | [5.35, 8.6] | [1.92, 1893.08] | null |
| drop_user | 0 | 0 | 1 |
| drop_correlation | 0 | 0 | 0 |
| target | 0 | 0 | 0 |

## Columns

- name: 20 distinct
- version: 1=321, 2=321, 3=321, 4=235, 5=213, 6=91, 7=38, 8=7, int 1..8
- feature: 335 distinct
- type: "num"=1036, "cat"=205, nulls=306
- range: nulls=306
- drop_user: 0=1342, 1=205
- drop_correlation: 0=1396, 1=151
- target: 0=1446, 1=101


# feature_importance

```sql
CREATE TABLE feature_importance (name TEXT, version INTEGER, step INTEGER, feature TEXT, importance NUMERIC);
```

## Rows

- total=2887

| column | latest | sample | sample |
|---|---|---|---|
| name | water quality 2 | iris | Hospital Mortality Prediction |
| version | 3 | 6 | 5 |
| step | 3 | 2 | 1 |
| feature | pH | SepalLengthCm | glucose |
| importance | 0.1067193676 | 0.7279693487 | 0.0126422250 |

## Columns

- name: 20 distinct
- version: 2=590, 1=586, 3=586, 4=454, 5=409, 6=169, 7=78, 8=15, int 1..8
- step: 1=1241, 2=1241, 3=405, int 1..3
- feature: 294 distinct
- importance: 2266 distinct, num -4.7142857143..3.4285714286
  - stats: average=0.104953, median=0.0288298


# model

```sql
CREATE TABLE model (name TEXT, version INTEGER, step INTEGER CHECK (step IN (1, 2, 3)), L1_model TEXT CHECK (L1_model IN ("regression", "tree")));
```

## Rows

- total=303

| column | latest | sample | sample |
|---|---|---|---|
| name | water quality 2 | Hospital Mortality Prediction | iris |
| version | 3 | 2 | 2 |
| step | 3 | 2 | 3 |
| L1_model | tree | regression | regression |

## Columns

- name: 20 distinct
- version: 1=60, 2=60, 3=60, 4=48, 5=42, 6=18, 7=12, 8=3, int 1..8
- step: 1=101, 2=101, 3=101, int 1..3
- L1_model: "regression"=213, "tree"=90


# model_importance

```sql
CREATE TABLE model_importance (name TEXT, version INTEGER, step INTEGER, model TEXT, importance NUMERIC);
```

## Rows

- total=2567

| column | latest | sample | sample |
|---|---|---|---|
| name | water quality 2 | lithium ion batteries | smoke detection iot |
| version | 3 | 3 | 4 |
| step | 3 | 1 | 1 |
| model | RFCG | MLPC1 | DTCG |
| importance | 0.1720506178 | 0.0071998507 | 0.0001172276 |

## Columns

- name: 20 distinct
- version: 1=537, 3=518, 2=477, 4=377, 5=351, 6=172, 7=107, 8=28, int 1..8
- step: 1=1661, 3=454, 2=452, int 1..3
- model: 45 distinct
- importance: 1897 distinct, num 0e-10..1.0000000000
  - stats: average=0.118037, median=0.0485232


# model_score

```sql
CREATE TABLE model_score (name TEXT, version INTEGER, step INTEGER, model TEXT, train_score NUMERIC, test_score NUMERIC);
```

## Rows

- total=2872

| column | latest | sample | sample |
|---|---|---|---|
| name | water quality 2 | PSS3E5 | water quality |
| version | 3 | 3 | 3 |
| step | 3 | 2 | 1 |
| model | Stack | LOGRLCV | LOGRLCV |
| train_score | 0.7664974619 | 0.5896032832 | 0.8493801653 |
| test_score | 0.6530612245 | 0.5663474692 | 0.8487603306 |

## Columns

- name: 20 distinct
- version: 1=597, 3=578, 2=537, 4=425, 5=395, 6=190, 7=119, 8=31, int 1..8
- step: 1=1762, 2=555, 3=555, int 1..3
- model: 46 distinct
- train_score: 613 distinct, num -85292809.8023026735..1.0000000000
  - stats: average=-59119, median=0.959412
- test_score: 568 distinct, num -65597190.8645909131..1.0000000000
  - stats: average=-48920.8, median=0.82587


# problem

```sql
CREATE TABLE problem (name TEXT NOT NULL UNIQUE, path TEXT, type TEXT CHECK (type IN ("classification", "regression")), target TEXT, PRIMARY KEY (name));
```

## Rows

- total=20

| column | latest | sample | sample |
|---|---|---|---|
| name | water quality 2 | diabetes | Delaney solubility |
| path | https://www.kaggle.com/datasets/saraharsh/water-quality | https://www.kaggle.com/datasets/akshaydattatraykhare/diabetes-dataset | https://www.kaggle.com/datasets/prashanthbairu/delaney-solubility-with-descriptors |
| type | classification | classification | regression |
| target | Water_Quality | Outcome | logS |

## Columns

- name: unique identifier
- path: all distinct
- type: "classification"=14, "regression"=6
- target: "I"=2, "target"=2, "Class"=1, "Concrete compressive strength(MPa, megapascals) "=1, "Crystal System"=1, "Dataset"=1, "Fire Alarm"=1, "LUNG_CANCER"=1, "Outcome"=1, "PCOS (Y/N)"=1, "Power Generated"=1, "Water_Quality"=1, "chf_exp [MW/m2]"=1, "is_safe"=1, "logS"=1, "outcome"=1, "quality"=1, "variety"=1


# solution

```sql
CREATE TABLE solution (name TEXT, version INTEGER, correlation NUMERIC, nb_model INTEGER, nb_feature INTEGER, score NUMERIC, test_size NUMERIC, resampling INTEGER CHECK (resampling IN (0, 1)) DEFAULT (0));
```

## Rows

- total=101

| column | latest | sample | sample |
|---|---|---|---|
| name | water quality 2 | smoke detection iot | iris |
| version | 3 | 1 | 6 |
| correlation | 0.7500000000 | 0.7500000000 | 0.7500000000 |
| nb_model | 5 | 5 | 5 |
| nb_feature | 5 | 5 | 5 |
| score | 0.7000000000 | 0.7000000000 | 0.7000000000 |
| test_size | 0.3300000000 | 0.3300000000 | 0.3300000000 |
| resampling | 0 | 0 | 0 |

## Columns

- name: 20 distinct
- version: 1=20, 2=20, 3=20, 4=16, 5=14, 6=6, 7=4, 8=1, int 1..8
- correlation: 0.7500000000=101
- nb_model: 5=50, 3=27, 7=12, 2=5, 4=4, 6=3, int 2..7
- nb_feature: 5=83, 3=8, 4=5, 7=2, 6=1, 8=1, 10=1, int 3..10
- score: 0.7000000000=69, 0.8000000000=8, 0.5500000000=5, 0.9000000000=5, 0.7500000000=4, 0.8500000000=4, 0.4500000000=3, 0.4000000000=2, 0.5000000000=1, num 0.4000000000..0.9000000000
- test_size: 0.3300000000=90, 0.2900000000=10, 0.3000000000=1, num 0.2900000000..0.3300000000
- resampling: 0=75, 1=26


# solution_ext

```sql
CREATE VIEW solution_ext AS select name, version, L1_model
from model
group by name, version, L1_model
order by name;
```

## Rows

- total=101

| column | latest | sample | sample |
|---|---|---|---|
| name | water quality 2 | concrete | lithium ion batteries |
| version | 3 | 5 | 3 |
| L1_model | tree | tree | regression |

## Columns

- name: 20 distinct
- version: 1=20, 2=20, 3=20, 4=16, 5=14, 6=6, 7=4, 8=1, int 1..8
- L1_model: "regression"=71, "tree"=30


# stack_ok

```sql
CREATE VIEW stack_ok AS select A.name, A.version, A.step, C.L1_model, 'strong' as status
        from (select name, version, step, max(test_score) as max_test_score 
              from model_score where model not in ('Stack') 
              group by name, version, step) as A
        inner join 
             (select name, version, step, test_score as stack_score 
              from model_score 
              where model = 'Stack') as B
        on A.name = B.name
        and A.version = B.version
        and A.step = B.step
        inner join 
            model as C
            on A.name = C.name
            and A.version = C.version
        where A.max_test_score < B.stack_score
        group by A.name, A.version, A.step
union all
select A.name, A.version, A.step, C.L1_model, 'soft' as status
        from (select name, version, step, max(test_score) as max_test_score 
              from model_score where model not in ('Stack') 
              group by name, version, step) as A
        inner join 
             (select name, version, step, test_score as stack_score 
              from model_score 
              where model = 'Stack') as B
        on A.name = B.name
        and A.version = B.version
        and A.step = B.step
        inner join 
            model as C
            on A.name = C.name
            and A.version = C.version
        where A.max_test_score = B.stack_score
        group by A.name, A.version, A.step
order by A.name, A.version;
```

## Rows

- total=139

| column | latest | sample | sample |
|---|---|---|---|
| name | water quality 2 | diabetes | lithium ion batteries |
| version | 2 | 3 | 1 |
| step | 3 | 1 | 2 |
| L1_model | regression | regression | regression |
| status | soft | strong | soft |

## Columns

- name: "Solar Power Generation"=16, "kindey stone urine analysis"=16, "oil spill"=15, "PSS3E5"=14, "Franck-Hertz"=12, "Tunnel diode"=11, "Delaney solubility"=9, "concrete"=7, "Critical Heat Flux"=6, "survey lung cancer"=6, "diabetes"=5, "smoke detection iot"=5, "iris"=4, "lithium ion batteries"=4, "Hospital Mortality Prediction"=3, "PCOS"=3, "Liver disease prediction"=1, "water quality"=1, "water quality 2"=1
- version: 2=28, 1=26, 3=26, 5=23, 4=18, 6=9, 7=9, int 1..7
- step: 3=53, 2=45, 1=41, int 1..3
- L1_model: "regression"=114, "tree"=25
- status: "strong"=92, "soft"=47


# stack_ok_score

```sql
CREATE VIEW stack_ok_score AS select distinct test_score_1.name, test_score_1.version, test_score_1.score_1, test_score_2.score_2, test_score_3.score_3
from
(select A.name, A.version, A.test_score as score_1
 from model_score as A
 inner join stack_ok as B
 on A.name = B.name
 and A.version = B.version
 where A.model = 'Stack'
 and A.step = 1) as test_score_1
inner join
(select A.name, A.version, A.test_score as score_2
 from model_score as A
 inner join stack_ok as B
 on A.name = B.name
 and A.version = B.version
 where A.model = 'Stack'
 and A.step = 2) as test_score_2
 on test_score_1.name = test_score_2.name
 and test_score_1.version = test_score_2.version
inner join
(select A.name, A.version, A.test_score as score_3
 from model_score as A
 inner join stack_ok as B
 on A.name = B.name
 and A.version = B.version
 where A.model = 'Stack'
 and A.step = 3) as test_score_3
 on test_score_1.name = test_score_3.name
 and test_score_1.version = test_score_3.version;
```

## Rows

- total=64

| column | latest | sample | sample |
|---|---|---|---|
| name | water quality 2 | Solar Power Generation | smoke detection iot |
| version | 2 | 6 | 5 |
| score_1 | 0.7857142857 | 0.9246534253 | 0.9999032320 |
| score_2 | 0.7755102041 | 0.9253691157 | 0.9997580801 |
| score_3 | 0.7755102041 | 0.9220322879 | 0.9999516160 |

## Columns

- name: "Solar Power Generation"=7, "kindey stone urine analysis"=6, "Franck-Hertz"=5, "PSS3E5"=5, "concrete"=5, "oil spill"=5, "Tunnel diode"=4, "smoke detection iot"=4, "survey lung cancer"=4, "Critical Heat Flux"=3, "Delaney solubility"=3, "diabetes"=3, "Hospital Mortality Prediction"=2, "iris"=2, "lithium ion batteries"=2, "Liver disease prediction"=1, "PCOS"=1, "water quality"=1, "water quality 2"=1
- version: 2=15, 1=13, 3=11, 5=10, 4=7, 6=4, 7=4, int 1..7
- score_1: 40 distinct, num 0.5759233926..1.0000000000
  - stats: average=0.895417, median=0.924653
- score_2: 49 distinct, num 0.3962737972..1.0000000000
  - stats: average=0.868297, median=0.925238
- score_3: 52 distinct, num 0.3962737972..1.0000000000
  - stats: average=0.872695, median=0.896136
