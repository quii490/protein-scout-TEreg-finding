---
type: gene-evaluation
gene: DGKD
date: 2026-06-28
tags: [nucleus-cytoplasm, diacylglycerol-kinase, lipid-signaling, membrane, incidental-nuclear]
status: shortlisted
---

# DGKD - Gene Evaluation

## 1. Basic Information

| Field | Value |
|-------|-------|
| **Gene Symbol** | DGKD |
| **UniProt Accession** | Q16760 |
| **Protein Name** | Diacylglycerol kinase delta |
| **Protein Length** | 1214 aa |
| **Molecular Function** | Diacylglycerol kinase (ATP:DAG phosphotransferase) |
| **Chromosome** | 2q37.1 |

## 2. Nuclear Localization Scoring

| Criterion | Score | Weight | Weighted | Notes |
|-----------|-------|--------|----------|-------|
| **GO-CC: Nucleus** | ×2 | ×4 | 8 | Nuclear GO-CC present but likely incidental |
| **Primary Localization** | ×1 | ×5 | 5 | Plasma membrane/cytoplasm (primary) |
| **Lipid Signaling** | ×1 | ×1 | 1 | Membrane-proximal function |
| **HPA Nuclear Evidence** | ×1 | ×3 | 3 | No HPA data available (unclassified_bare) |
| **Nuclear PPI Partners** | ×1 | ×2 | 2 | No strong nuclear PPI partners |
| **Literature Evidence** | ×1 | ×3 | 3 | Lipid signaling focus, no nuclear function |
| **Total** | | | **22** | |



| **加权总分** | | | **22.0/180** | |
| **归一化总分 (÷1.83)** | | | **12.0/100** | |
## 3. Detailed Analysis

### 3.1 Protein Function
DGKD is a diacylglycerol kinase that converts diacylglycerol (DAG) to phosphatidic acid (PA), regulating the balance between these two bioactive lipid second messengers. This positions DGKD as a central switch between DAG-mediated signaling (e.g., PKC activation) and PA-mediated signaling pathways. DGKD regulates EGFR signaling, cytoskeletal reorganization, and cellular proliferation.

### 3.2 Nuclear Localization Evidence
- **GO-CC terms**: Clathrin-coated pit, cytoplasm, cytoplasmic vesicle, cytosol, nucleus, plasma membrane
- **UniProt annotation**: "Membrane, clathrin-coated pit; Cytoplasm; Cell membrane"
- Nuclear GO-CC is one of many annotations and likely reflects incidental detection
- Primary functional localization is at the plasma membrane and clathrin-coated pits
- The enzyme's substrate (DAG) and product (PA) are membrane lipids
- No known nuclear lipid kinase function

### 3.3 Domain Architecture
DGKD is a large 1214 aa protein with:
- **Pleckstrin homology (PH) domain**: Phosphoinositide binding
- **Sterile alpha motif (SAM) domain**: Protein-protein interaction
- **Diacylglycerol kinase catalytic domain**: ATP-dependent DAG phosphorylation
- **Diacylglycerol kinase accessory domain**
- **C1 domain**: DAG/phorbol ester binding

### 3.4 Protein-Protein Interactions
- **DGKH**: Paralogous diacylglycerol kinase
- **HAX1**: Anti-apoptotic protein, mitochondrial/ER
- **IGSF21**: Immunoglobulin superfamily member
- No convincing nuclear functional PPI partners

### 3.5 Relevance to TE Regulation
Minimal direct relevance. DGKD functions in lipid signaling at membranes. While nuclear lipid signaling exists (e.g., nuclear phosphoinositides), DGKD has no established role in this compartment. No connection to chromatin, RNA processing, or TE biology.

## 4. Overall Assessment

**Classification: nucleus-cytoplasm** - Low confidence. DGKD is a large membrane-associated lipid kinase. The nuclear GO-CC annotation likely reflects incidental detection. The enzyme's substrate specificity for membrane lipids makes nuclear localization functionally implausible for its primary activity.

**Recommendation: Low priority.** No evidence of nuclear function and no mechanistic connection to TE regulation. Lipid signaling is distantly connected to TE biology at best.

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00109;SM00045;SM00046;SM00233;SM00454; |
| InterPro | IPR017438;IPR046349;IPR047478;IPR047477;IPR037607;IPR037606;IPR054474;IPR000756;IPR001206;IPR016064;IPR011993;IPR001849;IPR002219;IPR001660;IPR013761; |
| Pfam | PF00130;PF00609;PF00781;PF22944;PF00169;PF07647; |
| UniProt Domain | DOMAIN 53..146; /note="PH"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00145"; DOMAIN 317..451; /note="DAGKc"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00783"; DOMAIN 1145..1208; /note="SAM"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00184" |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000077044-DGKD

![](https://images.proteinatlas.org/27530/1259_A5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/27530/1259_A5_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/27530/1105_G5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/27530/1105_G5_2_blue_red_green.jpg)

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PNPLA2 | STRING | 723 |
| DGKD | BioGRID | 1 |
| SREK1 | BioGRID | 1 |
| TRIM25 | BioGRID | 1 |
| MYC | BioGRID | 1 |
| FMR1 | BioGRID | 1 |
| FXR2 | BioGRID | 1 |
| RHOA | BioGRID | 1 |


### TE 调控评估

该蛋白具有染色质/DNA 调控相关结构域，可能直接或间接参与 TE 沉默机制，值得进一步实验验证。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/DGKD

### PubMed

**Count: 50**

| PMID | Title |
|---|---|
| 42293249 | Cell type-stratified immunogenetic framework reveals immune drivers and therapeutic targets in kidney stone disease. |
| 41471601 | Deep Guided Exposure Correction with Knowledge Distillation. |
| 41431653 | Sex-specific circRNA-miRNA-mRNA networks in peripheral blood mononuclear cells of patients with idiopathic pulmonary arterial hypertension: a pilot st |
| 40921406 | Diacylglycerol kinase gene Dgkh deficiency disrupts testicular lipid balance in male mice without affecting fertility. |
| 40759569 | Genetic susceptibility to kidney stone disease: unveiling pathogenesis and potential therapeutic targets. |


## 5. Data Sources

- UniProt: Q16760 (accessed 2026-06-28 via REST API)
- GO-CC: clathrin-coated pit (GO:0005905), cytoplasm (GO:0005737), nucleus (GO:0005634), plasma membrane (GO:0005886)
- BioGRID PPI: human PPI dataset (DGKH, HAX1, IGSF21 interactions)
- HPA: unclassified_bare (no nuclear localization data)
