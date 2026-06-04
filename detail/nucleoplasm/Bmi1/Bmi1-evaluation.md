---
type: protein-evaluation
gene: "Bmi1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## Bmi1 — REJECTED (研究热度过高 (PubMed strict=1626，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | Bmi1 / PCGF4, RNF51 |
| 蛋白名称 | Polycomb complex protein BMI-1 |
| 蛋白大小 | 326 aa / 36.9 kDa |
| UniProt ID | P35226 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear bodies; 额外: Nucleoli, Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 326 aa / 36.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1626 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=76.7; PDB: 2H0D, 2NA1, 3RPG, 4R8P, 5FR6, 6WI7, 6WI8 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR032443, IPR001841, IPR013083, IPR017907; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear bodies; 额外: Nucleoli, Cytosol | Approved |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- heterochromatin (GO:0000792)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- PcG protein complex (GO:0031519)
- PRC1 complex (GO:0035102)
- ubiquitin ligase complex (GO:0000151)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1626 |
| PubMed broad count | 2848 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PCGF4, RNF51 |

**关键文献**:
1. Molecular basis of polycomb group protein-mediated fetal hemoglobin repression.. *Blood*. PMID: 36893455
2. BMI1 regulates human erythroid self-renewal through both gene repression and gene activation.. *Nature communications*. PMID: 40817093
3. SOX4-BMI1 axis promotes non-small cell lung cancer progression and facilitates angiogenesis by suppressing ZNF24.. *Cell death & disease*. PMID: 39349443
4. DROSHA, DICER, and damage-induced long ncRNA control BMI1-dependent transcriptional repression at DNA double-strand break.. *Cell reports*. PMID: 41348540
5. BMI1 fine-tunes gene repression and activation to safeguard undifferentiated spermatogonia fate.. *Frontiers in cell and developmental biology*. PMID: 37169021

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.7 |
| 高置信度残基 (pLDDT>90) 占比 | 52.1% |
| 置信残基 (pLDDT 70-90) 占比 | 9.8% |
| 中等置信 (pLDDT 50-70) 占比 | 13.2% |
| 低置信 (pLDDT<50) 占比 | 24.8% |
| 有序区域 (pLDDT>70) 占比 | 61.9% |
| 可用 PDB 条目 | 2H0D, 2NA1, 3RPG, 4R8P, 5FR6, 6WI7, 6WI8, 7ND1, 8GRM, 8PP7 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2H0D, 2NA1, 3RPG, 4R8P, 5FR6, 6WI7, 6WI8, 7ND1, 8GRM, 8PP7）+ AlphaFold极高置信度预测（pLDDT=76.7），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR032443, IPR001841, IPR013083, IPR017907; Pfam: PF16207, PF13923 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CBX8 | 0.999 | 0.935 | — |
| PHC2 | 0.999 | 0.906 | — |
| PHC1 | 0.999 | 0.896 | — |
| CBX4 | 0.999 | 0.926 | — |
| PCGF2 | 0.999 | 0.829 | — |
| RING1 | 0.999 | 0.960 | — |
| RNF2 | 0.999 | 0.999 | — |
| EZH2 | 0.999 | 0.610 | — |
| CBX2 | 0.999 | 0.863 | — |
| CBX7 | 0.999 | 0.893 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000365851.3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:34316702|imex:IM-29168 |
| Rnf2 | psi-mi:"MI:0018"(two hybrid) | pubmed:12183370 |
| SOCS2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CBX4 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:22078878|imex:IM-16600 |
| UBE2I | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| Kdm2b | psi-mi:"MI:0096"(pull down) | pubmed:17296600 |
| RING1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15696|pubmed:22493164 |
| VPS11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15696|pubmed:22493164 |
| RNF114 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15696|pubmed:22493164 |
| TRIM27 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15696|pubmed:22493164 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.7 + PDB: 2H0D, 2NA1, 3RPG, 4R8P, 5FR6,  | pLDDT=76.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm, Nuclear bodies; 额外: Nucleoli, Cytosol | 一致 |
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
1. Bmi1 — Polycomb complex protein BMI-1，研究基础较多，新颖性有限。
2. 蛋白大小326 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1626 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1626 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P35226
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168283-BMI1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=Bmi1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P35226
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
