# Security policy

## Reporting a vulnerability

Please do not open a public issue for a security problem. Use GitHub's
private vulnerability reporting instead:

<https://github.com/ppruchnerovic/ai-talks-universe/security/advisories/new>

You will get an acknowledgement within a week. The project is maintained in
spare time, so a fix may take longer, and you will be told what to expect.

## What counts

This is a static site plus a set of Python scripts that run on a user's
machine. The things worth reporting are:

- anything that lets content in the corpus (a talk title, a description, a
  transcript) execute script or load a foreign resource in `index.html`;
- a tool that writes outside the repository, follows a redirect it should
  not, or leaks an API key into a file, a log or a URL;
- a GitHub Actions workflow that could be made to publish or commit
  something it should not.

Bugs in search ranking, missing talks and wrong metadata are ordinary issues.

## Content takedown

To have a talk removed from the corpus, open an issue or use the private
form above if you prefer not to post publicly. See
[`DATA-NOTICE.md`](DATA-NOTICE.md).
