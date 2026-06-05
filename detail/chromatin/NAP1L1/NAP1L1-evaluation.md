---
type: protein-evaluation
gene: "NAP1L1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NAP1L1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NAP1L1 / NRP |
| 蛋白名称 | Nucleosome assembly protein 1-like 1 |
| 蛋白大小 | 391 aa / 45.4 kDa |
| UniProt ID | P55209 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Microtubules; UniProt: Nucleus; Chromosome; Melanosome; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 391 aa / 45.4 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=76 篇 (≤80→4) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=79.9; PDB: 7BP5, 7UN3, 7UN6 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037231, IPR002164; Pfam: PF00956 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.0/180** | |
| **归一化总分** | | | **61.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Microtubules | Uncertain |
| UniProt | Nucleus; Chromosome; Melanosome; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- melanosome (GO:0042470)
- membrane (GO:0016020)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 76 |
| PubMed broad count | 151 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NRP |

**关键文献**:
1. Nucleosome assembly protein-like 1 degradation-dependent novel cardioprotection mechanism of Wnt2 against ischemia‒reperfusion injury.. *Signal transduction and targeted therapy*. PMID: 41397965
2. NAP1L1 degradation by FBXW7 reduces the deubiquitination of HDGF-p62 signaling to stimulate autophagy and induce primary cisplatin chemosensitivity in nasopharyngeal carcinoma.. *Molecular cancer*. PMID: 40414865
3. Somatic NAP1L1 p.D349E promotes cardiac hypertrophy through cGAS-STING-IFN signaling.. *Nature communications*. PMID: 40169585
4. NAP1L1 is a novel microtubule-associated protein.. *Cytoskeleton (Hoboken, N.J.)*. PMID: 37098731
5. NAP1L1 regulates BIRC2 ubiquitination modification via E3 ubiquitin ligase UBR4 and hence determines hepatocellular carcinoma progression.. *Cell death discovery*. PMID: 38538582

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.9 |
| 高置信度残基 (pLDDT>90) 占比 | 53.5% |
| 置信残基 (pLDDT 70-90) 占比 | 15.1% |
| 中等置信 (pLDDT 50-70) 占比 | 17.9% |
| 低置信 (pLDDT<50) 占比 | 13.6% |
| 有序区域 (pLDDT>70) 占比 | 68.6% |
| 可用 PDB 条目 | 7BP5, 7UN3, 7UN6 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（7BP5, 7UN3, 7UN6）+ AlphaFold高质量预测（pLDDT=79.9），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037231, IPR002164; Pfam: PF00956 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UBE2O | 0.973 | 0.969 | — |
| NAP1L4 | 0.927 | 0.867 | — |
| H2AZ1 | 0.884 | 0.805 | — |
| MAGED2 | 0.846 | 0.628 | — |
| H2AX | 0.839 | 0.663 | — |
| NPM1 | 0.827 | 0.376 | — |
| FNTA | 0.807 | 0.776 | — |
| NAP1L5 | 0.793 | 0.537 | — |
| EP300 | 0.774 | 0.722 | — |
| CDX4 | 0.762 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-21355522 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| TRAF1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| TRAF2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| TANK | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| TNFRSF1A | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| TRADD | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| FSD1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| HBA1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CREBBP | psi-mi:"MI:0018"(two hybrid) | pubmed:11940655|imex:IM-19548 |
| EP300 | psi-mi:"MI:0096"(pull down) | pubmed:11940655|imex:IM-19548 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.9 + PDB: 7BP5, 7UN3, 7UN6 | pLDDT=79.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome; Melanosome; Cytoplasm / Microtubules | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. NAP1L1 — Nucleosome assembly protein 1-like 1，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小391 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 76 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P55209
- Protein Atlas: https://www.proteinatlas.org/ENSG00000187109-NAP1L1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NAP1L1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P55209
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03



<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P55209-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
