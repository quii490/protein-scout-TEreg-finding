---
type: protein-evaluation
gene: "GATA3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GATA3 — REJECTED (研究热度过高 (PubMed strict=3161，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GATA3 |
| 蛋白名称 | Trans-acting T-cell-specific transcription factor GATA-3 |
| 蛋白大小 | 443 aa / 47.9 kDa |
| UniProt ID | P23771 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 443 aa / 47.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=3161 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.1; PDB: 4HC7, 4HC9, 4HCA |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR016374, IPR039355, IPR000679, IPR013088; Pfam:  |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **86.0/180** | |
| **归一化总分** | | | **47.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3161 |
| PubMed broad count | 6578 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Comprehensive molecular portraits of human breast tumours.. *Nature*. PMID: 23000897
2. Gene of the month: GATA3.. *Journal of clinical pathology*. PMID: 37726118
3. GATA3 mediates doxorubicin resistance by inhibiting CYB5R2-catalyzed iron reduction in breast cancer cells.. *Drug resistance updates : reviews and commentaries in antimicrobial and anticancer chemotherapy*. PMID: 37230023
4. Barakat syndrome revisited.. *American journal of medical genetics. Part A*. PMID: 29663634
5. Hyperlipidemia Triggers Trophoblast Cell Dysfunction and Preeclampsia via the AMPK/GATA3/FTL Pathway.. *Hypertension (Dallas, Tex. : 1979)*. PMID: 40421527

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.1 |
| 高置信度残基 (pLDDT>90) 占比 | 18.3% |
| 置信残基 (pLDDT 70-90) 占比 | 4.3% |
| 中等置信 (pLDDT 50-70) 占比 | 24.6% |
| 低置信 (pLDDT<50) 占比 | 52.8% |
| 有序区域 (pLDDT>70) 占比 | 22.6% |
| 可用 PDB 条目 | 4HC7, 4HC9, 4HCA |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=58.1），有序残基占 22.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016374, IPR039355, IPR000679, IPR013088; Pfam: PF00320 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CCL5 | psi-mi:"MI:0412"(electrophoretic mobility supershi | imex:IM-27584|pubmed:10640782 |
| KRTAP12-1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ACTN2 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-25511|pubmed:25910212 |
| KRTAP6-2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TCP23 | psi-mi:"MI:1356"(validated two hybrid) | doi:10.1038/nmeth.4343|pubmed: |
| MYB52 | psi-mi:"MI:1356"(validated two hybrid) | doi:10.1038/nmeth.4343|pubmed: |
| AGL81 | psi-mi:"MI:1356"(validated two hybrid) | doi:10.1038/nmeth.4343|pubmed: |
| BHLH120 | psi-mi:"MI:2277"(Cr-two hybrid) | doi:10.1038/nmeth.4343|pubmed: |
| O65690 | psi-mi:"MI:2277"(Cr-two hybrid) | doi:10.1038/nmeth.4343|pubmed: |
| UPB1 | psi-mi:"MI:2277"(Cr-two hybrid) | doi:10.1038/nmeth.4343|pubmed: |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.1 + PDB: 4HC7, 4HC9, 4HCA | pLDDT=58.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. GATA3 — Trans-acting T-cell-specific transcription factor GATA-3，研究基础较多，新颖性有限。
2. 蛋白大小443 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3161 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=58.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 3161 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P23771
- Protein Atlas: https://www.proteinatlas.org/ENSG00000107485-GATA3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GATA3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P23771
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
