This repository hosts a **public demonstration of the Upstream Safety System (USS)**: a deterministic, auditable AI governance architecture designed to help regulators, platforms, and safety teams understand how policy can be enforced upstream — before harm occurs.

The demo is intentionally simple, transparent, and **non-enforcement**. It exists to show **governance structure**, not to moderate live systems.

**Hackathon demonstration video:** *(coming soon)*

---

# 🚀 The Upstream Safety System (USS)  
### Deterministic, Auditable AI Safety Architecture

The Upstream Safety System (USS) is a **policy-first, three-layer architecture** designed to produce transparent, reproducible, regulator-grade AI safety decisions.

USS enforces a **Technical Separation of Powers**:

- **Layer 3 → Diagnose** (classification + structured facts)  
- **Layer 2 → Decide** (deterministic policy rules)  
- **Layer 1 → Validate** (impact simulation measuring Dignity & Agency)

This repository includes **public technical documentation** and the **high-level model submitted to the 2025 MLAI Hackathon**, aligned with the **AISI voluntary guardrails**.

---

## 🧠 1. The Three-Layer Architecture

### **Layer 3 — Diagnostic Engine (Fact API)**
A deterministic **TF-IDF + Logistic Regression** classifier.

- **F1 Score:** 0.71902 (19,375-row validation)  
- **Cost:** ~$0.00004 per message  
- **Output:** Structured Facts via an interpretability model  
- **Property:** Fully reproducible (same input → same output)  

This layer is optimized for **auditability, speed, and economic scale**, not leaderboard chasing.

---

### **Layer 2 — Declarative Policy Engine**
A **Datalog-based rules system** that separates governance from classification.

- Explicit, human-readable policy rules  
- **Priority Ladder:** Human Safety > Human Rights  
- **Age-Stage Model:**
  - Child (0–12)  
  - Teen (13–19)  
  - Self-Selecting Early Career (18+)  
  - Mid Career  
  - Senior Career  
- Transparent, versioned, jurisdiction-specific rule sets  

This ensures that **policy cannot be influenced by ML outputs**.

---

### **Layer 1 — Impact Simulator**
A synthetic **micro-Citiverse testbed** that validates policy outcomes **before deployment**.

- **Measures:**
  - **Dignity:** remediation success, harm prevention  
  - **Agency:** autonomy support, choice-space preservation  
- **Aligns with:**
  - AISI guardrails  
  - eSafety Commissioner duty-of-care expectations  
  - DSA Article 35 systemic-risk requirements  
  - UK OSA impact transparency  

---

## 🏛️ 2. Governance Lineage & UN Legitimacy

The USS is the product of a **20-year generational governance lineage**, jointly developed by:

### **Stacy Gildenston — Strategic Architect**
- First WSIS Award winner (2003)  
- Led global certification programs (USENIX, Linux Professional Institute)  
- Pioneer of virtual-world governance (Discovery Channel, BBC, CNN)  
- Architect of the Inclusive Lifelong Multistakeholder Model  
- Designs policy logic, Age-Stage framework, and Priority Ladder  

### **Pyrate Ruby Passell — Technical Architect**
- Built and validated all three USS layers  
- Achieved 0.71902 deterministic F1 score  
- Mentor at ITU Citiverse Challenge  
- First under-18 Changemaker for UN Partnerships  
- Leads classifier design, interpretability, and cost optimisation  

### **DTC UN Participation (selected)**
- Invited to, participated in, and endorsed the UN Global Digital Compact  
- WSIS+20 model development (carried forward by Dr. Vint Cerf)  
- IGF advocacy on teen civil rights  
- ITU Citiverse mentorship  

USS is grounded in **real policy processes**, not theory.

---

## 👤 About Stacy (Co-Founder & Governance Lead)

Stacy is a WSIS Award recipient and former Director of Certification for LPI and Managing Director for the USENIX System Administration Certification Program. With three decades of experience in open systems, aerospace education, and digital governance — including work with the ITU leading into the original WSIS — she co-develops the ILMM and the Upstream Safety System (USS). Her background spans governance architecture, STEM education, environmental stewardship, and high-impact technical leadership.

---

## 👤 About Pyrate (Co-Founder & Technical / Governance Developer)

Pyrate Ruby Passell is a multidisciplinary maker and governance technologist contributing to the USS and ILMM. She is a UN Foundation Changemaker Under 18, a Mentor for the UN’s first Citiverse Challenge (ITU), and a CERN Open Quantum Institute (OQI) Friend. Her work blends hands-on engineering — winning the 2018 Australian Youth Rocketry Challenge — with digital governance innovation, youth inclusion, and upstream safety development.

---

## 📌 Status

- Public demo utility  
- Non-binding, non-enforcement  
- Pricing, pilots, and certifications forthcoming  

---

**Note:**  
This repository is published for **transparency and reference only**.  
External contributions are not accepted.
