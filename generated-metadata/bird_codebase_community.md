# Additional Metadata

## Clarified Semantics
- `postLinks.LinkTypeId`: enumerates link kind. Observed values 1 (10,186 rows) and 3 (916 rows), where 1 = ordinary "linked" relationship and 3 = duplicate-of relationship per Stack Exchange convention.
- `votes.VoteTypeId`: enumerates vote kind. Dominant values are 2 (up-mod) and 5 (favorite); lesser values include 1 (accept), 3 (down-mod), and bounty-related codes 8/9. Non-null `BountyAmount` appears on bounty vote types.
- `votes.BountyAmount`: present (non-null) only on bounty rows; values 25–200. ~99.5% of rows have it null.
- `postHistory.PostHistoryTypeId`: enumerates revision event kind. Top values are 2/5 (initial/edit body) and 1/3 (initial/edit title/tags); 24/25 and 16/10 correspond to additional edit and close-vote–style history entries.
- `posts.PostTypeId`: profile lists type counts; 1 ≈ question (42,912), 2 ≈ answer (47,755). Rows of types 4–7 are the small minority and are wiki/edge post kinds.
- `users.AccountId` is the StackExchange network account ID and may differ from the local `users.Id`; `Id=-1` appears as a sentinel (deleted/unregistered) user, and negative `OwnerUserId`/`LastEditorUserId` also signal deleted or anonymous posts, not valid user keys.
- `posts.CreaionDate` is a typo'd column (should be CreationDate); no separate CreationDate column exists.
- `comments.UserId` has nulls (≈2,835) for anonymous comments; `UserDisplayName` is null for the vast majority and only carries a value for users.
- `postHistory`, `postLinks`, and `votes` have no indexes; large scans on these tables may be needed.

## Potential Join Strategies
- **Q&A pairs**: join `posts.ParentId` → `posts.Id` to pair answers (PostTypeId=2) with their question, filter answers on `posts.ParentId IS NOT NULL` and questions on `PostTypeId=1`.
- **Accepted answers**: join `posts.AcceptedAnswerId` → `posts.Id` to recover the accepted answer post from a question; `AcceptedAnswerId` is null on most rows (~84%), so filter accordingly.
- **Post↔comments**: `comments.PostId` → `posts.Id`. Filter `comments.UserId IS NOT NULL` to drop anonymous comments before aggregating per user.
- **Post↔votes**: `votes.PostId` → `posts.Id`, additionally `votes.UserId` → `users.Id` only where `votes.UserId IS NOT NULL`. Note votes table is sparse (38,930 rows over 8,584 distinct posts) and `VoteTypeId` restricts semantics.
- **Related/duplicate posts**: `postLinks.PostId`/`RelatedPostId` → `posts.Id`. `LinkTypeId=1` (linked) links are ~11x more frequent than `LinkTypeId=3` (duplicates); cardinality is modest (11,102 rows).
- **Tag metadata**: join `tags.ExcerptPostId` → `posts.Id` (and `WikiPostId`, which is not FK-declared but points to posts) to attach tag descriptions; ~42% of tags have null excerpt/wiki IDs.
- **User activity aggregation**: `badges.UserId`, `comments.UserId`, `postHistory.UserId`, `posts.OwnerUserId`/`LastEditorUserId`, `votes.UserId` all → `users.Id`. Filter `OwnerUserId > 0` since negative `OwnerUserId` marks deleted-user posts and would otherwise join to the `Id=-1` sentinel user.
- **Editing history**: `postHistory.PostId` → `posts.Id` and `postHistory.UserId` → `users.Id`; every post virtually guarantees one history row (initial), so use history only when revision/edit events matter, and join on post `Id` as the left key to avoid fan-out.