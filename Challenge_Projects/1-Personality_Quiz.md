# Challenge Project: Personality Quiz

<img src="https://i.pinimg.com/originals/c8/67/d7/c867d7bed74dcd85220972edfc1a7cc7.jpg" width="40%" />

## Due 

## Introduction

Personality quizzes. Is there a better way to learn about yourself than answering nonsensical questions written by randos on the Internet? I think not!

- Which Hogwarts house are you in? (Slytherin, but I'd pretend to be Hufflepuff).
- Which Disney heroine are you? (Maid Marian from *Robin Hood*).
- [Myers-Briggs personality type](https://www.myersbriggs.org/my-mbti-personality-type/mbti-basics/the-16-mbti-types.htm)? (INTP).
- [Enneagram type](https://www.narrativeenneagram.org/tour-the-nine-types/)? (3, and far more useful than Myers-Briggs, in my opinion).
- [What Pokémon type are you](https://www.buzzfeed.com/sarahtooley5/what-pokamon-type-are-you-248el1snke)? (Poison).
- [Which minor villain from "Jojo's Bizarre Adventure" are you](https://www.buzzfeed.com/puppetmaster64/which-minor-jojo-villain-are-you-42nxcnqrfi)? (Steely Dan, and I didn't even have to make that up).

Buzzfeed is still the leading purveyor of these online quizzes, offering insight into, for example, how [your controversial anime opinions will reveal your true Hogwarts house](https://www.buzzfeed.com/shualien/tell-us-some-of-your-unpopular-anime-opinions-and-aailsw3wr0).

In this project, you're going to use your knowledge of culture, relationships, and Python to write a program that implements a Buzzfeed-style personality quiz. Your quiz can be about anything that you want. This program will let you practice writing a completely self-designed program that's a bit larger than anything we've done so far.

## Quiz Design

There are a number of ways to implement online quizzes. We're going to use the approach described in [this article](https://www.buzzfeed.com/annakopsky/everything-you-need-to-know-to-make-a-buzzfeed-personality).

First, determine the title and "hook" for your quiz. What's it going to be about? Then decide on 3-6 outcomes that will be the results the user sees at the end.

Each possible question answer in your quiz will correspond to one of your 3-6 final outcomes. Each time the user answers a question, assign a point to the associated outcome. At the end of the quiz, pick the final outcome with the most total points.

## Example

<img src="https://ahseeit.com//king-include/uploads/2021/05/43915181_326611507924503_5421316365027478799_n-7515047846.jpg" width="40%" />

