---
type: protein-evaluation
gene: "STON2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## STON2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | STON2 / STN2, STNB |
| 蛋白名称 | Stonin-2 |
| 蛋白大小 | 905 aa / 101.2 kDa |
| UniProt ID | Q8WXE9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli, Cytosol; UniProt: Cytoplasm; Membrane; Synapse, synaptosome |
| 蛋白大小 | 8/10 | ×1 | 8 | 905 aa / 101.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.2; PDB: 2JXC |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050431, IPR036168, IPR028565, IPR012320, IPR031 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.5/180** | |
| **归一化总分** | | | **71.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Cytosol | Approved |
| UniProt | Cytoplasm; Membrane; Synapse, synaptosome | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- AP-2 adaptor complex (GO:0030122)
- cytosol (GO:0005829)
- neuron projection (GO:0043005)
- nucleolus (GO:0005730)
- synaptic vesicle (GO:0008021)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 31 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: STN2, STNB |

**关键文献**:
1. STON2 variations are involved in synaptic dysfunction and schizophrenia-like behaviors by regulating Syt1 trafficking.. *Science bulletin*. PMID: 38402028
2. Stonin 2 activates lysosomal-mTOR axis for cell survival in oral cancer.. *Toxicology in vitro : an international journal published in association with BIBRA*. PMID: 36702439
3. Cortical surface area correlates with STON2 gene Ser307Pro polymorphism in first-episode treatment-naïve patients with schizophrenia.. *PloS one*. PMID: 23785397
4. Evaluating the association between single nucleotide polymorphisms in the stonin 2 (STON2) gene and keratoconus in a Han Chinese population.. *Annals of translational medicine*. PMID: 33987314
5. Keratoconus-susceptibility gene identification by corneal thickness genome-wide association study and artificial intelligence IBM Watson.. *Communications biology*. PMID: 32737415

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.2 |
| 高置信度残基 (pLDDT>90) 占比 | 27.0% |
| 置信残基 (pLDDT 70-90) 占比 | 16.8% |
| 中等置信 (pLDDT 50-70) 占比 | 8.1% |
| 低置信 (pLDDT<50) 占比 | 48.2% |
| 有序区域 (pLDDT>70) 占比 | 43.8% |
| 可用 PDB 条目 | 2JXC |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=61.2），有序残基占 43.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050431, IPR036168, IPR028565, IPR012320, IPR031228; Pfam: PF00928, PF12016 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EPS15 | 0.999 | 0.969 | — |
| SYT1 | 0.987 | 0.718 | — |
| EPS15L1 | 0.984 | 0.794 | — |
| ITSN1 | 0.983 | 0.292 | — |
| GTF2A1 | 0.980 | 0.000 | — |
| SYT2 | 0.962 | 0.473 | — |
| AP2M1 | 0.870 | 0.791 | — |
| SNAP91 | 0.845 | 0.000 | — |
| ITSN2 | 0.842 | 0.000 | — |
| PICALM | 0.802 | 0.511 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Syt1 | psi-mi:"MI:0096"(pull down) | pubmed:14726597 |
| Ap2m1 | psi-mi:"MI:0096"(pull down) | pubmed:14726597 |
| Ap2a2 | psi-mi:"MI:0096"(pull down) | pubmed:14726597 |
| VCAM1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-17358|pubmed:22623428 |
| BCR/ABL fusion | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:19380743|imex:IM-20432 |
| EPS15 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19380743|imex:IM-20432 |
| FN1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-14135|pubmed:19738201 |
| TGOLN2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| CAPZA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.2 + PDB: 2JXC | pLDDT=61.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Membrane; Synapse, synaptosome / Nucleoli, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. STON2 — Stonin-2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小905 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=61.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WXE9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000140022-STON2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=STON2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WXE9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
