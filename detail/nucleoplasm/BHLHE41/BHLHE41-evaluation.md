---
type: protein-evaluation
gene: "BHLHE41"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BHLHE41 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BHLHE41 |
| 蛋白名称 | BHLHE41 (UniProt未获取) |
| 蛋白大小 | 未知 aa / 未知 kDa |
| UniProt ID | BHLHE41 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: 暂无数据（UniProt获取失败） |
| 蛋白大小 | 5/10 | ×1 | 5 | 未知 aa / 未知 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=83 篇 (≤100→2) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | 暂无数据 (UniProt未获取) |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **78.5/180** | |
| **归一化总分** | | | **43.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Approved |
| UniProt | 暂无数据（UniProt获取失败） | 获取失败 |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释 (UniProt未获取)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 83 |
| PubMed broad count | 184 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. METTL3 Inhibits Antitumor Immunity by Targeting m(6)A-BHLHE41-CXCL1/CXCR2 Axis to Promote Colorectal Cancer.. *Gastroenterology*. PMID: 35700773
2. Approach to Functions of BHLHE41/DEC2 in Non-Small Lung Cancer Development.. *International journal of molecular sciences*. PMID: 37511489
3. BHLHE41, a transcriptional repressor involved in physiological processes and tumor development.. *Cellular oncology (Dordrecht, Netherlands)*. PMID: 39254779
4. Bhlhe40 and Bhlhe41 transcription factors regulate alveolar macrophage self-renewal and identity.. *The EMBO journal*. PMID: 31414712
5. O-GlcNAcylation of circadian clock protein Bmal1 impairs cognitive function in diabetic mice.. *The EMBO journal*. PMID: 39375536

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 暂无数据 (UniProt未获取) |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PER2 | 0.999 | 0.968 | — |
| ARNTL | 0.989 | 0.089 | — |
| NFIL3 | 0.989 | 0.057 | — |
| CRY1 | 0.978 | 0.521 | — |
| BHLHE40 | 0.971 | 0.449 | — |
| CLOCK | 0.969 | 0.332 | — |
| NPAS2 | 0.969 | 0.189 | — |
| PER3 | 0.960 | 0.457 | — |
| CRY2 | 0.948 | 0.418 | — |
| NR1D1 | 0.940 | 0.046 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSMUSP00000032386.5 | psi-mi:"MI:0018"(two hybrid) | pubmed:23555304|imex:IM-20564 |
| Clock | psi-mi:"MI:0018"(two hybrid) | pubmed:23555304|imex:IM-20564 |
| Cry1 | psi-mi:"MI:0018"(two hybrid) | pubmed:23555304|imex:IM-20564 |
| Csnk1e | psi-mi:"MI:0018"(two hybrid) | pubmed:23555304|imex:IM-20564 |
| Cry2 | psi-mi:"MI:0018"(two hybrid) | pubmed:23555304|imex:IM-20564 |
| CSNK2A1 | psi-mi:"MI:0018"(two hybrid) | pubmed:23555304|imex:IM-20564 |
| CSNK2A2 | psi-mi:"MI:0018"(two hybrid) | pubmed:23555304|imex:IM-20564 |
| CSNK2B | psi-mi:"MI:0018"(two hybrid) | pubmed:23555304|imex:IM-20564 |
| BHLHE40 | psi-mi:"MI:0018"(two hybrid) | pubmed:23555304|imex:IM-20564 |
| Btrc | psi-mi:"MI:0018"(two hybrid) | pubmed:23555304|imex:IM-20564 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | 暂无数据（UniProt获取失败） / Nucleoplasm; 额外: Vesicles | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. BHLHE41 — BHLHE41 (UniProt未获取)，研究基础较多，新颖性有限。
2. 蛋白大小未知 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 83 篇，已有一定研究基础
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/BHLHE41
- Protein Atlas: https://www.proteinatlas.org/ENSG00000123095-BHLHE41/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BHLHE41
- AlphaFold: https://alphafold.ebi.ac.uk/entry/BHLHE41
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
