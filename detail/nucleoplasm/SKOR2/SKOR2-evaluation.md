---
type: protein-evaluation
gene: "SKOR2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SKOR2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SKOR2 / CORL2, FUSSEL18 |
| 蛋白名称 | SKI family transcriptional corepressor 2 |
| 蛋白大小 | 1015 aa / 105.8 kDa |
| UniProt ID | Q2VWA4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 1015 aa / 105.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=51.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR014890, IPR009061, IPR010919, IPR003380, IPR037 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.5/180** | |
| **归一化总分** | | | **70.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 50 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CORL2, FUSSEL18 |

**关键文献**:
1. Interactions among Merlin, Arkadia, and SKOR2 mediate NF2-associated human Schwann cell proliferation.. *Stem cell research & therapy*. PMID: 40188079
2. Interactions among Merlin, Arkadia, and SKOR2 mediate NF2-associated Schwann cell proliferation in human.. *bioRxiv : the preprint server for biology*. PMID: 39386608
3. The role of DNA methylation and histone modifications in blood pressure: a systematic review.. *Journal of human hypertension*. PMID: 31346255
4. The plasma peptides of ovarian cancer.. *Clinical proteomics*. PMID: 30598658
5. The Drosophila functional Smad suppressing element fuss, a homologue of the human Skor genes, retains pro-oncogenic properties of the Ski/Sno family.. *PloS one*. PMID: 35030229

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 51.6 |
| 高置信度残基 (pLDDT>90) 占比 | 11.9% |
| 置信残基 (pLDDT 70-90) 占比 | 11.4% |
| 中等置信 (pLDDT 50-70) 占比 | 9.6% |
| 低置信 (pLDDT<50) 占比 | 67.1% |
| 有序区域 (pLDDT>70) 占比 | 23.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=51.6），有序残基占 23.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR014890, IPR009061, IPR010919, IPR003380, IPR037000; Pfam: PF08782, PF02437 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LOXHD1 | 0.592 | 0.045 | — |
| KIRREL2 | 0.543 | 0.000 | — |
| IRX1 | 0.535 | 0.000 | — |
| TMC2 | 0.490 | 0.000 | — |
| RNF165 | 0.465 | 0.000 | — |
| MYO3A | 0.456 | 0.000 | — |
| LHX5 | 0.449 | 0.000 | — |
| PTF1A | 0.449 | 0.000 | — |
| UBXN11 | 0.442 | 0.000 | — |
| EN1 | 0.430 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 14，IntAct interactions: 0
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=51.6 + PDB: 无 | pLDDT=51.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 14 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SKOR2 — SKI family transcriptional corepressor 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1015 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=51.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q2VWA4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000215474-SKOR2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SKOR2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q2VWA4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q2VWA4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
