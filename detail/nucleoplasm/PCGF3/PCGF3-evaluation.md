---
type: protein-evaluation
gene: "PCGF3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PCGF3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PCGF3 / RNF3, RNF3A |
| 蛋白名称 | Polycomb group RING finger protein 3 |
| 蛋白大小 | 242 aa / 28.1 kDa |
| UniProt ID | Q3KNV8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus; Nucleus, nucleoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 242 aa / 28.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=23 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=85.3; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR051507, IPR032443, IPR001841, IPR013083, IPR017 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **136.5/180** | |
| **归一化总分** | | | **75.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Nucleus, nucleoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- PcG protein complex (GO:0031519)
- PRC1 complex (GO:0035102)
- X chromosome (GO:0000805)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 33 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RNF3, RNF3A |

**关键文献**:
1. AUTS2 isoforms control neuronal differentiation.. *Molecular psychiatry*. PMID: 30953002
2. Genome-Wide RNAi Screen Identify Melanoma-Associated Antigen Mageb3 Involved in X Chromosome Inactivation.. *Journal of molecular biology*. PMID: 29800566
3. miR-210-3p Promotes Lung Cancer Development and Progression by Modulating USF1 and PCGF3.. *OncoTargets and therapy*. PMID: 34140779
4. Biological functions of chromobox (CBX) proteins in stem cell self-renewal, lineage-commitment, cancer and development.. *Bone*. PMID: 32979540
5. Linking DNA methylation in brain regions to Alzheimer's disease risk: a Mendelian randomization study.. *Human molecular genetics*. PMID: 40267236

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.3 |
| 高置信度残基 (pLDDT>90) 占比 | 74.4% |
| 置信残基 (pLDDT 70-90) 占比 | 7.4% |
| 中等置信 (pLDDT 50-70) 占比 | 3.3% |
| 低置信 (pLDDT<50) 占比 | 14.9% |
| 有序区域 (pLDDT>70) 占比 | 81.8% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=85.3，有序区 81.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051507, IPR032443, IPR001841, IPR013083, IPR017907; Pfam: PF16207, PF13923 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RING1 | 0.999 | 0.820 | — |
| RNF2 | 0.995 | 0.866 | — |
| PCGF5 | 0.993 | 0.309 | — |
| RYBP | 0.987 | 0.847 | — |
| PCGF2 | 0.985 | 0.309 | — |
| CBX7 | 0.985 | 0.673 | — |
| CBX6 | 0.982 | 0.616 | — |
| CBX8 | 0.981 | 0.657 | — |
| PCGF1 | 0.981 | 0.312 | — |
| PCGF6 | 0.980 | 0.197 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| UBE2C | psi-mi:"MI:0018"(two hybrid) | imex:IM-11696|pubmed:19549727 |
| Rnf2 | psi-mi:"MI:0096"(pull down) | pubmed:17296600 |
| RING1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15696|pubmed:22493164 |
| TRIM9 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15696|pubmed:22493164 |
| DZIP3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15696|pubmed:22493164 |
| BMI1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15696|pubmed:22493164 |
| CSNK2A2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-17578|pubmed:23455922 |
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| PHC1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| NISCH | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.3 + PDB: 无 | pLDDT=85.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, nucleoplasm / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. PCGF3 — Polycomb group RING finger protein 3，非常新颖，仅有少数基础研究。
2. 蛋白大小242 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q3KNV8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000185619-PCGF3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PCGF3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q3KNV8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
