---
type: protein-evaluation
gene: "MAB21L2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MAB21L2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MAB21L2 |
| 蛋白名称 | Protein mab-21-like 2 |
| 蛋白大小 | 359 aa / 40.9 kDa |
| UniProt ID | Q9Y586 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 359 aa / 40.9 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=44 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=94.8; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR046903, IPR046906, IPR024810; Pfam: PF03281, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.5/180** | |
| **归一化总分** | | | **65.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 44 |
| PubMed broad count | 61 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Deletion upstream of MAB21L2 highlights the importance of evolutionarily conserved non-coding sequences for eye development.. *Nature communications*. PMID: 39455595
2. A novel SMARCC1 BAFopathy implicates neural progenitor epigenetic dysregulation in human hydrocephalus.. *Brain : a journal of neurology*. PMID: 38128548
3. Identification of HSPA8 as an interacting partner of MAB21L2 and an important factor in eye development.. *Developmental dynamics : an official publication of the American Association of Anatomists*. PMID: 36576422
4. Zebrafish mab21l2 mutants possess severe defects in optic cup morphogenesis, lens and cornea development.. *Developmental dynamics : an official publication of the American Association of Anatomists*. PMID: 31037784
5. Requirement for Mab21l2 during development of murine retina and ventral body wall.. *Developmental biology*. PMID: 15385160

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.8 |
| 高置信度残基 (pLDDT>90) 占比 | 90.5% |
| 置信残基 (pLDDT 70-90) 占比 | 5.8% |
| 中等置信 (pLDDT 50-70) 占比 | 3.6% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 96.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=94.8，有序区 96.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR046903, IPR046906, IPR024810; Pfam: PF03281, PF20266 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MEIS2 | 0.850 | 0.818 | — |
| MEIS1 | 0.794 | 0.746 | — |
| PBX3 | 0.722 | 0.694 | — |
| PBX1 | 0.709 | 0.687 | — |
| PBX2 | 0.681 | 0.665 | — |
| MIEF1 | 0.621 | 0.558 | — |
| TGFB1 | 0.554 | 0.000 | — |
| PAX6 | 0.507 | 0.000 | — |
| GABRA5 | 0.468 | 0.000 | — |
| IMPG2 | 0.447 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SRPK2 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:23602568|imex:IM-17935 |
| EEF1E1 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| PTBP1 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| ENSP00000324701.4 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| TOM1 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| NONO | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| NEXN | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| NACA | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| LMO7 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| RACGAP1 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.8 + PDB: 无 | pLDDT=94.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. MAB21L2 — Protein mab-21-like 2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小359 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 44 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y586
- Protein Atlas: https://www.proteinatlas.org/ENSG00000181541-MAB21L2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MAB21L2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y586
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
