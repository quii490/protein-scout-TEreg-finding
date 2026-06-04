---
type: protein-evaluation
gene: "PDX1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PDX1 — REJECTED (研究热度过高 (PubMed strict=2136，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PDX1 / PDX1 |
| 蛋白名称 | Pyruvate dehydrogenase protein X component, mitochondrial |
| 蛋白大小 | 501 aa / 54.1 kDa |
| UniProt ID | O00330 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Mitochondrion matrix |
| 蛋白大小 | 10/10 | ×1 | 10 | 501 aa / 54.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=2136 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=77.3; PDB: 1ZY8, 2DNC, 2F5Z, 2F60, 6H60 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003016, IPR001078, IPR000089, IPR023213, IPR045 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Mitochondrion matrix | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- mitochondrial matrix (GO:0005759)
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)
- plasma membrane (GO:0005886)
- pyruvate dehydrogenase complex (GO:0045254)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2136 |
| PubMed broad count | 3525 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PDX1 |

**关键文献**:
1. Non-functional pancreatic neuroendocrine tumours: ATRX/DAXX and alternative lengthening of telomeres (ALT) are prognostically independent from ARX/PDX1 expression and tumour size.. *Gut*. PMID: 33849943
2. TAZ promotes PDX1-mediated insulinogenesis.. *Cellular and molecular life sciences : CMLS*. PMID: 35279781
3. Pancreatic agenesis and altered m6A methylation in the pancreas of PDX1-mutant cynomolgus macaques.. *Zoological research*. PMID: 39318126
4. CFTR represses a PDX1 axis to govern pancreatic ductal cell fate.. *iScience*. PMID: 39687022
5. CK2 regulates somatostatin expression in pancreatic delta cells.. *Islets*. PMID: 40474387

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.3 |
| 高置信度残基 (pLDDT>90) 占比 | 40.5% |
| 置信残基 (pLDDT 70-90) 占比 | 29.7% |
| 中等置信 (pLDDT 50-70) 占比 | 11.2% |
| 低置信 (pLDDT<50) 占比 | 18.6% |
| 有序区域 (pLDDT>70) 占比 | 70.2% |
| 可用 PDB 条目 | 1ZY8, 2DNC, 2F5Z, 2F60, 6H60 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1ZY8, 2DNC, 2F5Z, 2F60, 6H60）+ AlphaFold极高置信度预测（pLDDT=77.3），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003016, IPR001078, IPR000089, IPR023213, IPR045257; Pfam: PF00198, PF00364, PF02817 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SPOP | 0.972 | 0.971 | — |
| FOXA2 | 0.968 | 0.095 | — |
| INS | 0.966 | 0.000 | — |
| GCK | 0.965 | 0.000 | — |
| MAFA | 0.949 | 0.301 | — |
| PBX1 | 0.928 | 0.458 | — |
| ONECUT1 | 0.928 | 0.000 | — |
| PRKACG | 0.922 | 0.000 | — |
| PRKACA | 0.921 | 0.000 | — |
| PRKACB | 0.921 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SNZ1 | psi-mi:"MI:0018"(two hybrid) | pubmed:18719252 |
| SNZ3 | psi-mi:"MI:0018"(two hybrid) | pubmed:18719252 |
| SNZ2 | psi-mi:"MI:0018"(two hybrid) | pubmed:18719252 |
| EWSR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| LPD1 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| CYM1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| YHI9 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| PDB1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| RPS0A | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| TEF1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.3 + PDB: 1ZY8, 2DNC, 2F5Z, 2F60, 6H60 | pLDDT=77.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Mitochondrion matrix / Nucleoplasm | 一致 |
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
1. PDX1 — Pyruvate dehydrogenase protein X component, mitochondrial，研究基础较多，新颖性有限。
2. 蛋白大小501 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2136 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 2136 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O00330
- Protein Atlas: https://www.proteinatlas.org/ENSG00000139515-PDX1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PDX1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O00330
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
