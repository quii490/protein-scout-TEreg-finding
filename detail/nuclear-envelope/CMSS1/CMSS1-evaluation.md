---
type: protein-evaluation
gene: "CMSS1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CMSS1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CMSS1 |
| 蛋白名称 | Protein CMSS1 |
| 蛋白大小 | 279 aa / 31.9 kDa |
| UniProt ID | Q9BQ75 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoli; 额外: Nucleoplasm, Nuclear membrane, Mitochondria; UniProt: 无注释 |
| 蛋白大小 | 10/10 | x1 | 10 | 279 aa / 31.9 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=79.9; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.0/180** | |
| **归一化总分** | | | **72.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Nucleoplasm, Nuclear membrane, Mitochondria | Approved |
| UniProt | 无注释 | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 16 |
| 别名(未计入scoring) |  |

**关键文献**:
1. CMSS1 promoted CXCL8-CXCR1/2 pathway to accelerate the invasion and immune escape of triple-negative breast cancer.. *J Mol Histol*. PMID: 41493665
2. Cmss1 limits FMDV infection by enhancing antigen presentation and CD8(+) T cell responses.. *J Virol*. PMID: 41277842
3. Kazachstania pintolopesii triggers an immune-endothelial-fibroblast cascade and drives inflammatory arthritis and tissue fibrosis in genetically susceptible hosts.. *Front Cell Infect Microbiol*. PMID: 41459160
4. Cms1 Ribosomal Small Subunit Homolog Promotes HCC Proliferation and Migration by Modulating the TNF/NF-κB Signaling Pathway.. *J Hepatocell Carcinoma*. PMID: 41179490
5. Acceleration of Calvarial Bone Regeneration by Stem Cell Recruitment with a Multifunctional Hydrogel.. *Adv Healthc Mater*. PMID: 40556603

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.9 |
| 高置信度残基 (pLDDT>90) 占比 | 62.0% |
| 置信残基 (pLDDT 70-90) 占比 | 10.8% |
| 中等置信 (pLDDT 50-70) 占比 | 4.7% |
| 低置信 (pLDDT<50) 占比 | 22.6% |
| 有序区域 (pLDDT>70) 占比 | 72.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=79.9，有序区 72.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LTV1 | 0.000 | 0.000 | — |
| NOP53 | 0.000 | 0.000 | — |
| BYSL | 0.000 | 0.000 | — |
| ZC3H11B | 0.000 | 0.000 | — |
| UTP23 | 0.000 | 0.000 | — |
| NIFK | 0.000 | 0.000 | — |
| ESF1 | 0.000 | 0.000 | — |
| NOL10 | 0.000 | 0.000 | — |
| RBM28 | 0.000 | 0.000 | — |
| KRR1 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9BQ75 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P21453 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:O60245-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q00987-11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:C9J384 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.9 + PDB: 无 | pLDDT=79.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli; 额外: Nucleoplasm, Nuclear membrane, Mitoc | 待确认 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. CMSS1 -- Protein CMSS1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小279 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. 结构数据可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BQ75
- Protein Atlas: https://www.proteinatlas.org/ENSG00000184220-CMSS1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CMSS1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BQ75
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BQ75-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
