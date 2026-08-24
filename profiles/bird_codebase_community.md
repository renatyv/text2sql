---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:20:27.221922Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-d9ubgnvq/codebase_community.sqlite
schema: main
---

## Relationships

- "posts"."Id" ← "comments"."PostId", "postHistory"."PostId", "postLinks"."PostId", "postLinks"."RelatedPostId", "posts"."ParentId", "tags"."ExcerptPostId", "votes"."PostId"
- "users"."Id" ← "badges"."UserId", "comments"."UserId", "postHistory"."UserId", "posts"."LastEditorUserId", "posts"."OwnerUserId", "votes"."UserId"

# "badges"  (rows=79851)

columns:
"Id" int PK: unique identifier, 1..92240
"UserId" int FK: 25078 distinct, 2..55746, avg=18638.3, median=13651
"Name" text: 153 distinct
"Date" datetime: 65586 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| Id | 92240 | 67846 | 57347 |
| UserId | 12597 | 40620 | 5397 |
| Name | Autobiographer | Autobiographer | Notable Question |
| Date | 2014-09-14T02:31:28 | 2014-02-20T16:17:17 | 2013-11-07T09:17:02 |

# "comments"  (rows=174285)

columns:
"Id" int PK: unique identifier, 1..221292
"PostId" int FK: 1..115376, avg=54245.1
"Score" int: 0..90, avg=0.388398
"Text" text: profile metrics skipped
"CreationDate" datetime: profile metrics skipped
"UserId" int FK: nulls=2835, 3..55746, avg=12443.3
"UserDisplayName" text: nulls=171454

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| Id | 221292 | 190412 | 101498 |
| PostId | 115374 | 77846 | 51941 |
| Score | 1 | 0 | 1 |
| Text | @DilipSarwate indeed, in that case, the odds are even. | @NickCox If the models are nested, isn't looking at the change in $R^2$ equivalent to the partial F-test? | `What about an estimator which is an average over its closest k neighbors with the weights given to the neighbors decreasing with distance from the target point.` This is essentially inverse distance… |
| CreationDate | 2014-09-14T02:04:27 | 2014-05-15T01:30:01 | 2013-03-11T20:21:37 |
| UserId | 805 | 44451 | 1036 |
| UserDisplayName | null | null | null |

# "postHistory"  (rows=≈303155)

columns:
"Id" int PK UNIQ
"PostHistoryTypeId" int
"PostId" int FK
"RevisionGUID" text
"CreationDate" datetime
"UserId" int FK
"Text" text
"Comment" text
"UserDisplayName" text

indexes: none


# "postLinks"  (rows=11102)

columns:
"Id" int PK: unique identifier, 108..3356789
"CreationDate" datetime: 9450 distinct
"PostId" int FK: 7604 distinct, 4..115360, avg=60227.8, median=62679
"RelatedPostId" int FK: 5177 distinct, 1..115163, avg=32982.6, median=24077
"LinkTypeId" int: 1=10186, 3=916

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| Id | 3356789 | 1772083 | 3236567 |
| CreationDate | 2014-09-13T20:54:31 | 2012-08-30T08:09:51 | 2014-07-24T01:54:13 |
| PostId | 115360 | 35352 | 108928 |
| RelatedPostId | 60438 | 18603 | 35276 |
| LinkTypeId | 1 | 1 | 1 |

# "posts"  (rows=91966)

columns:
"Id" int PK UNIQ: unique identifier, 1..115378
"PostTypeId" int: 2=47755, 1=42912, 5=640, 4=639, 6=9, 3=6, 7=5, 1..7
"AcceptedAnswerId" int: all distinct, nulls=77269, 5..115345, avg=52239.7, median=49807
"CreaionDate" datetime: 91255 distinct
"Score" int: 130 distinct, -19..192, avg=2.79209, median=2
"ViewCount" int: 3714 distinct, nulls=49054, 1..175495, avg=565.835, median=128
"Body" text: 91732 distinct, nulls=220
"OwnerUserId" int FK: 21979 distinct, nulls=1392, -1..55746, avg=16544.9, median=11032
"LasActivityDate" datetime: 72647 distinct
"Title" text: 42877 distinct, nulls=49054
"Tags" text: 28528 distinct, nulls=49054
"AnswerCount" int: 31 distinct, nulls=49054, 0..136, avg=1.11272, median=1
"CommentCount" int: 39 distinct, 0..45, avg=1.89493, median=1
"FavoriteCount" int: 77 distinct, nulls=78723, 0..233, avg=2.54383, median=1
"LastEditorUserId" int FK: 6578 distinct, nulls=47361, -1..55733, avg=11923.2, median=7290
"LastEditDate" datetime: 44925 distinct, nulls=46934
"CommunityOwnedDate" datetime: 1938 distinct, nulls=89499
"ParentId" int FK: 29006 distinct, nulls=44211, 1..115375, avg=48358.3, median=44790
"ClosedDate" datetime: all distinct, nulls=90356
"OwnerDisplayName" text: 1613 distinct, nulls=89457
"LastEditorDisplayName" text: 59 distinct, nulls=91501

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| Id | 115378 | 20324 | 10598 |
| PostTypeId | 2 | 1 | 1 |
| AcceptedAnswerId | null | null | 14771 |
| CreaionDate | 2014-09-14T02:09:23 | 2011-12-28T17:32:36 | 2011-05-10T14:19:14 |
| Score | 0 | 1 | 7 |
| ViewCount | null | 246 | 397 |
| Body | <p>Decision trees are notoriously <strong>unstable</strong>: small perturbations in the training data can produce dramatically different trees, even though these trees can, and often do, perform abou… | <p>Background: I am developing a Python Statistics Framework, not because the ones out there are bad but because it will help me learn Python and Statistics. I have taken AP Stats, and read scattered… | <p>Various forms of the correlation, e.g., $r =  \\frac{\\Sigma_i x_i * y_i}{\\sigma_x  \\sigma_y}$ or $r = \\frac{\\Sigma_i (x_i-\\bar{x}) * (y_i-\\bar{y})}{\\sigma_x  \\sigma_y}$ are popular simila… |
| OwnerUserId | 7250 | 7711 | 2728 |
| LasActivityDate | 2014-09-14T02:09:23 | 2014-03-26T20:55:37 | 2011-08-24T19:32:05 |
| Title | null | How do I compare multiple arbitrary predictions for a given data set? | Correlation as a likelihood measure |
| Tags | null | <python><curve-fitting><nonparametric-bayes> | <probability><correlation><interpretation><likelihood-function> |
| AnswerCount | null | 2 | 2 |
| CommentCount | 0 | 1 | 2 |
| FavoriteCount | null | null | 2 |
| LastEditorUserId | null | 7711 | 2728 |
| LastEditDate | null | 2011-12-29T17:04:11 | 2011-05-10T14:30:19 |
| CommunityOwnedDate | null | null | null |
| ParentId | 115375 | null | null |
| ClosedDate | null | null | null |
| OwnerDisplayName | null | null | null |
| LastEditorDisplayName | null | null | null |

