---
type: protein-evaluation
gene: "ELOA2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ELOA2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ELOA2 / TCEB3B, TCEB3L |
| 蛋白名称 | Elongin-A2 |
| 蛋白大小 | 753 aa / 83.9 kDa |
| UniProt ID | Q8IYF1 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ELOA2/IF_images/REH_1.jpg|REH]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ELOA2/IF_images/HEK293_1.jpg|HEK293]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Nucleoli, Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 753 aa / 83.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=54.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051870, IPR010684, IPR003617, IPR035441, IPR017 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.0/180** | |
| **归一化总分** | | | **76.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli, Cytosol | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- elongin complex (GO:0070449)
- nucleoplasm (GO:0005654)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TCEB3B, TCEB3L |

**关键文献**:
1. A Novel Prognostic Model of Endometrial Cancer Based on Inflammation and Lipid Metabolism Genes.. *Genetic testing and molecular biomarkers*. PMID: 40810785
2. Ocular Mucous Membrane Pemphigoid Demonstrates a Distinct Autoantibody Profile from Those of Other Autoimmune Blistering Diseases: A Preliminary Study.. *Antibodies (Basel, Switzerland)*. PMID: 39584991

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 54.0 |
| 高置信度残基 (pLDDT>90) 占比 | 8.1% |
| 置信残基 (pLDDT 70-90) 占比 | 14.2% |
| 中等置信 (pLDDT 50-70) 占比 | 17.8% |
| 低置信 (pLDDT<50) 占比 | 59.9% |
| 有序区域 (pLDDT>70) 占比 | 22.3% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ELOA2/ELOA2-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=54.0），有序残基占 22.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051870, IPR010684, IPR003617, IPR035441, IPR017923; Pfam: PF06881, PF08711 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ELOC | 0.997 | 0.571 | — |
| ELOB | 0.987 | 0.314 | — |
| TCEA1 | 0.847 | 0.000 | — |
| TCEA2 | 0.810 | 0.000 | — |
| WDR61 | 0.800 | 0.000 | — |
| CUL5 | 0.792 | 0.000 | — |
| LEO1 | 0.767 | 0.052 | — |
| CDC73 | 0.761 | 0.000 | — |
| POLR2A | 0.745 | 0.050 | — |
| VHL | 0.734 | 0.106 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SOHLH2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CEP70 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| KRTAP4-12 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CBX5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| DVL2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TRAF2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| KXD1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ZBTB43 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CALCOCO2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ZNF165 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=54.0 + PDB: 无 | pLDDT=54.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Nucleoli, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. ELOA2 — Elongin-A2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小753 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=54.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IYF1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000206181-ELOA2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ELOA2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IYF1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ELOA2/ELOA2-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8IYF1 |
| SMART | SM00509; |
| UniProt Domain [FT] | DOMAIN 5..80; /note="TFIIS N-terminal"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00649" |
| InterPro | IPR051870;IPR010684;IPR003617;IPR035441;IPR017923; |
| Pfam | PF06881;PF08711; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000206181-ELOA2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CALCOCO2 | Intact | false |
| DVL2 | Intact | false |
| HSF2BP | Intact | false |
| NKAPD1 | Intact | false |
| RNPS1 | Intact | false |
| SREK1IP1 | Intact | false |
| TRAF2 | Intact | false |
| ZBTB43 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
