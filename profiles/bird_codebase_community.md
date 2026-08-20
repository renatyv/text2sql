---
generator: db-snooper
version: 0.0.31
generated_at_utc: 2026-08-20T17:25:52.069089Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-tjj92u_g/codebase_community.sqlite
schema: main
---

## Relationships

- "posts"."Id" ← "comments"."PostId", "postHistory"."PostId", "postLinks"."PostId", "postLinks"."RelatedPostId", "posts"."ParentId", "tags"."ExcerptPostId", "votes"."PostId"
- "users"."Id" ← "badges"."UserId", "comments"."UserId", "postHistory"."UserId", "posts"."LastEditorUserId", "posts"."OwnerUserId", "votes"."UserId"

# "badges"  (rows=79851)

columns:
"Id" int PK: unique identifier, 1..92240, avg=45430.1, median=45939
"UserId" int FK: 25078 distinct, 2..55746, avg=18638.3, median=13651
"Name" text: 153 distinct
"Date" datetime: 65586 distinct

indexes: none
fk: "UserId"→"users"."Id"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| Id | 92240 | 7119 | 41687 |
| UserId | 12597 | 4137 | 16908 |
| Name | Autobiographer | Student | Student |
| Date | 2014-09-14T02:31:28 | 2011-04-13T00:05:59 | 2013-04-02T21:57:42 |

# "comments"  (rows=174285)

columns:
"Id" int PK: unique identifier, 1..221292, avg=107698
"PostId" int FK: 1..115376, avg=54245.1
"Score" int: 0..90, avg=0.388398
"Text" text: profile metrics skipped
"CreationDate" datetime: profile metrics skipped
"UserId" int FK: nulls=2835, 3..55746, avg=12443.3
"UserDisplayName" text: nulls=171454

indexes: none
fk: "PostId"→"posts"."Id", "UserId"→"users"."Id"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| Id | 221292 | 145958 | 109858 |
| PostId | 115374 | 74806 | 57118 |
| Score | 1 | 0 | 6 |
| Text | @DilipSarwate indeed, in that case, the odds are even. | @gung Interesting read and certainly a place I can start.  Thanks. | The null hypothesis is not always the same. The null hypothesis is just an alternative "boring" hypothesis that you compare to your "interesting" hypothesis, to see whether the data supports one over the other. Actually, "no difference" is actually a bad null hypothesis, since you know a-priori it's false. Better is "the difference is below some threshold of me caring". |
| CreationDate | 2014-09-14T02:04:27 | 2013-11-07T01:04:10 | 2013-04-24T20:28:18 |
| UserId | 805 | 32428 | 13669 |
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
fk: "UserId"→"users"."Id", "PostId"→"posts"."Id"


# "postLinks"  (rows=11102)

columns:
"Id" int PK: unique identifier, 108..3356789, avg=2.32683e+06, median=2.56431e+06
"CreationDate" datetime: 9450 distinct
"PostId" int FK: 7604 distinct, 4..115360, avg=60227.8, median=62679
"RelatedPostId" int FK: 5177 distinct, 1..115163, avg=32982.6, median=24077
"LinkTypeId" int: 1=10186, 3=916

indexes: none
fk: "RelatedPostId"→"posts"."Id", "PostId"→"posts"."Id"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| Id | 3356789 | 1978849 | 1724802 |
| CreationDate | 2014-09-13T20:54:31 | 2012-12-13T14:08:14 | 2012-08-03T20:58:21 |
| PostId | 115360 | 44643 | 33526 |
| RelatedPostId | 60438 | 11457 | 20523 |
| LinkTypeId | 1 | 1 | 1 |

# "posts"  (rows=91966)