# "tags"  (rows=1032)

columns:
"Id" int PK: unique identifier, 1..1869
"TagName" text: all distinct
"Count" int: 272 distinct, 1..7244, avg=114.008, median=29
"ExcerptPostId" int FK: all distinct, nulls=436, 2331..114058, avg=54505.4, median=62654
"WikiPostId" int: all distinct, nulls=436, 2254..114057, avg=54504.3, median=62653

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| Id | 1869 | 1380 | 1246 |
| TagName | zero-inflated | deming-regression | big-data |
| Count | 1 | 6 | 28 |
| ExcerptPostId | null | null | 44122 |
| WikiPostId | null | null | 44121 |

# "users"  (rows=40325)

columns:
"Id" int PK UNIQ: unique identifier, -1..55747
"Reputation" int: 965 distinct, 1..87393, avg=84.0787, median=11
"CreationDate" datetime: 40315 distinct
"DisplayName" text: 35644 distinct
"LastAccessDate" datetime: 40287 distinct
"WebsiteUrl" text: 7787 distinct, nulls=32204
"Location" text: 2464 distinct, nulls=28634
"AboutMe" text: 9140 distinct, nulls=30946
"Views" int: 362 distinct, 0..20932, avg=8.90963, median=0
"UpVotes" int: 332 distinct, 0..11442, avg=6.58745, median=0
"DownVotes" int: 76 distinct, 0..1920, avg=0.260905, median=0
"AccountId" int: unique identifier, -1..5027354, avg=2e+06, median=1.8e+06
"Age" int: 70 distinct, nulls=32007, 13..94, avg=31.6426, median=30
"ProfileImageUrl" text: 13115 distinct, nulls=23846

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| Id | 55747 | 22202 | 18440 |
| Reputation | 1 | 11 | 101 |
| CreationDate | 2014-09-14T01:01:44 | 2013-03-19T01:01:07 | 2013-01-07T16:52:06 |
| DisplayName | Shivam Agrawal | vitasoy | palm3D |
| LastAccessDate | 2014-09-14T01:19:04 | 2013-03-23T01:21:43 | 2013-01-25T09:54:03 |
| WebsiteUrl | null | null | http://domain.invalid |
| Location | India | null | Belgium |
| AboutMe | <p>Maths Enthusiast </p>  | null | Computer scientist |
| Views | 0 | 16 | 0 |
| UpVotes | 0 | 0 | 0 |
| DownVotes | 0 | 0 | 0 |
| AccountId | 5027354 | 2512446 | 1953 |
| Age | null | null | 32 |
| ProfileImageUrl | https://lh4.googleusercontent.com/-ZsXhwVaFmiY/AAAAAAAAAAI/AAAAAAAAAqo/6UwTjH_MRIQ/photo.jpg | null | null |

# "votes"  (rows=38930)

columns:
"Id" int PK: unique identifier, 1..43538
"PostId" int FK: 8584 distinct, 1..16921, avg=4568.11, median=4372
"VoteTypeId" int: 2=33323, 5=3365, 1=1451, 3=444, 16=111, 15=72, 8=60, 9=59, 11=44, 10=1, 1..16
"CreationDate" date: 287 distinct
"UserId" int FK: 509 distinct, nulls=35505, 5..11954, avg=1433.24, median=850
"BountyAmount" int: 50=53, 100=30, 25=12, 150=3, 0=2, 200=1, nulls=38829, 0..200

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| Id | 43538 | 22361 | 9037 |
| PostId | 10202 | 4873 | 660 |
| VoteTypeId | 2 | 2 | 5 |
| CreationDate | 2011-05-01 | 2010-12-07 | 2010-09-12 |
| UserId | null | null | 1253 |
| BountyAmount | null | null | null |
