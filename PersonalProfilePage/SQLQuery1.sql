create table Service 
(
ServiceID int IDENTITY(1,1) PRIMARY KEY ,
ServiceName nvarchar(40),
Category nvarchar(40)
COLLATE SQL_Latin1_General_CP1253_CI_AI)


insert into Service
values  (N'ΦΙΛΟΛΟΓΙΚΑ',N'ΜΑΘΗΜΑΤΑ ΚΑΤ ΟΙΚΟΝ'),
		(N'ΜΑΘΗΜΑΤΑ ΧΟΡΟΥ',N'ΜΑΘΗΜΑΤΑ ΚΑΤ ΟΙΚΟΝ'),
		(N'ΥΔΡΑΥΛΙΚΟΣ',N'ΤΕΧΝΙΚΑ ΕΠΑΓΓΕΛΜΑΤΑ'),
		(N'ΗΛΕΚΤΡΟΛΟΓΟΣ',N'ΤΕΧΝΙΚΑ ΕΠΑΓΓΕΛΜΑΤΑ'),
		(N'ΤΕΧΝΙΚΟΣ Η/Υ',N'ΤΕΧΝΙΚΑ ΕΠΑΓΓΕΛΜΑΤΑ'),
		(N'ΜΗΧΑΝΙΚΟΣ ΑΥΤΟΚΙΝΗΤΩΝ',N'AYTOKINHTO'),
		(N'ΚΑΘΑΡΙΣΜΟΣ ΑΥΤΟΚΙΝΗΤΟΥ',N'AYTOKINHTO'),
		(N'ΦΑΝΟΠΟΙΟΣ',N'AYTOKINHTO'),
		(N'ΟΙΚΙΑΚΗ ΒΟΗΘΟΣ',N'ΣΠΙΤΙ ΚΑΙ ΟΙΚΟΓΕΝΕΙΑ'),
		(N'ΦΥΛΑΞΗ ΠΑΙΔΙΩΝ',N'ΣΠΙΤΙ ΚΑΙ ΟΙΚΟΓΕΝΕΙΑ'),
		(N'ΦΡΟΝΤΙΔΑ ΗΛΙΚΙΩΜΕΝΩΝ',N'ΣΠΙΤΙ ΚΑΙ ΟΙΚΟΓΕΝΕΙΑ'),
		(N'ΚΗΠΟΥΡΟΣ',N'ΓΕΩΡΓΙΚΑ ΕΠΑΓΓΕΛΜΑΤΑ'),
		(N'ΓΕΩΠΟΝΟΣ',N'ΓΕΩΡΓΙΚΑ ΕΠΑΓΓΕΛΜΑΤΑ'),
		(N'ΤΕΧΝΙΚΟΣ ΑΣΦΑΛΕΙΑΣ',N'ΑΣΦΑΛΕΙΑ'),
		(N'ΚΟMΜΩΤΙΚΗ',N'ΣΩΜΑ ΚΑΙ ΑΙΣΘΗΤΙΚΗ'),
		(N'ΚΟΣΜΗΤΙΚΗ',N'ΣΩΜΑ ΚΑΙ ΑΙΣΘΗΤΙΚΗ'),
		(N'ΜΑΣΕΡ',N'ΣΩΜΑ ΚΑΙ ΑΙΣΘΗΤΙΚΗ'),
		(N'ΓΥΜΝΑΣΤΗΣ',N'ΣΩΜΑ ΚΑΙ ΑΙΣΘΗΤΙΚΗ')

/*select * from Service*/

create table Members
(
UserName nvarchar(40) PRIMARY KEY,
FirstName nvarchar(40), 
LastName nvarchar(40), 
balance int, 
email nvarchar(25),
[password] nvarchar(128), 
phoneNumber bigint,
Address nvarchar(128),
Photo nvarchar(128),
summary nvarchar(500) 
COLLATE SQL_Latin1_General_CP1253_CI_AI)


insert into Members
values ('nikosk',N'Νίκος', N'Κωνσταντινίδης', 1000, 'nikosk@demoapp.com', 'nikos123', 5551232454, N'Λευκάδας 4 Κοζάνη', NULL, NULL),
	   ('mariak',N'Μαρία', N'Καλφούντζου', 1000, 'mariak@demoapp.com', 'maria123', 5559881223, N'Νάξου 6 Αγρίνιο', NULL, NULL),
	   ('billyn',N'Βασίλης', N'Νίκος', 1000, 'billyn@demoapp.com', 'billyn123', 5550988231, N'Λυκαίου 4 Αθήνα', NULL, NULL),
	   ('tonyv',N'Αντώνης', N'Βάλσαμος', 1000, 'tonyv@demoapp.com', 'tony123', 5554566090, N'Κύπρου 6 Αθήνα', NULL, NULL)    

/*select * from Members*/


create table MembersService
(
	MembersID nvarchar(40) FOREIGN KEY REFERENCES Members(UserName),
	ServiceID int NOT NULL FOREIGN KEY REFERENCES Service(ServiceID),
	CONSTRAINT MembersServiceID PRIMARY KEY (MembersID,ServiceID),
	ServiceCostPerHour int NOT NULL
);



insert into MembersService
values ('billyn',3,50), ('mariak',13,20), ('nikosk',12,30), ('tonyv',4,10)

/*select * from MembersService*/





