---
type: protein-evaluation
gene: "GIMAP4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GIMAP4 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GIMAP4 / IAN1, IMAP4 |
| 蛋白名称 | GTPase IMAP family member 4 |
| 蛋白大小 | 329 aa / 37.5 kDa |
| UniProt ID | Q9NUV9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Vesicles, Cytosol; UniProt: Cytoplasm, cytosol |
| 蛋白大小 | 10/10 | ×1 | 10 | 329 aa / 37.5 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=40 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=85.5; PDB: 3LXX |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR006703, IPR045058, IPR027417; Pfam: PF04548 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **109.0/180** | |
| **归一化总分** | | | **60.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles, Cytosol | Approved |
| UniProt | Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 40 |
| PubMed broad count | 51 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: IAN1, IMAP4 |

**关键文献**:
1. Gimap4 accelerates T-cell death.. *Blood*. PMID: 16569770
2. Identification and Validation of Potential Immune-Related Genes for Endometriosis.. *American journal of reproductive immunology (New York, N.Y. : 1989)*. PMID: 40367358
3. Prognostic Value of GIMAP4 and Its Role in Promoting Immune Cell Infiltration into Tumor Microenvironment of Lung Adenocarcinoma.. *BioMed research international*. PMID: 36246963
4. Tubulin- and actin-associating GIMAP4 is required for IFN-γ secretion during Th cell differentiation.. *Immunology and cell biology*. PMID: 25287446
5. Identification of hub genes for early detection of bone metastasis in breast cancer.. *Frontiers in endocrinology*. PMID: 36246872

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.5 |
| 高置信度残基 (pLDDT>90) 占比 | 67.2% |
| 置信残基 (pLDDT 70-90) 占比 | 19.1% |
| 中等置信 (pLDDT 50-70) 占比 | 3.6% |
| 低置信 (pLDDT<50) 占比 | 10.0% |
| 有序区域 (pLDDT>70) 占比 | 86.3% |
| 可用 PDB 条目 | 3LXX |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=85.5，有序区 86.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006703, IPR045058, IPR027417; Pfam: PF04548 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GIMAP7 | 0.929 | 0.000 | — |
| GIMAP8 | 0.911 | 0.000 | — |
| GIMAP6 | 0.907 | 0.000 | — |
| GIMAP5 | 0.898 | 0.000 | — |
| GIMAP1 | 0.818 | 0.000 | — |
| FGL2 | 0.606 | 0.069 | — |
| GZMA | 0.559 | 0.107 | — |
| TAL1 | 0.547 | 0.000 | — |
| ARHGAP30 | 0.540 | 0.000 | — |
| GIMAP1-GIMAP5 | 0.525 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| nhaD | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| GNA13 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CDH5 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:39232006|imex:IM-30239 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.5 + PDB: 3LXX | pLDDT=85.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol / Vesicles, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GIMAP4 — GTPase IMAP family member 4，非常新颖，仅有少数基础研究。
2. 蛋白大小329 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 40 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NUV9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000133574-GIMAP4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GIMAP4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NUV9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
