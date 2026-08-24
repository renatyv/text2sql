---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:59:28.731475Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-36qn47co/stacking.sqlite
schema: main
---

# "eda"  (rows=1547)

columns:
"name" text: 20 distinct
"version" int: 1=321, 2=321, 3=321, 4=235, 5=213, 6=91, 7=38, 8=7, 1..8
"feature" text: 335 distinct
"type" text: "num"=1036, "cat"=205, nulls=306
"range" bytes→text: nulls=306
"drop_user" int: 0=1342, 1=205
"drop_correlation" int: 0=1396, 1=151
"target" int: 0=1446, 1=101

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| name | water quality 2 | oil spill | PCOS |
| version | 3 | 1 | 1 |
| feature | pH | f_49 | AMH(ng/mL) |
| type | num | null | num |
| drop_user | 0 | 1 | 0 |
| drop_correlation | 0 | 0 | 0 |
| target | 0 | 0 | 0 |

# "feature_importance"  (rows=2887)

columns:
"name" text: 20 distinct
"version" int: 2=590, 1=586, 3=586, 4=454, 5=409, 6=169, 7=78, 8=15, 1..8
"step" int: 1=1241, 2=1241, 3=405, 1..3
"feature" text: 294 distinct
"importance" numeric: 2266 distinct, -4.7142857143..3.4285714286, avg=0.104953, median=0.0288298

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| name | water quality 2 | survey lung cancer | Solar Power Generation |
| version | 3 | 4 | 5 |
| step | 3 | 1 | 2 |
| feature | pH | YELLOW_FINGERS | Sky Cover |
| importance | 0.106719 | 0.0418376 | 0.0422912 |

# "model"  (rows=303)

columns:
"name" text: 20 distinct
"version" int: 1=60, 2=60, 3=60, 4=48, 5=42, 6=18, 7=12, 8=3, 1..8
"step" int: 1=101, 2=101, 3=101, 1..3
"L1_model" text: "regression"=213, "tree"=90

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| name | water quality 2 | Solar Power Generation | Critical Heat Flux |
| version | 3 | 4 | 3 |
| step | 3 | 2 | 1 |
| L1_model | tree | regression | tree |

# "model_importance"  (rows=2567)

columns:
"name" text: 20 distinct
"version" int: 1=537, 3=518, 2=477, 4=377, 5=351, 6=172, 7=107, 8=28, 1..8
"step" int: 1=1661, 3=454, 2=452, 1..3
"model" text: 45 distinct
"importance" numeric: 1897 distinct, 0..1, avg=0.118037, median=0.0485232

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| name | water quality 2 | Delaney solubility | lithium ion batteries |
| version | 3 | 2 | 1 |
| step | 3 | 1 | 3 |
| model | RFCG | MLPR2 | KERC |
| importance | 0.172051 | 0.000280517 | 0.256491 |

# "model_score"  (rows=2872)

columns:
"name" text: 20 distinct
"version" int: 1=597, 3=578, 2=537, 4=425, 5=395, 6=190, 7=119, 8=31, 1..8
"step" int: 1=1762, 2=555, 3=555, 1..3
"model" text: 46 distinct
"train_score" numeric: 613 distinct, -85292809.8023..1, avg=-59119, median=0.959412
"test_score" numeric: 568 distinct, -65597190.8646..1, avg=-48920.8, median=0.82587

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| name | water quality 2 | Hospital Mortality Prediction | Pumpkin Seeds |
| version | 3 | 3 | 3 |
| step | 3 | 3 | 1 |
| model | Stack | GPCQ | RFCE |
| train_score | 0.766497 | 1 | 1 |
| test_score | 0.653061 | 0.848485 | 0.878788 |

# "problem"  (rows=20)

columns:
"name" text PK UNIQ: unique identifier
"path" text: all distinct
"type" text: "classification"=14, "regression"=6
"target" text: "I"=2, "target"=2, "Class"=1, "Concrete compressive strength(MPa, megapascals) "=1, "Crystal System"=1, "Dataset"=1, "Fire Alarm"=1, "LUNG_CANCER"=1, "Outcome"=1, "PCOS (Y/N)"=1, "Power Generated"=1, "Water_Quality"=1, "chf_exp [MW/m2]"=1, "is_safe"=1, "logS"=1, "outcome"=1, "quality"=1, "variety"=1

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| name | water quality 2 | Solar Power Generation | Hospital Mortality Prediction |
| path | https://www.kaggle.com/datasets/saraharsh/water-quality | https://www.kaggle.com/datasets/vipulgote4/solar-power-generation | https://www.kaggle.com/datasets/saurabhshahane/in-hospital-mortality-prediction |
| type | classification | regression | classification |
| target | Water_Quality | Power Generated | outcome |

