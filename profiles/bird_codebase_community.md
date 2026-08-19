---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T07:18:38.556000Z
dialect: sqlite
database: /Users/renatyuldashev/Documents/ai-sql/custom-bench/data/bird_mini_dev/databases/dev_databases/codebase_community/codebase_community.sqlite
schema: main
---

## Relationships

- posts.Id ← comments.PostId, postHistory.PostId, postLinks.PostId, postLinks.RelatedPostId, posts.ParentId, tags.ExcerptPostId, votes.PostId
- users.Id ← badges.UserId, comments.UserId, postHistory.UserId, posts.LastEditorUserId, posts.OwnerUserId, votes.UserId

# badges

```sql
CREATE TABLE badges
(
    Id     INTEGER          not null
        primary key,
    UserId INTEGER          null,
    Name   TEXT null,
    Date   DATETIME     null,
        foreign key (UserId) references users (Id)
            on update cascade on delete cascade
);
```

## Rows

- total=79851

| column | latest | sample | sample |
|---|---|---|---|
| Id | 92240 | 79972 | 4957 |
| UserId | 12597 | 46912 | 2811 |
| Name | Autobiographer | Student | Autobiographer |
| Date | 2014-09-14T02:31:28 | 2014-06-07T10:59:46 | 2011-01-17T21:46:45 |

## Columns

- Id: unique identifier, int 1..92240
  - stats: average=45430.1, median=45939
- UserId: 25078 distinct, int 2..55746
  - stats: average=18638.3, median=13651
- Name: 153 distinct
- Date: 65586 distinct


# comments

```sql
CREATE TABLE comments
(
    Id              INTEGER          not null
        primary key,
    PostId          INTEGER          null,
    Score           INTEGER          null,
    Text            TEXT     null,
    CreationDate    DATETIME     null,
    UserId          INTEGER          null,
    UserDisplayName TEXT null,
        foreign key (PostId) references posts (Id)
            on update cascade on delete cascade,
        foreign key (UserId) references users (Id)
            on update cascade on delete cascade
);
```

## Rows

- total=174285

| column | latest | sample | sample |
|---|---|---|---|
| Id | 221292 | 108395 | 215211 |
| PostId | 115374 | 56213 | 112282 |
| Score | 1 | 0 | 0 |
| Text | @DilipSarwate indeed, in that case, the odds are even. | Unfortunately there is no general answer to your problem, as it explicitly depends on the specific data you have which make up your M observations of your k features. There are two basic approaches, filter methods and wrapper methods. Filter methods select features based on searches in combinatorial spaces based on metrics. Wrapper methods incorporate a classifier/s of choice into the feature selection process. Wrapper methods are more specific to the problem at hand but may be computationally expensive. A variety of metrics and classifiers are available to plug into the two approaches. | Linking to one of your own questions (which has at present not been found clear enough to prompt any anwers yet) is not helpful. |
| CreationDate | 2014-09-14T02:04:27 | 2013-04-16T08:41:49 | 2014-08-18T10:11:41 |
| UserId | 805 | 10065 | 1739 |
| UserDisplayName | null | null | null |

## Columns

- Id: unique identifier, int 1..221292
  - stats: average=107698
- PostId: int 1..115376
  - stats: average=54245.1
- Score: int 0..90
  - stats: average=0.388398
- Text: profile metrics skipped
- CreationDate: profile metrics skipped
- UserId: nulls=2835, int 3..55746
  - stats: average=12443.3
- UserDisplayName: nulls=171454


# postHistory

```sql
CREATE TABLE postHistory
(
    Id                INTEGER          not null UNIQUE
        primary key,
    PostHistoryTypeId INTEGER          null,
    PostId            INTEGER          null,
    RevisionGUID      TEXT null,
    CreationDate      DATETIME     null,
    UserId            INTEGER          null,
    Text              TEXT     null,
    Comment           TEXT         null,
    UserDisplayName   TEXT null,
        foreign key (PostId) references posts (Id)
            on update cascade on delete cascade,
        foreign key (UserId) references users (Id)
            on update cascade on delete cascade
);
```

## Rows

- total=303155

