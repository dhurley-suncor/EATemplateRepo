# EATemplateRepo
EA Template Repository Example

# Prerequisites
The below prerequisites must be installed before proceeding with setup steps.
* conda

# Setup
1. Clone this repository and navigate to the root
2. Open `environment.yaml` and update `name: `
3. Open a terminal and run `export my_env_name="<name>"` - replace `<name>` with that in step 2.
4. Open a  terminal and run `source setup.sh` - this will build the use case environment.

Since most group members are using windows and we are shifting away from Azure ML it is not easy to implement Makefile for everyone. This is why we are using a `setup.sh`. We could switch to `.devcontainer` or other dockerized methods but for now this is maybe more universal across machines.
