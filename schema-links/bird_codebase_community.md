# Schema Links

- generator: local introspection
- dialect: sqlite
- database: codebase_community

## Declared Links

- `badges.UserId` → `users.Id`
- `comments.PostId` → `posts.Id`
- `comments.UserId` → `users.Id`
- `postHistory.PostId` → `posts.Id`
- `postHistory.UserId` → `users.Id`
- `postLinks.PostId` → `posts.Id`
- `postLinks.RelatedPostId` → `posts.Id`
- `posts.LastEditorUserId` → `users.Id`
- `posts.OwnerUserId` → `users.Id`
- `posts.ParentId` → `posts.Id`
- `tags.ExcerptPostId` → `posts.Id`
- `votes.PostId` → `posts.Id`
- `votes.UserId` → `users.Id`

## Same-name Candidates

- `CreationDate`: `comments.CreationDate`, `postHistory.CreationDate`, `postLinks.CreationDate`, `users.CreationDate`, `votes.CreationDate`
- `Id`: `badges.Id`, `comments.Id`, `postHistory.Id`, `postLinks.Id`, `posts.Id`, `tags.Id`, `users.Id`, `votes.Id`
- `PostId`: `comments.PostId`, `postHistory.PostId`, `postLinks.PostId`, `votes.PostId`
- `Score`: `comments.Score`, `posts.Score`
- `Text`: `comments.Text`, `postHistory.Text`
- `UserDisplayName`: `comments.UserDisplayName`, `postHistory.UserDisplayName`
- `UserId`: `badges.UserId`, `comments.UserId`, `postHistory.UserId`, `votes.UserId`