| column | latest | sample | sample |
|---|---|---|---|
| Id | 386848 | 71612 | 185948 |
| PostHistoryTypeId | 5 | 2 | 3 |
| PostId | 115377 | 23376 | 58523 |
| RevisionGUID | 91050683-844a-4e89-ad8e-f00f564bc985 | bfa34fb0-ccad-4dd3-bd21-9ab5ed69d32f | 5226b335-57a2-49a2-bc93-4b034a8f0dfd |
| CreationDate | 2014-09-14T02:54:13 | 2012-02-17T10:21:16 | 2013-05-08T22:07:45 |
| UserId | 805 | 7170 | 16036 |
| Text | As a practical answer to the real questions you're addressing, such high quantiles will generally be quite sensitive to issues with model choice (especially such things as whether you model the right censoring and how heavy the tails are in the components). \\n\\nBut in any case - especially when dealing with high quantiles where ordinary simulation becomes impractical - that has great value in its own right; it's an interesting question from both theoretical and practical standpoints.\\n\\n---\\n\\nA couple of other approaches to this problem are using the Fast Fourier Transform and direct numerical integration.\\n\\nOne useful reference on this topic is Luo and Shevchenko (2009)$^{[1]}$.\\n\\nIn it they develop an adaptive direct numerical integration approach that's faster than simulation and competitive with FFT.\\n\\nThe more traditional approach in actuarial work was been Panjer recursion, which can be found in numerous texts. Embrechts and Frei (2009)$^{[2]}$ discuss and compare Panjer recursion and FFT. (Note that both of these techniques involve discretization of the continuous distribution.)\\n\\n\\n [1]: Luo, X. and Shevchenko, P.V. (2009),  \\n"Computing Tails of Compound Distributions Using Direct Numerical Integration,"  \\n*Journal of Computational Finance*, **13** (2), 73-111.   \\n[arXiv preprint available [here](http://arxiv.org/abs/0904.0830)]\\n\\n\\n [2]: Embrechts, P., and Frei, M. (2009),  \\n"Panjer recursion versus FFT for compound distributions,"    \\n*Mathematical Methods of Operations Research*, **69**:3 (July) pp 497-508.  \\n[seems to be a pre-publication version [here](http://www.math.ethz.ch/~embrecht/ftp/PanjerVsFFTcorrected.pdf)]\\n\\n | I think this is a more about Engineering Problem Solving. Most successful engineering project did not duplicate expert's reasoning or nature exactly. They solved problem in a different way. \\nFor example washing machines uses a different technique than humans , airplanes uses different dynamics than birds.\\n\\n\\nIf you are duplicating Expert Reasoning, their input is **everything**. But if you are solving same problem using different techniques (fast search,huge memory ...), their input is only **helpful**.\\n | <correlation> |
| Comment | added 92 characters in body |  |  |
| UserDisplayName |  |  |  |

## Columns

- Id: unique identifier, int 1..386848
  - stats: average=188490
- PostHistoryTypeId: int 1..38
  - stats: average=4.90865
- PostId: int 1..115378
  - stats: average=56538.5
- RevisionGUID: profile metrics skipped
- CreationDate: profile metrics skipped
- UserId: nulls=21326, int -1..55746
  - stats: average=16035
- Text: profile metrics skipped
- Comment: profile metrics skipped
- UserDisplayName: profile metrics skipped


# postLinks

```sql
CREATE TABLE postLinks
(
    Id            INTEGER      not null
        primary key,
    CreationDate  DATETIME null,
    PostId        INTEGER      null,
    RelatedPostId INTEGER      null,
    LinkTypeId    INTEGER      null,
        foreign key (PostId) references posts (Id)
            on update cascade on delete cascade,
        foreign key (RelatedPostId) references posts (Id)
            on update cascade on delete cascade
);
```

## Rows

- total=11102

| column | latest | sample | sample |
|---|---|---|---|
| Id | 3356789 | 1719171 | 3015399 |
| CreationDate | 2014-09-13T20:54:31 | 2012-07-31T10:54:54 | 2014-04-29T18:57:51 |
| PostId | 115360 | 33377 | 95685 |
| RelatedPostId | 60438 | 1459 | 21658 |
| LinkTypeId | 1 | 1 | 1 |

## Columns

