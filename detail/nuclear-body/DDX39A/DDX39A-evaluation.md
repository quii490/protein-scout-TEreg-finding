---
type: protein-evaluation
gene: "DDX39A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DDX39A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DDX39A / DDX39 |
| 蛋白名称 | ATP-dependent RNA helicase DDX39A |
| 蛋白大小 | 427 aa / 49.1 kDa |
| UniProt ID | O00148 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nuclear speckles; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | x1 | 10 | 427 aa / 49.1 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=37 篇 (≤40→8) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=85.3; PDB: 8IJU |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR011545, IPR014001, IPR001650, IPR027417, IPR014 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.5/180** | |
| **归一化总分** | | | **71.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Approved |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- membrane (GO:0016020)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 37 |
| PubMed broad count | 85 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DDX39 |

**关键文献**:
1. DDX39A resolves replication fork-associated RNA-DNA hybrids to balance fork protection and cleavage for genomic stability maintenance.. *Molecular cell*. PMID: 39706185
2. Intron Retention of DDX39A Driven by SNRPD2 is a Crucial Splicing Axis for Oncogenic MYC/Spliceosome Program in Hepatocellular Carcinoma.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39018261
3. SUMOylation of DDX39A Alters Binding and Export of Antiviral Transcripts to Control Innate Immunity.. *Journal of immunology (Baltimore, Md. : 1950)*. PMID: 32393512
4. Comprehensive analysis of lactylation-related gene and immune microenvironment in atrial fibrillation.. *Frontiers in cardiovascular medicine*. PMID: 40329965
5. SNRPB-mediated regulation of DDX39A splicing promotes ovarian cancer progression by regulating α6 integrin subunit expression.. *Oncogene*. PMID: 40216968

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.3 |
| 高置信度残基 (pLDDT>90) 占比 | 66.0% |
| 置信残基 (pLDDT 70-90) 占比 | 18.5% |
| 中等置信 (pLDDT 50-70) 占比 | 4.7% |
| 低置信 (pLDDT<50) 占比 | 10.8% |
| 有序区域 (pLDDT>70) 占比 | 84.5% |
| 可用 PDB 条目 | 8IJU |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度（pLDDT=85.3，有序区 84.5%）。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011545, IPR014001, IPR001650, IPR027417, IPR014014; Pfam: PF00270, PF00271 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SARNP | 0.999 | 0.928 | — |
| ALYREF | 0.994 | 0.917 | — |
| THOC2 | 0.980 | 0.897 | — |
| DDX39B | 0.967 | 0.845 | — |
| THOC1 | 0.937 | 0.754 | — |
| POLDIP3 | 0.924 | 0.636 | — |
| THOC7 | 0.919 | 0.564 | — |
| CHTOP | 0.911 | 0.420 | — |
| THOC5 | 0.893 | 0.476 | — |
| FYTTD1 | 0.885 | 0.071 | — |

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
| 三维结构 | AlphaFold pLDDT=85.3 + PDB: 8IJU | pLDDT=85.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DDX39A -- ATP-dependent RNA helicase DDX39A，非常新颖，仅有少数基础研究。
2. 蛋白大小427 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 37 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O00148
- Protein Atlas: https://www.proteinatlas.org/ENSG00000123136-DDX39A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DDX39A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O00148
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000123136-DDX39A/subcellular

![](https://images.proteinatlas.org/55334/1081_B7_1_red_green.jpg)
![](https://images.proteinatlas.org/55334/1081_B7_2_red_green.jpg)
![](https://images.proteinatlas.org/55334/875_F5_1_red_green.jpg)
![](https://images.proteinatlas.org/55334/875_F5_4_red_green.jpg)
![](https://images.proteinatlas.org/55334/883_F5_1_red_green.jpg)
![](https://images.proteinatlas.org/55334/883_F5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O00148-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
