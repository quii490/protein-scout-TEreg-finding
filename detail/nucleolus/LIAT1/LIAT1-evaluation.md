---
type: protein-evaluation
gene: "LIAT1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LIAT1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LIAT1 / C17orf97 |
| 蛋白名称 | Protein LIAT1 |
| 蛋白大小 | 453 aa / 49.7 kDa |
| UniProt ID | Q6ZQX7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; 额外: Cytosol; UniProt: Nucleus, nucleolus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 453 aa / 49.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=46.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR038794 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 13 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Cytosol | Approved |
| UniProt | Nucleus, nucleolus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleolus (GO:0005730)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C17orf97 |

**关键文献**:
1. tRNA (Arg) binds in vitro TDP-43 RNA recognition motifs and ligand of Ate1 protein LIAT1.. *microPublication biology*. PMID: 39081859
2. Liat1, an arginyltransferase-binding protein whose evolution among primates involved changes in the numbers of its 10-residue repeats.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 25369936
3. Erratum: Corrigendum: tRNA (Arg) binds in vitro TDP-43 RNA recognition motifs and ligand of Ate1 protein LIAT1.. *microPublication biology*. PMID: 39897169
4. The Ligand of Ate1 is intrinsically disordered and participates in nucleolar phase separation regulated by Jumonji Domain Containing 6.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 33443146

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 46.4 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 4.4% |
| 中等置信 (pLDDT 50-70) 占比 | 31.8% |
| 低置信 (pLDDT<50) 占比 | 63.8% |
| 有序区域 (pLDDT>70) 占比 | 4.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=46.4），有序残基占 4.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR038794 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KRT7 | 0.960 | 0.000 | — |
| CDX2 | 0.904 | 0.000 | — |
| KRT19 | 0.877 | 0.000 | — |
| KRT5 | 0.824 | 0.000 | — |
| NAPSA | 0.814 | 0.000 | — |
| SYP | 0.812 | 0.000 | — |
| PIP | 0.810 | 0.000 | — |
| KRT18 | 0.801 | 0.000 | — |
| PAX8 | 0.792 | 0.000 | — |
| CEACAM5 | 0.788 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| VWF | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| VIM | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| RAB5A | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| ACTA1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| HSPD1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| PECAM1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| PLD1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| ESR1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| CYP3A4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| ATP1A3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:32814053|imex:IM-28217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 13
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 13 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=46.4 + PDB: 无 | pLDDT=46.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus, nucleolus; Cytoplasm / Nucleoli; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 13 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. LIAT1 — Protein LIAT1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小453 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=46.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZQX7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000187624-C17orf97/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LIAT1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZQX7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