- Id: unique identifier, int 108..3356789
  - stats: average=2.32683e+06, median=2.56431e+06
- CreationDate: 9450 distinct
- PostId: 7604 distinct, int 4..115360
  - stats: average=60227.8, median=62679
- RelatedPostId: 5177 distinct, int 1..115163
  - stats: average=32982.6, median=24077
- LinkTypeId: 1=10186, 3=916


# posts

```sql
CREATE TABLE posts
(
    Id                    INTEGER          not null UNIQUE
        primary key,
    PostTypeId            INTEGER          null,
    AcceptedAnswerId      INTEGER          null,
    CreaionDate           DATETIME     null,
    Score                 INTEGER          null,
    ViewCount             INTEGER          null,
    Body                  TEXT     null,
    OwnerUserId           INTEGER          null,
    LasActivityDate       DATETIME     null,
    Title                 TEXT null,
    Tags                  TEXT null,
    AnswerCount           INTEGER          null,
    CommentCount          INTEGER          null,
    FavoriteCount         INTEGER          null,
    LastEditorUserId      INTEGER          null,
    LastEditDate          DATETIME     null,
    CommunityOwnedDate    DATETIME    null,
    ParentId              INTEGER          null,
    ClosedDate            DATETIME     null,
    OwnerDisplayName      TEXT null,
    LastEditorDisplayName TEXT null,
        foreign key (LastEditorUserId) references users (Id)
            on update cascade on delete cascade,
        foreign key (OwnerUserId) references users (Id)
            on update cascade on delete cascade,
        foreign key (ParentId) references posts (Id)
            on update cascade on delete cascade
);
```

## Rows

- total=91966

| column | latest | sample | sample |
|---|---|---|---|
| Id | 115378 | 13799 | 24493 |
| PostTypeId | 2 | 1 | 1 |
| AcceptedAnswerId | null | null | null |
| CreaionDate | 2014-09-14T02:09:23 | 2011-08-03T10:59:38 | 2012-03-12T05:03:44 |
| Score | 0 | 1 | 2 |
| ViewCount | null | 150 | 722 |
| Body | <p>Decision trees are notoriously <strong>unstable</strong>: small perturbations in the training data can produce dramatically different trees, even though these trees can, and often do, perform about the same on held-out data. Decision trees are particularly prone to this because they make a series of sequential decisions and the decisions are discrete. </p>  <p>If you just want to classify your data, this isn't really an issue. Cross-validation is telling you that your approach (training a decision tree) works with your data. Assuming the performance is acceptably high, I'd fit a final tree with all of the data and deploy it. </p>  <p>It is worth noting that this instability can actually be turned to your advantage. <strong>Model-averaging</strong> or ensemble methods fit a collection of decision trees, using subsets of the data/features each time. The results of these trees are then combined and used to make predictions. This is the idea behind <strong>bagging</strong> and <strong>random forests.</strong></p>  <p>On the other hand, if you need to examine the structure of your decision tree, there have been a couple of attempts at creating more stable decision trees, like <a href="http://dl.acm.org/citation.cfm?id=775131" rel="nofollow">this</a> and <a href="http://www.cs.cmu.edu/~einat/Stability.pdf" rel="nofollow">this paper</a></p>  | <p>I am trying to compute the entropy for different sets of data and then compare the obtained values.</p>  <p>The idea is that the sets of data may change their size, I might have sets sizes ranging from 10 to 200 values.</p>  <p>In order to compare the entropy level obtained for them should I first normalize it with respect to the set sizes (basically just divide it by the number of data values within each set)?</p>  <p>How should I proceed in this matter?</p>  | <p>I have a basic doubt in dimension reduction for text dataset eg. 20Newsgroup, rcv1 etc. Initially I extract the number of word occurrence in each document, i.e word x document matrix would be $n \\times d$  where $n$ is the number of documents and $d$ is the dimension.</p>  <p>I would like to reduce the dimension, say $d_1 &lt;&lt; d$. What is the standard technique of reducing the dimension?</p>  <ol> <li>Choose the top $d_1$ feature from the original word occurrence matrix$( n \\times d)$ and then calculate TF-IDF for the reduced matrix $(n \\times d_1)$,  or</li> <li>Calculate the TF-IDF matrix for $n \\times d$ matrix and then select top $d_1$ features.  </li> </ol>  <p>Also, it is mentioned in many literature that top feature are selected. I wanted to know what is selecting the top features means? How do they define it?</p>  |
| OwnerUserId | 7250 | 5228 | 4290 |
| LasActivityDate | 2014-09-14T02:09:23 | 2011-08-03T11:55:42 | 2012-03-12T08:35:16 |
| Title | null | Entropy value for different sets of data | How to reduce dimension for text document dataset? |
| Tags | null | <data-mining><entropy> | <dataset><text-mining><dimensionality-reduction> |
| AnswerCount | null | 0 | 1 |
| CommentCount | 0 | 2 | 1 |
| FavoriteCount | null | 2 | null |
| LastEditorUserId | null | 88 | 930 |
| LastEditDate | null | 2011-08-03T11:55:42 | 2012-03-12T07:30:55 |
| CommunityOwnedDate | null | null | null |
| ParentId | 115375 | null | null |
| ClosedDate | null | null | null |
| OwnerDisplayName | null | null | null |
| LastEditorDisplayName | null | null | null |

