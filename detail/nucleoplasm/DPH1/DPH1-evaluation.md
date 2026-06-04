---
type: protein-evaluation
gene: "DPH1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DPH1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DPH1 / DPH2L, DPH2L1, OVCA1 |
| 蛋白名称 | 2-(3-amino-3-carboxypropyl)histidine synthase subunit 1 |
| 蛋白大小 | 438 aa / 48.1 kDa |
| UniProt ID | Q9BZG8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cell Junctions; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 438 aa / 48.1 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=51 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=86.1; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR016435, IPR042263, IPR042264, IPR042265; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.5/180** | |
| **归一化总分** | | | **65.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cell Junctions | Approved |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 2-(3-amino-3-carboxypropyl)histidine synthase complex (GO:0120513)
- cell junction (GO:0030054)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 51 |
| PubMed broad count | 107 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DPH2L, DPH2L1, OVCA1 |

**关键文献**:
1. Accelerating novel candidate gene discovery in neurogenetic disorders via whole-exome sequencing of prescreened multiplex consanguineous families.. *Cell reports*. PMID: 25558065
2. Context-specific roles of diphthamide deficiency in hepatocellular carcinogenesis.. *The Journal of pathology*. PMID: 35781884
3. Translational fidelity and growth of Arabidopsis require stress-sensitive diphthamide biosynthesis.. *Nature communications*. PMID: 35817801
4. DPH1 Gene Mutations Identify a Candidate SAM Pocket in Radical Enzyme Dph1•Dph2 for Diphthamide Synthesis on EF2.. *Biomolecules*. PMID: 38002337
5. Insights into diphthamide, key diphtheria toxin effector.. *Toxins*. PMID: 23645155

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.1 |
| 高置信度残基 (pLDDT>90) 占比 | 79.9% |
| 置信残基 (pLDDT 70-90) 占比 | 2.3% |
| 中等置信 (pLDDT 50-70) 占比 | 1.8% |
| 低置信 (pLDDT<50) 占比 | 16.0% |
| 有序区域 (pLDDT>70) 占比 | 82.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=86.1，有序区 82.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016435, IPR042263, IPR042264, IPR042265; Pfam: PF01866 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DPH2 | 0.999 | 0.984 | — |
| DPH5 | 0.996 | 0.099 | — |
| DPH3 | 0.993 | 0.593 | — |
| EEF2 | 0.984 | 0.710 | — |
| OVCA2 | 0.964 | 0.000 | — |
| DPH7 | 0.927 | 0.000 | — |
| RBM8A | 0.880 | 0.230 | — |
| DNAJC24 | 0.871 | 0.186 | — |
| DPH6 | 0.809 | 0.000 | — |
| ELP3 | 0.707 | 0.089 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MINT-216436 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-26346|pubmed:23695164| |
| Cdk4 | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |
| DPH2 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| EFT1 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| IMD3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| RNR2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| RPC82 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| SSA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| SSB1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| TEF1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.1 + PDB: 无 | pLDDT=86.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm; 额外: Cell Junctions | 一致 |
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
1. DPH1 — 2-(3-amino-3-carboxypropyl)histidine synthase subunit 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小438 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 51 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BZG8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000108963-DPH1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DPH1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BZG8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
