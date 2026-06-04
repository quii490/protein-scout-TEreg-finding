---
type: protein-evaluation
gene: "THRB"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## THRB — REJECTED (研究热度过高 (PubMed strict=422，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | THRB / ERBA2, NR1A2, THR1 |
| 蛋白名称 | Thyroid hormone receptor beta |
| 蛋白大小 | 461 aa / 52.8 kDa |
| UniProt ID | P10828 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nuclear bodies; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 461 aa / 52.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=422 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=80.2; PDB: 1BSX, 1N46, 1NAX, 1NQ0, 1NQ1, 1NQ2, 1NUO |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR035500, IPR000536, IPR050234, IPR001723, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **104.0/180** | |
| **归一化总分** | | | **57.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- RNA polymerase II transcription regulator complex (GO:0090575)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 422 |
| PubMed broad count | 593 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ERBA2, NR1A2, THR1 |

**关键文献**:
1. Thyroid hormone receptors and resistance to thyroid hormone disorders.. *Nature reviews. Endocrinology*. PMID: 25135573
2. Resistance to Thyroid Hormone Beta: A Focused Review.. *Frontiers in endocrinology*. PMID: 33868182
3. Actions of thyroid hormones and thyromimetics on the liver.. *Nature reviews. Gastroenterology & hepatology*. PMID: 39420154
4. Obesity disrupts the pituitary-hepatic UPR communication leading to NAFLD progression.. *Cell metabolism*. PMID: 38718793
5. Small mobilizable multi-purpose cloning vectors derived from the Escherichia coli plasmids pK18 and pK19: selection of defined deletions in the chromosome of Corynebacterium glutamicum.. *Gene*. PMID: 8045426

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.2 |
| 高置信度残基 (pLDDT>90) 占比 | 69.2% |
| 置信残基 (pLDDT 70-90) 占比 | 7.6% |
| 中等置信 (pLDDT 50-70) 占比 | 2.0% |
| 低置信 (pLDDT<50) 占比 | 21.3% |
| 有序区域 (pLDDT>70) 占比 | 76.8% |
| 可用 PDB 条目 | 1BSX, 1N46, 1NAX, 1NQ0, 1NQ1, 1NQ2, 1NUO, 1Q4X, 1R6G, 1XZX |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1BSX, 1N46, 1NAX, 1NQ0, 1NQ1, 1NQ2, 1NUO, 1Q4X, 1R6G, 1XZX）+ AlphaFold极高置信度预测（pLDDT=80.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR035500, IPR000536, IPR050234, IPR001723, IPR001728; Pfam: PF00104, PF00105 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RXRA | 0.993 | 0.988 | — |
| NCOA2 | 0.993 | 0.965 | — |
| NCOA1 | 0.985 | 0.855 | — |
| NCOR1 | 0.982 | 0.859 | — |
| PIK3R1 | 0.966 | 0.345 | — |
| NCOR2 | 0.964 | 0.848 | — |
| TXNRD2 | 0.959 | 0.045 | — |
| THRA | 0.938 | 0.000 | — |
| NCOA3 | 0.938 | 0.651 | — |
| MAPK3 | 0.916 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Ncoa6 | psi-mi:"MI:0018"(two hybrid) | pubmed:10866662 |
| PRMT2 | psi-mi:"MI:0096"(pull down) | pubmed:12039952 |
| groEL | psi-mi:"MI:0096"(pull down) | pubmed:16606699 |
| glpD | psi-mi:"MI:0096"(pull down) | pubmed:16606699 |
| ADAT3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| PTCHD3 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| - | psi-mi:"MI:0432"(one hybrid) | imex:IM-26689|pubmed:31481462 |
| ENSG00000148120 | psi-mi:"MI:0432"(one hybrid) | imex:IM-26689|pubmed:31481462 |
| ENSG00000183722 | psi-mi:"MI:0432"(one hybrid) | imex:IM-26689|pubmed:31481462 |
| ENSG00000158321 | psi-mi:"MI:0432"(one hybrid) | imex:IM-26689|pubmed:31481462 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.2 + PDB: 1BSX, 1N46, 1NAX, 1NQ0, 1NQ1,  | pLDDT=80.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nuclear bodies | 一致 |
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
1. THRB — Thyroid hormone receptor beta，研究基础较多，新颖性有限。
2. 蛋白大小461 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 422 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 422 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P10828
- Protein Atlas: https://www.proteinatlas.org/ENSG00000151090-THRB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=THRB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P10828
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
