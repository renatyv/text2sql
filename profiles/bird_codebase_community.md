---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:55:25.354379Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-7u6ab_5n/codebase_community.sqlite
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
| Id | 92240 | 9999 | 15480 |
| UserId | 12597 | 5434 | 8817 |
| Name | Autobiographer | Autobiographer | Teacher |
| Date | 2014-09-14T02:31:28 | 2011-08-05T09:14:17 | 2012-01-29T23:22:32 |

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
| Id | 221292 | 130988 | 166963 |
| PostId | 115374 | 67816 | 85537 |
| Score | 1 | 0 | 0 |
| Text | @DilipSarwate indeed, in that case, the odds are even. | This isn't very effective for movie recommendation, since when user $i$ is asking for a movie to watch, your estimated ratings are all of the form $a_i + b_j$. Since $a_i$ is constant, your recommend… | @whuber DGP is data generating process. Z is the standard normal distribution. b is indeed the OLS as you mentioned. And I let $x$ denote a random vector of the $x_i$'s, but I'm not sure whether my n… |
| CreationDate | 2014-09-14T02:04:27 | 2013-08-20T03:31:42 | 2014-02-06T07:54:12 |
| UserId | 805 | 9964 | 31563 |
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
| Id | 3356789 | 477351 | 2638685 |
| CreationDate | 2014-09-13T20:54:31 | 2011-04-12T15:23:59 | 2013-09-13T20:28:22 |
| PostId | 115360 | 9475 | 69982 |
| RelatedPostId | 60438 | 3331 | 69898 |
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
| Id | 115378 | 26319 | 49927 |
| PostTypeId | 2 | 2 | 1 |
| AcceptedAnswerId | null | null | null |
| CreaionDate | 2014-09-14T02:09:23 | 2012-04-12T00:26:12 | 2013-02-13T18:41:30 |
| Score | 0 | 0 | 2 |
| ViewCount | null | null | 100 |
| Body | <p>Decision trees are notoriously <strong>unstable</strong>: small perturbations in the training data can produce dramatically different trees, even though these trees can, and often do, perform abou… | <p>For SAS, there is Ron Cody's <a href="http://rads.stackoverflow.com/amzn/click/1580256007" rel="nofollow">Data Cleaning Techniques using SAS Software</a>. There is a saying on SAS-L: "You can neve… | <p>Can someone provide a simple definition of what a binary explanatory variable is?  A description in simple terms would be ideal.  How would you recognize one?  </p>  |
| OwnerUserId | 7250 | 686 | 20812 |
| LasActivityDate | 2014-09-14T02:09:23 | 2012-04-12T00:26:12 | 2014-07-07T03:06:39 |
| Title | null | null | What is a binary explanatory variable? |
| Tags | null | null | <terminology><binary> |
| AnswerCount | null | null | 1 |
| CommentCount | 0 | 1 | 3 |
| FavoriteCount | null | null | null |
| LastEditorUserId | null | null | 7290 |
| LastEditDate | null | null | 2013-02-13T20:20:35 |
| CommunityOwnedDate | null | null | null |
| ParentId | 115375 | 26296 | null |
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
| Id | 1869 | 793 | 1308 |
| TagName | zero-inflated | zipf | mad |
| Count | 1 | 11 | 16 |
| ExcerptPostId | null | null | 30241 |
| WikiPostId | null | null | 30240 |

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
| Id | 55747 | 1064 | 5037 |
| Reputation | 1 | 101 | 21 |
| CreationDate | 2014-09-14T01:01:44 | 2010-08-23T16:20:03 | 2011-06-15T18:05:17 |
| DisplayName | Shivam Agrawal | S.Skov | tom |
| LastAccessDate | 2014-09-14T01:19:04 | 2010-12-01T19:35:45 | 2013-05-29T16:28:00 |
| WebsiteUrl | null | http://www.xteprofiler.com | null |
| Location | India | Denmark | null |
| AboutMe | <p>Maths Enthusiast </p>  | null | null |
| Views | 0 | 0 | 2 |
| UpVotes | 0 | 1 | 0 |
| DownVotes | 0 | 0 | 0 |
| AccountId | 5027354 | 48019 | 510043 |
| Age | null | null | null |
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
| Id | 43538 | 38147 | 7470 |
| PostId | 10202 | 3035 | 2252 |
| VoteTypeId | 2 | 2 | 2 |
| CreationDate | 2011-05-01 | 2011-03-28 | 2010-09-01 |
| UserId | null | null | null |
| BountyAmount | null | null | null |
