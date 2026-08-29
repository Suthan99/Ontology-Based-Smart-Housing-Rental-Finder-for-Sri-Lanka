# Ontology-Based-Smart-Housing-Rental-Finder-for-Sri-Lanka

This project presents a web-based housing and rental finder designed using ontology and semantic web technologies. It helps users search for suitable housing options in Sri Lanka by using structured property information. The system also provides a visual representation of the knowledge graph, making it easier to understand the connections between properties, locations, facilities, tenants, and other related information.

---

## 🔍 Problem Statement

Finding a suitable house or rental property in Sri Lanka can be difficult because property information is not always organized in a clear and structured way. Many existing property websites mainly depend on simple keyword searches, which may not always give users the results they are looking for. Users can also face difficulties when trying to apply detailed filters or find properties that closely match their individual preferences. 

---

## 💡 Proposed Solution

This project aims to develop a web-based housing and rental finder for Sri Lanka using an ontology-based approach. The system organizes housing-related knowledge using RDF and OWL, allowing different property details to be linked and represented in a structured way. 
This makes it easier for users to search and find relevant housing information based on their requirements.

---

## 🧠 Key Features

- Ontology-based semantic search
- Relevance-based result ranking
- Best property highlighted
- Interactive knowledge graph visualization
- Ontology designed using Protégé

---

## 🛠 Technologies Used

### Semantic Web
- OWL (Web Ontology Language)
- RDF (Resource Description Framework)
- SPARQL

### Backend
- Python
- Flask
- RDFLib

### Visualization
- PyVis

### Frontend
- HTML5
- Bootstrap 5

---

## 🧩 Ontology Design

The ontology models:
- Property (Apartment, House, Room)
- City
- Tenant (Student, Family, Professional)
- Lease
- Landlord

Key object properties:
- `locatedIn`
- `leaseFor`
- `ownedBy`

The ontology was created using **Protégé**.
