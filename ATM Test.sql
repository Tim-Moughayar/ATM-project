CREATE DATABASE CIS206ATM;
CREATE TABLE Users (
	PIN Int NOT NULL PRIMARY KEY,
	Name varchar(255)
	);
CREATE TABLE Accounts (
	AccountID Int NOT NULL PRIMARY KEY,
	FOREIGN KEY (PIN) REFERENCES Users(PIN),
	Name varchar(255),
	AccountType varchar(255),
	Balance Int
	);
INSERT INTO Users (PIN, Name)
VALUES ('1111', 'Bryan');
INSERT INTO Users (PIN, Name)
VALUES ('2222', 'Ravina');
INSERT INTO Users (PIN, Name)
VALUES ('3333', 'Frank');
INSERT INTO Users (PIN, Name)
VALUES ('4444', 'Alexis');
INSERT INTO Users (PIN, Name)
VALUES ('5555', 'Timothy');
INSERT INTO Users (PIN, Name)
VALUES ('6666', 'Michael');

UPDATE Accounts
SET Name = 'Bryan', AccountType = 'Checking', Balance = 100000
WHERE PIN = '1111';
UPDATE Accounts
SET Name = 'Ravina', AccountType = 'Checking', Balance = 100000
WHERE PIN = '2222';
UPDATE Accounts
SET Name = 'Frank', AccountType = 'Checking', Balance = 100000
WHERE PIN = '3333';
UPDATE Accounts
SET Name = 'Alexis', AccountType = 'Checking', Balance = 100000
WHERE PIN = '4444';
UPDATE Accounts
SET Name = 'Timothy', AccountType = 'Checking', Balance = 100000
WHERE PIN = '5555';
UPDATE Accounts
SET Name = 'Michael', AccountType = 'Checking', Balance = 100000
WHERE PIN = '6666';
COMMIT;
	