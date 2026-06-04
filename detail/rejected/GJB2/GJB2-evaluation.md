---
type: protein-evaluation
gene: "GJB2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GJB2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=1635，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GJB2 |
| 蛋白名称 | Gap junction beta-2 protein |
| 蛋白大小 | 226 aa / 26.2 kDa |
| UniProt ID | P29033 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Mitochondria; UniProt: Cell membrane; Cell junction, gap junction |
| 蛋白大小 | 10/10 | ×1 | 10 | 226 aa / 26.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1635 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=86.2; PDB: 2ZW3, 3IZ1, 3IZ2, 5ER7, 5ERA, 5KJ3, 5KJG |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000500, IPR002268, IPR019570, IPR017990, IPR013 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **72.5/180** | |
| **归一化总分** | | | **40.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria | Approved |
| UniProt | Cell membrane; Cell junction, gap junction | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- connexin complex (GO:0005922)
- endoplasmic reticulum-Golgi intermediate compartment (GO:0005793)
- gap junction (GO:0005921)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1635 |
| PubMed broad count | 2867 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. GJB2 Promotes HCC Progression by Activating Glycolysis Through Cytoplasmic Translocation and Generating a Suppressive Tumor Microenvironment Based on Single Cell RNA Sequencing.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39162005
2. Combined AAV-mediated specific Gjb2 expression restores hearing in DFNB1 mouse models.. *Molecular therapy : the journal of the American Society of Gene Therapy*. PMID: 40121530
3. GJB2 mutations and degree of hearing loss: a multicenter study.. *American journal of human genetics*. PMID: 16380907
4. AAV-mediated base editing restores cochlear gap junction in GJB2 dominant-negative mutation-associated syndromic hearing loss model.. *JCI insight*. PMID: 40059830
5. The association between GJB2 gene (producing Cx26 protein) and the ventricular storm: A case report.. *ARYA atherosclerosis*. PMID: 39170815

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.2 |
| 高置信度残基 (pLDDT>90) 占比 | 51.3% |
| 置信残基 (pLDDT 70-90) 占比 | 35.8% |
| 中等置信 (pLDDT 50-70) 占比 | 10.2% |
| 低置信 (pLDDT<50) 占比 | 2.7% |
| 有序区域 (pLDDT>70) 占比 | 87.1% |
| 可用 PDB 条目 | 2ZW3, 3IZ1, 3IZ2, 5ER7, 5ERA, 5KJ3, 5KJG, 6UVR, 6UVS, 6UVT |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2ZW3, 3IZ1, 3IZ2, 5ER7, 5ERA, 5KJ3, 5KJG, 6UVR, 6UVS, 6UVT）+ AlphaFold极高置信度预测（pLDDT=86.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000500, IPR002268, IPR019570, IPR017990, IPR013092; Pfam: PF00029 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CD14 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| Cnst | psi-mi:"MI:0018"(two hybrid) | pubmed:19864490|imex:IM-19064 |
| GPR42 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| GJA5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| AMIGO1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TLCD4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ARL13B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| LHFPL5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TM2D2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TMX2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.2 + PDB: 2ZW3, 3IZ1, 3IZ2, 5ER7, 5ERA,  | pLDDT=86.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Cell junction, gap junction / Mitochondria | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. GJB2 — Gap junction beta-2 protein，研究基础较多，新颖性有限。
2. 蛋白大小226 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1635 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P29033
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165474-GJB2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GJB2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P29033
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
