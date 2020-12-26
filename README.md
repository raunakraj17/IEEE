IMPLEMENT LOGISTICS REGRESSION ON TITANIC DATASET
started with importing pandas, numpy, matplotlib.pyplot and seaborn for handling functions and plotting figures
then, read the file to see what are the data available
it contains PassengerId- Specific number for every passenger
Survived- 0 or 1 showing 1 for survived and 0 for not
Pclass- Info about the passenger's class if the passenger travelled in class 1-Upper, 2-Middle or 3-Lower
Name- Name of passenger
Sex- Male or Female
Age- Age of passenger in Float type
SibSp- Sibling or spouse with passenger
Parch-Parents and children with passenger
Ticket- Unoque Ticket number/Id
Fare- Cost of ticket
Cabin-Cabin number
Embarked- Boarding point of passenger, S- SOUTHAMPTON, C-CHERBOURG and Q-QUEENSTOWN
then, plotted some figures to get a better idea of the data
there where null values too, 177 in Age, 687 in Cabin and 2 in Embarked
In the age null values filled the values as average of its respective Pclass
In Embarked as most people embarked from southampton, thats why filled s in two missing values
removed the cabin column as it was of no use and can be predicted with help of fare
defined train and test cases, created a confusion matrix and got the accuracy score all from importing sklearn
