---
type: protein-evaluation
gene: "TERB1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TERB1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TERB1 / CCDC79 |
| 蛋白名称 | Telomere repeats-binding bouquet formation protein 1 |
| 蛋白大小 | 727 aa / 83.1 kDa |
| UniProt ID | Q8NA31 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cell Junctions, Cytosol; UniProt: Chromosome, telomere; Nucleus inner membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 727 aa / 83.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=71.6; PDB: 5WIR, 5XUP, 6J07 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011989, IPR016024, IPR009057, IPR001005, IPR042 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **140.5/180** | |
| **归一化总分** | | | **78.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cell Junctions, Cytosol | Approved |
| UniProt | Chromosome, telomere; Nucleus inner membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromosome, telomeric region (GO:0000781)
- nuclear envelope (GO:0005635)
- nuclear inner membrane (GO:0005637)
- shelterin complex (GO:0070187)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 24 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CCDC79 |

**关键文献**:
1. The TRF1-binding protein TERB1 promotes chromosome movement and telomere rigidity in meiosis.. *Nature cell biology*. PMID: 24413433
2. Dissecting the telomere-inner nuclear membrane interface formed in meiosis.. *Nature structural & molecular biology*. PMID: 29083414
3. The TERB1 MYB domain suppresses telomere erosion in meiotic prophase I.. *Cell reports*. PMID: 35081355
4. The meiotic TERB1-TERB2-MAJIN complex tethers telomeres to the nuclear envelope.. *Nature communications*. PMID: 30718482
5. Distinct TERB1 Domains Regulate Different Protein Interactions in Meiotic Telomere Movement.. *Cell reports*. PMID: 29141207

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.6 |
| 高置信度残基 (pLDDT>90) 占比 | 42.2% |
| 置信残基 (pLDDT 70-90) 占比 | 21.7% |
| 中等置信 (pLDDT 50-70) 占比 | 5.9% |
| 低置信 (pLDDT<50) 占比 | 30.1% |
| 有序区域 (pLDDT>70) 占比 | 63.9% |
| 可用 PDB 条目 | 5WIR, 5XUP, 6J07 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（5WIR, 5XUP, 6J07）+ AlphaFold高质量预测（pLDDT=71.6），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR009057, IPR001005, IPR042359; Pfam: PF00249 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TERB2 | 0.999 | 0.900 | — |
| TERF1 | 0.992 | 0.946 | — |
| MAJIN | 0.991 | 0.000 | — |
| SUN1 | 0.969 | 0.095 | — |
| LRRD1 | 0.951 | 0.000 | — |
| CCDC155 | 0.890 | 0.095 | — |
| SLC36A3 | 0.771 | 0.000 | — |
| SUN2 | 0.753 | 0.091 | — |
| SPDYA | 0.733 | 0.000 | — |
| HORMAD2 | 0.708 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.6 + PDB: 5WIR, 5XUP, 6J07 | pLDDT=71.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Chromosome, telomere; Nucleus inner membrane / Nucleoplasm; 额外: Cell Junctions, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TERB1 — Telomere repeats-binding bouquet formation protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小727 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NA31
- Protein Atlas: https://www.proteinatlas.org/ENSG00000249961-TERB1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TERB1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NA31
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000249961-TERB1/subcellular

![](https://images.proteinatlas.org/79436/1975_B8_2_red_green.jpg)
![](https://images.proteinatlas.org/79436/1975_B8_3_red_green.jpg)
![](https://images.proteinatlas.org/79436/2017_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/79436/2017_G5_2_red_green.jpg)
![](https://images.proteinatlas.org/79436/2047_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/79436/2047_G5_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NA31-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
