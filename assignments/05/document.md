## Data Fields

birth: Birth date of the character <br>
death: Death date of the character <br>
gender: Gender of the character <br>
hair: Hair color of the character <br>
height: Height of the character <br>
name: Name of the character <br>
race: Race of the character <br>
realm: Realm of origin <br>
spouse: Spouse of the character

## Data Cleaning Steps
1. Removed unnecessary whitespace in the birth and death columns.
2. Consolidated hair color in the hair column by removing additional information in parentheses.
3. Filled missing values with "Unknown".
4. Removed rows with missing names, as they are critical for the analysis.

## Shell and Regex Analyses
### Commands and Results
1. Total number of dialogue lines and unique words:
    ```bash
    wc -l lotr_characters_cleaned.csv
    awk '{ for (i=1;i<=NF;i++) words[$i]++ } END { print length(words) }' lotr_characters_cleaned.csv
    ```

2. Distribution across the three films (assuming a corresponding field exists):
    ```bash
    grep -o 'Fellowship' lotr_characters_cleaned.csv | wc -l
    grep -o 'Two Towers' lotr_characters_cleaned.csv | wc -l
    grep -o 'Return of the King' lotr_characters_cleaned.csv | wc -l
    ```

3. Top 5 characters based on char:
    ```bash
    awk -F',' '{names[$6]++} END {for (name in names) print names[name], name}' lotr_characters_cleaned.csv | sort -nr | head -5
    ```

4. Top 5 characters based on dialogues:
    ```bash
    awk -F',' '{dialogues[$6]+=$NF} END {for (char in dialogues) print dialogues[char], char}' lotr_characters_cleaned.csv | sort -nr | head -5
    ```
