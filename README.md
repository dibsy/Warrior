# Warrior
## Warrior is a tool for performing security analysis of a war files. 

v.10
Integration with OWASP Dependency Check to perform vulnerability analysis of .JAR files present within the .WAR files

![Warrior 1.0](https://github.com/dibsy/Warrior/blob/master/warrior.PNG)

## Steps to setup
Grap a copy of the latest OWASP Dependency Check from here (https://jeremylong.github.io/DependencyCheck/dependency-check-cli/index.html)

Extract the contents and put the warrior.py file inside the dependency-check/bin/ location.
![Save](https://github.com/dibsy/Warrior/blob/master/save.PNG)

usage : python warrior.py "ProjectName" "location_of_war_file"
C:\dependency-check-2.1.0-release\dependency-check\bin>python warior.py Test_Project C:\pwm.war

![Report Location](https://github.com/dibsy/Warrior/blob/master/test_report.PNG)

![Report ](https://github.com/dibsy/Warrior/blob/master/report.PNG)
