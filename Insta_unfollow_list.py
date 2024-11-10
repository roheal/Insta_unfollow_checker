import instaloader
import time
import csv

# Instagram login credentials
username = "hello123"  # Replace with your Instagram username
password = "your_password"  # Replace with your Instagram password

# Initialize Instaloader
L = instaloader.Instaloader()

# Access the session directly through the context and update the headers
L.context._session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
})

def fetch_data():
    try:
        # Log in to Instagram
        L.login(username, password)
        print("Logged in successfully.")

        # Fetch the profile
        profile = instaloader.Profile.from_username(L.context, username)

        # Get followers and following lists
        followers = {follower.username for follower in profile.get_followers()}
        following = {followee.username for followee in profile.get_followees()}

        # Find users who don't follow back
        not_following_back = following - followers

        # Save the result to a CSV file
        with open("not_following_back.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Username"])
            for user in not_following_back:
                writer.writerow([user])

        print("Data saved to not_following_back.csv.")

    except instaloader.exceptions.BadCredentialsException:
        print("Error: Incorrect username or password.")
    except instaloader.exceptions.TwoFactorAuthRequiredException:
        verification_code = input("Enter the 2FA code: ")
        L.two_factor_login(verification_code)
    except instaloader.exceptions.QueryReturnedBadRequestException as e:
        print("Rate limit exceeded. Waiting for a while before retrying...")
        time.sleep(600)  # Wait for 10 minutes before retrying
        fetch_data()  # Retry after waiting
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
fetch_data()
