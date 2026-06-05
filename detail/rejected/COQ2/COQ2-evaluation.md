---
type: protein-evaluation
gene: "COQ2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## COQ2 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3); 研究热度过高 (PubMed strict=219，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COQ2 |
| 蛋白名称 | 4-hydroxybenzoate polyprenyltransferase, mitochondrial |
| 蛋白大小 | 371 aa / 40.5 kDa |
| UniProt ID | Q96H96 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Cytosol; UniProt: Mitochondrion inner membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 371 aa / 40.5 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=219 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=85.3; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **64.5/180** | |
| **归一化总分** | | | **35.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Mitochondrion inner membrane | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 219 |
| PubMed broad count | 251 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Genetic Variants and Clinical Characteristics of Young-Onset Parkinson's Disease in the Hakka Population of Western Fujian.. *Brain Behav*. PMID: 42204920
2. FSP1 reduces exogenous coenzyme Q10 and inhibits ferroptosis to alleviate intestinal ischemia-reperfusion injury.. *J Adv Res*. PMID: 40902893
3. Atypical COQ2-Related Retinopathy in Identical Twins with Nephropathy Mimicking Intermediate Uveitis.. *Ocul Immunol Inflamm*. PMID: 42206750
4. Successful treatment of neonatal COQ2 deficiency with 4-hydroxybenzoic acid.. *Brain*. PMID: 41566942
5. Preclinical and first-in-human evidence of 4-hydroxybenzoic acid for mitochondrial COQ2 deficiency.. *Brain*. PMID: 40929079

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.3 |
| 高置信度残基 (pLDDT>90) 占比 | 74.1% |
| 置信残基 (pLDDT 70-90) 占比 | 8.1% |
| 中等置信 (pLDDT 50-70) 占比 | 2.7% |
| 低置信 (pLDDT<50) 占比 | 15.1% |
| 有序区域 (pLDDT>70) 占比 | 82.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=85.3，有序区 82.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PDSS1 | 0.000 | 0.000 | — |
| PDSS2 | 0.000 | 0.000 | — |
| COQ8A | 0.000 | 0.000 | — |
| COQ9 | 0.000 | 0.000 | — |
| COQ6 | 0.000 | 0.000 | — |
| UBIAD1 | 0.000 | 0.000 | — |
| COQ3 | 0.000 | 0.000 | — |
| COQ8B | 0.000 | 0.000 | — |
| COQ4 | 0.000 | 0.000 | — |
| SALL3 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:P06753-2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9H3K6 | psi-mi:"MI:0030"(cross-linking study) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O43809 | psi-mi:"MI:0030"(cross-linking study) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q12905 | psi-mi:"MI:0030"(cross-linking study) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:A8MWD9 | psi-mi:"MI:0030"(cross-linking study) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q92522 | psi-mi:"MI:0030"(cross-linking study) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q15424 | psi-mi:"MI:0030"(cross-linking study) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P05141 | psi-mi:"MI:0030"(cross-linking study) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P45880 | psi-mi:"MI:0030"(cross-linking study) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P04908 | psi-mi:"MI:0030"(cross-linking study) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.3 + PDB: 无 | pLDDT=85.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Mitochondrion inner membrane / Cytosol | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. COQ2 -- 4-hydroxybenzoate polyprenyltransferase, mitochondrial，研究基础较多，新颖性有限。
2. 蛋白大小371 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 219 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96H96
- Protein Atlas: https://www.proteinatlas.org/ENSG00000173085-COQ2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COQ2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96H96
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96H96-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
