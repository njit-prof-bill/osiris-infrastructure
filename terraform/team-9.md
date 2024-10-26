
# Team TBD - Team 9 - Terraform Scripts and Infrastructure Management

### Team Members: Jeremy Kurian, Ari Kamat, Safwan Noor, Noah Paul, Haitham Awad

Trello: [https://trello.com/invite/b/671d7336f9029021da68dfb0/ATTI8d745f8caad0f22d3da337a181ae6775EA58340B/cs490-tbd-team-9](https://trello.com/invite/b/671d7336f9029021da68dfb0/ATTI8d745f8caad0f22d3da337a181ae6775EA58340B/cs490-tbd-team-9)

### Technologies Used

-   Tech Stack: Python, FastAPI, Swagger (for documentation), pytest (for testing), python-terraform, docker (dockerfile), jsonify
    
-   Language: Python
    
-   Framework: FastAPI
    
-   Libraries: Swagger (for docs), pytest (for testing), python-terraform, docker, jsonify
    

### Workflow

-   **Feature** branches for each API task -> Merges feature branches into **Develop** branch, merges develop branch into **prod/master** branch
    
-   Needs code reviews by two people before merging into develop branch
    
-   Integration testing is needed before merging into master/prod
    
-   Unit tests for all API functions, minimum 70% test coverage
    

  

## Assignments

### Jeremy Kurian (Project Manager)
    

-   Frequently check in with developers to follow timeline
    
-   - **API 1**: `Initialize Terraform Command` - Implement the initTerraform API, which initializes a new Terraform configuration by downloading necessary providers and modules.
    
-   - **API 2**: `Plan Terraform Infrastructure Command` - Implement the planTerraform API, which generates and displays an execution plan for provisioning infrastructure using Terraform.
    
-   Delegate Tasks
    

### Ari Kamat
    

-   - **API 3**: `Apply Terraform Configuration Command` - Implement the applyTerraform API, which applies a Terraform configuration to provision or update infrastructure.
    
-   - **API 4**: `Destroy Terraform Infrastructure Command` - Implement the ``destroyTerraform`` API, which destroys all resources managed by a Terraform configuration.
    
-   Integration testing
    

### Safwan Noor
    

-   - **API 5**: `Refresh Terraform State Command` - Implement the ``refreshTerraformState`` API, which updates the Terraform state file to match the current real-world infrastructure.
    
-   - **API 6**: `Validate Terraform Configuration Command` - Implement the ``validateTerraform`` API, which validates a Terraform configuration to check for errors and best practices.
    

### Noah Paul
    

-   - **API 7**: `Output Terraform Variables Command` - Implement the ``getTerraformOutput`` API, which retrieves output values from a Terraform configuration after applying it.
    
-   - **API 8**: `Lock Terraform State Command` - Implement the ``lockTerraformState`` API, which locks the Terraform state to prevent multiple users or processes from modifying the same infrastructure at the same time.
    
### Haitham Awad
    

-   - **API 9**: `Unlock Terraform State Command` - Implement the unlockTerraformState API, which unlocks the Terraform state after infrastructure operations are complete.
    
-   - **API 10**: `Import Existing Resources Command` - Implement the ``importTerraformResource`` API, which imports an existing infrastructure resource into the Terraform state file for management.
    

  

## Each team member will also continuously do code reviews, and documentation, and write unit tests for API functions that they have developed.