# "solution"  (rows=101)

columns:
"name" text: 20 distinct
"version" int: 1=20, 2=20, 3=20, 4=16, 5=14, 6=6, 7=4, 8=1, 1..8
"correlation" numeric: 0.75=101
"nb_model" int: 5=50, 3=27, 7=12, 2=5, 4=4, 6=3, 2..7
"nb_feature" int: 5=83, 3=8, 4=5, 7=2, 6=1, 8=1, 10=1, 3..10
"score" numeric: 0.7=69, 0.8=8, 0.55=5, 0.9=5, 0.75=4, 0.85=4, 0.45=3, 0.4=2, 0.5=1, 0.4..0.9
"test_size" numeric: 0.33=90, 0.29=10, 0.3=1, 0.29..0.33
"resampling" int: 0=75, 1=26

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| name | water quality 2 | survey lung cancer | kindey stone urine analysis |
| version | 3 | 3 | 4 |
| correlation | 0.75 | 0.75 | 0.75 |
| nb_model | 5 | 7 | 3 |
| nb_feature | 5 | 5 | 5 |
| score | 0.7 | 0.7 | 0.85 |
| test_size | 0.33 | 0.29 | 0.33 |
| resampling | 0 | 1 | 1 |

# "solution_ext"  (rows=101)

```sql
CREATE VIEW solution_ext AS select name, version, L1_model
from model
group by name, version, L1_model
order by name;
```

columns:
"name" text: 20 distinct
"version" int: 1=20, 2=20, 3=20, 4=16, 5=14, 6=6, 7=4, 8=1, 1..8
"L1_model" text: "regression"=71, "tree"=30

samples:
| column | latest | sample | sample |
|---|---|---|---|
| name | water quality 2 | Tunnel diode | water quality 2 |
| version | 3 | 1 | 3 |
| L1_model | tree | regression | tree |

# "stack_ok"  (rows=139)

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

columns:
"name" text: "Solar Power Generation"=16, "kindey stone urine analysis"=16, "oil spill"=15, "PSS3E5"=14, "Franck-Hertz"=12, "Tunnel diode"=11, "Delaney solubility"=9, "concrete"=7, "Critical Heat Flux"=6, "survey lung cancer"=6, "diabetes"=5, "smoke detection iot"=5, "iris"=4, "lithium ion batteries"=4, "Hospital Mortality Prediction"=3, "PCOS"=3, "Liver disease prediction"=1, "water quality"=1, "water quality 2"=1
"version" int: 2=28, 1=26, 3=26, 5=23, 4=18, 6=9, 7=9, 1..7
"step" int: 3=53, 2=45, 1=41, 1..3
"L1_model" text: "regression"=114, "tree"=25
"status" text: "strong"=92, "soft"=47

samples:
| column | latest | sample | sample |
|---|---|---|---|
| name | water quality 2 | kindey stone urine analysis | Solar Power Generation |
| version | 2 | 2 | 2 |
| step | 3 | 3 | 3 |
| L1_model | regression | regression | regression |
| status | soft | soft | strong |

# "stack_ok_score"  (rows=64)

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

columns:
"name" text: "Solar Power Generation"=7, "kindey stone urine analysis"=6, "Franck-Hertz"=5, "PSS3E5"=5, "concrete"=5, "oil spill"=5, "Tunnel diode"=4, "smoke detection iot"=4, "survey lung cancer"=4, "Critical Heat Flux"=3, "Delaney solubility"=3, "diabetes"=3, "Hospital Mortality Prediction"=2, "iris"=2, "lithium ion batteries"=2, "Liver disease prediction"=1, "PCOS"=1, "water quality"=1, "water quality 2"=1
"version" int: 2=15, 1=13, 3=11, 5=10, 4=7, 6=4, 7=4, 1..7
"score_1" numeric: 40 distinct, 0.5759233926..1, avg=0.895417, median=0.924653
"score_2" numeric: 49 distinct, 0.3962737972..1, avg=0.868297, median=0.925238
"score_3" numeric: 52 distinct, 0.3962737972..1, avg=0.872695, median=0.896136

samples:
| column | latest | sample | sample |
|---|---|---|---|
| name | water quality 2 | kindey stone urine analysis | Solar Power Generation |
| version | 2 | 4 | 5 |
| score_1 | 0.785714 | 1 | 0.924653 |
| score_2 | 0.77551 | 1 | 0.925106 |
| score_3 | 0.77551 | 1 | 0.885477 |
