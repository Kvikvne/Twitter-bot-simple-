# Internet Speed Twitter Bot

This program uses Selenium to interact with the speedtest.net website to check the internet speed and post the results to Twitter. 

## Prerequisites
- Install Selenium using `pip install selenium`
- Download the appropriate ChromeDriver for your operating system and add it to your PATH or specify the path in the code.

## Usage

1. Replace `YOUR EMAIL` and `YOUR PASSWORD` with your Twitter credentials in the code.
2. Change the promised download and upload speeds (PROMISED_DOWN and PROMISED_UP) if necessary.
3. Run the code using `python filename.py`

## Code Explanation

The code uses Selenium to interact with the Chrome browser. The `InternetSpeedTwitterbot` class initializes the Chrome browser with the specified path to the ChromeDriver and sets the download and upload speed to 0. 

The `get_internet_speed` method navigates to speedtest.net and gets the internet speed by finding the elements for download and upload speed on the page.

The `tweet_at_provider` method navigates to Twitter, logs in using the provided credentials, and tweets the message `"i am a bot uWu"`. Obviously you'll need to change that.
