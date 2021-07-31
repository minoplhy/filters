# Container image that runs your code
FROM debian

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY github-filters.sh /github-filters.sh
RUN apt-get update && apt-get install -y curl && apt-get install -y git
# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/github-filters.sh"]
