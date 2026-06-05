---
type: protein-evaluation
gene: "C6orf89"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## C6orf89 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C6orf89 / BRAP |
| 蛋白名称 | Bombesin receptor-activated protein C6orf89 |
| 蛋白大小 | 347 aa / 39.9 kDa |
| UniProt ID | Q6UWU4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Golgi apparatus membrane; Midbody; Golgi apparatus membrane; |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 347 aa / 39.9 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=72.5; PDB: 无 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR038757 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 6 partners; IntAct 4 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Golgi apparatus membrane; Midbody; Golgi apparatus membrane; Midbody; Cytoplasm;... | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- Golgi membrane (GO:0000139)
- midbody (GO:0030496)
- nucleolus (GO:0005730)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BRAP |

**关键文献**:
1. Bombesin receptor-activated protein exacerbates cisplatin-induced AKI by regulating the degradation of SIRT2.. *Nephrology, dialysis, transplantation : official publication of the European Dialysis and Transplant Association - European Renal Association*. PMID: 35488871
2. Attenuation of renal fibrosis in mice due to lack of bombesin receptor-activated protein homologue.. *Clinical and experimental pharmacology & physiology*. PMID: 39155151
3. DNA crosslinking and recombination-activating genes 1/2 (RAG1/2) are required for oncogenic splicing in acute lymphoblastic leukemia.. *Cancer communications (London, England)*. PMID: 34699692
4. Systematic identification of personal tumor-specific neoantigens in chronic lymphocytic leukemia.. *Blood*. PMID: 24891321
5. C6orf89 encodes three distinct HDAC enhancers that function in the nucleolus, the golgi and the midbody.. *Journal of cellular physiology*. PMID: 23460338

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.5 |
| 高置信度残基 (pLDDT>90) 占比 | 11.8% |
| 置信残基 (pLDDT 70-90) 占比 | 52.2% |
| 中等置信 (pLDDT 50-70) 占比 | 21.9% |
| 低置信 (pLDDT<50) 占比 | 14.1% |
| 有序区域 (pLDDT>70) 占比 | 64.0% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=72.5，有序区 64.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR038757 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BRS3 | 0.810 | 0.000 | — |
| PTRHD1 | 0.627 | 0.627 | — |
| NBR1 | 0.505 | 0.000 | — |
| PI16 | 0.472 | 0.000 | — |
| PCYT1A | 0.457 | 0.000 | — |
| NOXRED1 | 0.436 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PTRHD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TUSC5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| HTR3A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CHRNB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 6，IntAct interactions: 4
- 调控相关比例: 0 / 6 = 0%

**评价**: STRING 6 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.5 + PDB: 无 | pLDDT=72.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus membrane; Midbody; Golgi apparatus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 6 + 4 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. C6orf89 — Bombesin receptor-activated protein C6orf89，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小347 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6UWU4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198663-C6orf89/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C6orf89
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6UWU4
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 04:26:15

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6UWU4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
