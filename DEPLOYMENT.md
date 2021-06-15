# Deployment guide
This includes instructions for deploying Hermes in the Clinical Genomics :hospital: setting. General instructions for deployment is in the [development guide][development-guide]

## Branch model

hermes is following the [GitHub flow][gh-flow] branching model which means that every time a PR is merged to master a new release is created.

## Requirements

- [poetry]

## Steps

1. Check in the PR if the change is a minor, mayor or patch.
1. Make sure you are on `main` (`git checkout main`)
1. Bump version according using poetry: `poetry version <patch | minor | major>` to step 1 with git, example: `git tag 0.2.0`
1. Push the commit: `git push --tags`
1. First deploy on stage so log into hasta and run:
    - `us`
    - `cg deploy hermes`
1. Deploy in productions by running the following commands:
    - `down`
    - `up`
    - `cg deploy hermes`
1. Take a screen shot that includes the name of the environment and publish it as a comment on the PR: ![Deployed][confirm-deploy]
1. Great job :whale2:





[poetry]: https://python-poetry.org/docs/#installation
[confirm-deploy]: docs/img/confirm_deploy.png
[development-guide]: http://www.clinicalgenomics.se/development/publish/prod/
[gh-flow]: http://www.clinicalgenomics.se/development/dev/models/#rolling-release-github-flow
