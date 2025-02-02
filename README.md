# Tweet Analysis 

## Tweet Extraction 

Implementing the first step of ETL - Extraction. 
I have extracted tweets from Twitter using Twikit version 2.2.2

### Pre-requisites
Visual Studio code, Python 3.10+ 

### Steps:
1. Connecting to twitter using client.login()
2. Saving the login cookie information
3. Loading the cookie to a file locally
4. Exracting tweets (minimum 30) related to "Deepseek" using client.search_tweet()
5. Writing it to a csv file
6. To introduce human behavior, I have used fetched tweets after few seconds usingtime.sleep(wait_time)


#### Clone the Repository:
    git clone https://github.com/preethicindy/tweet_analysis.git
    cd tweet_analysis
    
#### Set Up a Virtual Environment:
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

### Version History:

v1.0: Initial commit - Extracted tweets from Twitter using the Twikit library.

### Acknowledgments:

References:
https://twikit.readthedocs.io/en/latest/twikit.html
