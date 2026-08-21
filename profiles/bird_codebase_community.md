---
generator: db-snooper
version: 0.0.33
generated_at_utc: 2026-08-21T12:31:01.374956Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-cosf85lh/codebase_community.sqlite
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
| Id | 92240 | 37159 | 37047 |
| UserId | 12597 | 11462 | 862 |
| Name | Autobiographer | Supporter | Popular Question |
| Date | 2014-09-14T02:31:28 | 2013-02-06T15:24:52 | 2013-02-05T03:11:27 |

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
| Id | 221292 | 71156 | 63263 |
| PostId | 115374 | 35473 | 32287 |
| Score | 1 | 0 | 0 |
| Text | @DilipSarwate indeed, in that case, the odds are even. | 1)I suspect, in some cases, the difference that is “different enough” is really unknown (maybe until a certain level). Would it be appropriate to make a table of [difference, significance]? Would it… | I can't know what you might intend. You can see definition of "factor analysis" by pointing on the tag (or read in Wikipedia). Does its meaning fit your case? |
| CreationDate | 2014-09-14T02:04:27 | 2012-09-01T00:07:28 | 2012-07-14T14:35:50 |
| UserId | 805 | null | 3277 |
| UserDisplayName | null | user13760 | null |

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
| Id | 3356789 | 102058 | 3038528 |
| CreationDate | 2014-09-13T20:54:31 | 2010-10-27T10:02:57 | 2014-05-12T20:59:28 |
| PostId | 115360 | 3989 | 97365 |
| RelatedPostId | 60438 | 4017 | 9751 |
| LinkTypeId | 1 | 1 | 3 |

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
| Id | 115378 | 44336 | 56450 |
| PostTypeId | 2 | 1 | 1 |
| AcceptedAnswerId | null | 44337 | null |
| CreaionDate | 2014-09-14T02:09:23 | 2012-11-24T16:35:57 | 2013-04-18T10:06:08 |
| Score | 0 | 0 | 0 |
| ViewCount | null | 758 | 71 |
| Body | <p>Decision trees are notoriously <strong>unstable</strong>: small perturbations in the training data can produce dramatically different trees, even though these trees can, and often do, perform abou… | <p>In <code>matlab</code>, classregtree can be used to implement classification and regression trees (CART) you can find this in <a href="http://www.mathworks.co.uk/help/stats/classregtree.html" rel=… | <p>I am developing network meta-analysis BUGS model that I will use to compare  Hazard Ratios in studies that assume Box Proportional Hazard model. </p>  <p>As input I am given pairs: (log HR, its st… |
| OwnerUserId | 7250 | 6875 | 10069 |
| LasActivityDate | 2014-09-14T02:09:23 | 2012-11-24T16:50:58 | 2013-05-01T07:49:23 |
| Title | null | Classification and regression trees (cart) | How to model repeated measures' results in meta-analysis? |
| Tags | null | <classification><matlab><cart> | <meta-analysis><bugs> |
| AnswerCount | null | 1 | 1 |
| CommentCount | 0 | 0 | 0 |
| FavoriteCount | null | null | null |
| LastEditorUserId | null | 686 | null |
| LastEditDate | null | 2012-11-24T16:46:41 | null |
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
| Id | 1869 | 419 | 1435 |
| TagName | zero-inflated | cointegration | pymc |
| Count | 1 | 108 | 54 |
| ExcerptPostId | null | 69311 | 46637 |
| WikiPostId | null | 69310 | 46636 |

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
| Id | 55747 | 20751 | 31977 |
| Reputation | 1 | 63 | 6 |
| CreationDate | 2014-09-14T01:01:44 | 2013-02-12T04:43:01 | 2013-10-28T02:12:59 |
| DisplayName | Shivam Agrawal | Rebecca | Malc |
| LastAccessDate | 2014-09-14T01:19:04 | 2014-09-03T21:10:01 | 2014-03-15T07:13:32 |
| WebsiteUrl | null | null | null |
| Location | India | null | Taipei City, Taiwan |
| AboutMe | <p>Maths Enthusiast </p>  | null | <p>I'm a French engineering student in robotics. I like control and programming stuffs.</p>  |
| Views | 0 | 6 | 3 |
| UpVotes | 0 | 4 | 0 |
| DownVotes | 0 | 0 | 0 |
| AccountId | 5027354 | 2355672 | 3026038 |
| Age | null | null | 23 |
| ProfileImageUrl | https://lh4.googleusercontent.com/-ZsXhwVaFmiY/AAAAAAAAAAI/AAAAAAAAAqo/6UwTjH_MRIQ/photo.jpg | null | http://i.stack.imgur.com/oEaaA.jpg |

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
| Id | 43538 | 6991 | 12220 |
| PostId | 10202 | 2169 | 3271 |
| VoteTypeId | 2 | 2 | 2 |
| CreationDate | 2011-05-01 | 2010-08-27 | 2010-10-04 |
| UserId | null | null | null |
| BountyAmount | null | null | null |
