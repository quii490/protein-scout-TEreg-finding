---
type: protein-evaluation
gene: "PROX1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PROX1 — REJECTED (研究热度过高 (PubMed strict=613，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PROX1 |
| 蛋白名称 | Prospero homeobox protein 1 |
| 蛋白大小 | 737 aa / 83.2 kDa |
| UniProt ID | Q92786 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 737 aa / 83.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=613 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.4; PDB: 2LMD |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR023082, IPR037131, IPR009057, IPR039350; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.5/180** | |
| **归一化总分** | | | **44.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 613 |
| PubMed broad count | 1333 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Increased CSF drainage by non-invasive manipulation of cervical lymphatics.. *Nature*. PMID: 40468071
2. Decoding the development of the human hippocampus.. *Nature*. PMID: 31942070
3. Nasopharyngeal lymphatic plexus is a hub for cerebrospinal fluid drainage.. *Nature*. PMID: 38200313
4. Lipid droplet degradation by autophagy connects mitochondria metabolism to Prox1-driven expression of lymphatic genes and lymphangiogenesis.. *Nature communications*. PMID: 35589749
5. Molecules That Have Rarely Been Studied in Lymphatic Endothelial Cells.. *International journal of molecular sciences*. PMID: 39596293

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.4 |
| 高置信度残基 (pLDDT>90) 占比 | 27.1% |
| 置信残基 (pLDDT 70-90) 占比 | 8.1% |
| 中等置信 (pLDDT 50-70) 占比 | 11.0% |
| 低置信 (pLDDT<50) 占比 | 53.7% |
| 有序区域 (pLDDT>70) 占比 | 35.2% |
| 可用 PDB 条目 | 2LMD |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=60.4），有序残基占 35.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR023082, IPR037131, IPR009057, IPR039350; Pfam: PF05044 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PDPN | 0.913 | 0.000 | — |
| SOX18 | 0.867 | 0.000 | — |
| VEGFD | 0.843 | 0.000 | — |
| LYVE1 | 0.826 | 0.045 | — |
| VEGFC | 0.821 | 0.000 | — |
| NR5A2 | 0.819 | 0.510 | — |
| FOXN4 | 0.808 | 0.000 | — |
| FLT4 | 0.778 | 0.000 | — |
| HNF4A | 0.777 | 0.364 | — |
| ONECUT1 | 0.770 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CTBP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15364|pubmed:21988832 |
| SMAD3 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| GIT2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| LBH | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CEBPZ | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| MBD3L2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| Cyfip1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| IRF4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| CCL26 | psi-mi:"MI:0432"(one hybrid) | doi:10.1093/nar/gkaa1055|pubme |
| IL18 | psi-mi:"MI:0432"(one hybrid) | doi:10.1093/nar/gkaa1055|pubme |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.4 + PDB: 2LMD | pLDDT=60.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. PROX1 — Prospero homeobox protein 1，研究基础较多，新颖性有限。
2. 蛋白大小737 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 613 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=60.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 613 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92786
- Protein Atlas: https://www.proteinatlas.org/ENSG00000117707-PROX1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PROX1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92786
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
