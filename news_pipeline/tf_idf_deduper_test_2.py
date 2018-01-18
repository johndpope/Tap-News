# -*- coding: utf-8 -*

from sklearn.feature_extraction.text import TfidfVectorizer

news1 = """
Derek Carr got his new contract from the Oakland Raiders last week -- a sweet, $25-million-a-year job with $40 million in full guarantees at the time of signing. It's the latest big quarterback deal to be handed out, but it surely won't be the last.\n\nWho will be next? Which quarterbacks will be looking for (and receiving) new contracts in the coming months and years? Let's take a look at the next several guys in line for big quarterback deals and hereby present our best guess as to the order in which they will sign them.\n\nWith one year and $16.5 million left on his contract, Stafford and his agent have already had some talks with the Lions about an extension. There's a strong likelihood it gets done before the 2017 season starts, as it would cost the Lions $26.4 million to franchise Stafford next year and more than $31 million the year after that. Having recently seen star defensive tackle Ndamukong Suh price himself out of Detroit due to high franchise tag numbers, the Lions know the dangers of delaying this too long.\n\nEditor's Picks Derek Carr's deal doesn't shock the QB market The Raiders quarterback now is the league's \"highest-paid player\" on a deal that is perfect for him, but the $125 million extension fails to shake up the marketplace for other signal-callers.\n\nBarnwell: The NFL's top QB deals ... and a little reality Derek Carr got a massive deal Thursday, but he also taught us a lesson in NFL contracts. 1 Related\n\nBut Stafford, who has five years and 19,000 yards on Carr, will look to beat that $25 million average annual salary. Agent Tom Condon, whose big-money quarterback client list includes Eli Manning, Drew Brees and Philip Rivers, will be paying close attention to the guaranteed money and the schedule for those guarantees paying out. Carr's deal delays the guaranteed payments year to year after the first two seasons. Condon's recent deals tend to make sure the first two and three years house the big money and big guarantees. And since Condon also has Matt Ryan, who'll be due an extension this time next year, he'll be interested in trying to elevate the ceiling here on a Stafford deal.\n\n2. Drew Brees, New Orleans Saints\n\nThe Saints' 38-year-old future Hall of Famer did an extension last year that voids after this season, which means he'd be a free agent at 39. Coming off his fifth 5,000-yard passing season (no one else in history has had more than one), Brees doesn't appear to be slowing down. But he does appear content to go year-to-year on his contract at this point and to want to finish his career in New Orleans. It's not a stretch to imagine he and the Saints do another one-year extension before this season starts.\n\nJust putting it here because it's worth watching to see whether Brady gets any new money added to his deal this offseason. He signed a two-year, $41 million extension last offseason that included a $28 million signing bonus. Three years earlier, he did a deal that came with a $30 million signing bonus. So there's precedent here. Brady's current deal runs through 2019, and since he turns 40 in August it's hard to imagine the Patriots adding years at this point. But with a base salary of just $1 million this year, Brady wouldn't be nuts to expect another new-money \"extension\" that comes with a similarly sized ($25 million-$30 million) signing-bonus reward and reworks the remaining years on the deal. Should this get done soon, it could help set a framework for any new deal Brees might want to do with the Saints, now or next spring.\n\nTom Brady could be in line for another extension that comes with a big signing bonus. Greg M. Cooper/USA TODAY Sports\n\nBradford's contract runs out after this season, as does that of fellow Minnesota quarterback Teddy Bridgewater, whose catastrophic training camp injury last summer is the reason Bradford is in Minnesota in the first place. Bradford, who set the single-season record for completion percentage in 2016, is making $18 million this year in salary and bonuses. His future in Minnesota is tied to Bridgewater's: If the Vikings are encouraged by Bridgewater's health this summer and fall, that will lessen their need to do a deal with Bradford that would head off his unrestricted free agency. If Bridgewater's health and/or Bradford's performance give the Vikings reason to believe the 29-year-old veteran is their better long-term option, this is another Condon client who could be in line for a nice extension sometime this calendar year.\n\n5. Kirk Cousins, Washington\n\nThe team's designated franchise player for the second year in a row, Cousins is fully guaranteed a $23,943,600 salary for this season and nothing thereafter. If Washington doesn't sign Cousins to a long-term deal before July 17, franchise-tag rules say it cannot negotiate one with him until after the end of its 2017 season. Which means, if they don't get an extension done in the next three weeks, Cousins could become an unrestricted free agent in March. It would cost Washington nearly $35 million to franchise Cousins again in 2018, and $28.8 million to use the transition tag on him. Cousins' 2017 guarantee means he would need much more than Carr to sign by the July 17 deadline, and so far the team has been unwilling to offer him the kind of deal that would entice him away from the promises of unrestricted free agency with multiple teams bidding next spring. The bet here is that he hits the market and gets more than $30 million a year on his new deal, setting a new benchmark for quarterback salaries.\n\n6. Matt Ryan, Atlanta Falcons\n\nIf Cousins or Stafford or someone gets to free agency in March and blows through that $30 million-a-year barrier, the reigning league MVP would go into next summer with one year left on his contract and looking to do an extension with Atlanta that would elevate that ceiling even higher. Ryan is making $18.15 million in salary and bonuses this year and $21.65 million in 2018. A repeat of his 2016 performance would put him in a position to become the highest-paid player in the league at this time next year, regardless of the deals his peers do or don't get in the meantime.\n\nMatt Ryan has a chance to become the NFL's highest-paid player when he does his next contract. AP Photo/Eric Gay\n\nThe Jags hold a $19.053 million option on Bortles for 2018, but that's only guaranteed against injury right now. It doesn't become fully guaranteed until the start of the 2018 league year. If the Jags decide to move on from Bortles before then, he's not likely to get any kind of major extension. But if they decide he's their guy for the long term (or even just for 2018), then he's positioned for an extension sometime next summer or the one after that. And it'll be worth watching even if he's not elite. Bortles' next deal could serve as a floor for contract expectations to come for mid-tier QBs who outperform him.\n\nYeah, remember him? If you just ranked all the quarterbacks in the league based on quality, Rodgers would deserve to earn the most. But he signed a long-term extension in 2013 that runs through 2019, which means he's probably two years away from being able to demand an extension. By that time, Rodgers' $22 million average annual salary will look antiquated and silly. It's possible Green Bay could look to do a deal sooner than the summer of 2019 if they need cap help or if they just want to do right by their superstar quarterback. But since Rodgers will be 36 at the end of his current contract, they might prefer to wait. And given what could happen to the top of the quarterback market in the next year or two, Rodgers might prefer to wait, as well.\n\nWilson's deal runs through 2019, as well, which means he'd be looking at an extension two summers from now. Wilson will turn 31 during that 2019 season. He could be in line to score a longer extension than even Rodgers.\n\nRussell Wilson should get at least one more big contract in his career. Otto Greule Jr/Getty Images\n\nOTHERS TO WATCH\n\n2019 Free Agents\n\nTyrod Taylor has two years to show the Buffalo Bills he's a franchise quarterback, and if he does, he could be in line for a big deal heading into 2019.\n\nAlex Smith could be out after this year with the Kansas City Chiefs, but if that's the case, he likely isn't getting another big deal. Smith's best bet is to play lights-out for the next two years and hit free agency when it's time for Patrick Mahomes II to take over in K.C.\n\n2020 Free Agents\n\nDak Prescott's deal runs through the 2019 season, and since he was not a first-round pick, the Dallas Cowboys don't hold his fifth-year option. They're not allowed to do an extension with him until after 2018. So assuming Prescott continues to play well, he'll be talking extension with the Cowboys two summers from now, and it could be a doozy.\n\nMarcus Mariota in Tennessee and Jameis Winston in Tampa Bay were first-rounders in 2015, which means 2019 would be their fifth-year-option seasons and they'd be due for extensions either that summer or the summer of 2020. (Andrew Luck signed his extension before his option year.) What's worth watching about the summer of 2020 is that, as of now, there would be only one year left on the CBA. Depending on the labor climate and the expectations for the new deal (assuming it's not in place by then), 2020 free agents could be inclined to wait and risk the franchise tag.\n\nThe current contracts of Eli Manning, Philip Rivers, Ben Roethlisberger and Tom Brady all expire after 2019. While it's not impossible to think one or more of them could get extensions in the meantime, those players will be 39, 38, 37 and 42, respectively, at the end of the 2019 season. There's a strong chance each is already on the final deal of his career, and any extension these guys get at this point would be closer to what Brees is doing than what Carr, Stafford and Cousins are eyeing.\n\nThe Cowboys will get Dak Prescott on the cheap for the next two seasons before he's eligible for an extension. Tom Pennington/Getty Images\n\n2021 Free Agents\n\nJared Goff and Carson Wentz, the top two picks in the 2016 draft, would be fifth-year-option players in 2020 and eligible for free agency or the franchise tag in 2021. Obviously, it's far too early for forecast where either might fit into the bigger quarterback-contract picture by that point, but keep an eye on their agents, the California-based Tollner brothers. They represent not only Roethlisberger, but also Wentz, Goff, Mariota, Blake Bortles and Mitchell Trubisky. The way Condon has helped dictate the quarterback market for the past couple of decades, the Tollners could be in a position to help shape the coming wave of QB deals.\n\nCarolina's Cam Newton and Cincinnati's Andy Dalton are the two big veteran quarterbacks whose deals run through 2020 at this point. The Panthers and Bengals can get out of those deals with relatively little pain after 2018. But assuming each continues to perform as a franchise quarterback, Newton would be 31 and Dalton would be 32 when they'd be looking for extensions in the summer of 2020.\n\nThe Miami Dolphins' Ryan Tannehill is another one worth watching here. He has signed through 2020 on a deal that averages $19.25 million per year. He's not as established yet as Newton and Dalton are, but he showed promise in his first year under Adam Gase and continued production could put him on a big-contract track.\n\n2022 Free Agents\n\nThis would include any quarterback drafted in the first round this year -- Mitchell Trubisky, Patrick Mahomes II and Deshaun Watson, whose fifth-year-option seasons would be 2021. But again, too early to know on any of them.\n\nThe veterans whose current deals run out after 2021 include Andrew Luck, who will be 31 that summer and possibly in line to set a contract record for the second time in his career, and Joe Flacco, who will be 36 and probably has already made his money.\n\n2023 Free Agents\n\nDerek Carr! He'll be 31 in the summer of 2022, when there will be one year left on the deal he just signed. And yeah, that brings this exercise to a close.
"""
news2 = """
President Donald Trump on Saturday again attacked a federal judge whose decision he disliked, criticizing Judge James Robart, a George W. Bush appointee who temporarily stopped his controversial travel ban Friday night.
President Trump’s attacks quickly drew objections from Democrats, who said he was attacking an independent judiciary. And by Saturday afternoon, President Trump was openly accusing Robart of potentially allowing “many very bad and dangerous people” to flow into the US and warning of dire consequences if the executive order is not enforced.
He also said, “What is our country coming to when a judge can halt a Homeland Security ban and anyone, even with bad intentions, can come into the U.S.?”
What is our country coming to when a judge can halt a Homeland Security travel ban and anyone, even with bad intentions, can come into U.S.?
— Donald J. Trump (@realDonaldTrump) February 4, 2017
Shortly after 8 a.m. ET, the President tweeted, “The opinion of this so-called judge, which essentially takes law-enforcement away from our country, is ridiculous and will be overturned.”
The opinion of this so-called judge, which essentially takes law-enforcement away from our country, is ridiculous and will be overturned!
— Donald J. Trump (@realDonaldTrump) February 4, 2017
The tweet was one of several President Trump issued Saturday morning in which he defended his executive order on immigration, which bars citizens of seven Muslim-majority countries from entering the US for 90 days, all refugees for 120 days and indefinitely halts refugees from Syria.
“When a country is no longer able to say who can, and who cannot , come in & out, especially for reasons of safety &.security – big trouble,” President Trump next tweeted.
When a country is no longer able to say who can, and who cannot , come in & out, especially for reasons of safety &.security – big trouble!
— Donald J. Trump (@realDonaldTrump) February 4, 2017
“Interesting that certain Middle-Eastern countries agree with the ban. They know if certain people are allowed in it’s death & destruction,” he added, though he didn’t name any countries.
Interesting that certain Middle-Eastern countries agree with the ban. They know if certain people are allowed in it's death & destruction!
— Donald J. Trump (@realDonaldTrump) February 4, 2017
Saturday afternoon, President Trump resumed his criticism, tweeting: “What is our country coming to when a judge can halt a Homeland Security travel ban and anyone, even with bad intentions, can come into U.S.?”
He followed up with, “Because the ban was lifted by a judge, many very bad and dangerous people may be pouring into our country. A terrible decision.”
Because the ban was lifted by a judge, many very bad and dangerous people may be pouring into our country. A terrible decision
— Donald J. Trump (@realDonaldTrump) February 4, 2017
It is highly unusual for a President to publicly criticize a federal judge, but during the campaign, President Trump memorably railed against Judge Gonzalo Curiel, who was overseeing a lawsuit against Trump University. President Trump said Curiel, who was born in Indiana, was unable to fairly preside over the lawsuit because of his “Mexican heritage.” President Trump had introduced plans to build a wall along the Mexican border and take a hard stance on immigration.
Democrats pounced on President Trump’s criticism of Robart, with Democratic senators flatly saying the President’s comments will factor into the confirmation hearings for Supreme Court nominee Neil Gorsuch.
“Attack on federal judge from POTUS is beneath the dignity of that office. That attitude can lead America to calamity,” Washington Gov. Jay Inslee tweeted Saturday.
Attack on federal judge from POTUS is beneath the dignity of that office. That attitude can lead America to calamity.
— Governor Jay Inslee (@GovInslee) February 4, 2017
“The President’s attack on Judge James Robart, a Bush appointee who passed with 99 votes, shows a disdain for an independent judiciary that doesn’t always bend to his wishes and a continued lack of respect for the Constitution, making it more important that the Supreme Court serve as an independent check on the administration,” Senate Minority Leader Chuck Schumer said in a statement.
“With each action testing the Constitution, and each personal attack on a judge, President Trump raises the bar even higher for Judge Gorsuch’s nomination to serve on the Supreme Court. His ability to be an independent check will be front and center throughout the confirmation process.”
Vermont. Sen. Patrick Leahy, the ranking member of the Judiciary Committee, said President Trump’s “hostility toward the rule of law is not just embarrassing, it is dangerous.”
“We need a nominee for the Supreme Court willing to demonstrate he or she will not cower to an overreaching executive. This makes it even more important that Judge Gorsuch, and every other judge this president may nominate, demonstrates the ability to be an independent check and balance on an administration that shamefully and harmfully seems to reject the very concept.”
Robart’s order on Friday was a significant setback to President Trump’s ban and set up the nation for a second straight weekend of confusion about the policy’s legality.
The White House said Friday the Department of Justice will challenge the decision. In a statement, White House press secretary Sean Spicer initially called Robart’s order “outrageous” before quickly issuing another statement that dropped that word.
Robart has presided in the US District Court for the Western District of Washington state since 2004. He assumed senior status in 2016.
"""

documents = [news1, news2]

tfidf = TfidfVectorizer().fit_transform(documents)
pairwise_sim = tfidf * tfidf.T 

print pairwise_sim.A