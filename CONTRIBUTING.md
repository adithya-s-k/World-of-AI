# 🎇Contributing Guidelines

This documentation contains a set of guidelines to help you during the contribution process.

I'm happy to welcome all contributions from anyone willing to add new scripts to this repository. Thank you for helping out, and remember, **no contribution is too small.**

## 💻Before Contributing

Welcome to [AI Simplified](https://github.com/CognitiveLab-io/AI-Simplified). Before sending your pull requests, make sure that you **read the whole guidelines**. If you have any doubt about the contributing guide, please feel free to reach out.

## 🙌Contribution

Any contribution is accepted, from fixing grammatical mistakes to implementing complex algorithms. Please read this section if you are contributing to your work.

### 🔖Steps to Contribute

Following are the steps to guide you:

- Step 1: Fork the repo and Go to your Git terminal and clone it on your machine.
- Step 2: Add an upstream link to the main branch in your cloned repo
  ```
  git remote add upstream https://github.com/CognitiveLab-io/AI-Simplified.git
  ```
- Step 3: Keep your cloned repo up to date by pulling from upstream (this will also avoid any merge conflicts while committing new changes)
  ```
  git pull upstream main https://github.com/CognitiveLab-io/AI-Simplified.git
  ```
- Step 4: Create your feature branch (This is a necessary step, so don't skip it)
  ```
  git checkout -b <feature-name>
  ```
- Step 5: Commit all the changes (Write commit message as "Small Message")
  ```
  git commit -m "Write a meaningful but small commit message"
  ```
- Step 6: Push the changes for review
  ```
  git push origin <branch-name>
  ```
- Step 7: Create a PR on Github. (Don't just hit the create a pull request button, you must write a PR message to clarify why and what are you contributing)

### 🔨Note:

> - Do not edit/delete someone else's code in this repository. You can only insert new files/folders in this repository.

> - Give a meaningful name to whatever file or folder you are adding. (For example, if you have written an AI code on Loan Prediction, then `loan_prediction.ipynb` is one example of a valid name)

## 🔑Guidelines

1. Welcome to this repository if you are here as an open-source program participant/contributor.
2. Participants/contributors have to **comment** on issues they would like to work on, and mentors or the PA will assign you.
3. Issues will be assigned on a **first-come, first-serve basis.**
4. Participants/contributors can also **open their issues** using [issue_template], but it needs to be verified and labeled by a mentor or PA. Please discuss with the team once before opening your issues. We respect all your contributions, whether it is an issue or a pull request.
5. When you raise an issue, make sure you get it assigned to you before you start working on that project.
6. Each participant/contributor will be **assigned 1 issue (max)** at a time to work.
7. Participants are expected to follow **project guidelines** . **Structured code** is one of our top priorities.
8. Try to **explain your approach** to solve any issue in the comments. This will increase the chances of you being assigned.
9. Don't create issues that are **already listed.**
10. Please don't pick up an issue already assigned to someone else. Work on the issues after it is **assigned to you**.
11. Make sure you **discuss issues** before working on the issue.
12. Pull requests will be merged after being **reviewed** by a mentor or PA.
13. It might take **a day or two** to review your pull request. Please have patience and be nice.
14. Always create a pull request from a **branch** other than `main`.
15. Participants/contributors have to complete issues before the decided deadline. If you fail to make a PR within the deadline, then the issue will be assigned to another person in the queue.
16. While making PRs, don't forget to **add a description** of your work.
17. Include issue number (Fixes:issuenumber) in your commit message while creating a pull request.
18. Make sure your solution to any issue is better in terms of performance and other parameters in comparison to the previous work.
19. We all are here to learn. You are allowed to make mistakes. That's how you learn,so don't be afraid to ask for help or guidance from the mentors or the community.

### 🧲Pull Requests Review Criteria

1. Please fill the **[PR Template]** properly while making a Pull Request.
2. You must add your code `.ipynb` file into the respective **folders**.
3. Your work must be original, written by you, not copied from other resources.
4. You must comment on your code where necessary.
5. For frontend changes, kindly share screenshots and work samples of your work before sending a PR.
6. Follow the proper [style guides](https://google.github.io/styleguide/) for your work.
7. For any queries or discussions, please feel free to drop a message.

## 📍Other points to remember while submitting your work:

We want your work to be readable by others; therefore, we encourage you to note the following:

- If Titanic Survival Prediction is submitted, for example, the Folder Name should be "Titanic Survival Prediction," and the File Name should be "titanic_survival_prediction.ipynb."
- File extension for code should be `.ipynb`.
- Strictly use snake_case (underscore_separated) in your file_name, as it will be easy to parse in the future using scripts.
- Please avoid creating new directories if at all possible. Try to fit your work into the existing directory structure you have created for your project. If you want to, please contact before doing so.
- The basic project folder should have 2 repositories: Dataset and Model. Dataset should have the related dataset files for the project to work, and Model should have the program file and other related files concerning the project for AI, Deep learning, Computer Vision, NLP enthusiasts.
- The [README.md] file should be concise and clear about what the project is about and what it does.
- It should be documented briefly enough to let readers understand.
- If you have modified/added code work, make sure that the algorithm works before submitting.
- If you have modified/added documentation work, ensure your language is concise and contains no grammar errors.
- For front-end designers, back-end developers, and UI/UX designers, follow the project structure mentioned in [README]
- Do not update the [README.md] and [Contributing_Guidelines.md].
- Avoid importing external libraries for basic algorithms. Only use those libraries for complicated algorithms. **Usage of NumPY is highly recommended.**

## 📖Resources

1. Markdown: Markdown is a lightweight markup language like HTML, with plain text formatting syntax.

- [Markdown Cheat-Sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

2. Git: Git is a distributed version-control system for tracking changes in source code during software development. It is designed for coordinating work among programmers, but it can be used to track changes in any set of files.

- [Videos to get started](https://www.youtube.com/watch?v=xAAmje1H9YM&list=PLeo1K3hjS3usJuxZZUBdjAcilgfQHkRzW)
- [Cheat Sheet](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet)

3. [PEP 8 style guide](https://pep8.org/)

## 🤔Need more help?

You can refer to the following articles on the basics of Git and Github and also contact the admins or mentors in case you are stuck:

- [Forking a Repo](https://help.github.com/en/github/getting-started-with-github/fork-a-repo)
- [Cloning a Repo](https://help.github.com/en/desktop/contributing-to-projects/creating-an-issue-or-pull-request)
- [How to create a Pull Request](https://opensource.com/article/19/7/create-pull-request-github)
- [Getting started with Git and GitHub](https://towardsdatascience.com/getting-started-with-git-and-github-6fcd0f2d4ac6)
- [Learn GitHub from Scratch](https://lab.github.com/githubtraining/introduction-to-github)

🎉 🎊 😃 Happy Contributing 😃 🎊 🎉

For more information about Cognitive Lab, please visit our [website](https://www.cognitivelab.tech/). To reach out to the admins, please visit our [admins link](https://github.com/adithya-s-k). To access the repository, please visit our [repo link](https://github.com/CognitiveLab-io/AI-Simplified).
