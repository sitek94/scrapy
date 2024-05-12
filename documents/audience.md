# Audience

## Define your audience

Serious documentation efforts spend considerable time and energy on defining their audience. These efforts might involve
surveys, user experience studies, focus groups, and documentation testing. You probably don't have that much time, so
this unit takes a simpler approach.

Begin by identifying your audience's _role_(s). Sample roles include:

- Software engineers
- Technical, non-engineer roles (such as technical program managers)
- Scientists
- Professionals in scientific fields (for example, physicians)
- Undergraduate engineering students
- Graduate engineering students
- Non-technical positions

We happily appreciate that many people in non-technical roles have great technical and mathematical skills. However,
roles remain an essential first-order approximation in defining your audience. People within the same role _generally_
share certain base skills and knowledge. For example:

- Most software engineers know popular sorting algorithms, big O notation, and at least one programming language.
  Therefore, you can depend on software engineers knowing what O(n) means, but you can't depend on non-technical roles
  knowing O(n).
- A research report targeted at physicians should look very different from a newspaper article about the same research
  aimed at a lay audience.
- A professor's explanation of a new machine learning approach to graduate students should differ from the explanation
  to first-year undergraduate students.

Writing would be so much easier if everyone in the same role shared exactly the same knowledge. Unfortunately, knowledge
within the same role quickly diverges. Amal is an expert in Python, Sharon's expertise is C++, and Micah's is in Java.
Kara loves Linux, but David only knows iOS.

Roles, by themselves, are insufficient for defining an audience. That is, you must also consider your audience's
_proximity_ to the knowledge. The software engineers in Project Frombus know something about related Project Dingus but
nothing about unrelated Project Carambola. The average heart specialist knows more about ear problems than the average
software engineer but far less than an audiologist.

Time also affects proximity. Almost all software engineers, for example, studied calculus. However, most software
engineers don't use calculus in their jobs, so their knowledge of calculus gradually fades. Conversely, experienced
engineers typically know vastly more about their current project than new engineers on the same project.

### Sample audience analysis

The following is a sample audience analysis for fictitious Project Zylmon:

> The target audience for Project Zylmon falls into the following roles:

- Software engineers
- Technical product managers

The target audience has the following proximity to the knowledge:

- My target audience already knows the Zyljeune APIs, which are somewhat similar to the Zylmon APIs.
- My target audience knows C++, but has not typically built C++ programs in the new Winged Victory development
  environment.
- My target audience took linear algebra in university, but many members of the team need a refresher on matrix
  multiplication.

## Determine what your audience needs to learn

Write down a list of everything your target audience needs to learn to accomplish goals. In some cases, the list should
hold tasks that the target audience needs to _perform_. For example:

> After reading the documentation, the audience will know how to do the following tasks:

- Use the Zylmon API to list hotels by price.
- Use the Zylmon API to list hotels by location.
- Use the Zylmon API to list hotels by user ratings.

Note that your audience must sometimes master tasks in a certain order. For example, your audience might need to learn
how to build and execute programs in a new development environment _before_ learning how to write particular kinds of
programs.

If you are writing a design spec, then your list should focus on information your target audience should learn rather
than on mastering specific tasks. For example:

> After reading the design spec, the audience will learn the following:

- Three reasons why Zylmon outperforms Zyljeune.
- Five reasons why Zylmon consumed 5.25 engineering years to develop.

## Fit documentation to your audience

Writing to meet your audience's needs requires unselfish empathy. You must create explanations that satisfy your
audience's curiosity rather than your own. How do you step out of yourself in order to fit documentation to the
audience? Unfortunately, we can offer no easy answers. We can, however, offer a few parameters to focus on.

### Vocabulary and concepts

Match your vocabulary to your audience. See [Words](/tech-writing/one/words) for help.

Be mindful of proximity. The people on your team probably understand your team's abbreviations, but do people on other
teams understand those same abbreviations? As your target audience widens, assume that you must explain more.

Similarly, experienced people on your software team probably understand the implementation details and data structures
of your team's project, but nearly everyone else (including new members of your team) does not. Unless you are writing
specifically for other experienced members of your team, you typically must explain more than you expect.

### Curse of knowledge

Experts often suffer from _the curse of knowledge_, which means that their expert understanding of a topic ruins their
explanations to newcomers. As experts, it is easy to forget that novices don’t know what you already know. Novices might
not understand explanations that make passing reference to subtle interactions and deep systems that the expert doesn’t
stop to explain.

From the novice's point of view, the curse of knowledge is a "File not found" linker error due to a module not yet
compiled.

### Simple words

English has become the dominant language for technical communication worldwide. However, a significant percentage of
technical readers are more comfortable in languages other than English. Therefore, prefer simple words over complex
words; avoid obsolete or overly-complex English words. [Sesquipedalian](https://www.google.com/search?q=sesquipedalian)
and rare words repel some readers.

### Cultural neutrality and idioms

Keep your writing culturally neutral. Do not require readers to understand the intricacies of NASCAR, cricket, or sumo
in order to understand how a piece of software works. For example, the following sentence—packed with baseball metaphors
as American as apple pie—might puzzle some Parisian readers:

> If Frambus 5.0 was a solid single, Frambus 6.0 is a stand-up double.

_Idioms_ are phrases whose overall meaning differs from the literal meaning of the individual words in that phrase. For
example, the following phrases are idioms:

- a piece of cake
- Bob's your uncle

Cake? Bob? Most readers from the United States recognize the first idiom; most British readers recognize the second
idiom. If you are writing strictly for a British audience, then _Bob's your uncle_ can be fine. However, if you are
writing for an international audience, then replace that idiom with _this task is done_.

Idioms are so deeply ingrained in our speech that the special nonliteral meaning of idioms becomes invisible to us. That
is, idioms are another form of the curse of knowledge.

Note that some people in your audience use translation software to read your documentation. Translation software tends
to struggle more with cultural references and idioms than with plain, simple English.