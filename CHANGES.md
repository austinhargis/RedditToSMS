# Changelog

## March 19th, 2020

Additions:
- Added the ability to change what subreddit you want to get news from with a dedicated variable.
- Added the ability to change how many posts are searched when the app refreshes.

Changes:
- Logs are now flushed (saved) everytime one is created, rather than at the end of a cycle.
- Getting the time is now done through a dedicated function, rather than using stftime in every log string. 
- All variable assignments are now done only if RetrieveNews itself is executed, instead of everytime it is called.

## March 21st, 2020

Additions:
- Multiple phone numbers can be texted news at a time. 

Changes:
- The destination phone number is now stored in a list, to allow for a new feature.