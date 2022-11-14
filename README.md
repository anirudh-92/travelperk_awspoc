
### CI/CD

The repository leverages the [AWS Github Actions](https://github.com/aws-actions/)
maintained by AWS.

The main goal is to provide an example configuration of the following workflow:

- Run the integration tests
- Build the Docker image
- Publish it to a private ECR
- Update the corresponding ECS Service (by editing the task image)
