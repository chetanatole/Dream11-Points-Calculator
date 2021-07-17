# Dream11-Points-Calculator
Dream11 Points Calclulator will calculate the fantasy points for each player of a match and print players in sorted manner based on fantasy points.<br><br> By default the points system used for calculating fantasy points is Dream11 points system released in 2021. You can change the points system by editing in <a href="https://github.com/chetanatole/Dream11-Points-Calculator/blob/main/points_calculator.py">points_calculator.py</a> file.<br><br>
Steps :
* Run points_calculator.py
```
$ python points_calculator.py
```
* Select type of match
```
Select Type of Match
1.T20
2.One Day
Enter Choice : 1
```
* Enter the ESPN CricInfo Scorecard URL of the match <br><br>
![link](https://user-images.githubusercontent.com/31009167/126044962-afe0ffe3-59b4-44d4-b3a6-1174780ec0ad.png)<br>
```
Enter ESPN Cricinfo scorecard link : https://www.espncricinfo.com/series/pakistan-tour-of-england-2021-1239529/england-vs-pakistan-1st-t20i-1239540/full-scorecard
```
* Result
```
Liam Livingstone     149
Babar Azam           125
Shaheen Shah Afridi  119
Shadab Khan          97
Mohammad Rizwan      89
Jason Roy            68
David Willey         59
Tom Curran           59
Haris Rauf           43
Mohammad Hafeez      41
Jonny Bairstow       40
Fakhar Zaman         37
Imad Wasim           36
Lewis Gregory        33
Mohammad Hasnain     31
Sohaib Maqsood       28
Saqib Mahmood        25
Eoin Morgan          22
Azam Khan            10
Dawid Malan          5
Moeen Ali            5
Matt Parkinson       -2
```