## Columns

- Id: unique identifier, int 1..115378
  - stats: average=56144.9, median=56780
- PostTypeId: 2=47755, 1=42912, 5=640, 4=639, 6=9, 3=6, 7=5, int 1..7
- AcceptedAnswerId: all distinct, nulls=77269, int 5..115345
  - stats: average=52239.7, median=49807
- CreaionDate: 91255 distinct
- Score: 130 distinct, int -19..192
  - stats: average=2.79209, median=2
- ViewCount: 3714 distinct, nulls=49054, int 1..175495
  - stats: average=565.835, median=128
- Body: 91732 distinct, nulls=220
- OwnerUserId: 21979 distinct, nulls=1392, int -1..55746
  - stats: average=16544.9, median=11032
- LasActivityDate: 72647 distinct
- Title: 42877 distinct, nulls=49054
- Tags: 28528 distinct, nulls=49054
- AnswerCount: 31 distinct, nulls=49054, int 0..136
  - stats: average=1.11272, median=1
- CommentCount: 39 distinct, int 0..45
  - stats: average=1.89493, median=1
- FavoriteCount: 77 distinct, nulls=78723, int 0..233
  - stats: average=2.54383, median=1
- LastEditorUserId: 6578 distinct, nulls=47361, int -1..55733
  - stats: average=11923.2, median=7290
- LastEditDate: 44925 distinct, nulls=46934
- CommunityOwnedDate: 1938 distinct, nulls=89499
- ParentId: 29006 distinct, nulls=44211, int 1..115375
  - stats: average=48358.3, median=44790
- ClosedDate: all distinct, nulls=90356
- OwnerDisplayName: 1613 distinct, nulls=89457
- LastEditorDisplayName: 59 distinct, nulls=91501


# tags

```sql
CREATE TABLE tags
(
    Id            INTEGER          not null
        primary key,
    TagName       TEXT null,
    Count         INTEGER          null,
    ExcerptPostId INTEGER          null,
    WikiPostId    INTEGER          null,
    foreign key (ExcerptPostId) references posts (Id)
        on update cascade on delete cascade
);
```

## Rows

- total=1032

| column | latest | sample | sample |
|---|---|---|---|
| Id | 1869 | 1666 | 1770 |
| TagName | zero-inflated | convolution | flexmix |
| Count | 1 | 26 | 1 |
| ExcerptPostId | null | null | null |
| WikiPostId | null | null | null |

## Columns

- Id: unique identifier, int 1..1869
  - stats: average=952.367, median=948
- TagName: all distinct
- Count: 272 distinct, int 1..7244
  - stats: average=114.008, median=29
- ExcerptPostId: all distinct, nulls=436, int 2331..114058
  - stats: average=54505.4, median=62654
- WikiPostId: all distinct, nulls=436, int 2254..114057
  - stats: average=54504.3, median=62653


# users