columns:
"Id" int PK UNIQ: unique identifier, 1..115378, avg=56144.9, median=56780
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
fk: "ParentId"→"posts"."Id", "OwnerUserId"→"users"."Id", "LastEditorUserId"→"users"."Id"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| Id | 115378 | 104385 | 55160 |
| PostTypeId | 2 | 1 | 2 |
| AcceptedAnswerId | null | null | null |
| CreaionDate | 2014-09-14T02:09:23 | 2014-06-23T11:52:08 | 2013-04-04T17:40:19 |
| Score | 0 | 1 | 1 |
| ViewCount | null | 34 | null |
| Body | <p>Decision trees are notoriously <strong>unstable</strong>: small perturbations in the training data can produce dramatically different trees, even though these trees can, and often do, perform about the same on held-out data. Decision trees are particularly prone to this because they make a series of sequential decisions and the decisions are discrete. </p>  <p>If you just want to classify your data, this isn't really an issue. Cross-validation is telling you that your approach (training a decision tree) works with your data. Assuming the performance is acceptably high, I'd fit a final tree with all of the data and deploy it. </p>  <p>It is worth noting that this instability can actually be turned to your advantage. <strong>Model-averaging</strong> or ensemble methods fit a collection of decision trees, using subsets of the data/features each time. The results of these trees are then combined and used to make predictions. This is the idea behind <strong>bagging</strong> and <strong>random forests.</strong></p>  <p>On the other hand, if you need to examine the structure of your decision tree, there have been a couple of attempts at creating more stable decision trees, like <a href="http://dl.acm.org/citation.cfm?id=775131" rel="nofollow">this</a> and <a href="http://www.cs.cmu.edu/~einat/Stability.pdf" rel="nofollow">this paper</a></p>  | <p>The objective of my work is to cluster the text documents. Once the documents are clustered, traditionally the system will assign numeric value for the clustered group. For example if I have 5 categories, then the clustered documents are labeled by any one of these numerical values {1,2,3,4,5}. I would like to assign the cluster name (e.g., philosophy, biology,...) automatically rather than labeling it as {1,2,3,...} for further processing. My initial idea is to provide the cluster name by counting the highest frequency word in that cluster. I am confused if this approach is good or not. I am using k-means clustering. Currently I am excluding LDA (Latent Diriclet Allocation) or other methods. </p>  | <p>I don't use R but here is a schedule which I hope will help you to compute the value of BIC or AIC clustering criterions for any given clustering solution.</p>  <pre><code>X is data matrix, N objects x P quantitative variables. Y is column of length N designating cluster membership; clusters 1, 2,..., K. 1. Compute 1 x K row Nc showing number of objects in each cluster. 2. Compute P x K matrix Vc containing variances by clusters.    Use denominator "n", not "n-1", to compute those, because there may be clusters with just one object. 3. Compute P x 1 column containing variances for the whole sample. Use "n-1" denominator.    Then propagate the column to get P x K matrix V. 4. Compute log-likelihood LL, 1 x K row. LL = -Nc &amp;* csum( ln(Vc + V)/2 ),    where "&amp;*" means usual, elementwise multiplication;    "csum" means sum of elements within columns. 5. Compute BIC value. BIC = -2 * rsum(LL) + 2*K*P * ln(N),    where "rsum" means sum of elements within row. 6. Also could compute AIC value. AIC = -2 * rsum(LL) + 4*K*P </code></pre>  <p>AIC and BIC clustering criterions are used not only with K-means  clustering. They may be useful for any clustering method which treats within-cluster density as within-cluster variance. Because AIC and BIC are to penalize for "excessive parameters", they <em>unambiguously tend to prefer</em> solutions with less clusters. "Less clusters more dissociated from one another" could be their motto.</p>  |
| OwnerUserId | 7250 | 37582 | 3277 |
| LasActivityDate | 2014-09-14T02:09:23 | 2014-06-23T13:48:56 | 2013-04-06T05:56:03 |
| Title | null | Assigning meaningful cluster name automatically | null |
| Tags | null | <clustering><text-mining><k-means> | null |
| AnswerCount | null | 1 | null |
| CommentCount | 0 | 3 | 2 |
| FavoriteCount | null | null | null |
| LastEditorUserId | null | 7290 | 3277 |
| LastEditDate | null | 2014-06-23T13:48:56 | 2013-04-06T05:56:03 |
| CommunityOwnedDate | null | null | null |
| ParentId | 115375 | null | 55147 |
| ClosedDate | null | null | null |
| OwnerDisplayName | null | null | null |
| LastEditorDisplayName | null | null | null |

