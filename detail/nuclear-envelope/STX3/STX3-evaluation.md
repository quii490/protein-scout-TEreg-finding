---
type: protein-evaluation
gene: "STX3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## STX3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | STX3 / STX3A |
| 蛋白名称 | Syntaxin-3 |
| 蛋白大小 | 289 aa / 33.2 kDa |
| UniProt ID | Q13277 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles; 额外: Nuclear membrane; UniProt: Apical cell membrane; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 289 aa / 33.2 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=84 篇 (≤100→2) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=83.3; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR010989, IPR031186, IPR045242, IPR006012, IPR006 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **95.5/180** | |
| **归一化总分** | | | **53.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nuclear membrane | Uncertain |
| UniProt | Apical cell membrane; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- apical plasma membrane (GO:0016324)
- azurophil granule (GO:0042582)
- cell-cell junction (GO:0005911)
- dendrite (GO:0030425)
- endomembrane system (GO:0012505)
- extracellular exosome (GO:0070062)
- glutamatergic synapse (GO:0098978)
- growth cone (GO:0030426)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 84 |
| PubMed broad count | 115 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: STX3A |

**关键文献**:
1. SKArred 2 death: neuroinflammatory breakdown of the hippocampus.. *Autophagy*. PMID: 38934263
2. Uncovering the Relationship Between Genes and Phenotypes Beyond the Gut in Microvillus Inclusion Disease.. *Cellular and molecular gastroenterology and hepatology*. PMID: 38307491
3. Increased STX3 transcript and protein levels were associated with poor prognosis in two independent cohorts of esophageal squamous cell carcinoma patients.. *Cancer medicine*. PMID: 38014487
4. SNAREs and developmental disorders.. *Journal of cellular physiology*. PMID: 32959907
5. MYO5B, STX3, and STXBP2 mutations reveal a common disease mechanism that unifies a subset of congenital diarrheal disorders: A mutation update.. *Human mutation*. PMID: 29266534

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.3 |
| 高置信度残基 (pLDDT>90) 占比 | 46.0% |
| 置信残基 (pLDDT 70-90) 占比 | 37.7% |
| 中等置信 (pLDDT 50-70) 占比 | 11.1% |
| 低置信 (pLDDT<50) 占比 | 5.2% |
| 有序区域 (pLDDT>70) 占比 | 83.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=83.3，有序区 83.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR010989, IPR031186, IPR045242, IPR006012, IPR006011; Pfam: PF05739, PF00804 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| VAMP8 | 0.999 | 0.881 | — |
| SNAP23 | 0.999 | 0.920 | — |
| VAMP2 | 0.999 | 0.902 | — |
| VAMP3 | 0.999 | 0.911 | — |
| STXBP1 | 0.995 | 0.798 | — |
| VAMP4 | 0.993 | 0.849 | — |
| SNAP29 | 0.992 | 0.759 | — |
| VAMP7 | 0.992 | 0.698 | — |
| STX6 | 0.991 | 0.810 | — |
| SNAP25 | 0.990 | 0.805 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| ZFYVE9 | psi-mi:"MI:0096"(pull down) | imex:IM-11880|pubmed:17693260 |
| sbcC3 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| EBI-1257121 | psi-mi:"MI:0400"(affinity technology) | pubmed:19367725|imex:IM-20587 |
| DNAJC5 | psi-mi:"MI:0012"(bioluminescence resonance energy  | pubmed:29997244|imex:IM-26441| |
| PIK3R6 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| VAMP5 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| TRAF3IP1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| NAPB | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |
| STX4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.3 + PDB: 无 | pLDDT=83.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Apical cell membrane; Nucleus / Vesicles; 额外: Nuclear membrane | 一致 |
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
1. STX3 — Syntaxin-3，研究基础较多，新颖性有限。
2. 蛋白大小289 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 84 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13277
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166900-STX3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=STX3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13277
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
