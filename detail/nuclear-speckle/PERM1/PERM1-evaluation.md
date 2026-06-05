---
type: protein-evaluation
gene: "PERM1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PERM1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PERM1 / C1orf170 |
| 蛋白名称 | PGC-1 and ERR-induced regulator in muscle protein 1 |
| 蛋白大小 | 790 aa / 81.4 kDa |
| UniProt ID | Q5SV97 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nuclear bodies; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 790 aa / 81.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=25 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=44.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR043442 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 11 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.5/180** | |
| **归一化总分** | | | **66.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 25 |
| PubMed broad count | 38 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C1orf170 |

**关键文献**:
1. PERM1 regulates genes involved in fatty acid metabolism in the heart by interacting with PPARα and PGC-1α.. *Scientific reports*. PMID: 36028747
2. NOR-1 Overexpression Elevates Myoglobin Expression via PERM1 and Enhances Mitochondrial Function and Endurance in Skeletal Muscles of Aged Mice.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 40235231
3. Perm1 promotes cardiomyocyte mitochondrial biogenesis and protects against hypoxia/reoxygenation-induced damage in mice.. *The Journal of biological chemistry*. PMID: 34029594
4. Adeno-associated virus-mediated gene delivery of Perm1 enhances cardiac contractility in mice.. *American journal of physiology. Heart and circulatory physiology*. PMID: 39269449
5. Perm1 regulates CaMKII activation and shapes skeletal muscle responses to endurance exercise training.. *Molecular metabolism*. PMID: 30862473

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 44.4 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 6.2% |
| 中等置信 (pLDDT 50-70) 占比 | 14.2% |
| 低置信 (pLDDT<50) 占比 | 79.6% |
| 有序区域 (pLDDT>70) 占比 | 6.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=44.4），有序残基占 6.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043442 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ESRRA | 0.846 | 0.050 | — |
| PPARGC1A | 0.678 | 0.069 | — |
| CREB1 | 0.526 | 0.000 | — |
| PLEKHN1 | 0.492 | 0.000 | — |
| ANK2 | 0.490 | 0.098 | — |
| TFB2M | 0.440 | 0.067 | — |
| FCRL1 | 0.419 | 0.107 | — |
| KRTAP10-3 | 0.418 | 0.000 | — |
| HRC | 0.412 | 0.095 | — |
| ESRRG | 0.411 | 0.050 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 11，IntAct interactions: 0
- 调控相关比例: 0 / 11 = 0%

**评价**: STRING 11 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=44.4 + PDB: 无 | pLDDT=44.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 11 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PERM1 — PGC-1 and ERR-induced regulator in muscle protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小790 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 25 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=44.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5SV97
- Protein Atlas: https://www.proteinatlas.org/ENSG00000187642-PERM1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PERM1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5SV97
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000187642-PERM1/subcellular

![](https://images.proteinatlas.org/31711/1320_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/31711/1320_G6_3_red_green.jpg)
![](https://images.proteinatlas.org/31711/2275_F1_163_red_green.jpg)
![](https://images.proteinatlas.org/31711/2275_F1_238_red_green.jpg)
![](https://images.proteinatlas.org/31711/366_E3_1_red_green.jpg)
![](https://images.proteinatlas.org/31711/366_E3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5SV97-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
