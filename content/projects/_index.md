---
title: "Projects"
draft: false
description: "As a freelance software and DevOps engineer based in Heidelberg, I offer tailor-made software solutions adapted to your requirements. My current focus lies on software architecture, backend development, data engineering, DevOps, and AWS."
type: "page"
---

### Development of a distributed orchestration system – 11.2022 – 02.2024

**Role:**  
Senior Software Developer

**Description:**  
A custom orchestration system, inspired by Kubernetes, was created to streamline the cloud provisioning process for hundreds of products across thousands of customers. This new orchestration system took inspiration from Kubernetes' “operator pattern” approach, enabling different teams to integrate their operators for tailored product provisioning. The architecture of the orchestration system was designed to ensure high scalability and availability including components such as API Server, Controller Manager, Namespaces, etc. to accommodate business requirements as well as ever growing load and number of customers. The provisioning system itself was hosted on a Kubernetes cluster within AWS.  

**Responsibilities:**
- Involved in architecture design of the system.
- Actively contributed to the development of multiple components,
including the API Server and Controller Manager.
- Development of multiple Kubernetes operators for essential core functionalities of the system.
- Designed and developed client SDKs to facilitate controller development
by various development teams.
- Integrated Prometheus as the primary tool for monitoring metrics
within the product.
- Provided support to numerous stakeholders throughout the project.

**Stack:**
`Go(lang)`, `WebSocket`, `OpenSearch`, `LocalStack`, `Redis`, `Prometheus`, `Grafana`, `AWS S3`, `Kubernetes`

---

### Elevating SAP Analytics Cloud’s SLA from 99.9% to 99.99% – 03.2022 – 11.2022

**Role:**
Technical Lead

**Description:**
To enhance the availability of the SAP Analytics Cloud product, it was necessary to elevate its Service Level Agreement (SLA) from 99.9% to 99.99%. Achieving this required extensive technical collaboration among various teams within the organization. The goal was to address existing bottlenecks in the current architecture design, which were causing extended system upgrade durations. Additionally, efforts were made to identify opportunities and possibilities for reducing the required upgrade downtime through improvements in component designs or overall system design.
      
**Responsibilities:**
- Conducting requirements analysis and effectively communicating with stakeholders.
- Facilitating collaboration among all stakeholders to clarify requirements and establish deadlines.
- Contributing to the design of the overall architecture.
- Validating ideas and concepts through prototyping and proof of
concepts.
- Defining a project timeline, budget, and the required number of team members (headcount).

---

### Enablement of SAP Analytics Cloud’s SaaS offering – 01.2021 – 03.2022

**Role:**
Senior Cloud Engineer

**Description:**
To enable the Software-as-a-Service (SaaS) offering of SAP Analytics Cloud (SAC) via the Cloud Foundry marketplace, we needed to develop a service broker, metering, and billing microservices. These components would facilitate communication with various backend services like capacity management and system provisioning, enabling customers to access the SAC product using a pay-as-you-go pricing model.
      
**Responsibilities:**
- Developed a service broker for Cloud Foundry using Node.js.
- Registered the new SaaS product on the Cloud Foundry marketplace.
- Designed and implemented billing and metering microservices using
Java.
- Ensured continuous monitoring of these services using Prometheus and
Grafana.

**Stack:**
`Cloud Foundry`, `Node.js`, `Java`, `Prometheus`, `API gateway`, `Redis`, `Postgres`

---

### Developed cloud infra. for the SAP HANA-as-a-Service – 04.2019 – 01.2021


**Role:**
DevOps Engineer

**Description:**
To bring the HANA-as-a-Service product to SAP, we had to create a strong and adaptable cloud infrastructure on AWS. Since SAP serves customers worldwide, we needed to deploy this infrastructure in various regions, requiring an approach that ensures the infrastructure remains unchanged over time by using Infrastructure as Code (IaC) tools and practices. Furthermore, to bolster the security of customer data, the infrastructure had to be placed within a Virtual Private Cloud (VPC) in each region. Additionally, we automated the HANA installation and upgrade processes to support scalability and automation.
      
**Responsibilities:**
- Created Terraform and Ansible playbooks for HANA installation and upgrades.
- Developed a lightweight agent to respond to HashiCorp Consul changes, triggering the appropriate Ansible playbook for various tasks.
- Built customer-facing APIs using Go(lang) for HANA system orders.   
- Contributed to setting up the VPC on AWS, including EC2 configuration
and update policies.
- Stored HANA backups on AWS S3 and AWS Glacier for both hot and cold
system recovery.

**Stack:**
`HashiCorp (Terraform, Vault, Consul)`, `Ansible`, `AWS (VPC, EC2, S3, Glacier, Cloud Watch, API Gateway)`, `Cloud Foundry`, `Python`, `Go(lang)`, `Bash`</td>
    
---

### Development of an elastic caching microservice – 07.2018 – 04.2019


**Role:**
Software Developer

**Description:**
To speed up analytical query responses in our analytics platform, we created an elastic caching solution. This solution caches incoming queries and their responses, considering factors like user roles, permissions, and analytical details such as cube dimensions. We also successfully managed cache invalidation, which was a challenge. Ensuring the service's elasticity was a critical requirement to achieve horizontal scalability for the caching layer.
      
**Responsibilities:**
- Designed and built an elastic caching microservice adhering to 12-factor cloud development principles.
- Deployed the service on Kubernetes to ensure high availability and horizontal scalability.
- Monitored service performance using the Prometheus framework.

**Stack:**
`Go(lang)`, `Redis`, `MongoDB`, `Kubernetes`, `Prometheus`

---
