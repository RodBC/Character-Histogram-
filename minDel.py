#1 - Construct a character histogram of a given string.
def string_histogram(string):
    histogram = {}
    for char in string:
        if char in histogram.keys():
            histogram[char] += 1
        else:
            histogram[char] = 1
    return histogram

string = "Iae, galera da IC!"
histogram = string_histogram(string)
print(histogram)

#2 - IF two strings have different character histograms, what minimum deletions are needed to make them equal?
def calculate_min_deletions(string1, string2):
    histogram1 = string_histogram(string1)
    histogram2 = string_histogram(string2)
    if histogram1 == histogram2:
        print("they've the same histogram! there's no need to delete any character.")
    else:
        return find_min_deletions(histogram1, histogram2)

def find_min_deletions(histogram1, histogram2):
    min_deletions = 0
    all_chars = set(histogram1.keys()).union(histogram2.keys())
    
    for char in all_chars:
        count1 = histogram1.get(char, 0)
        count2 = histogram2.get(char, 0)
        min_deletions += abs(count1 - count2)
    
    return f"there has to be at least ---> {min_deletions} character deletion to make them equal"

string1 = "vaga de IC"
string2 = "vaga para IC"
min_deletions = calculate_min_deletions(string1, string2)
print(min_deletions)