# ml-service
Example Machine Learning service.

# Components
* Registry: tracking server used for experiment tracking, metadata management, model versioning.
* Registry Backend: database backend which stores experiment metadata.
* Artifact Store: file storage for experiment artifacts (models, datasets, etc).
* Service: client interface to model.