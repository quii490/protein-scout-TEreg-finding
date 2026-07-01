---
type: protein-evaluation
gene: "CCDC3"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## CCDC3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CCDC3 |
| 蛋白名称 | Coiled-coil domain-containing protein 3 |
| 蛋白大小 | 270 aa / 30.7 kDa |
| UniProt ID | Q9BQI4 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28.0 | Cytosol; Nucleoplasm (Uncertain) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 270 aa |
| 新颖性 | 9/10 | ×5 | 45.0 | PubMed=25 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=75.4; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | CCDC3 |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=4 |
| **加权总分** | | | **121/180** | |
| **归一化总分** | | | **67.2/100** | 互证: +2 |

### 3. 分析
- Cytosol; Nucleoplasm (Uncertain)
- PubMed strict=25 broad=31
- AF pLDDT=75.4 PDB=0
- InterPro: CCDC3
- Pfam: CCDC3_C
- PPI degree=4 ChIP: None
37263799: Extracellular and intracellular functions of coiled-coil domain containing 3. | 37052857: CCDC3 Gene Regulates the Proliferation of Breast Cancer Cells. | 41792471: Combining AI to reveal CCDC3-mediated pathways of colorectal cancer liver metast

### 4. 总体评价
**67.2/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Coiled-coil domain-containing protein 3

**功能**: Negatively regulates TNF-induced pro-inflammatory response in endothelial cells (ECs) via inhibition of TNF-induced NF-kappaB activation in ECs (PubMed:25193116). Positively regulates lipid accumulation in adipose cells (By similarity)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR040311 |
| Pfam | PF28297 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TOP3B | BioGRID | 1 |
| TP53 | BioGRID | 1 |
| MDM2 | BioGRID | 1 |
| PSMC4 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9BQI4-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/CCDC3

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000151468-CCDC3

![](https://images.proteinatlas.org/62425/1273_F2_2_red_green.jpg)
![](https://images.proteinatlas.org/62425/1273_F2_3_red_green.jpg)
![](https://images.proteinatlas.org/62425/1163_H10_5_red_green.jpg)
![](https://images.proteinatlas.org/62425/1163_H10_6_red_green.jpg)
![](https://images.proteinatlas.org/62425/1159_H10_4_red_green.jpg)
![](https://images.proteinatlas.org/62425/1159_H10_10_red_green.jpg)

### 深度机制分析

**结构域架构**：CCDC3（Coiled-coil domain-containing protein 3, 270 aa / 30.7 kDa）的主要结构域注释为IPR040311（CCDC3 family）——此为较新的InterPro entry, 反映出该家族的功能保守性尚未在classical domain databases中充分体现。Pfam识别到PF28297（CCDC3_C, C-terminal conserved region）。该蛋白的pLDDT=75.4（高置信度），结构预测显示全蛋白主要为coiled-coil fold, 无实验PDB结构。PubMed=25（低文献量），研究集中于adipose biology, endothelial inflammation和cancer。

**PPI互作网络解读**：PPI network（degree=4）——BioGRID记录的关键互作伙伴包括TOP3B（DNA topoisomerase III beta, RNA/DNA topoisomerase）、TP53（p53 tumor suppressor）、MDM2（p53 E3 ubiquitin ligase）和PSMC4（26S proteasome regulatory subunit）。TP53和MDM2的互作直接将CCDC3连接到p53 tumor suppressor pathway——CCDC3可能作为p53-MDM2 regulatory loop的modulator。TOP3B的互作提示CCDC3可能参与RNA processing——TOP3B functions in mRNA metabolism as RNA topoisomerase。

**结构解读**：CCDC3的coiled-coil domain是该蛋白唯一被注释的structural feature。Coiled-coil motif是protein-protein interaction的经典scaffold, 常见于oligomerization（如leucine zipper transcription factors, cytoskeletal proteins）。CCDC3_C domain (PF28297) 为新近定义的conserved region, 其specific function未明确, 但positional conservation暗示其参与specific protein-protein recognition。pLDDT=75.4且全长均一性良好——提示该蛋白主要fold为single domain with coiled-coil architecture, 无disordered region。

**机制模型**：CCDC3的机制推演：(1) Canonical function——negatively regulates TNF-induced NF-kappaB activation in endothelial cells. CC domain可能介导CCDC3与NF-kappaB pathway component的direct binding, 从而interfere with signal transduction. 文献PMID:25193116提供该功能的实验基础。(2) Nuclear function——CCDC3在Nucleoplasm中的定位(Uncertain)提示可能具有尚未被experimentally validated的核内功能。Coiled-coil domain可能使其作为transcription factor co-activator or co-repressor的adaptor protein。(3) p53 pathway interaction——CCDC3-TP53-MDM2三角互作暗示CCDC3可能通过modulating p53 protein stability（compete with MDM2 for p53 binding）间接调控p53-dependent transcriptional programs。

**TE调控展望**：CCDC3的TE regulation潜力为indirect inference。TE调控关联性取决于：(1) CCDC3-p53 interaction是否影响p53-mediated TE silencing——p53已知通过与DAXX/ATRX complex协作调控pericentromeric repetitive elements的H3K9me3 deposition；(2) NF-kappaB pathway modulation是否indirectly affect inflammatory signaling-driven TE expression——LINE-1 expression known to be upregulated under inflammatory conditions；(3) CCDC3的coiled-coil domain能否被co-opted为chromatin-associated complex的assembly scaffold。建议通过co-IP验证CCDC3-TP53 endogenous interaction, 在p53-wildtype vs p53-null cell line中比较CCDC3 loss对TE expression的影响, 以及luciferase reporter assay评估CCDC3对NF-kappaB-responsive TE promoter（如LTR-driven promoter）的transcriptional effect。

### PubMed

**Count: 31**

| PMID | Title |
|---|---|
| 42211118 | Integrating gene-microbiome interactions and single-cell transcriptomics reveals therapeutic strategies for aortic aneurysm. |
| 42094695 | Genome-wide association study of myopia progression in Chinese adolescents and application of polygenic risk score prediction. |
| 41792471 | Combining AI to reveal CCDC3-mediated pathways of colorectal cancer liver metastasis. |
| 41745594 | Circulating CCDC3 as an Indicator of Visceral Fat Accumulation in Patients with Type 2 Diabetes Mellitus. |
| 41605187 | Regulation of Lipid Biology-Associated Gene Expression in Granulosa Cells in Hyperandrogenic PCOS: A Possible Link Between Dyslipidemia and Hyperandro |


