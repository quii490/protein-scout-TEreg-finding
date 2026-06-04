---
type: protein-evaluation
gene: "KLHDC2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KLHDC2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KLHDC2 / HCA33 |
| 蛋白名称 | Kelch domain-containing protein 2 |
| 蛋白大小 | 406 aa / 46.1 kDa |
| UniProt ID | Q9Y2U9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear membrane; 额外: Nuclear bodies; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 406 aa / 46.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=19 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=89.7; PDB: 6DO3, 6DO4, 6DO5, 8EBL, 8EBM, 8EBN, 8PIF |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR015915; Pfam: PF24681 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **146.0/180** | |
| **归一化总分** | | | **81.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear membrane; 额外: Nuclear bodies | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- Cul2-RING ubiquitin ligase complex (GO:0031462)
- nuclear body (GO:0016604)
- nuclear membrane (GO:0031965)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 19 |
| PubMed broad count | 23 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HCA33 |

**关键文献**:
1. Principles of paralog-specific targeted protein degradation engaging the C-degron E3 KLHDC2.. *Nature communications*. PMID: 39396041
2. Targeted protein degradation by KLHDC2 ligands identified by high-throughput screening.. *eLife*. PMID: 40522120
3. E3 ligase autoinhibition by C-degron mimicry maintains C-degron substrate fidelity.. *Molecular cell*. PMID: 36805027
4. Mycobacterium tuberculosis effector protein PE5 hijacks the host CRL2 ubiquitin ligase complex.. *bioRxiv : the preprint server for biology*. PMID: 40661520
5. Targeted kinase degradation via the KLHDC2 ubiquitin E3 ligase.. *Cell chemical biology*. PMID: 37567174

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.7 |
| 高置信度残基 (pLDDT>90) 占比 | 75.1% |
| 置信残基 (pLDDT 70-90) 占比 | 14.8% |
| 中等置信 (pLDDT 50-70) 占比 | 2.2% |
| 低置信 (pLDDT<50) 占比 | 7.9% |
| 有序区域 (pLDDT>70) 占比 | 89.9% |
| 可用 PDB 条目 | 6DO3, 6DO4, 6DO5, 8EBL, 8EBM, 8EBN, 8PIF, 8SGE, 8SGF, 8SH2 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（6DO3, 6DO4, 6DO5, 8EBL, 8EBM, 8EBN, 8PIF, 8SGE, 8SGF, 8SH2）+ AlphaFold极高置信度预测（pLDDT=89.7），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015915; Pfam: PF24681 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ELOB | 0.977 | 0.569 | — |
| CUL2 | 0.971 | 0.460 | — |
| APPBP2 | 0.948 | 0.000 | — |
| RBX1 | 0.947 | 0.397 | — |
| FEM1C | 0.943 | 0.071 | — |
| PRAMEF6 | 0.940 | 0.066 | — |
| ZYG11B | 0.937 | 0.000 | — |
| ZER1 | 0.932 | 0.000 | — |
| KLHDC3 | 0.932 | 0.000 | — |
| PRAMEF15 | 0.931 | 0.066 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EZH2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| STRN4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| DDX19B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| argD | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| capR | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| UBXN7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| kefB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ENSP00000298307.5 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| CUL2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| 1C | psi-mi:"MI:0096"(pull down) | imex:IM-15828|pubmed:22593156 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.7 + PDB: 6DO3, 6DO4, 6DO5, 8EBL, 8EBM,  | pLDDT=89.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nuclear membrane; 额外: Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. KLHDC2 — Kelch domain-containing protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小406 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 19 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y2U9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165516-KLHDC2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KLHDC2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y2U9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
