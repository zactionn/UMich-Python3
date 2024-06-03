# Output file
resulting_data_file = "resulting_data.csv"

# List of punctuation characters
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

# Function to strip punctuation from a word
def strip_punctuation(word: str) -> str:
    for char in punctuation_chars:
        word = word.replace(char, "")
    return word

# Function to count positive words
def get_pos(text: str) -> int:
    text = text.lower()
    text_without_punctuation = strip_punctuation(text)
    words = text_without_punctuation.split()
    count_pos = 0
    for word in words:
        if word in positive_words:
            count_pos += 1
    return count_pos

# Function to count negative words
def get_neg(text: str) -> int:
    text = text.lower()
    text_without_punctuation = strip_punctuation(text)
    words = text_without_punctuation.split()
    count_neg = 0
    for word in words:
        if word in negative_words:
            count_neg += 1
    return count_neg

# Initialize vars
project_twitter_data = []

# Read positive words
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

# Read negative words
negative_words = []
with open("negative_words.txt") as neg_f:
    for lin in neg_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

# Read project twitter data
with open("project_twitter_data.csv") as prj_twit_data:
    lines = prj_twit_data.readlines()
    for line in lines[1:]:  # Skip header
        if line.strip() == '':
            print(f"Skipping empty line: {line}")
            continue

        parts = line.strip().split(',')
        if len(parts) < 3:
            print(f"Skipping line due to insufficient parts: {line}")
            continue

        tweet_text = ','.join(parts[:-2]).strip()  # Join all parts except the last two
        try:
            # Extract number of retweets and replies
            num_retweets = int(parts[-2].strip())
            num_replies = int(parts[-1].strip())

            # Calculate positive and negative scores
            pos_score = get_pos(tweet_text)
            neg_score = get_neg(tweet_text)
            net_score = pos_score - neg_score

            tweet_data = {
                'positive score': pos_score,
                'negative score': neg_score,
                'net score': net_score,
                'num of retweets': num_retweets,
                'num of replies': num_replies
            }

            # Add the tweet data to the project list
            project_twitter_data.append(tweet_data)
        except ValueError as e:
            print(f"Skipping line due to ValueError: {line}, error: {e}")

# Write the results to a CSV file
with open(resulting_data_file, 'w') as csvfile:
    # Write the header with spaces after commas
    csvfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n')
    # Write the data rows
    for tweet_data in project_twitter_data:
        row = f"{tweet_data['num of retweets']}, {tweet_data['num of replies']}, {tweet_data['positive score']}, {tweet_data['negative score']}, {tweet_data['net score']}\n"
        csvfile.write(row)