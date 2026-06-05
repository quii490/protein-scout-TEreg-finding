---
type: protein-evaluation
gene: "LURAP1L"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LURAP1L 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LURAP1L / C9orf150 |
| 蛋白名称 | Leucine rich adaptor protein 1-like |
| 蛋白大小 | 228 aa / 24.4 kDa |
| UniProt ID | Q8IV03 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; 额外: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 228 aa / 24.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039499, IPR037443; Pfam: PF14854 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 10 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129/180** | |
| **归一化总分** | | | **71.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 11 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C9orf150 |

**关键文献**:
1. Exploring the molecular mechanisms of ferroptosis-related genes in periodontitis: a multi-dataset analysis.. *BMC oral health*. PMID: 38802844
2. Joint genotype and ancestry analysis identify novel loci associated with atopic dermatitis in African American population.. *HGG advances*. PMID: 39245941
3. PDGF-BB regulates the transformation of fibroblasts into cancer-associated fibroblasts via the lncRNA LURAP1L-AS1/LURAP1L/IKK/IκB/NF-κB signaling pathway.. *Oncology letters*. PMID: 34079593
4. Transcriptome analyses reveal reduced hepatic lipid synthesis and accumulation in more feed efficient beef cattle.. *Scientific reports*. PMID: 29740082
5. Clinical significance and immune landscape of a novel ferroptosis-related prognosis signature in osteosarcoma.. *BMC cancer*. PMID: 36899330

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.6 |
| 高置信度残基 (pLDDT>90) 占比 | 21.5% |
| 置信残基 (pLDDT 70-90) 占比 | 10.5% |
| 中等置信 (pLDDT 50-70) 占比 | 38.2% |
| 低置信 (pLDDT<50) 占比 | 29.8% |
| 有序区域 (pLDDT>70) 占比 | 32.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.6），有序残基占 32.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039499, IPR037443; Pfam: PF14854 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SHTN1 | 0.507 | 0.504 | — |
| CDC42BPA | 0.470 | 0.444 | — |
| SLC4A3 | 0.468 | 0.000 | — |
| CDC42BPB | 0.463 | 0.438 | — |
| HSF1 | 0.449 | 0.449 | — |
| UBE2G1 | 0.440 | 0.000 | — |
| SNTB2 | 0.438 | 0.438 | — |
| FBXO28 | 0.422 | 0.422 | — |
| NEFM | 0.420 | 0.421 | — |
| FAM126B | 0.405 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 10，IntAct interactions: 0
- 调控相关比例: 0 / 10 = 0%

**评价**: STRING 10 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.6 + PDB: 无 | pLDDT=64.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli; 额外: Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 10 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. LURAP1L — Leucine rich adaptor protein 1-like，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小228 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=64.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IV03
- Protein Atlas: https://www.proteinatlas.org/ENSG00000153714-LURAP1L/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LURAP1L
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IV03
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000153714-LURAP1L/subcellular

![](https://images.proteinatlas.org/24407/224_F4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/24407/224_F4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/24407/226_F4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/24407/226_F4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/24407/261_F4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/24407/261_F4_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IV03-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
