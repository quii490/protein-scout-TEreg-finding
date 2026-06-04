---
type: protein-evaluation
gene: "CDT1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CDT1 — REJECTED (研究热度过高 (PubMed strict=385，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CDT1 |
| 蛋白名称 | DNA replication factor Cdt1 |
| 蛋白大小 | 546 aa / 60.4 kDa |
| UniProt ID | Q9H211 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Nuclear bodies; UniProt: Nucleus; Chromosome, centromere, kinetochore |
| 蛋白大小 | 10/10 | ×1 | 10 | 546 aa / 60.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=385 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=73.4; PDB: 2LE8, 2WVR, 6QCG, 8RWV, 8S0E, 8S0F |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR045173, IPR032054, IPR038090, IPR014939, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **102.0/180** | |
| **归一化总分** | | | **56.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies | Supported |
| UniProt | Nucleus; Chromosome, centromere, kinetochore | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- kinetochore (GO:0000776)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 385 |
| PubMed broad count | 736 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. FUCCI Reporter Gene-Based Cell Cycle Analysis.. *Methods in molecular biology (Clifton, N.J.)*. PMID: 37142935
2. Two coral fluorescent proteins of distinct colors for sharp visualization of cell-cycle progression.. *Cell structure and function*. PMID: 37394513
3. Self-assembling protein microarrays.. *Science (New York, N.Y.)*. PMID: 15232106
4. GMNN mutations cause female infertility characterized by preimplantation embryo arrest through regulating DNA re-replication.. *Science China. Life sciences*. PMID: 40455380
5. A high-throughput screening identifies MCM chromatin loading inhibitors targeting cells with increased replication origins.. *iScience*. PMID: 39184446

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.4 |
| 高置信度残基 (pLDDT>90) 占比 | 33.7% |
| 置信残基 (pLDDT 70-90) 占比 | 27.7% |
| 中等置信 (pLDDT 50-70) 占比 | 12.6% |
| 低置信 (pLDDT<50) 占比 | 26.0% |
| 有序区域 (pLDDT>70) 占比 | 61.4% |
| 可用 PDB 条目 | 2LE8, 2WVR, 6QCG, 8RWV, 8S0E, 8S0F |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2LE8, 2WVR, 6QCG, 8RWV, 8S0E, 8S0F）+ AlphaFold极高置信度预测（pLDDT=73.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045173, IPR032054, IPR038090, IPR014939, IPR036390; Pfam: PF08839, PF16679 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ORC1 | 0.999 | 0.997 | — |
| GMNN | 0.999 | 0.997 | — |
| MCM5 | 0.999 | 0.965 | — |
| MCM4 | 0.999 | 0.974 | — |
| ORC4 | 0.999 | 0.966 | — |
| MCM7 | 0.999 | 0.971 | — |
| MCM6 | 0.999 | 0.992 | — |
| MCM2 | 0.999 | 0.919 | — |
| ORC2 | 0.999 | 0.997 | — |
| MCM3 | 0.999 | 0.964 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| dup | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |
| CG34379-RG | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| ari-2 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Cdc5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20353594|imex:IM-17302| |
| unmet | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Ar1 | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| Men | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| dally | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| Gdi | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| Gprk2 | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.4 + PDB: 2LE8, 2WVR, 6QCG, 8RWV, 8S0E,  | pLDDT=73.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome, centromere, kinetochore / Nucleoplasm; 额外: Nuclear bodies | 一致 |
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
1. CDT1 — DNA replication factor Cdt1，研究基础较多，新颖性有限。
2. 蛋白大小546 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 385 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 385 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H211
- Protein Atlas: https://www.proteinatlas.org/ENSG00000167513-CDT1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CDT1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H211
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