```sql
CREATE TABLE users
(
    Id              INTEGER          not null UNIQUE
        primary key,
    Reputation      INTEGER          null,
    CreationDate    DATETIME     null,
    DisplayName     TEXT null,
    LastAccessDate  DATETIME     null,
    WebsiteUrl      TEXT null,
    Location        TEXT null,
    AboutMe         TEXT     null,
    Views           INTEGER          null,
    UpVotes         INTEGER          null,
    DownVotes       INTEGER          null,
    AccountId       INTEGER          null,
    Age             INTEGER          null,
    ProfileImageUrl TEXT null
);
```

## Rows

- total=40325

| column | latest | sample | sample |
|---|---|---|---|
| Id | 55747 | 28214 | 54686 |
| Reputation | 1 | 11 | 101 |
| CreationDate | 2014-09-14T01:01:44 | 2013-07-19T14:08:15 | 2014-08-25T20:14:29 |
| DisplayName | Shivam Agrawal | Sally | Akim |
| LastAccessDate | 2014-09-14T01:19:04 | 2013-08-26T22:18:24 | 2014-08-27T06:01:24 |
| WebsiteUrl | null | null | http://akimboyko.github.io/ |
| Location | India | null | Kiev, Ukraine |
| AboutMe | <p>Maths Enthusiast </p>  | null | <p>Paying off technical debts and reducing complexity</p>  |
| Views | 0 | 0 | 0 |
| UpVotes | 0 | 0 | 2 |
| DownVotes | 0 | 0 | 0 |
| AccountId | 5027354 | 3068588 | 198606 |
| Age | null | null | 34 |
| ProfileImageUrl | https://lh4.googleusercontent.com/-ZsXhwVaFmiY/AAAAAAAAAAI/AAAAAAAAAqo/6UwTjH_MRIQ/photo.jpg | null | https://www.gravatar.com/avatar/925df81271c71363d2a528032d57bb4b?s=128&d=identicon&r=PG |

## Columns

- Id: unique identifier, int -1..55747
  - stats: average=28037.4, median=28042
- Reputation: 965 distinct, int 1..87393
  - stats: average=84.0787, median=11
- CreationDate: 40315 distinct
- DisplayName: 35644 distinct
- LastAccessDate: 40287 distinct
- WebsiteUrl: 7787 distinct, nulls=32204
- Location: 2464 distinct, nulls=28634
- AboutMe: 9140 distinct, nulls=30946
- Views: 362 distinct, int 0..20932
  - stats: average=8.90963, median=0
- UpVotes: 332 distinct, int 0..11442
  - stats: average=6.58745, median=0
- DownVotes: 76 distinct, int 0..1920
  - stats: average=0.260905, median=0
- AccountId: unique identifier, int -1..5027354
  - stats: average=2.03255e+06, median=1.81644e+06
- Age: 70 distinct, nulls=32007, int 13..94
  - stats: average=31.6426, median=30
- ProfileImageUrl: 13115 distinct, nulls=23846


# votes

```sql
CREATE TABLE votes
(
    Id           INTEGER  not null
        primary key,
    PostId       INTEGER  null,
    VoteTypeId   INTEGER  null,
    CreationDate DATE null,
    UserId       INTEGER  null,
    BountyAmount INTEGER  null,
        foreign key (PostId) references posts (Id)
            on update cascade on delete cascade,
        foreign key (UserId) references users (Id)
            on update cascade on delete cascade
);
```

## Rows

- total=38930

| column | latest | sample | sample |
|---|---|---|---|
| Id | 43538 | 19861 | 25502 |
| PostId | 10202 | 4638 | 5990 |
| VoteTypeId | 2 | 2 | 2 |
| CreationDate | 2011-05-01 | 2010-11-17 | 2011-01-04 |
| UserId | null | null | null |
| BountyAmount | null | null | null |

## Columns

- Id: unique identifier, int 1..43538
  - stats: average=21984.2, median=22178.5
- PostId: 8584 distinct, int 1..16921
  - stats: average=4568.11, median=4372
- VoteTypeId: 2=33323, 5=3365, 1=1451, 3=444, 16=111, 15=72, 8=60, 9=59, 11=44, 10=1, int 1..16
- CreationDate: 287 distinct
- UserId: 509 distinct, nulls=35505, int 5..11954
  - stats: average=1433.24, median=850
- BountyAmount: 50=53, 100=30, 25=12, 150=3, 0=2, 200=1, nulls=38829, int 0..200
