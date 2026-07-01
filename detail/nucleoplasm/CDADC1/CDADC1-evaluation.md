---
type: protein-evaluation
gene: "CDADC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, E-batch]
status: scored
---

## CDADC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CDADC1 / — |
| 蛋白名称 | Cytidine and dCMP deaminase domain-containing protein 1 |
| 蛋白大小 | 514 aa / 58.5 kDa |
| UniProt ID | Q9BWV3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 10/10 | ×4 | 40 | HPA: Nucleoplasm; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 514 aa / 58.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=79.6; PDB: 暂无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR016192, IPR002125, IPR016193, IPR015517, IPR035105; Pfam: PF00383 |
| PPI 网络 | 9/10 | ×3 | 27 | STRING 15 partners; IntAct 12 interactions |
| 互证加分 | — | max +3 | 1.5 | AlphaFold 结构预测: +0.25 |
| **原始总分** | | | **163.5/180** | |
| **归一化总分 (÷1.83)** | | | **89.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Cytoplasm | ECO:0000305
| UniProt | Nucleus | ECO:0000305

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- cytoplasm (GO:0005737) [IMP:UniProtKB]
- nucleus (GO:0005634) [IMP:UniProtKB]

**结论**: HPA: Nucleoplasm; UniProt: Cytoplasm; Nucleus

#### 3.2 蛋白大小评估

**评价**: 514 aa / 58.5 kDa，大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed 搜索链接 | [CDADC1 PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=CDADC1) |

**关键文献**:
暂无文献记录。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.6 |
| 高置信度残基 (pLDDT>90) 占比 | 61.9% |
| 置信残基 (pLDDT 70-90) 占比 | 11.5% |
| 中等置信 (pLDDT 50-70) 占比 | 8.9% |
| 低置信 (pLDDT<50) 占比 | 17.7% |
| 有序区域 (pLDDT>70) 占比 | 73.4% |
| 可用 PDB 条目 | 暂无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量中等。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016192, IPR002125, IPR016193, IPR015517, IPR035105; Pfam: PF00383 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TYMS | 0.799 | 0.000 | — |
| TK1 | 0.795 | 0.000 | — |
| TYMP | 0.727 | 0.000 | — |
| FNDC3A | 0.702 | 0.000 | — |
| CAB39L | 0.666 | 0.000 | — |
| SETDB2 | 0.647 | 0.000 | — |
| NUDT15 | 0.646 | 0.000 | — |
| RCBTB1 | 0.641 | 0.000 | — |
| MLNR | 0.596 | 0.000 | — |
| PHF11 | 0.593 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| H1-1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653|doi:10.1074/mcp.ra118.000924 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| BLTP3B | psi-mi:"MI:2222"(inference by socio-affinity scoring) | pubmed:unassigned1312 |
| AMOTL1 | psi-mi:"MI:2222"(inference by socio-affinity scoring) | pubmed:unassigned1312 |
| HMBOX1 | psi-mi:"MI:2222"(inference by socio-affinity scoring) | pubmed:unassigned1312 |
| TLK2 | psi-mi:"MI:2222"(inference by socio-affinity scoring) | pubmed:unassigned1312 |
| IFFO1 | psi-mi:"MI:2222"(inference by socio-affinity scoring) | pubmed:unassigned1312 |
| DDHD1 | psi-mi:"MI:2222"(inference by socio-affinity scoring) | pubmed:unassigned1312 |
| COBLL1 | psi-mi:"MI:2222"(inference by socio-affinity scoring) | pubmed:unassigned1312 |
| SCML1 | psi-mi:"MI:2222"(inference by socio-affinity scoring) | pubmed:unassigned1312 |

**PPI 互证分析**:
STRING 15 个预测互作，IntAct 12 个实验互作。调控相关配体占比 0/15。

**评价**: STRING + IntAct 双源 PPI 数据充分。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold | pLDDT=79.6, v6 | 预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 12 interactions | 数据充分 |

**互证加分明细**:
- AlphaFold 结构预测: +0.25
- 多库定位一致 (HPA+UniProt): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5

**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐

**归一化总分**: 89.3/100

**核心优势**:
1. CDADC1 — Cytidine and dCMP deaminase domain-containing protein 1，极度新颖，几乎未被系统研究（PubMed 4 篇）。
2. 蛋白大小514 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| IFFO1 | BioGRID | 1 |
| SCML1 | BioGRID | 1 |
| HMBOX1 | BioGRID | 1 |
| HDAC2 | BioGRID | 1 |
| DYNLL1 | BioGRID | 1 |
| DYNLL2 | BioGRID | 1 |
| AMOTL1 | BioGRID | 0 |
| COBLL1 | BioGRID | 0 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与核内 TE 调控过程，但目前无直接实验证据支持。需实验验证。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/CDADC1

### PubMed

**Count: 7**

| PMID | Title |
|---|---|
| 40504152 | CDADC1 is a vertebrate-specific dCTP deaminase that metabolizes gemcitabine and decitabine to prevent cellular toxicity. |
| 40324085 | Activity and structure of human (d)CTP deaminase CDADC1. |
| 39628352 | Targeted RNA sequencing in diagnostically challenging head and neck carcinomas identifies novel MON2::STAT6, NFATC2::NUTM2B, POC5::RAF1, and NSD3::NCO |
| 39099665 | Development and Validation of Diagnostic Models for Transcriptomic Signature Genes for Multiple Tissues in Osteoarthritis. |
| 28589857 | Identification of epigenetic interactions between miRNA and DNA methylation associated with gene expression as potential prognostic markers in bladder |


