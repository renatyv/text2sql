# Schema Links

- version: 0.0.5
- dialect: sqlite
- database: file:/Users/renatyuldashev/Documents/ai-sql/custom-bench/data/bird_mini_dev/databases/dev_databases/codebase_community/codebase_community.sqlite
- schema: main

## Declared PK/FK Links

badges.UserId -> users.Id
comments.PostId -> posts.Id
comments.UserId -> users.Id
postHistory.PostId -> posts.Id
postHistory.UserId -> users.Id
postLinks.PostId -> posts.Id
postLinks.RelatedPostId -> posts.Id
posts.LastEditorUserId -> users.Id
posts.OwnerUserId -> users.Id
posts.ParentId -> posts.Id
tags.ExcerptPostId -> posts.Id
votes.PostId -> posts.Id
votes.UserId -> users.Id

## Inferred Links

All inferred links are implied by the declared PK/FK links above.
