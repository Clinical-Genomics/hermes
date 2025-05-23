# Deployment guide
This includes instructions for deploying Hermes in the Clinical Genomics :hospital: setting.

## Steps
When all tests are done and successful and the PR is approved by codeowners, follow these steps:

### Deploy feature branch for testing
To deploy your feature branch to test it, run
1. `hermes-test-deploy <branch_name>`
2. `hermes-test --help` or the command you want to test.

This will pull the latest image tagged with your branch from Dockerhub and make it available with `hermes-test`. Note that it is not necessary to paxa the environment to do this.


### Deploy to stage and production
1. Select "Squash and merge" to merge branch into default branch (master/main).
2. Append version increment value `( major | minor | patch )` in the commit message to specify what kind of release is to be created.
3. Review the details and merge the branch into master.
4. Deploy the latest version to stage and production with `hermes-deploy`.
5. Take a screenshot or copy log text and post as a comment on the PR. Screenshot should include environment and that it succeeded.
6. Great job :whale2: