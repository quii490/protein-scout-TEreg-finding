---
type: protein-evaluation
gene: "DDX39B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DDX39B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DDX39B / BAT1, UAP56 |
| 蛋白名称 | Spliceosome RNA helicase DDX39B |
| 蛋白大小 | 428 aa / 49.0 kDa |
| UniProt ID | Q13838 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nuclear speckles; UniProt: Nucleus; Nucleus speckle; Cytoplasm |
| 蛋白大小 | 10/10 | x1 | 10 | 428 aa / 49.0 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=51 篇 (≤60→6) |
| 三维结构 | 10/10 | x3 | 30 | AlphaFold v6 pLDDT=84.8; PDB: 1T5I, 1T6N, 1XTI, 1XTJ, 1XTK, 7APK, 7ZNK |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR011545, IPR014001, IPR001650, IPR027417, IPR014 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.5/180** | |
| **归一化总分** | | | **69.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Enhanced |
| UniProt | Nucleus; Nucleus speckle; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- spliceosomal complex (GO:0005681)
- transcription export complex (GO:0000346)
- U4 snRNP (GO:0005687)
- U6 snRNP (GO:0005688)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 51 |
| PubMed broad count | 156 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BAT1, UAP56 |

**关键文献**:
1. DDX39B K63-linked ubiquitination mediated by TRIM28 promotes NSCLC metastasis by enhancing ECAD lysosomal degradation.. *Signal transduction and targeted therapy*. PMID: 40664668
2. Structural mechanism of DDX39B regulation by human TREX-2 and a related complex in mRNP remodeling.. *Nature communications*. PMID: 40595470
3. De novo and inherited variants in DDX39B cause a novel neurodevelopmental syndrome.. *Brain : a journal of neurology*. PMID: 39918047
4. Structures and mRNP remodeling mechanism of the TREX-2 complex.. *Structure (London, England : 1993)*. PMID: 39862860
5. The RNA-binding protein DDX39B promotes colorectal adenocarcinoma progression by stabilizing DCLK1.. *Human molecular genetics*. PMID: 40583564

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.8 |
| 高置信度残基 (pLDDT>90) 占比 | 63.3% |
| 置信残基 (pLDDT 70-90) 占比 | 19.9% |
| 中等置信 (pLDDT 50-70) 占比 | 6.5% |
| 低置信 (pLDDT<50) 占比 | 10.3% |
| 有序区域 (pLDDT>70) 占比 | 83.2% |
| 可用 PDB 条目 | 1T5I, 1T6N, 1XTI, 1XTJ, 1XTK, 7APK, 7ZNK, 7ZNL, 8ENK, 9DLP |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构 + AlphaFold极高置信度（pLDDT=84.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011545, IPR014001, IPR001650, IPR027417, IPR014014; Pfam: PF00270, PF00271 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| THOC5 | 0.999 | 0.971 | — |
| THOC6 | 0.999 | 0.957 | — |
| SARNP | 0.999 | 0.898 | — |
| ALYREF | 0.999 | 0.979 | — |
| CHTOP | 0.999 | 0.829 | — |
| THOC2 | 0.999 | 0.996 | — |
| THOC3 | 0.999 | 0.955 | — |
| EIF4A3 | 0.999 | 0.994 | — |
| THOC1 | 0.999 | 0.976 | — |
| THOC7 | 0.999 | 0.968 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.8 + PDB: 1T5I, 1T6N, 1XTI, 1XTJ, 1XTK,  | pLDDT=84.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus speckle; Cytoplasm / Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DDX39B -- Spliceosome RNA helicase DDX39B，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小428 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 51 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13838
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198563-DDX39B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DDX39B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13838
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (enhanced)。来源: https://www.proteinatlas.org/ENSG00000198563-DDX39B/subcellular

![](https://images.proteinatlas.org/34012/924_A12_1_red_green.jpg)
![](https://images.proteinatlas.org/34012/924_A12_2_red_green.jpg)
![](https://images.proteinatlas.org/34012/932_A12_1_red_green.jpg)
![](https://images.proteinatlas.org/34012/932_A12_2_red_green.jpg)
![](https://images.proteinatlas.org/34012/971_A12_1_red_green.jpg)
![](https://images.proteinatlas.org/34012/971_A12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q13838-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
