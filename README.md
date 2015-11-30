# CSC485


The goal of this project is to provide a secured and unsecured  implementation of the same functionality.

You must select 3 vulnerabilities from the top 10 and provide for each a secured and an unsecured implementation.

What you must provide:
	-Documentation of the system, use case scenario  (10 points)
	-Documentation of which vulnerability you selected and for each,  a vulnerable implementation, code/script to take advantage of the vulnerability and a non-vulnerable implementation of the same functionality and how to verify that it is not vulnerable
	(25 points by vulnerability:
		5 DOCUMENTATION,
		10 IMPLEMENTATIONS,
		10 HOW TO TAKE ADVANTAGE OF THE VULNERABILITY)
	-Code of the system
	-Demo in class (10 minutes): 3-5 slides to present what you did, a a demo of each vulnerability, how to take advantage of it and how you secure it (10 points)
	-Email status ( 5 points): every Friday, each team must email me their status: what vulnerabilities you selected ? for each, is the implementation completed ? the script to take advantage of it ? the non-vulnerable implementation ? its documentation ?
	-Bonus: 10 points if you implement a 4th vulnerability

Deadline: Nov 22nd
Demo in class: Nov. 30th
Submission: one zip file in moodle, which includes the documentation, the source code and the presentation.

To do the project with Python.
	You can use web.py to do the implementation(http://webpy.org/), it is installed under python 2.7.
	Please read the tutorial: http://webpy.org/docs/0.3/tutorial  
	Take a look at the code.zip with an index page and a template.
	To start the code: python code.py <optionnal port number>
	You can type : http://localhost:8080/ to access the index page in your browser. 
	http://localhost:8080/?name=Joe to test with a parameter.

	It should display data such as:
		#	Name	Last name	Birth date		Role			Department		E-mail	
		101	John	Smith		12-12-1980		Manager			Sales			john.smith@abc.com	
		102	Laura	Adams		02-11-1979		Manager			IT				laura.adams@abc.com	
		103	Peter	Williams	22-10-1966		Coordinator		HR				peter.williams@abc.com	
		104	Joana	Sanders		11-11-1976		Manager			Marketing		joana.sanders@abc.com	
		105	John	Drake		18-08-1988		Coordinator		Finance			john.drake@abc.com	
		106	Samuel	Williams	22-03-1985		Coordinator		Finance			samuel.williams@abc.com
		(*** lines alternate color and shit... ***)

A1 Injection:
	Scenario #1: The application uses untrusted data in the construction of the following vulnerable SQL call:
		String query = "SELECT * FROM accounts WHERE custID='" + request.getParameter("id") + "'";
	Scenario #2: Similarly, an application’s blind trust in frameworks may result in queries that are still vulnerable, (e.g., Hibernate Query Language (HQL)):
		Query HQLQuery = session.createQuery(“FROM accounts WHERE custID='“ + request.getParameter("id") + "'");
	In both cases, the attacker modifies the ‘id’ parameter value in her browser to send: ' or '1'='1. For example:
		http://example.com/app/accountView?id=' or '1'='1
		This changes the meaning of both queries to return all the records from the accounts table. More dangerous attacks could modify data or even invoke stored procedures.
	Preventing injection requires keeping untrusted data separate from commands and queries.
		The preferred option is to use a safe API which avoids the use of the interpreter entirely or provides a parameterized interface. Be careful with APIs, such as stored procedures, that are parameterized, but can still introduce injection under the hood.
		If a parameterized API is not available, you should carefully escape special characters using the specific escape syntax for that interpreter. OWASP’s ESAPI provides many of these escaping routines.
		Positive or “white list” input validation is also recommended, but is not a complete defense as many applications require special characters in their input. If special characters are required, only approaches 1. and 2. above will make their use safe. OWASP’s ESAPI has an extensible library of white list input validation routines.
	https://www.owasp.org/index.php/Top_10_2013-A1-Injection
	
A4 Insecure Direct Object References:
	The application uses unverified data in a SQL call that is accessing account information:
		String query = "SELECT * FROM accts WHERE account = ?";
		PreparedStatement pstmt = connection.prepareStatement(query , … );
		pstmt.setString( 1, request.getParameter("acct"));
		ResultSet results = pstmt.executeQuery( );
	The attacker simply modifies the ‘acct’ parameter in their browser to send whatever account number they want. If not verified, the attacker can access any user’s account, instead of only the intended customer’s account.
		http://example.com/app/accountInfo?acct=notmyacct
	Preventing insecure direct object references requires selecting an approach for protecting each user accessible object (e.g., object number, filename):
		Use per user or session indirect object references. This prevents attackers from directly targeting unauthorized resources. For example, instead of using the resource’s database key, a drop down list of six resources authorized for the current user could use the numbers 1 to 6 to indicate which value the user selected. The application has to map the per-user indirect reference back to the actual database key on the server. OWASP’s ESAPI includes both sequential and random access reference maps that developers can use to eliminate direct object references.
		Check access. Each use of a direct object reference from an untrusted source must include an access control check to ensure the user is authorized for the requested object.
	https://www.owasp.org/index.php/Top_10_2013-A4-Insecure_Direct_Object_References
A6 Sensitive Data Exposure:
	Scenario #1: An application encrypts credit card numbers in a database using automatic database encryption. However, this means it also decrypts this data automatically when retrieved, allowing an SQL injection flaw to retrieve credit card numbers in clear text. The system should have encrypted the credit card numbers using a public key, and only allowed back-end applications to decrypt them with the private key.
	Scenario #2: A site simply doesn’t use SSL for all authenticated pages. Attacker simply monitors network traffic (like an open wireless network), and steals the user’s session cookie. Attacker then replays this cookie and hijacks the user’s session, accessing the user’s private data.
	Scenario #3: The password database uses unsalted hashes to store everyone’s passwords. A file upload flaw allows an attacker to retrieve the password file. All of the unsalted hashes can be exposed with a rainbow table of precalculated hashes.
	The full perils of unsafe cryptography, SSL usage, and data protection are well beyond the scope of the Top 10. That said, for all sensitive data, do all of the following, at a minimum:
		Considering the threats you plan to protect this data from (e.g., insider attack, external user), make sure you encrypt all sensitive data at rest and in transit in a manner that defends against these threats.
		Don’t store sensitive data unnecessarily. Discard it as soon as possible. Data you don’t have can’t be stolen.
		Ensure strong standard algorithms and strong keys are used, and proper key management is in place. Consider using FIPS 140 validated cryptographic modules.
		Ensure passwords are stored with an algorithm specifically designed for password protection, such as bcrypt, PBKDF2, or scrypt.
		Disable autocomplete on forms collecting sensitive data and disable caching for pages that contain sensitive data.
	https://www.owasp.org/index.php/Top_10_2013-A6-Sensitive_Data_Exposure
