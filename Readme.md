# Instagram Unfollow Checker

This repository contains scripts to check who is not following you back on Instagram.

## Scripts
- `fetch_and_store_data.py`: Fetches and stores the list of followers and following from Instagram.
- `check_unfollowers.py`: Compares the stored lists and identifies people who have unfollowed you.

## Requirements
- Python 3.x
- `instaloader` library

## Warning: Use with Caution
This repository contains automation scripts that interact with Instagram's platform using the instaloader library. While the scripts are intended to help users track unfollowers and manage their Instagram accounts more efficiently, please be aware of the following:

- Instagram's Terms of Service:
Using automation tools on Instagram (such as scraping, bot-like behavior, and automated interactions) may violate Instagram's Terms of Service. Instagram explicitly prohibits the use of bots, scraping, and other unauthorized automation on their platform.
Engaging in such activities can result in account suspension or permanent banning. Always ensure you are in compliance with Instagram’s guidelines before running any automation scripts.

- Rate Limiting & Account Restrictions:
Instagram may impose rate limits on accounts that make too many requests within a short period. This can lead to temporary account restrictions or CAPTCHA verification requests.
Automated scraping or excessive interaction with the platform may trigger Instagram’s spam detection system, causing your account to be flagged as suspicious.

- Use of Credentials:
Never hard-code your username and password directly into the scripts or commit them to version control systems. Always use environment variables or external configuration files to securely manage sensitive information.
Consider using a dedicated Instagram account for automation purposes to minimize the risks associated with your primary account.

- Impact on User Experience:
Frequent scraping and requests may impact Instagram’s performance or cause server overload. Please be mindful and avoid aggressive automation that may disrupt the platform or cause delays in your own account's activity.

- Respect Other Users:
Be cautious and considerate about your actions. Unfollowing users automatically may violate trust or result in a poor user experience for others.

- Account Monitoring:
Ensure you monitor the health of your account regularly. If you notice unusual activity, it’s advisable to stop using the automation temporarily and review your actions.

## By using this repository, you acknowledge and accept these risks.
This warning helps users understand the potential risks associated with automating actions on Instagram. Be sure to regularly review Instagram’s Terms of Service to stay up-to-date with their policies.