---
type: protein-evaluation
gene: "XRCC2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## XRCC2 — REJECTED (研究热度过高 (PubMed strict=310，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | XRCC2 |
| 蛋白名称 | DNA repair protein XRCC2 |
| 蛋白大小 | 280 aa / 32.0 kDa |
| UniProt ID | O43543 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Vesicles; UniProt: Nucleus; Cytoplasm, cytoskeleton, microtubule organizing cen |
| 蛋白大小 | 10/10 | ×1 | 10 | 280 aa / 32.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=310 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=87.1; PDB: 8FAZ, 8GBJ, 8OUY, 8OUZ |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR027417, IPR013632, IPR020588, IPR030547; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **93.0/180** | |
| **归一化总分** | | | **51.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles | Approved |
| UniProt | Nucleus; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- nucleoplasm (GO:0005654)
- Rad51B-Rad51C-Rad51D-XRCC2 complex (GO:0033063)
- replication fork (GO:0005657)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 310 |
| PubMed broad count | 489 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Rare, protein-truncating variants in ATM, CHEK2 and PALB2, but not XRCC2, are associated with increased breast cancer risks.. *Journal of medical genetics*. PMID: 28779002
2. Structure and function of the RAD51B-RAD51C-RAD51D-XRCC2 tumour suppressor.. *Nature*. PMID: 37344587
3. Functional and Clinical Characterization of Variants of Uncertain Significance Identifies a Hotspot for Inactivating Missense Variants in RAD51C.. *Cancer research*. PMID: 37253112
4. Fanconi Anemia.. **. PMID: 20301575
5. Prioritizing Variants in Complete Hereditary Breast and Ovarian Cancer Genes in Patients Lacking Known BRCA Mutations.. *Human mutation*. PMID: 26898890

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.1 |
| 高置信度残基 (pLDDT>90) 占比 | 66.8% |
| 置信残基 (pLDDT 70-90) 占比 | 20.4% |
| 中等置信 (pLDDT 50-70) 占比 | 5.7% |
| 低置信 (pLDDT<50) 占比 | 7.1% |
| 有序区域 (pLDDT>70) 占比 | 87.2% |
| 可用 PDB 条目 | 8FAZ, 8GBJ, 8OUY, 8OUZ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（8FAZ, 8GBJ, 8OUY, 8OUZ）+ AlphaFold高质量预测（pLDDT=87.1），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027417, IPR013632, IPR020588, IPR030547; Pfam: PF08423 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RAD51B | 0.999 | 0.844 | — |
| RAD51D | 0.999 | 0.949 | — |
| XRCC3 | 0.999 | 0.130 | — |
| RAD51C | 0.999 | 0.855 | — |
| RAD51D-2 | 0.999 | 0.092 | — |
| BRCA2 | 0.982 | 0.098 | — |
| RAD51 | 0.981 | 0.710 | — |
| BRCA1 | 0.954 | 0.000 | — |
| MRE11 | 0.912 | 0.000 | — |
| SFR1 | 0.911 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Cfp1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| EBI-467052 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| cg15011 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| Miro | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| pk | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| slo | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| oc | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| mRNA-cap | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| raw | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| "su | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.1 + PDB: 8FAZ, 8GBJ, 8OUY, 8OUZ | pLDDT=87.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytoskeleton, microtubule orga / Nucleoplasm, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. XRCC2 — DNA repair protein XRCC2，研究基础较多，新颖性有限。
2. 蛋白大小280 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 310 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 310 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43543
- Protein Atlas: https://www.proteinatlas.org/ENSG00000196584-XRCC2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=XRCC2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43543
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000196584-XRCC2/subcellular

![](https://images.proteinatlas.org/65153/1151_F4_1_red_green.jpg)
![](https://images.proteinatlas.org/65153/1151_F4_2_red_green.jpg)
![](https://images.proteinatlas.org/65153/1154_F4_2_red_green.jpg)
![](https://images.proteinatlas.org/65153/1154_F4_3_red_green.jpg)
![](https://images.proteinatlas.org/65153/1202_C6_1_red_green.jpg)
![](https://images.proteinatlas.org/65153/1202_C6_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O43543-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
