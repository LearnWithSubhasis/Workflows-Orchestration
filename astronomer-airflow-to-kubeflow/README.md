# Steps for complex DAG, calling kubeflow pipeline from airflow DAG

## 1. Install Docker Desktop for Mac
https://docs.docker.com/desktop/install/mac-install/

NOTE: If you are using Linux or Windows OS, please follow relevant installation steps.

## 2. Install Astronomer
https://docs.astronomer.io/astro/cli/get-started

## 3. Initialize Astronomer Project
astro dev init
astro dev start

### 3.a. Access Astronomer UI
http://localhost:8080

admin/admin

## 4. Create New DAG 
Optional:
astro dev kill
astro dev start

or
astro dev restart

## 5. Run DAG

## 6. Terminate Astronomer Project
astro dev kill