# "tags"  (rows=1032)

columns:
"Id" int PK: unique identifier, 1..1869, avg=952.367, median=948
"TagName" text: all distinct
"Count" int: 272 distinct, 1..7244, avg=114.008, median=29
"ExcerptPostId" int FK: all distinct, nulls=436, 2331..114058, avg=54505.4, median=62654
"WikiPostId" int: all distinct, nulls=436, 2254..114057, avg=54504.3, median=62653

indexes: none
fk: "ExcerptPostId"→"posts"."Id"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| Id | 1869 | 1724 | 1009 |
| TagName | zero-inflated | ordered-logit | centering |
| Count | 1 | 20 | 31 |
| ExcerptPostId | null | 86507 | 81338 |
| WikiPostId | null | 86506 | 81337 |

# "users"  (rows=40325)

columns:
"Id" int PK UNIQ: unique identifier, -1..55747, avg=28037.4, median=28042
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
"AccountId" int: unique identifier, -1..5027354, avg=2.03255e+06, median=1.81644e+06
"Age" int: 70 distinct, nulls=32007, 13..94, avg=31.6426, median=30
"ProfileImageUrl" text: 13115 distinct, nulls=23846

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| Id | 55747 | 48404 | 41431 |
| Reputation | 1 | 101 | 54 |
| CreationDate | 2014-09-14T01:01:44 | 2014-06-15T05:11:58 | 2014-03-06T14:09:12 |
| DisplayName | Shivam Agrawal | difley | hmmmm |
| LastAccessDate | 2014-09-14T01:19:04 | 2014-07-11T05:57:11 | 2014-03-16T09:08:37 |
| WebsiteUrl | null | null | http://none |
| Location | India | null | United Kingdom |
| AboutMe | <p>Maths Enthusiast </p>  | null | <p>Currently studying for an Msc in Mathematics</p>  |
| Views | 0 | 0 | 6 |
| UpVotes | 0 | 0 | 5 |
| DownVotes | 0 | 0 | 0 |
| AccountId | 5027354 | 161857 | 1000228 |
| Age | null | null | 23 |
| ProfileImageUrl | https://lh4.googleusercontent.com/-ZsXhwVaFmiY/AAAAAAAAAAI/AAAAAAAAAqo/6UwTjH_MRIQ/photo.jpg | http://i.stack.imgur.com/YPEe1.jpg?s=128&g=1 | https://www.gravatar.com/avatar/2e0cff874c0a90d674345d12286eb222?s=128&d=identicon&r=PG |

# "votes"  (rows=38930)

columns:
"Id" int PK: unique identifier, 1..43538, avg=21984.2, median=22178.5
"PostId" int FK: 8584 distinct, 1..16921, avg=4568.11, median=4372
"VoteTypeId" int: 2=33323, 5=3365, 1=1451, 3=444, 16=111, 15=72, 8=60, 9=59, 11=44, 10=1, 1..16
"CreationDate" date: 287 distinct
"UserId" int FK: 509 distinct, nulls=35505, 5..11954, avg=1433.24, median=850
"BountyAmount" int: 50=53, 100=30, 25=12, 150=3, 0=2, 200=1, nulls=38829, 0..200

indexes: none
fk: "UserId"→"users"."Id", "PostId"→"posts"."Id"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| Id | 43538 | 18722 | 22972 |
| PostId | 10202 | 2379 | 5379 |
| VoteTypeId | 2 | 2 | 2 |
| CreationDate | 2011-05-01 | 2010-11-10 | 2010-12-11 |
| UserId | null | null | null |
| BountyAmount | null | null | null |
