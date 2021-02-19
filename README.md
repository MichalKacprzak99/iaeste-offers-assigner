# Offer Assigner
![GitHub top language](https://img.shields.io/github/languages/top/MichalKacprzak99/iaeste-offers-assigner)
![GitHub](https://img.shields.io/github/license/MichalKacprzak99/iaeste-offers-assigner)
![GitHub last commit](https://img.shields.io/github/last-commit/MichalKacprzak99/iaeste-offers-assigner)
## Table of Content
* [Project Description](#project-description)
* [Demo](#demo)
* [Further Development](#further-development)
## Project Description
I am a member of [IAESTE AGH](https://agh.iaeste.pl/) and the main goal of this 
organization is to enable students to go abroad for internships. 
Students wishing to do such an internship are classified on the basis of their average grade
and knowledge of the English language. Each candidate can choose 3 offers they are interested in. 
The team responsible for the exchange process must assign offers to the students by ranking. 
This program is designed to automate this task.
## Demo
Assume that we have an Excel file with candidates which looks like this:

<a href="https://ibb.co/K5LZYGs">
<img src="https://i.ibb.co/cyC5Pv8/candidates.png" alt="candidates" border="0">
</a>

After running program the **`results.ods`** file will be created and will looks like:

<a href="https://ibb.co/ZT8b8dW">
<img src="https://i.ibb.co/NYjGjxZ/results.png" alt="results" border="0">
</a>

Candidates are sorted by their point and if possible, 
each candidate is assigned to an offer.

## Further development
- [ ] optimize finding offers
- [ ] automate sending email to candidate
- [ ] better data preprocessing
- [ ] create executable